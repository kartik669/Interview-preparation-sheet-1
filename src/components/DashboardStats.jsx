import React from 'react';
import { CheckCircle2, Code2, GitBranch, Cpu, Trophy, TrendingUp, AlertCircle } from 'lucide-react';

export default function DashboardStats({ questions, onToggleMachineCoding }) {
  const total = questions.length;
  const completed = questions.filter(q => q.status === 'Completed').length;
  const inProgress = questions.filter(q => q.status === 'In Progress').length;
  const overallPercentage = total > 0 ? Math.round((completed / total) * 100) : 0;

  // DSA Stats
  const dsaQuestions = questions.filter(q => q.category === 'DSA');
  const dsaTotal = dsaQuestions.length;
  const dsaCompleted = dsaQuestions.filter(q => q.status === 'Completed').length;
  const dsaPercent = dsaTotal > 0 ? Math.round((dsaCompleted / dsaTotal) * 100) : 0;

  // Interview Questions (Git + Technical)
  const interviewQuestions = questions.filter(q => q.category === 'Git' || q.category === 'Technical');
  const interviewTotal = interviewQuestions.length;
  const interviewCompleted = interviewQuestions.filter(q => q.status === 'Completed').length;
  const interviewPercent = interviewTotal > 0 ? Math.round((interviewCompleted / interviewTotal) * 100) : 0;

  // Machine Coding Item
  const machineCodingItem = questions.find(q => q.category === 'Machine Coding');
  const mcStatus = machineCodingItem ? machineCodingItem.status : 'Pending';

  const getStatusBadge = (status) => {
    switch (status) {
      case 'Completed':
        return 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30';
      case 'In Progress':
        return 'bg-amber-500/10 text-amber-400 border-amber-500/30';
      default:
        return 'bg-zinc-800 text-zinc-400 border-zinc-700';
    }
  };

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
      {/* 1. Overall Progress Card */}
      <div className="relative overflow-hidden bg-zinc-900/80 border border-zinc-800/80 rounded-2xl p-5 shadow-xl shadow-black/40 backdrop-blur-sm">
        <div className="flex items-center justify-between mb-3">
          <span className="text-xs font-semibold uppercase tracking-wider text-zinc-400">Overall Progress</span>
          <div className="w-8 h-8 rounded-lg bg-orange-500/10 text-orange-400 flex items-center justify-center border border-orange-500/20">
            <Trophy className="w-4 h-4" />
          </div>
        </div>
        <div className="flex items-baseline gap-2 mb-3">
          <span className="text-3xl font-extrabold text-white tracking-tight">{overallPercentage}%</span>
          <span className="text-xs text-zinc-400">({completed}/{total} solved)</span>
        </div>
        <div className="w-full bg-zinc-800 rounded-full h-2.5 overflow-hidden">
          <div
            className="bg-gradient-to-r from-orange-500 to-amber-500 h-2.5 rounded-full transition-all duration-700 ease-out"
            style={{ width: `${overallPercentage}%` }}
          />
        </div>
        <div className="mt-2.5 flex items-center justify-between text-[11px] text-zinc-500">
          <span>{inProgress} in progress</span>
          <span>{total - completed - inProgress} pending</span>
        </div>
      </div>

      {/* 2. DSA Problems Card */}
      <div className="relative overflow-hidden bg-zinc-900/80 border border-zinc-800/80 rounded-2xl p-5 shadow-xl shadow-black/40 backdrop-blur-sm">
        <div className="flex items-center justify-between mb-3">
          <span className="text-xs font-semibold uppercase tracking-wider text-zinc-400">DSA (LeetCode)</span>
          <div className="w-8 h-8 rounded-lg bg-blue-500/10 text-blue-400 flex items-center justify-center border border-blue-500/20">
            <Code2 className="w-4 h-4" />
          </div>
        </div>
        <div className="flex items-baseline gap-2 mb-3">
          <span className="text-3xl font-extrabold text-white tracking-tight">{dsaCompleted}</span>
          <span className="text-sm text-zinc-400">/ {dsaTotal} problems</span>
        </div>
        <div className="w-full bg-zinc-800 rounded-full h-2.5 overflow-hidden">
          <div
            className="bg-blue-500 h-2.5 rounded-full transition-all duration-500 ease-out"
            style={{ width: `${dsaPercent}%` }}
          />
        </div>
        <p className="mt-2.5 text-[11px] text-zinc-400 flex items-center gap-1">
          <TrendingUp className="w-3.5 h-3.5 text-blue-400" />
          {dsaPercent === 100 ? 'All 5 DSA problems verified!' : `${5 - dsaCompleted} remaining for Drive upload`}
        </p>
      </div>

      {/* 3. Interview Questions Card (Git + Tech) */}
      <div className="relative overflow-hidden bg-zinc-900/80 border border-zinc-800/80 rounded-2xl p-5 shadow-xl shadow-black/40 backdrop-blur-sm">
        <div className="flex items-center justify-between mb-3">
          <span className="text-xs font-semibold uppercase tracking-wider text-zinc-400">Technical Q&A</span>
          <div className="w-8 h-8 rounded-lg bg-purple-500/10 text-purple-400 flex items-center justify-center border border-purple-500/20">
            <GitBranch className="w-4 h-4" />
          </div>
        </div>
        <div className="flex items-baseline gap-2 mb-3">
          <span className="text-3xl font-extrabold text-white tracking-tight">{interviewCompleted}</span>
          <span className="text-sm text-zinc-400">/ {interviewTotal} prepared</span>
        </div>
        <div className="w-full bg-zinc-800 rounded-full h-2.5 overflow-hidden">
          <div
            className="bg-purple-500 h-2.5 rounded-full transition-all duration-500 ease-out"
            style={{ width: `${interviewPercent}%` }}
          />
        </div>
        <p className="mt-2.5 text-[11px] text-zinc-400">
          5 Git scenarios + 5 Full-Stack technical
        </p>
      </div>

      {/* 4. Machine Coding Round Card */}
      <div className="relative overflow-hidden bg-zinc-900/80 border border-zinc-800/80 rounded-2xl p-5 shadow-xl shadow-black/40 backdrop-blur-sm">
        <div className="flex items-center justify-between mb-3">
          <span className="text-xs font-semibold uppercase tracking-wider text-zinc-400">Machine Coding</span>
          <div className="w-8 h-8 rounded-lg bg-emerald-500/10 text-emerald-400 flex items-center justify-center border border-emerald-500/20">
            <Cpu className="w-4 h-4" />
          </div>
        </div>
        <div className="flex items-center justify-between mb-3">
          <span className="text-lg font-bold text-white tracking-tight truncate max-w-[130px]">
            Practice Tracker
          </span>
          <button
            onClick={onToggleMachineCoding}
            title="Click to toggle status"
            className={`px-2.5 py-1 rounded-full text-xs font-medium border transition-colors cursor-pointer ${getStatusBadge(mcStatus)}`}
          >
            {mcStatus}
          </button>
        </div>
        <div className="w-full bg-zinc-800 rounded-full h-2.5 overflow-hidden">
          <div
            className={`h-2.5 rounded-full transition-all duration-500 ease-out ${
              mcStatus === 'Completed' ? 'w-full bg-emerald-500' : mcStatus === 'In Progress' ? 'w-2/3 bg-amber-500' : 'w-1/4 bg-zinc-600'
            }`}
          />
        </div>
        <p className="mt-2.5 text-[11px] text-zinc-400 flex items-center justify-between">
          <span>React + Vite + Tailwind</span>
          <span className="text-orange-400 font-medium">Toggle</span>
        </p>
      </div>
    </div>
  );
}
