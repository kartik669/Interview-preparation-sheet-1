# Section 2: Git & GitHub Scenario-Based Technical Interview Answers

Format: Designed specifically for technical interviews. Each scenario follows the required structure:
1. **What I Would Do** (Step-by-step commands & concrete workflow)
2. **Why** (Git internals & mechanisms)
3. **Follow-Up Questions & Answers** (Deep-dive technical considerations)

---

## Scenario 1: Wrong Branch, Correct Work
**Prompt**: *You accidentally made 4 commits on `main` instead of your feature branch. How would you move the work to the correct branch without losing it?*

### 1. What I Would Do
Assuming the commits are still only on my local machine:
```bash
# 1. Create and switch to the new feature branch from the current HEAD (which contains the 4 commits)
git checkout -b feature/my-feature

# 2. Switch back to main
git checkout main

# 3. Reset main back by 4 commits to restore it to the clean state
git reset --hard HEAD~4
```

### 2. Why
In Git, a branch is merely a lightweight, movable pointer (40-byte SHA-1/SHA-256 reference) to a specific commit. 
When we run `git checkout -b feature/my-feature`, Git creates a new branch pointer pointing to the current commit `HEAD` (holding all 4 commits). 
When we switch back to `main` and run `git reset --hard HEAD~4`, we move `main`'s pointer back 4 commits without deleting the commits from the object database because `feature/my-feature` is still referencing them.

### 3. Follow-Ups
- **Would your approach change if the commits were already pushed to the remote?**
  - **Yes, significantly.** If `main` is a shared branch and already pushed, running `git reset --hard` followed by a force-push (`git push --force`) rewrites public commit history, which can break other developers' local copies.
  - If force-pushing is prohibited or discouraged by team policy:
    1. Check out `feature/my-feature` at the current tip.
    2. On `main`, use `git revert HEAD~4..HEAD` to create 4 new inverse commits that undo the changes cleanly without rewriting history.
- **When would you use cherry-pick here?**
  - I would use `git cherry-pick` if the feature branch *already existed* prior to making those commits and had separate commits of its own:
    ```bash
    git checkout feature/my-feature
    git cherry-pick main~4..main
    git checkout main
    git reset --hard HEAD~4
    ```
- **What would you do if teammates were already using main?**
  - I would immediately notify the team via Slack/Discord to avoid anyone pulling the erroneous commits. If teammates have already pulled `main`, I would avoid `--force` push and instead use `git revert` on `main`, or coordinate a safe fast-forward synchronization after communicating clearly.

---

## Scenario 2: Merge Conflict During PR
**Prompt**: *Your feature branch has a merge conflict with `main` just before the PR is merged. Walk through the complete process of resolving it safely.*

### 1. What I Would Do
```bash
# 1. Ensure clean working directory and fetch the freshest main
git checkout main
git pull origin main

# 2. Switch to feature branch
git checkout feature/my-feature

# 3. Rebase onto main (or merge main into feature based on team convention)
git rebase main

# 4. Git will pause on conflicting files. Open files and inspect conflict markers:
# <<<<<<< HEAD (code from main)
# =======
# >>>>>>> feature-commit (code from feature)

# 5. Resolve conflicts manually in code editor, save files, and stage them:
git add <resolved-files>

# 6. Continue rebase (never commit during rebase):
git rebase --continue

# 7. Run full build and test suite locally:
npm run test && npm run build

# 8. Push to remote feature branch:
git push --force-with-lease origin feature/my-feature
```

### 2. Why
A merge conflict occurs when the same line of code in the same file was modified differently on both branches since their common ancestor (`merge-base`). Resolving it on the feature branch ensures the pull request preview updates cleanly and guarantees that the integration burden is solved before touching the production branch. Using `--force-with-lease` guarantees that we do not overwrite any remote commits pushed by collaborators that we haven't seen.

### 3. Follow-Ups
- **How do you verify that the conflict resolution did not break existing functionality?**
  1. **Automated Unit & Integration Tests**: Run `npm test` to verify assertions still hold.
  2. **Diff Verification**: Run `git diff main..feature/my-feature` to visually inspect that only intended changes exist and no incoming features from `main` were accidentally erased.
  3. **Local Runtime Smoke Test**: Start the dev server and test affected user flows manually.
- **Would you merge main into the feature branch or rebase? Explain the trade-off.**
  - **Rebase (`git rebase main`)**:
    - *Pros*: Linear, clean commit graph without redundant "Merge branch 'main' into feature" clutter. Makes `git bisect` much easier to identify bugs.
    - *Cons*: Rewrites commit SHAs, requiring `--force-with-lease`; can cause multiple conflict resolution passes if many commits touched the same lines.
  - **Merge (`git merge main`)**:
    - *Pros*: Completely non-destructive, preserves exact historical timestamp of when commits were created, safe on shared feature branches with multiple contributors.
    - *Cons*: Creates a cluttered, non-linear commit graph ("diamond history").
- **What should you do before pushing the resolved branch?**
  - Run the linter (`npm run lint`), run unit/e2e tests, check `git status` to ensure no leftover temporary files or unresolved markers exist, and inspect `git log -p -n 1` to confirm the final commit state.

---

## Scenario 3: Secret Accidentally Committed
**Prompt**: *A developer committed an API key to GitHub and immediately realizes the mistake. What steps should they take?*

### 1. What I Would Do
1. **Immediately Invalidate / Revoke the Key**: Go to the provider console (e.g., Stripe, AWS, OpenAI, GitHub) and revoke/delete the exposed credential immediately. Generate a new key.
2. **Purge the Secret from Git History**:
   - If the commit has NOT been pushed yet:
     ```bash
     # Remove secret from file, add to .env
     git commit --amend --no-edit
     ```
   - If already pushed to remote:
     Use tools like **BFG Repo-Cleaner** or **`git-filter-repo`** to scrub the secret from every commit, blob, and tree across all branches:
     ```bash
     git filter-repo --replace-text passwords.txt
     git push origin --force --all
     ```
