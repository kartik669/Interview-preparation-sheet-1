export const INITIAL_QUESTIONS = [
  // SECTION 1: DSA (LeetCode)
  {
    id: 'dsa-1',
    title: 'Two Sum',
    category: 'DSA',
    difficulty: 'Easy',
    status: 'Completed',
    link: 'https://leetcode.com/problems/two-sum/',
    description: 'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.',
    keyPoints: [
      'One-pass Hash Map approach (O(n) time, O(n) space)',
      'Calculate complement = target - nums[i]',
      'Store visited value -> index mapping'
    ],
    createdAt: '2026-10-14T10:00:00.000Z'
  },
  {
    id: 'dsa-2',
    title: 'Remove Duplicates from Sorted Array',
    category: 'DSA',
    difficulty: 'Easy',
    status: 'Completed',
    link: 'https://leetcode.com/problems/remove-duplicates-from-sorted-array/',
    description: 'Remove duplicates in-place such that each unique element appears only once. Relative order of elements should be kept.',
    keyPoints: [
      'Two-pointer technique in-place (O(n) time, O(1) space)',
      'Slow pointer k tracks the position of last unique element',
      'Fast pointer i scans array'
    ],
    createdAt: '2026-10-14T11:00:00.000Z'
  },
  {
    id: 'dsa-3',
    title: 'Move Zeroes',
    category: 'DSA',
    difficulty: 'Easy',
    status: 'Completed',
    link: 'https://leetcode.com/problems/move-zeroes/',
    description: 'Move all 0s to the end of the array while maintaining the relative order of non-zero elements in-place.',
    keyPoints: [
      'Two-pointer swap technique (O(n) time, O(1) space)',
      'Pointer lastNonZero tracks write destination',
      'Swap non-zero with lastNonZero on each encounter'
    ],
    createdAt: '2026-10-15T09:30:00.000Z'
  },
  {
    id: 'dsa-4',
    title: 'Rotate Array',
    category: 'DSA',
    difficulty: 'Medium',
    status: 'In Progress',
    link: 'https://leetcode.com/problems/rotate-array/',
    description: 'Rotate an array to the right by k steps, where k is non-negative.',
    keyPoints: [
      'Triple reversal algorithm (O(n) time, O(1) space)',
      'Normalize k = k % n',
      'Reverse all, reverse first k, reverse remainder'
    ],
    createdAt: '2026-10-15T14:00:00.000Z'
  },
  {
    id: 'dsa-5',
    title: '3Sum',
    category: 'DSA',
    difficulty: 'Medium',
    status: 'In Progress',
    link: 'https://leetcode.com/problems/3sum/',
    description: 'Find all unique triplets [nums[i], nums[j], nums[k]] that sum up to 0 without containing duplicate triplets.',
    keyPoints: [
      'Sort + Two Pointers (O(n²) time, O(1) extra space)',
      'Fixed pointer i with two-pointer search on remaining subarray',
      'Skip duplicate values on both i, left, and right'
    ],
    createdAt: '2026-10-15T16:20:00.000Z'
  },

  // SECTION 2: Git & GitHub
  {
    id: 'git-1',
    title: 'Wrong Branch, Correct Work (4 Commits on Main)',
    category: 'Git',
    difficulty: 'Medium',
    status: 'Completed',
    link: '',
    description: 'Accidentally made 4 commits on main instead of feature branch. Move work safely to feature branch.',
    keyPoints: [
      'git checkout -b feature/branch (creates pointer at current HEAD)',
      'git checkout main && git reset --hard HEAD~4 (resets main locally)',
      'Follow-up: Handle remote push using git revert or coordinate with team'
    ],
    createdAt: '2026-10-16T09:00:00.000Z'
  },
  {
    id: 'git-2',
    title: 'Merge Conflict During PR',
    category: 'Git',
    difficulty: 'Medium',
    status: 'In Progress',
    link: '',
    description: 'Feature branch has a merge conflict with main just before PR is merged. Safe resolution walkthrough.',
    keyPoints: [
      'git checkout feature && git rebase main or git merge main',
      'Resolve markers (<<<<<<< HEAD ... >>>>>>>)',
      'Verify with unit tests & git diff before git push --force-with-lease'
    ],
    createdAt: '2026-10-16T11:00:00.000Z'
  },
  {
    id: 'git-3',
    title: 'Secret Accidentally Committed',
    category: 'Git',
    difficulty: 'Hard',
    status: 'Pending',
    link: '',
    description: 'Developer committed an API key to GitHub and realized immediately. Required remediation steps.',
    keyPoints: [
      'Immediately revoke & rotate the exposed key at the provider',
      'Purge from git history with git-filter-repo or BFG Repo-Cleaner',
      'Prevent future leaks via Husky + Gitleaks pre-commit hooks'
    ],
    createdAt: '2026-10-16T12:30:00.000Z'
  },
  {
    id: 'git-4',
    title: 'PR Review With New Changes',
    category: 'Git',
    difficulty: 'Easy',
    status: 'Pending',
    link: '',
    description: 'Reviewer asks for changes after pushing commits. Keeping the review understandable.',
    keyPoints: [
      'Push new descriptive fix commits during review so reviewer sees diff',
      'Squash into clean atomic commits only upon final merge approval',
      'Avoid uncoordinated force-pushing on shared branches'
    ],
    createdAt: '2026-10-16T14:00:00.000Z'
  },
  {
    id: 'git-5',
    title: 'Recovering Lost Local Work (Git Reflog)',
    category: 'Git',
    difficulty: 'Medium',
    status: 'Pending',
    link: '',
    description: 'Ran a Git command incorrectly and branch no longer points to commit containing yesterday work.',
    keyPoints: [
      'Use git reflog to trace all HEAD pointer movements',
      'Inspect dangling commit with git show <SHA>',
      'Recover via git branch recovery <SHA> or git reset --hard <SHA>'
    ],
    createdAt: '2026-10-16T15:00:00.000Z'
  },

  // SECTION 3: Full-Stack Technical Interview
  {
    id: 'tech-1',
    title: 'JavaScript Async Flow & Event Loop',
    category: 'Technical',
    difficulty: 'Medium',
    status: 'Completed',
    link: '',
    description: 'Explain Event Loop execution order when fetch(), UI update, and setTimeout() are combined.',
    keyPoints: [
      'Microtask queue (Promises) has strict priority over Macrotask queue (setTimeout)',
      'All microtasks drain completely before the next macrotask runs',
      'Synchronous long loops block Call Stack and freeze the UI rendering thread'
    ],
    createdAt: '2026-10-16T16:00:00.000Z'
  },
  {
    id: 'tech-2',
    title: 'React Unnecessary Re-render Optimization',
    category: 'Technical',
    difficulty: 'Medium',
    status: 'In Progress',
    link: '',
    description: 'Parent component re-renders frequently causing slow child components. Investigation and fixes.',
    keyPoints: [
      'Profile with React DevTools Profiler ("Record why each component rendered")',
      'React.memo for shallow prop comparison + useCallback for stable function refs',
      'Avoid premature memoization everywhere due to memory and closure overhead'
    ],
    createdAt: '2026-10-16T17:00:00.000Z'
  },
  {
    id: 'tech-3',
    title: 'REST API + Express Request Flow (401 Debugging)',
    category: 'Technical',
    difficulty: 'Easy',
    status: 'Completed',
    link: '',
    description: 'Protected GET /api/profile endpoint returning 401 for logged-in user. Complete flow & debugging.',
    keyPoints: [
      'Request cycle: Client -> CORS -> Parser -> Auth Middleware -> Controller',
      'Check Bearer token format, JWT expiration, secret mismatch, CORS headers',
      '401 Unauthorized (Identity missing) vs 403 Forbidden (Insufficient rights)'
    ],
    createdAt: '2026-10-17T09:00:00.000Z'
  },
  {
    id: 'tech-4',
    title: 'MongoDB + Mongoose Duplicate Data Race Condition',
    category: 'Technical',
    difficulty: 'Medium',
    status: 'Pending',
    link: '',
    description: 'Registration API allowing two users with same email under concurrent race condition.',
    keyPoints: [
      'Application-level findOne is non-atomic and vulnerable to TOCTOU race condition',
      'Enforce unique B-Tree index at MongoDB level (unique: true)',
      'Catch error.code === 11000 in Express error handler and return 409 Conflict'
    ],
    createdAt: '2026-10-17T10:30:00.000Z'
  },
  {
    id: 'tech-5',
    title: 'Auth + Authorization + ImageKit Security Flow',
    category: 'Technical',
    difficulty: 'Hard',
    status: 'Pending',
    link: '',
    description: 'Prevent student from accessing another student private resource/upload (IDOR) & ImageKit integration.',
    keyPoints: [
      'Derive identity strictly from authenticated JWT (req.user.id), never URL param',
      'Scope DB queries: Submission.findOne({ _id: id, studentId: req.user.id })',
      'ImageKit direct upload using backend-generated HMAC auth signatures'
    ],
    createdAt: '2026-10-17T11:45:00.000Z'
  },

  // SECTION 4: Machine Coding
  {
    id: 'mc-1',
    title: 'Interview Practice Tracker (Machine Coding)',
    category: 'Machine Coding',
    difficulty: 'Medium',
    status: 'In Progress',
    link: 'https://github.com/kartik-sakharkar/interview-practice-tracker',
    description: 'Responsive dashboard to track weekly interview preparation work with search, filters, progress, and local persistence.',
    keyPoints: [
      'Dashboard stats: Total, Completed DSA, Completed Tech, Machine Coding status',
      'Category/Status/Difficulty filtering and live title search',
      'Full LocalStorage persistence and empty/no-results states'
    ],
    createdAt: '2026-10-17T14:00:00.000Z'
  }
];

export const CATEGORIES = ['All', 'DSA', 'Git', 'Technical', 'Machine Coding'];
export const STATUSES = ['All', 'Completed', 'In Progress', 'Pending'];
export const DIFFICULTIES = ['All', 'Easy', 'Medium', 'Hard'];
