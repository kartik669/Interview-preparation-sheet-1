# 🚀 Interview Practice Tracker (Sheryians Sheet 01)

A responsive, feature-rich dashboard built for students to organize, track, and master their weekly interview preparation across Data Structures & Algorithms (LeetCode), Git & GitHub scenario questions, Full-Stack Technical interview questions, and Machine Coding challenges.

Built as part of **Sheryians Coding School (Cohort 3.0) — Sheet 01 Weekly Interview Preparation**.

---

## 🌟 Live Demo & Video Walkthrough
- 🌐 **Live Deployed App**: [Deploy with Vercel](#-deployment-guide) (Ready for 1-click Vercel / Netlify deployment)
- 📹 **Demo Video Guide**: Included in [`docs/SUBMISSION_AND_RECORDING_GUIDE.md`](./docs/SUBMISSION_AND_RECORDING_GUIDE.md)

---

## 📑 Repository Structure & Sheet 01 Deliverables

This repository is organized into comprehensive modules covering all 4 sections of Sheet 01:

```
├── docs/
│   ├── SECTION_1_DSA_SOLUTIONS.md        # LeetCode 1, 26, 283, 189, 15 optimal solutions & complexity
│   ├── SECTION_2_GIT_GITHUB_ANSWERS.md   # 5 Git scenario-based interview answers & follow-ups
│   ├── SECTION_3_FULLSTACK_ANSWERS.md    # 5 Full-Stack interview answers (JS, React, Express, Mongo, ImageKit)
│   └── SUBMISSION_AND_RECORDING_GUIDE.md # Step-by-step Drive folder structure, recording script & WorkDir guide
├── src/
│   ├── components/
│   │   ├── DashboardStats.jsx            # Progress bar, DSA metrics, Technical stats & Machine Coding toggle
│   │   ├── DetailModal.jsx               # Deep-dive question modal with concepts & LeetCode link
│   │   ├── EmptyState.jsx                # Friendly zero-state & no-search-results state
│   │   ├── FilterBar.jsx                 # Category pills, difficulty/status dropdowns & live search
│   │   ├── Header.jsx                    # Navigation, branding & quick actions
│   │   ├── QuestionCard.jsx              # Responsive card with one-click status toggle & edit/delete
│   │   └── QuestionModal.jsx             # Add & Edit form with validations
│   ├── constants/
│   │   └── initialData.js                # Pre-populated with all 16 questions from Sheet 01
│   ├── App.jsx                           # Core app logic, LocalStorage sync & confetti celebration
│   ├── index.css                         # Tailwind CSS styling & custom scrollbars
│   └── main.jsx
├── dist/                                 # Production build output
├── index.html
├── package.json
├── tailwind.config.js
└── vite.config.js
```

---

## 🎯 Features Implemented

### 1. 📊 Interactive Dashboard Metrics
- **Real-time Completion Rate**: Visual gradient progress bar dynamically updating percentage based on solved questions.
- **DSA Problem Tracker**: Tracks completed LeetCode problems out of total required.
- **Technical Q&A Progress**: Monitors progress across Git scenarios and Full-Stack questions.
- **Machine Coding Status Pill**: Quick toggle to switch status between *Pending*, *In Progress*, and *Completed*.
- **Confetti Celebration**: Fires festive confetti effects upon reaching 100% completion!

### 2. 🔍 Real-Time Search & Multi-Level Filtering
- **Live Search**: Instant keyword filtering across question titles, problem prompts, and key discussion focus points.
- **Category Filter Pills**: Filter by `All`, `DSA`, `Git`, `Technical`, and `Machine Coding` with live item counts.
- **Status Filter**: Filter by `Completed`, `In Progress`, and `Pending`.
- **Difficulty Filter**: Filter by `Easy`, `Medium`, and `Hard`.
- **One-Click Clear**: Quickly reset active filters back to default.

### 3. 📝 Question Management & Form Validation
- **Add New Question**: Modal form to add custom practice questions or mock interview questions.
- **Form Validations**: Required title (min 3 chars), category, difficulty, status, and URL syntax checking.
- **One-Click Quick Toggle**: Directly click any status badge on a card to cycle through statuses (*Pending → In Progress → Completed*).
- **Edit & Delete**: Full CRUD capabilities for any card.
- **Detail View**: Full modal view displaying the detailed problem prompt, key technical concepts, and external practice link.

### 4. 💾 LocalStorage Persistence
- All question modifications, newly added questions, status updates, and deletions are saved to the browser's `localStorage` (`sheryians_interview_tracker_sheet01`).
- Data remains intact across page refreshes and browser restarts.
- Includes a **"Reset Defaults"** button to restore the original 16 Sheet 01 questions at any time.

### 5. 📱 Responsive Modern UI
- Clean dark theme matching Sheryians aesthetics (`#09090b` zinc dark with warm orange `#f97316` brand accents).
- Fully responsive on mobile phones, tablets, laptops, and ultra-wide desktop monitors.
- Empty states for zero questions and no-search-results states with recovery actions.

---

## 🛠️ Tech Stack
- **Frontend Library**: React 18
- **Build Tool**: Vite 5
- **Styling**: Tailwind CSS 3
- **Icons**: Lucide React
- **Animations / Effects**: Canvas Confetti
- **Storage**: Browser `localStorage` API

---

## ⚙️ Installation & Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/interview-practice-tracker.git
   cd interview-practice-tracker
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   ```
   Open [http://localhost:3000](http://localhost:3000) in your browser.

4. **Create a production build**:
   ```bash
   npm run build
   ```
   Preview the production build locally:
   ```bash
   npm run preview
   ```

---

## 🚀 Deployment Guide (Vercel)

1. Push your repository to your GitHub account:
   ```bash
   git init
   git add .
   git commit -m "feat: complete Interview Preparation Sheet 01"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```
2. Log in to [Vercel](https://vercel.com) and click **"Add New Project"**.
3. Import this GitHub repository. Vercel automatically detects the **Vite** preset.
4. Click **Deploy**. Your app will be live with an HTTPS URL in under 60 seconds!

---

## 📌 Assumptions & Architectural Decisions
1. **Client-Side Storage**: In line with the Machine Coding requirements ("Backend not required"), data persistence is handled completely via browser `localStorage`.
2. **Sheet 01 Seed Data**: Initialized with all 16 questions from Sheet 01 to allow mentors and peers to immediately evaluate the interface without manual data entry.
3. **Optimistic Updates**: Status changes take effect immediately in the UI and sync synchronously with `localStorage`.