3. **Audit Access Logs**: Check API provider request logs during the exposure window to check for unauthorized usage.
4. **Setup `.env` and `.gitignore`**: Place secret in `.env` and ensure `.env` is listed in `.gitignore`.

### 2. Why
Deleting the secret in a *new commit* leaves the secret intact in all historical commits and git snapshots. Anyone can browse the GitHub commit history or fetch the blob SHA directly. Automated GitHub scraping bots scan commits within seconds of a push. Therefore, the secret must be considered permanently compromised the instant it hits a public or shared remote.

### 3. Follow-Ups
- **Why is deleting the commit/file not enough?**
  - Git is an append-only directed acyclic graph (DAG). Creating a new commit that deletes the file only records the deletion in a new snapshot; previous commits in Git history still hold the file in full plain text. Furthermore, GitHub caches commit SHAs even if branches are rebased.
- **What should happen to the exposed key itself?**
  - It must be considered burned. It must be **revoked immediately**, deactivated in the provider dashboard, rotated to a new key, and system access logs must be audited for suspicious queries or spikes in resource consumption.
- **How would you prevent similar secrets from being committed again?**
  - Install a **pre-commit hook** using **Husky** and **`gitleaks`** or **`git-secrets`** to scan for entropy and API key patterns before any commit can be created.
  - Enable **GitHub Secret Scanning** and **Push Protection** on the repository.
  - Use `.env.example` templates and load secrets via environment variables or secret managers (e.g., AWS Secrets Manager, Doppler, Vault).

---

## Scenario 4: PR Review With New Changes
**Prompt**: *A reviewer asks for changes on your pull request after you have already pushed several commits. How would you update the PR while keeping the review understandable?*

### 1. What I Would Do
```bash
# 1. Make the requested fixes in the codebase
# 2. Stage and commit with a clear, descriptive commit message referencing review feedback:
git commit -m "fix(auth): address PR review comments - sanitize email and add unit tests"

# 3. Push normally to the feature branch:
git push origin feature/my-feature
```

### 2. Why
During an active code review, adding distinct new commits allows the reviewer to view only the *diff of new changes* rather than re-reviewing the entire PR from scratch. GitHub and GitLab provide a dropdown allowing reviewers to see "Changes since last review". Once the reviewer gives final approval (LGTM), the commits can be squashed if required by the repository's merge policy (e.g., using GitHub's "Squash and Merge" button).

### 3. Follow-Ups
- **Would you create a new commit or amend/squash?**
  - **During Review**: Create **new commits**. Amending or squashing rewrites SHAs, wipes out previous review inline comments, and forces the reviewer to re-read the entire PR diff.
  - **Post Approval**: Squash into atomic, clean commits either locally with interactive rebase (`git rebase -i HEAD~n`) or automatically via the GitHub PR merge strategy.
- **When can force-push become risky?**
  - Force-pushing overwrites the remote branch. If another teammate pulled your branch to test or contribute, their local tracking branch diverges. Additionally, force-pushing without `--force-with-lease` can overwrite commits added by someone else on the PR.
- **How would you communicate a significant change to the reviewer?**
  - Reply directly to the specific PR comment threads with the commit hash link (e.g., `Fixed in commit a1b2c3d`).
  - If the architectural approach changed significantly, write a top-level PR comment summarizing:
    1. What changed and why.
    2. Any trade-offs or assumptions made.
    3. Screenshots or short video/Loom showing the new behavior.

---

## Scenario 5: Recovering Lost Local Work
**Prompt**: *You ran a Git command incorrectly and your local branch no longer points to the commit containing yesterday's work. How would you investigate and recover it?*

### 1. What I Would Do
```bash
# 1. Open Git's reference log to see all HEAD history
git reflog

# 2. Locate the commit hash where yesterday's work was intact (e.g., HEAD@{3} or commit abc1234)
# 3. Inspect the commit to verify it holds the lost work without modifying branches:
git show HEAD@{3}

# 4. Recover the work safely:
# Option A: Create a recovery branch pointing to that commit:
git branch recovery-branch HEAD@{3}

# Option B: If on the correct branch, reset back to that commit:
git reset --hard HEAD@{3}
```

### 2. Why
`git reflog` (Reference Logs) records every single update made to the local tip of branches and `HEAD` (such as `checkout`, `commit`, `rebase`, `reset`, `merge`). Even if a branch is deleted or a `git reset --hard` is executed, the orphaned commit objects are not immediately deleted; they remain in Git's object database as "dangling commits" until Git's garbage collection (`git gc`) runs (usually 30–90 days).

### 3. Follow-Ups
- **What is git reflog and why can it help?**
  - `git reflog` is a local log of all pointer movements of `HEAD`. It acts as an undo history for Git itself. Even if a commit is detached from any branch, `reflog` remembers its SHA.
- **How would you verify the recovered commit before changing the branch?**
  - Use `git show <commit-sha>` to read commit metadata and diffs.
  - Or run `git checkout <commit-sha>` to enter a "detached HEAD" state, run tests, and confirm application functionality before pointing any branch pointer at it.
- **What habit would reduce the chance of permanent loss?**
  1. Commit early and often locally with atomic commits (work can always be squashed later).
  2. Use `git stash push -u -m "WIP: description"` before experimenting with risky Git commands.
  3. Push feature branches to remote forks as a remote backup.
  4. Avoid using `git reset --hard` without first running `git status` and `git diff`.
