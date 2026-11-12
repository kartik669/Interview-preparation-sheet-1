import React from 'react';
import { SearchX, Inbox, Plus, RotateCcw } from 'lucide-react';

export default function EmptyState({ isSearching, onResetFilters, onAddQuestion, onResetDefaults }) {
  if (isSearching) {
    return (
      <div className="bg-zinc-900/40 border border-zinc-800/80 rounded-2xl p-10 text-center my-6 flex flex-col items-center justify-center">
        <div className="w-14 h-14 rounded-2xl bg-zinc-800/80 flex items-center justify-center text-zinc-400 mb-4 border border-zinc-700">
          <SearchX className="w-7 h-7 text-zinc-400" />
        </div>
        <h3 className="text-base font-bold text-white mb-1">No matching questions found</h3>
        <p className="text-xs text-zinc-400 max-w-sm mb-5">
          We couldn't find any questions matching your active search keywords or filter criteria.
        </p>
        <button
          onClick={onResetFilters}
          className="px-4 py-2 rounded-xl text-xs font-semibold text-orange-400 hover:text-white bg-orange-500/10 hover:bg-orange-500 border border-orange-500/30 transition-all"
        >
          Clear All Filters
        </button>
      </div>
    );
  }

  return (
    <div className="bg-zinc-900/40 border border-zinc-800/80 rounded-2xl p-12 text-center my-6 flex flex-col items-center justify-center">
      <div className="w-16 h-16 rounded-2xl bg-orange-500/10 flex items-center justify-center text-orange-400 mb-4 border border-orange-500/20">
        <Inbox className="w-8 h-8 text-orange-400" />
      </div>
      <h3 className="text-lg font-bold text-white mb-1.5">No questions tracked yet</h3>
      <p className="text-xs text-zinc-400 max-w-sm mb-6">
        Your question tracker is currently empty. You can add custom questions or populate the Sheet 01 questions.
      </p>
      <div className="flex items-center gap-3">
        <button
          onClick={onAddQuestion}
          className="flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold text-white bg-orange-500 hover:bg-orange-600 transition-colors"
        >
          <Plus className="w-4 h-4" />
          <span>Add Custom Question</span>
        </button>
        <button
          onClick={onResetDefaults}
          className="flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-medium text-zinc-300 hover:text-white bg-zinc-800 hover:bg-zinc-700 transition-colors border border-zinc-700"
        >
          <RotateCcw className="w-4 h-4" />
          <span>Load Sheet 01 Defaults</span>
        </button>
      </div>
    </div>
  );
}
