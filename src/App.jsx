import React, { useState, useEffect, useMemo } from 'react';
import confetti from 'canvas-confetti';
import Header from './components/Header';
import DashboardStats from './components/DashboardStats';
import FilterBar from './components/FilterBar';
import QuestionCard from './components/QuestionCard';
import QuestionModal from './components/QuestionModal';
import DetailModal from './components/DetailModal';
import EmptyState from './components/EmptyState';
import { INITIAL_QUESTIONS } from './constants/initialData';

const STORAGE_KEY = 'sheryians_interview_tracker_sheet01';

export default function App() {
  // Load questions from LocalStorage or seed with INITIAL_QUESTIONS
  const [questions, setQuestions] = useState(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        return JSON.parse(saved);
      }
    } catch (e) {
      console.error('Failed to load from LocalStorage', e);
    }
    return INITIAL_QUESTIONS;
  });

  // Filter States
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [selectedStatus, setSelectedStatus] = useState('All');
  const [selectedDifficulty, setSelectedDifficulty] = useState('All');

  // Modal States
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingQuestion, setEditingQuestion] = useState(null);
  const [viewingQuestion, setViewingQuestion] = useState(null);

  // Toast notification
  const [toastMessage, setToastMessage] = useState('');

  // Persist to LocalStorage on state change
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(questions));
    } catch (e) {
      console.error('Failed to save to LocalStorage', e);
    }
  }, [questions]);

  const showToast = (msg) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(''), 3000);
  };

  // Trigger celebration if all questions are completed
  useEffect(() => {
    if (questions.length > 0 && questions.every(q => q.status === 'Completed')) {
      confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
      });
      showToast('🎉 Outstanding! All Sheet 01 interview tasks completed!');
    }
  }, [questions]);

  // Category counts computation for filter pills
  const categoryCounts = useMemo(() => {
    const counts = { All: questions.length };
    questions.forEach(q => {
      counts[q.category] = (counts[q.category] || 0) + 1;
    });
    return counts;
  }, [questions]);

  // Filtered & Searched Questions
  const filteredQuestions = useMemo(() => {
    return questions.filter(q => {
      // Category Match
      if (selectedCategory !== 'All' && q.category !== selectedCategory) {
        return false;
      }
      // Status Match
      if (selectedStatus !== 'All' && q.status !== selectedStatus) {
        return false;
      }
      // Difficulty Match
      if (selectedDifficulty !== 'All' && q.difficulty !== selectedDifficulty) {
        return false;
      }
      // Search Query
      if (searchQuery.trim()) {
        const query = searchQuery.toLowerCase();
        const titleMatch = q.title.toLowerCase().includes(query);
        const descMatch = (q.description || '').toLowerCase().includes(query);
        const keyPointsMatch = (q.keyPoints || []).some(k => k.toLowerCase().includes(query));
        return titleMatch || descMatch || keyPointsMatch;
      }
      return true;
    });
  }, [questions, selectedCategory, selectedStatus, selectedDifficulty, searchQuery]);

  // Handlers
  const handleSaveQuestion = (questionData) => {
    if (editingQuestion) {
      // Update existing
      setQuestions(prev => prev.map(q => q.id === editingQuestion.id ? { ...q, ...questionData } : q));
      showToast('Question updated successfully!');
    } else {
      // Add new
      const newQuestion = {
        ...questionData,
        id: `custom-${Date.now()}`,
        createdAt: new Date().toISOString()
      };
      setQuestions(prev => [newQuestion, ...prev]);
      showToast('New question added to tracker!');
    }
    setIsModalOpen(false);
    setEditingQuestion(null);
  };

  const handleEditClick = (question) => {
    setEditingQuestion(question);
    setIsModalOpen(true);
  };

  const handleDelete = (id) => {
    if (window.confirm('Are you sure you want to delete this question?')) {
      setQuestions(prev => prev.filter(q => q.id !== id));
      showToast('Question deleted');
    }
  };

  const handleToggleStatus = (id, newStatus) => {
    setQuestions(prev => prev.map(q => {
      if (q.id === id) {
        return { ...q, status: newStatus };
      }
      return q;
    }));
    showToast(`Status updated to ${newStatus}`);
  };

  const handleToggleMachineCoding = () => {
    const mcItem = questions.find(q => q.category === 'Machine Coding');
    if (!mcItem) return;
    const nextStatus = mcItem.status === 'Completed' ? 'In Progress' : mcItem.status === 'In Progress' ? 'Pending' : 'Completed';
    handleToggleStatus(mcItem.id, nextStatus);
  };

  const handleResetDefaults = () => {
    if (window.confirm('Reset all questions back to Sheet 01 original default questions?')) {
      setQuestions(INITIAL_QUESTIONS);
      showToast('Reset to Sheet 01 questions!');
    }
  };

  const handleResetFilters = () => {
    setSearchQuery('');
    setSelectedCategory('All');
    setSelectedStatus('All');
    setSelectedDifficulty('All');
  };

  return (
    <div className="min-h-screen bg-[#09090b] text-zinc-100 flex flex-col">
      {/* Top Navigation */}
      <Header
        onOpenAddModal={() => {
          setEditingQuestion(null);
          setIsModalOpen(true);
        }}
        onResetData={handleResetDefaults}
        totalQuestions={questions.length}
        completedQuestions={questions.filter(q => q.status === 'Completed').length}
      />

      {/* Main Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Dashboard Metric Summary Cards */}
        <DashboardStats
          questions={questions}
          onToggleMachineCoding={handleToggleMachineCoding}
        />

        {/* Search, Category, Difficulty, & Status Controls */}
        <FilterBar
          searchQuery={searchQuery}
          setSearchQuery={setSearchQuery}
          selectedCategory={selectedCategory}
          setSelectedCategory={setSelectedCategory}
          selectedStatus={selectedStatus}
          setSelectedStatus={setSelectedStatus}
          selectedDifficulty={selectedDifficulty}
          setSelectedDifficulty={setSelectedDifficulty}
          categoryCounts={categoryCounts}
          onResetFilters={handleResetFilters}
        />

        {/* Question Cards Grid or Empty State */}
        {questions.length === 0 ? (
          <EmptyState
            isSearching={false}
            onAddQuestion={() => {
              setEditingQuestion(null);
              setIsModalOpen(true);
            }}
            onResetDefaults={handleResetDefaults}
          />
        ) : filteredQuestions.length === 0 ? (
          <EmptyState
            isSearching={true}
            onResetFilters={handleResetFilters}
          />
        ) : (
          <div>
            <div className="flex items-center justify-between mb-4">
              <span className="text-xs font-semibold uppercase tracking-wider text-zinc-400">
                Questions ({filteredQuestions.length} of {questions.length})
              </span>
              <span className="text-xs text-zinc-400">
                Click any status badge to quickly toggle progress
              </span>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {filteredQuestions.map((q) => (
                <QuestionCard
                  key={q.id}
                  question={q}
                  onToggleStatus={handleToggleStatus}
                  onEdit={handleEditClick}
                  onDelete={handleDelete}
                  onViewDetails={setViewingQuestion}
                />
              ))}
            </div>
          </div>
        )}
      </main>

      {/* Add / Edit Question Modal */}
      <QuestionModal
        isOpen={isModalOpen}
        onClose={() => {
          setIsModalOpen(false);
          setEditingQuestion(null);
        }}
        onSave={handleSaveQuestion}
        editQuestion={editingQuestion}
      />

      {/* Details View Modal */}
      <DetailModal
        question={viewingQuestion}
        isOpen={!!viewingQuestion}
        onClose={() => setViewingQuestion(null)}
      />

      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 bg-zinc-900 border border-orange-500/40 text-orange-400 px-4 py-2.5 rounded-xl shadow-xl text-xs sm:text-sm font-medium animate-bounce">
          {toastMessage}
        </div>
      )}
    </div>
  );
}
