import React from 'react';
import { ExternalLink, CheckCircle2, Clock, AlertCircle, Edit3, Trash2, Eye, Sparkles } from 'lucide-react';

export default function QuestionCard({ question, onToggleStatus, onEdit, onDelete, onViewDetails }) {
  // Category styles
  const getCategoryBadge = (cat) => {
    switch (cat) {
      case 'DSA':
        return 'bg-blue-500/10 text-blue-400 border-blue-500/30';
      case 'Git':
        return 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30';
      case 'Technical':
        return 'bg-purple-500/10 text-purple-400 border-purple-500/30';
      case 'Machine Coding':
        return 'bg-orange-500/10 text-orange-400 border-orange-500/30';
      default:
        return 'bg-zinc-800 text-zinc-400 border-zinc-700';
    }
  };

  // Difficulty styles
  const getDifficultyBadge = (diff) => {
    switch (diff) {
      case 'Easy':
        return 'bg-emerald-950/60 text-emerald-400 border-emerald-800/40';
      case 'Medium':
        return 'bg-amber-950/60 text-amber-400 border-amber-800/40';
      case 'Hard':
        return 'bg-rose-950/60 text-rose-400 border-rose-800/40';
      default:
        return 'bg-zinc-900 text-zinc-400 border-zinc-800';
    }
  };

  // Status icon & style
  const getStatusConfig = (status) => {
    switch (status) {
      case 'Completed':
        return {
          badge: 'bg-emerald-500/15 text-emerald-300 border-emerald-500/30 hover:bg-emerald-500/25',
          icon: <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />,
          next: 'Pending'
        };
      case 'In Progress':
        return {
          badge: 'bg-amber-500/15 text-amber-300 border-amber-500/30 hover:bg-amber-500/25',
          icon: <Clock className="w-3.5 h-3.5 text-amber-400" />,
          next: 'Completed'
        };
      default:
        return {
          badge: 'bg-zinc-800/80 text-zinc-400 border-zinc-700/80 hover:bg-zinc-800',
          icon: <AlertCircle className="w-3.5 h-3.5 text-zinc-400" />,
          next: 'In Progress'
        };
    }
  };

  const statusConfig = getStatusConfig(question.status);

  return (
    <div className="group relative bg-zinc-900/70 hover:bg-zinc-900 border border-zinc-800/80 hover:border-zinc-700 rounded-2xl p-5 shadow-lg shadow-black/20 transition-all duration-200 flex flex-col justify-between">
      {/* Top row: Badges and Quick Actions */}
      <div>
        <div className="flex items-center justify-between gap-2 mb-3">
          <div className="flex items-center gap-1.5 flex-wrap">
            <span className={`px-2.5 py-0.5 rounded-lg text-[11px] font-semibold border ${getCategoryBadge(question.category)}`}>
              {question.category}
            </span>
            <span className={`px-2.5 py-0.5 rounded-lg text-[11px] font-medium border ${getDifficultyBadge(question.difficulty)}`}>
              {question.difficulty}
            </span>
          </div>

          {/* Status Quick-Toggle Button */}
          <button
            onClick={() => onToggleStatus(question.id, statusConfig.next)}
            title={`Current: ${question.status}. Click to change to ${statusConfig.next}`}
            className={`flex items-center gap-1.5 px-2.5 py-1 rounded-xl text-xs font-medium border transition-all cursor-pointer ${statusConfig.badge}`}
          >
            {statusConfig.icon}
            <span>{question.status}</span>
          </button>
        </div>

        {/* Question Title */}
        <h3 className="text-base font-semibold text-zinc-100 group-hover:text-white mb-2 leading-snug">
          {question.title}
        </h3>

        {/* Description snippet */}
        <p className="text-xs text-zinc-400 line-clamp-2 mb-4 leading-relaxed">
          {question.description || 'No description provided.'}
        </p>

        {/* Key Points preview */}
        {question.keyPoints && question.keyPoints.length > 0 && (
          <div className="mb-4 bg-zinc-950/60 rounded-xl p-2.5 border border-zinc-800/60">
            <span className="text-[10px] font-bold uppercase tracking-wider text-zinc-400 mb-1 block">
              Key Discussion Focus
            </span>
            <ul className="space-y-1">
              {question.keyPoints.slice(0, 2).map((point, idx) => (
                <li key={idx} className="text-xs text-zinc-300 flex items-start gap-1.5">
                  <span className="text-orange-500 font-bold">•</span>
                  <span className="truncate">{point}</span>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>

      {/* Footer / Action Toolbar */}
      <div className="pt-3 border-t border-zinc-800/80 flex items-center justify-between text-xs text-zinc-400">
        <div className="flex items-center gap-2">
          {question.link ? (
            <a
              href={question.link}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1 text-orange-400 hover:text-orange-300 font-medium transition-colors"
            >
              <span>Practice / Link</span>
              <ExternalLink className="w-3 h-3" />
            </a>
          ) : (
            <span className="text-zinc-400 text-[11px]">Interview Prep Q&A</span>
          )}
        </div>

        <div className="flex items-center gap-1">
          <button
            onClick={() => onViewDetails(question)}
            title="View Details & Notes"
            className="p-1.5 rounded-lg text-zinc-400 hover:text-zinc-200 hover:bg-zinc-800 transition-colors"
          >
            <Eye className="w-3.5 h-3.5" />
          </button>
          <button
            onClick={() => onEdit(question)}
            title="Edit Question"
            className="p-1.5 rounded-lg text-zinc-400 hover:text-zinc-200 hover:bg-zinc-800 transition-colors"
          >
            <Edit3 className="w-3.5 h-3.5" />
          </button>
          <button
            onClick={() => onDelete(question.id)}
            title="Delete Question"
            className="p-1.5 rounded-lg text-zinc-400 hover:text-rose-400 hover:bg-rose-500/10 transition-colors"
          >
            <Trash2 className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  );
}
