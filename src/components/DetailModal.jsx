import React from 'react';
import { X, ExternalLink, Calendar, CheckCircle2, Clock, AlertCircle } from 'lucide-react';

export default function DetailModal({ question, isOpen, onClose }) {
  if (!isOpen || !question) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-fade-in">
      <div className="bg-zinc-900 border border-zinc-800 w-full max-w-2xl rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[85vh]">
        {/* Header */}
        <div className="p-6 border-b border-zinc-800 flex items-start justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 mb-2 flex-wrap">
              <span className="px-2.5 py-0.5 rounded-lg text-xs font-semibold bg-orange-500/10 text-orange-400 border border-orange-500/20">
                {question.category}
              </span>
              <span className="px-2.5 py-0.5 rounded-lg text-xs font-medium bg-zinc-800 text-zinc-300 border border-zinc-700">
                {question.difficulty}
              </span>
              <span className={`px-2.5 py-0.5 rounded-lg text-xs font-medium border ${
                question.status === 'Completed'
                  ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30'
                  : question.status === 'In Progress'
                  ? 'bg-amber-500/10 text-amber-400 border-amber-500/30'
                  : 'bg-zinc-800 text-zinc-400 border-zinc-700'
              }`}>
                {question.status}
              </span>
            </div>
            <h2 className="text-xl font-bold text-white tracking-tight">{question.title}</h2>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-lg text-zinc-400 hover:text-white hover:bg-zinc-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 overflow-y-auto space-y-6">
          {/* Description */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-zinc-400 mb-2">
              Problem Description / Interview Prompt
            </h4>
            <div className="bg-zinc-950 p-4 rounded-xl border border-zinc-800/80 text-sm text-zinc-200 leading-relaxed">
              {question.description || 'No description provided.'}
            </div>
          </div>

          {/* Key Discussion Points */}
          {question.keyPoints && question.keyPoints.length > 0 && (
            <div>
              <h4 className="text-xs font-bold uppercase tracking-wider text-zinc-400 mb-2">
                Key Technical Concepts & Follow-Ups
              </h4>
              <div className="bg-zinc-950/80 p-4 rounded-xl border border-zinc-800/80">
                <ul className="space-y-2">
                  {question.keyPoints.map((pt, idx) => (
                    <li key={idx} className="text-sm text-zinc-300 flex items-start gap-2.5">
                      <span className="text-orange-500 font-bold mt-0.5">•</span>
                      <span>{pt}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          )}

          {/* External Link */}
          {question.link && (
            <div>
              <h4 className="text-xs font-bold uppercase tracking-wider text-zinc-400 mb-2">
                Resource / Submission Link
              </h4>
              <a
                href={question.link}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-orange-500/10 hover:bg-orange-500/20 text-orange-400 border border-orange-500/30 text-sm font-semibold transition-colors"
              >
                <span>Open Problem on LeetCode</span>
                <ExternalLink className="w-4 h-4" />
              </a>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-zinc-800 bg-zinc-950/50 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-2 rounded-xl text-xs sm:text-sm font-medium text-zinc-300 hover:text-white bg-zinc-800 hover:bg-zinc-700 transition-colors"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}

