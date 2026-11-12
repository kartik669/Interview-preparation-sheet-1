# Sheryians Cohort 3.0: Sheet 01 Complete Submission & Recording Guide

This step-by-step guide walks you through completing the requirements for **Interview Preparation Sheet 1** and submitting it on **WorkDir** (`learn.sheryians.com/tasks`).

---

## 1. WorkDir Submission Form Breakdown
When you click **Submit Task** on WorkDir, you will see 4 fields:
1. **Repository URL \***: Your public GitHub repository link (e.g. `https://github.com/kartik-sakharkar/interview-practice-tracker`).
2. **Live URL \***: The deployed URL of your Machine Coding project on Vercel or Netlify (e.g. `https://interview-practice-tracker.vercel.app`).
3. **Google Drive Link \***: Link to your Google Drive folder set to **"Anyone with the link can view"**.
4. **Notes**: A clear summary for your mentor/evaluator.

---

## 2. Google Drive Setup (Screenshots & Recordings)

### Step 1: Create the Folder Structure in Google Drive
Create a main folder named:
```
Kartik Sakharkar - Sheet 01 Submission
├── Sheet 01 → DSA
│   ├── 01_Two_Sum_Accepted.png
│   ├── 02_Remove_Duplicates_Accepted.png
│   ├── 03_Move_Zeroes_Accepted.png
│   ├── 04_Rotate_Array_Accepted.png
│   └── 05_3Sum_Accepted.png
└── Recordings
    ├── Git_And_FullStack_Self_Recording.mp4
    └── Machine_Coding_Project_Demo.mp4
```

### Step 2: DSA Screenshots
1. Open each problem on LeetCode:
   - [LC 1: Two Sum](https://leetcode.com/problems/two-sum/)
   - [LC 26: Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
   - [LC 283: Move Zeroes](https://leetcode.com/problems/move-zeroes/)
   - [LC 189: Rotate Array](https://leetcode.com/problems/rotate-array/)
   - [LC 15: 3Sum](https://leetcode.com/problems/3sum/)
2. Paste the optimal solutions from `docs/SECTION_1_DSA_SOLUTIONS.md` and hit **Submit**.
3. Once you see **"Accepted"** (with Runtime and Memory beats percentage), take a clear screenshot showing:
   - Problem Title
   - Green "Accepted" status badge
   - Submission time & runtime stats
4. Upload all 5 screenshots into the `Sheet 01 → DSA` folder.

### Step 3: Self-Recording Video (Sections 2 & 3)
According to the Sheryians guidelines:
- **Length**: 2–4 minutes.
- **Tools**: Loom, OBS Studio, or Windows Game Bar (`Win + Alt + R`).
- **Format**: Ask the question aloud, then explain your answer naturally (do not just read text).
- **Suggested Questions to Speak On**:
  - *Git*: Scenario 1 (Wrong branch: 4 commits on main) and Scenario 3 (Secret committed).
  - *Full-Stack*: Question 1 (Event Loop & Microtask vs Macrotask) and Question 4 (MongoDB race condition & unique index).

### Step 4: Machine Coding Demo Video (1–2 minutes)
- Show the app running on localhost or Vercel.
- Highlight features:
  - Metric cards (Total, Completed, Progress percentage).
  - Add a new question with category, difficulty, and status.
  - Search by keyword and filter by category or status.
  - Toggle a question from Pending -> Completed to show the progress bar update dynamically.
  - Refresh the page to demonstrate LocalStorage persistence.

### Step 5: Make Google Drive Link Public
1. Right-click your main folder `Kartik Sakharkar - Sheet 01 Submission`.
2. Click **Share** -> Change general access from *Restricted* to **"Anyone with the link" (Viewer)**.
3. Click **Copy link**.

---

## 3. GitHub & Vercel Deployment

### Push to GitHub:
```bash
git init
git add .
git commit -m "feat: complete Interview Preparation Sheet 01 with Interview Practice Tracker"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

### Deploy to Vercel in 2 Minutes:
1. Go to [https://vercel.com](https://vercel.com) and log in with GitHub.
2. Click **Add New...** -> **Project**.
3. Select your repository and click **Import**.
4. Framework Preset will auto-detect **Vite**.
5. Click **Deploy**.
6. Copy your live URL (e.g., `https://interview-practice-tracker-rho.vercel.app`).

---

## 4. WorkDir Submission Template (Copy & Paste)

When submitting on `learn.sheryians.com/tasks`:

- **Repository URL**: `https://github.com/<your-username>/interview-practice-tracker`
- **Live URL**: `https://<your-project>.vercel.app`
- **Google Drive Link Link**: `https://drive.google.com/drive/folders/<your-folder-id>?usp=sharing`
- **Notes**:
```text
Hi Mentor,

Here is my submission for Interview Preparation Sheet 01 (Cohort 3.0):

1. Section 1 (DSA): Solved all 5 LeetCode problems (Two Sum, Remove Duplicates, Move Zeroes, Rotate Array, 3Sum). All 5 Accepted screenshots are organized inside the 'Sheet 01 → DSA' Google Drive folder.
2. Section 2 & 3 (Git & Full-Stack): Documented detailed, interview-ready answers with follow-ups in the repository under /docs. Also recorded a self-interview video uploaded to Drive.
3. Section 4 (Machine Coding): Built and deployed the 'Interview Practice Tracker' using React, Tailwind CSS, Lucide Icons, and LocalStorage persistence.

Thank you!
```
