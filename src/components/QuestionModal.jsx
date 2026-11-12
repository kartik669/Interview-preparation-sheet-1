import React, { useState, useEffect } from 'react';
import { X, Plus, Trash2, CheckCircle2 } from 'lucide-react';
import { CATEGORIES, STATUSES, DIFFICULTIES } from '../constants/initialData';

export default function QuestionModal({ isOpen, onClose, onSave, editQuestion }) {
  const [formData, setFormData] = useState({
    title: '',
    category: 'DSA',
    difficulty: 'Medium',
    status: 'Pending',
    link: '',
    description: '',
    keyPoints: ['']
  });

  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (editQuestion) {
      setFormData({
        title: editQuestion.title || '',
        category: editQuestion.category || 'DSA',
        difficulty: editQuestion.difficulty || 'Medium',
        status: editQuestion.status || 'Pending',
        link: editQuestion.link || '',
        description: editQuestion.description || '',
        keyPoints: editQuestion.keyPoints && editQuestion.keyPoints.length > 0 ? editQuestion.keyPoints : ['']
      });
    } else {
      setFormData({
        title: '',
        category: 'DSA',
        difficulty: 'Medium',
        status: 'Pending',
        link: '',
        description: '',
        keyPoints: ['']
      });
    }
    setErrors({});
  }, [editQuestion, isOpen]);

  if (!isOpen) return null;

  // Validation
  const validate = () => {
    const errs = {};
    if (!formData.title.trim()) {
      errs.title = 'Title is required';
    } else if (formData.title.trim().length < 3) {
      errs.title = 'Title must be at least 3 characters';
    }

    if (formData.link && !formData.link.startsWith('http://') && !formData.link.startsWith('https://')) {
      errs.link = 'Link must start with http:// or https://';
    }

    setErrors(errs);
    return Object.keys(errs).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validate()) return;

    const cleanedKeyPoints = formData.keyPoints.map(p => p.trim()).filter(Boolean);

    onSave({
      ...formData,
      title: formData.title.trim(),
      description: formData.description.trim(),
      link: formData.link.trim(),
      keyPoints: cleanedKeyPoints
    });
  };

  const handleKeyPointChange = (index, val) => {
    const updated = [...formData.keyPoints];
    updated[index] = val;
    setFormData({ ...formData, keyPoints: updated });
  };

  const addKeyPoint = () => {
    setFormData({ ...formData, keyPoints: [...formData.keyPoints, ''] });
  };

  const removeKeyPoint = (index) => {
    const updated = formData.keyPoints.filter((_, i) => i !== index);
    setFormData({ ...formData, keyPoints: updated.length > 0 ? updated : [''] });
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-sm animate-fade-in">
      <div className="bg-zinc-900 border border-zinc-800 w-full max-w-xl rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
        {/* Header */}
        <div className="px-6 py-4 border-b border-zinc-800 flex items-center justify-between">
          <h2 className="text-lg font-bold text-white">
            {editQuestion ? 'Edit Question' : 'Add New Question'}
          </h2>
          <button
            onClick={onClose}
            className="p-1 rounded-lg text-zinc-400 hover:text-white hover:bg-zinc-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Form Body */}
        <form onSubmit={handleSubmit} className="p-6 overflow-y-auto space-y-4">
          {/* Title */}
          <div>
            <label className="block text-xs font-semibold text-zinc-300 mb-1.5">
              Question Title <span className="text-orange-500">*</span>
            </label>
            <input
              type="text"
              value={formData.title}
              onChange={(e) => setFormData({ ...formData, title: e.target.value })}
              placeholder="e.g. 3Sum or Event Loop Order of Execution"
              className={`w-full bg-zinc-950 border ${errors.title ? 'border-rose-500' : 'border-zinc-800'} rounded-xl px-3.5 py-2.5 text-sm text-zinc-100 placeholder:text-zinc-600 focus:outline-none focus:border-orange-500`}
            />
            {errors.title && <p className="text-xs text-rose-400 mt-1">{errors.title}</p>}
          </div>

          {/* Category, Difficulty & Status Row */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            {/* Category */}
            <div>
              <label className="block text-xs font-semibold text-zinc-300 mb-1.5">Category</label>
              <select
                value={formData.category}
                onChange={(e) => setFormData({ ...formData, category: e.target.value })}
                className="w-full bg-zinc-950 border border-zinc-800 rounded-xl px-3 py-2 text-sm text-zinc-100 focus:outline-none focus:border-orange-500"
              >
                {CATEGORIES.filter(c => c !== 'All').map(c => (
                  <option key={c} value={c}>{c}</option>
                ))}
              </select>
            </div>

            {/* Difficulty */}
            <div>
              <label className="block text-xs font-semibold text-zinc-300 mb-1.5">Difficulty</label>
              <select
                value={formData.difficulty}
                onChange={(e) => setFormData({ ...formData, difficulty: e.target.value })}
                className="w-full bg-zinc-950 border border-zinc-800 rounded-xl px-3 py-2 text-sm text-zinc-100 focus:outline-none focus:border-orange-500"
              >
                {DIFFICULTIES.filter(d => d !== 'All').map(d => (
                  <option key={d} value={d}>{d}</option>
                ))}
              </select>
            </div>

            {/* Status */}
            <div>
              <label className="block text-xs font-semibold text-zinc-300 mb-1.5">Status</label>
              <select
                value={formData.status}
                onChange={(e) => setFormData({ ...formData, status: e.target.value })}
                className="w-full bg-zinc-950 border border-zinc-800 rounded-xl px-3 py-2 text-sm text-zinc-100 focus:outline-none focus:border-orange-500"
              >
                {STATUSES.filter(s => s !== 'All').map(s => (
                  <option key={s} value={s}>{s}</option>
                ))}
              </select>
            </div>
          </div>

          {/* Problem Link */}
          <div>
            <label className="block text-xs font-semibold text-zinc-300 mb-1.5">Problem / Resource URL</label>
            <input
              type="url"
              value={formData.link}
              onChange={(e) => setFormData({ ...formData, link: e.target.value })}
              placeholder="https://leetcode.com/problems/... (optional)"
              className={`w-full bg-zinc-950 border ${errors.link ? 'border-rose-500' : 'border-zinc-800'} rounded-xl px-3.5 py-2 text-sm text-zinc-100 placeholder:text-zinc-600 focus:outline-none focus:border-orange-500`}
            />
            {errors.link && <p className="text-xs text-rose-400 mt-1">{errors.link}</p>}
          </div>

          {/* Description */}
          <div>
            <label className="block text-xs font-semibold text-zinc-300 mb-1.5">Problem Prompt / Description</label>
            <textarea
              rows={3}
              value={formData.description}
              onChange={(e) => setFormData({ ...formData, description: e.target.value })}
              placeholder="Explain the interview question scenario or LeetCode problem statement..."
              className="w-full bg-zinc-950 border border-zinc-800 rounded-xl px-3.5 py-2 text-sm text-zinc-100 placeholder:text-zinc-600 focus:outline-none focus:border-orange-500"
            />
          </div>

          {/* Key Discussion Points */}
          <div>
            <div className="flex items-center justify-between mb-1.5">
              <label className="text-xs font-semibold text-zinc-300">Key Points / Approach Highlights</label>
              <button
                type="button"
                onClick={addKeyPoint}
                className="text-xs text-orange-400 hover:text-orange-300 flex items-center gap-1 font-medium"
              >
                <Plus className="w-3.5 h-3.5" />
                Add Point
              </button>
            </div>
            <div className="space-y-2">
              {formData.keyPoints.map((pt, idx) => (
                <div key={idx} className="flex items-center gap-2">
                  <input
                    type="text"
                    value={pt}
                    onChange={(e) => handleKeyPointChange(idx, e.target.value)}
                    placeholder={`Key point #${idx + 1}`}
                    className="flex-1 bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-1.5 text-xs text-zinc-100 placeholder:text-zinc-600 focus:outline-none focus:border-orange-500"
                  />
                  {formData.keyPoints.length > 1 && (
                    <button
                      type="button"
                      onClick={() => removeKeyPoint(idx)}
                      className="p-1.5 text-zinc-500 hover:text-rose-400 transition-colors"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  )}
                </div>
              ))}
            </div>
          </div>

          {/* Footer Buttons */}
          <div className="pt-4 border-t border-zinc-800 flex items-center justify-end gap-3">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded-xl text-xs sm:text-sm font-medium text-zinc-400 hover:text-zinc-200 bg-zinc-800 hover:bg-zinc-700 transition-colors"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-5 py-2 rounded-xl text-xs sm:text-sm font-semibold text-white bg-orange-500 hover:bg-orange-600 shadow-md shadow-orange-500/20 transition-all"
            >
              {editQuestion ? 'Save Changes' : 'Create Question'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

