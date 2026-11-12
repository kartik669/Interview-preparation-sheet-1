import React from 'react';
import { Search, X, SlidersHorizontal } from 'lucide-react';
import { CATEGORIES, STATUSES, DIFFICULTIES } from '../constants/initialData';

export default function FilterBar({
  searchQuery,
  setSearchQuery,
  selectedCategory,
  setSelectedCategory,
  selectedStatus,
  setSelectedStatus,
  selectedDifficulty,
  setSelectedDifficulty,
  categoryCounts,
  onResetFilters
}) {
  const hasActiveFilters = searchQuery !== '' || selectedCategory !== 'All' || selectedStatus !== 'All' || selectedDifficulty !== 'All';

  return (
    <div className="bg-zinc-900/60 border border-zinc-800 rounded-2xl p-4 sm:p-5 mb-6 backdrop-blur-sm">
      {/* Search Input & Reset Filter */}
      <div className="flex flex-col sm:flex-row items-center gap-3 mb-4">
        <div className="relative w-full">
          <Search className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-zinc-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search questions by title, concepts, or keywords..."
            className="w-full bg-zinc-950 border border-zinc-800 rounded-xl pl-10 pr-10 py-2.5 text-sm text-zinc-100 placeholder:text-zinc-500 focus:outline-none focus:border-orange-500/80 focus:ring-1 focus:ring-orange-500/50 transition-all"
          />
          {searchQuery && (
            <button
              onClick={() => setSearchQuery('')}
              className="absolute right-3.5 top-1/2 -translate-y-1/2 text-zinc-500 hover:text-zinc-300"
            >
              <X className="w-4 h-4" />
            </button>
          )}
        </div>

        {hasActiveFilters && (
          <button
            onClick={onResetFilters}
            className="w-full sm:w-auto px-3 py-2 text-xs font-semibold text-orange-400 hover:text-orange-300 hover:bg-orange-500/10 rounded-lg border border-orange-500/20 whitespace-nowrap transition-colors flex items-center justify-center gap-1.5"
          >
            <X className="w-3.5 h-3.5" />
            Clear Filters
          </button>
        )}
      </div>

      {/* Category Pills */}
      <div className="flex flex-wrap items-center gap-2 mb-4 pb-3 border-b border-zinc-800/80">
        <span className="text-xs font-medium text-zinc-400 mr-1 flex items-center gap-1">
          <SlidersHorizontal className="w-3 h-3 text-zinc-400" />
          Category:
        </span>
        {CATEGORIES.map((cat) => {
          const isSelected = selectedCategory === cat;
          const count = categoryCounts[cat] || 0;
          return (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-3 py-1.5 rounded-xl text-xs font-medium transition-all flex items-center gap-1.5 ${
                isSelected
                  ? 'bg-orange-500 text-white font-semibold shadow-md shadow-orange-500/20'
                  : 'bg-zinc-800/70 text-zinc-400 hover:text-zinc-200 hover:bg-zinc-800'
              }`}
            >
              <span>{cat}</span>
              <span className={`text-[10px] px-1.5 py-0.2 rounded-full ${isSelected ? 'bg-orange-600/80 text-white' : 'bg-zinc-900 text-zinc-500'}`}>
                {count}
              </span>
            </button>
          );
        })}
      </div>

      {/* Sub-Filters: Status & Difficulty Dropdowns */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
        {/* Status Filter */}
        <div className="flex items-center gap-2">
          <label className="text-xs text-zinc-400 min-w-[55px]">Status:</label>
          <div className="grid grid-cols-4 gap-1 w-full bg-zinc-950 p-1 rounded-xl border border-zinc-800">
            {STATUSES.map((st) => (
              <button
                key={st}
                onClick={() => setSelectedStatus(st)}
                className={`py-1 text-center rounded-lg text-xs font-medium transition-colors ${
                  selectedStatus === st
                    ? 'bg-zinc-800 text-white shadow-sm'
                    : 'text-zinc-400 hover:text-zinc-200'
                }`}
              >
                {st}
              </button>
            ))}
          </div>
        </div>

        {/* Difficulty Filter */}
        <div className="flex items-center gap-2">
          <label className="text-xs text-zinc-400 min-w-[55px]">Difficulty:</label>
          <div className="grid grid-cols-4 gap-1 w-full bg-zinc-950 p-1 rounded-xl border border-zinc-800">
            {DIFFICULTIES.map((diff) => (
              <button
                key={diff}
                onClick={() => setSelectedDifficulty(diff)}
                className={`py-1 text-center rounded-lg text-xs font-medium transition-colors ${
                  selectedDifficulty === diff
                    ? 'bg-zinc-800 text-white shadow-sm'
                    : 'text-zinc-400 hover:text-zinc-200'
                }`}
              >
                {diff}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

