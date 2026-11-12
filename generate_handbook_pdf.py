import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Preformatted
)
from reportlab.pdfgen import canvas

PDF_FILENAME = "Sheryians_Sheet_01_Complete_Solved_Handbook.pdf"

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 36
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN

C_ORANGE = colors.HexColor("#ea580c")
C_ORANGE_LIGHT = colors.HexColor("#fff7ed")
C_ORANGE_BORDER = colors.HexColor("#fed7aa")
C_DARK = colors.HexColor("#0f172a")
C_DARK_CARD = colors.HexColor("#18181b")
C_GRAY_BG = colors.HexColor("#f8fafc")
C_GRAY_BORDER = colors.HexColor("#e2e8f0")
C_TEXT_DARK = colors.HexColor("#1e293b")
C_TEXT_MUTED = colors.HexColor("#64748b")
C_CODE_BG = colors.HexColor("#1e1e24")
C_CODE_TEXT = colors.HexColor("#f8fafc")
C_WHITE = colors.HexColor("#ffffff")


class SolvedNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(C_TEXT_MUTED)
        self.drawString(MARGIN, 22, "Sheet 01 Complete Solved Handbook • Cohort 3.0")
        self.drawRightString(
            PAGE_WIDTH - MARGIN,
            22,
            f"Sheryians Coding School · Page {self._pageNumber} of {total_pages}"
        )
        self.restoreState()


def create_handbook_pdf():
    doc = SimpleDocTemplate(
        PDF_FILENAME,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=28,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    s_title = ParagraphStyle('HTitle', fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=C_DARK)
    s_sub = ParagraphStyle('HSub', fontName='Helvetica', fontSize=9, leading=12, textColor=C_TEXT_MUTED)
    s_sec = ParagraphStyle('HSec', fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=C_DARK)
    s_card_h = ParagraphStyle('HCardH', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=C_DARK)
    s_body = ParagraphStyle('HBody', fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=C_TEXT_DARK)
    s_bullet = ParagraphStyle('HBul', fontName='Helvetica', fontSize=8, leading=11, textColor=C_TEXT_DARK)
    s_code = ParagraphStyle('HCode', fontName='Courier', fontSize=7.5, leading=9.5, textColor=C_CODE_TEXT)
    s_callout = ParagraphStyle('HCall', fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=colors.HexColor("#9a3412"))

    story = []

    # ==========================================
    # COVER / HEADER
    # ==========================================
    header_table_data = [
        [
            Paragraph("<b><font color='#ea580c' size=14>■</font> SHERYIANS</b> CODING SCHOOL", ParagraphStyle('Brd', fontName='Helvetica-Bold', fontSize=10, textColor=C_DARK)),
            Paragraph("<font color='#ffffff'><b>SOLVED HANDBOOK</b></font>", ParagraphStyle('Pill', fontName='Helvetica-Bold', fontSize=8.5, alignment=2, textColor=C_WHITE))
        ]
    ]
    header_table = Table(header_table_data, colWidths=[CONTENT_WIDTH - 120, 120])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (1, 0), (1, 0), C_ORANGE),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (1, 0), (1, 0), 8),
        ('LEFTPADDING', (1, 0), (1, 0), 8),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 10))

    story.append(Paragraph("Weekly Interview Preparation: <font color='#ea580c'><b>Sheet 01 Solutions</b></font>", s_title))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Complete Optimal Solutions, Code, Complexity, Technical Q&amp;A Answers, and Machine Coding Architecture", s_sub))
    story.append(Spacer(1, 10))

    banner = Table([[Paragraph(
        "<b>Submission Status:</b> 5/5 DSA Solved &bull; 5/5 Git Scenarios Documented &bull; 5/5 Technical Questions Answered &bull; Practice Tracker App Built &amp; Tested",
        s_callout
    )]], colWidths=[CONTENT_WIDTH])
    banner.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_ORANGE_LIGHT),
        ('LINELEFT', (0, 0), (0, -1), 3, C_ORANGE),
        ('BOX', (0, 0), (-1, -1), 0.5, C_ORANGE_BORDER),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(banner)
    story.append(Spacer(1, 14))

    # ==========================================
    # SECTION 1: DSA SOLUTIONS
    # ==========================================
    sec1_hdr = Table([
        [
            Paragraph("<b><font color='#ffffff' size=11>&nbsp;1&nbsp;</font></b>", ParagraphStyle('HN1', fontName='Helvetica-Bold', fontSize=10, textColor=C_WHITE, alignment=1)),
            Paragraph("<b>Section 1: DSA Solutions &amp; Complexity</b>", s_sec)
        ]
    ], colWidths=[24, CONTENT_WIDTH - 24])
    sec1_hdr.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (0, 0), C_DARK),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(sec1_hdr)
    story.append(Spacer(1, 8))

    dsa_items = [
        (
            "01. Two Sum (LC 1 - Easy)",
            "One-pass Hash Map | Time: O(n) | Space: O(n)",
            """var twoSum = function(nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (map.has(complement)) return [map.get(complement), i];
        map.set(nums[i], i);
    }
    return [];
};"""
        ),
        (
            "02. Remove Duplicates from Sorted Array (LC 26 - Easy)",
            "Two Pointers (In-place) | Time: O(n) | Space: O(1)",
            """var removeDuplicates = function(nums) {
    if (nums.length === 0) return 0;
    let k = 0;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[k]) {
            k++;
            nums[k] = nums[i];
        }
    }
    return k + 1;
};"""
        ),
        (
            "03. Move Zeroes (LC 283 - Easy)",
            "Two Pointers (In-place Swap) | Time: O(n) | Space: O(1)",
            """var moveZeroes = function(nums) {
    let lastNonZero = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            [nums[lastNonZero], nums[i]] = [nums[i], nums[lastNonZero]];
            lastNonZero++;
        }
    }
};"""
        ),
        (
            "04. Rotate Array (LC 189 - Medium)",
            "Three Reversals Algorithm | Time: O(n) | Space: O(1)",
            """var rotate = function(nums, k) {
    k = k % nums.length;
    const rev = (arr, s, e) => {
        while (s < e) { [arr[s], arr[e]] = [arr[e], arr[s]]; s++; e--; }
    };
    rev(nums, 0, nums.length - 1);
    rev(nums, 0, k - 1);
    rev(nums, k, nums.length - 1);
};"""
        ),
        (
            "05. 3Sum (LC 15 - Medium)",
            "Sorting + Two Pointers | Time: O(n²) | Space: O(1)",
            """var threeSum = function(nums) {
    const res = []; nums.sort((a, b) => a - b);
    for (let i = 0; i < nums.length - 2; i++) {
        if (nums[i] > 0) break;
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        let l = i + 1, r = nums.length - 1;
        while (l < r) {
            const sum = nums[i] + nums[l] + nums[r];
            if (sum === 0) {
                res.push([nums[i], nums[l], nums[r]]);
                while (l < r && nums[l] === nums[l + 1]) l++;
                while (l < r && nums[r] === nums[r - 1]) r--;
                l++; r--;
            } else if (sum < 0) l++; else r--;
        }
    }
    return res;
};"""
        )
    ]

    for title, meta, code in dsa_items:
        card = []
        card.append(Paragraph(f"<b><font color='#ea580c'>●</font> {title}</b>", s_card_h))
        card.append(Paragraph(f"<font color='#64748b'>{meta}</font>", s_sub))
        card.append(Spacer(1, 3))
        # Code table
        c_tbl = Table([[Paragraph(f"<pre>{code.replace('<', '&lt;').replace('>', '&gt;')}</pre>", s_code)]], colWidths=[CONTENT_WIDTH - 24])
        c_tbl.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), C_CODE_BG),
            ('ROUNDEDCORNERS', [4, 4, 4, 4]),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        card.append(c_tbl)

        c_box = Table([[card]], colWidths=[CONTENT_WIDTH])
        c_box.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), C_GRAY_BG),
            ('BOX', (0, 0), (-1, -1), 0.5, C_GRAY_BORDER),
            ('ROUNDEDCORNERS', [6, 6, 6, 6]),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        story.append(c_box)
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # ==========================================
    # SECTION 2: GIT & GITHUB ANSWERS
    # ==========================================
    sec2_hdr = Table([
        [
            Paragraph("<b><font color='#ffffff' size=11>&nbsp;2&nbsp;</font></b>", ParagraphStyle('HN2', fontName='Helvetica-Bold', fontSize=10, textColor=C_WHITE, alignment=1)),
            Paragraph("<b>Section 2: Git &amp; GitHub Interview Answers</b>", s_sec)
        ]
    ], colWidths=[24, CONTENT_WIDTH - 24])
    sec2_hdr.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (0, 0), C_DARK),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(sec2_hdr)
    story.append(Spacer(1, 8))

    git_answers = [
        (
            "1. Wrong Branch, Correct Work (4 commits on main)",
            "What I Would Do: git checkout -b feature/my-feature; git checkout main; git reset --hard HEAD~4\n"
            "Why: Git branches are lightweight pointer files. Creating the feature branch pins current HEAD, resetting main moves main's pointer back without deleting commit objects.\n"
            "Follow-up: If already pushed, use git revert HEAD~4..HEAD or coordinate force-with-lease. Use cherry-pick if feature branch already had separate commits."
        ),
        (
            "2. Merge Conflict During PR",
            "What I Would Do: git checkout feature; git rebase main; manually resolve conflict markers (<<<<<<< HEAD); git add <files>; git rebase --continue; run tests; git push --force-with-lease origin feature.\n"
            "Why & Verification: Rebasing creates a clean linear history. Verify via npm test and git diff main..feature to ensure no functional regressions before pushing."
        ),
        (
            "3. Secret Accidentally Committed",
            "What I Would Do: 1) Immediately revoke and regenerate the exposed credential at the provider. 2) Purge git history using git-filter-repo or BFG. 3) Push force to all branches. 4) Audit logs.\n"
            "Why deleting file is not enough: Commits are immutable DAG nodes; previous snapshots retain the plaintext key. Automated bots scrape GitHub within seconds. Prevent via Husky + Gitleaks pre-commit hooks."
        ),
        (
            "4. PR Review With New Changes",
            "What I Would Do: Push new descriptive fix commits during review so the reviewer can inspect only the new diff ('Changes since last review'). Squash only after final LGTM.\n"
            "Risks: Force-pushing during active review breaks collaborator tracking branches and overwrites review comment contexts."
        ),
        (
            "5. Recovering Lost Local Work (Git Reflog)",
            "What I Would Do: Run git reflog to trace all HEAD pointer movements. Inspect commit with git show HEAD@{n}. Recover via git branch recovery-branch HEAD@{n}.\n"
            "Why: Dangling commits remain in Git's object database until garbage collected (30-90 days). Prevent permanent loss by committing early and using git stash."
        )
    ]

    for title, ans in git_answers:
        card = []
        card.append(Paragraph(f"<b><font color='#ea580c'>●</font> {title}</b>", s_card_h))
        card.append(Spacer(1, 2))
        for line in ans.split('\n'):
            card.append(Paragraph(f"• &nbsp;{line}", s_bullet))
        c_box = Table([[card]], colWidths=[CONTENT_WIDTH])
        c_box.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), C_GRAY_BG),
            ('BOX', (0, 0), (-1, -1), 0.5, C_GRAY_BORDER),
            ('ROUNDEDCORNERS', [6, 6, 6, 6]),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        story.append(c_box)
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # ==========================================
    # SECTION 3: FULL-STACK TECHNICAL ANSWERS
    # ==========================================
    sec3_hdr = Table([
        [
            Paragraph("<b><font color='#ffffff' size=11>&nbsp;3&nbsp;</font></b>", ParagraphStyle('HN3', fontName='Helvetica-Bold', fontSize=10, textColor=C_WHITE, alignment=1)),
            Paragraph("<b>Section 3: Full-Stack Technical Answers</b>", s_sec)
        ]
    ], colWidths=[24, CONTENT_WIDTH - 24])
    sec3_hdr.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (0, 0), C_DARK),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(sec3_hdr)
    story.append(Spacer(1, 8))

    tech_answers = [
        (
            "1. JavaScript Async Flow & Event Loop",
            "Event Loop Mechanism: Call Stack -> Web APIs -> Microtask Queue (Promises, queueMicrotask) vs Macrotask Queue (setTimeout, setInterval, I/O).\n"
            "Execution Order: Microtasks have strict priority and must completely drain before the next macrotask is dequeued.\n"
            "UI Freezing: JavaScript runs on the same main thread as the browser rendering engine. Heavy synchronous execution blocks the Event Loop from painting frames (targeting 16.6ms / 60fps)."
        ),
        (
            "2. React Unnecessary Re-render Optimization",
            "Investigation: Profile using React DevTools Profiler ('Record why each component rendered') and @welldone-software/why-did-you-render.\n"
            "React.memo: Shallowly compares props. Helps when parent re-renders due to unrelated state and child has heavy render cost.\n"
            "useMemo & useCallback: Preserves memory references across renders to prevent breaking React.memo shallow equality checks. Avoid memoizing everywhere due to memory allocation and closure overhead."
        ),
        (
            "3. REST API + Express Request Flow (401 Debugging)",
            "Request Flow: Client -> cors() -> express.json() -> authMiddleware() -> Controller -> Response.\n"
            "Debugging 401: Verify 'Authorization: Bearer <token>' header exists, verify JWT secret matches process.env.JWT_SECRET, and verify token has not expired.\n"
            "401 vs 403: 401 Unauthorized = Missing or invalid identity ('Who are you?'). 403 Forbidden = Identity verified, but lacks permission to access resource ('Access denied')."
        ),
        (
            "4. MongoDB + Mongoose Duplicate Data Race Condition",
            "Why App-Level findOne Fails: Concurrent requests execute findOne simultaneously before either document is written, bypassing the check (TOCTOU race condition).\n"
            "Solution: Enforce unique B-Tree index at MongoDB level ({ email: { type: String, unique: true, index: true } }).\n"
            "API Handling: Catch MongoDB error code 11000 in Express error middleware and return HTTP 409 Conflict with a clean user-friendly JSON message."
        ),
        (
            "5. Auth + Authorization + ImageKit Security",
            "IDOR Prevention: Never trust client parameters (URL params or body userId). Scope queries strictly to req.user.id (e.g. Submission.findOne({ _id, studentId: req.user.id })).\n"
            "ImageKit Integration: Express generates backend HMAC signature (/api/imagekit-auth) -> Client uploads directly to ImageKit with signature -> ImageKit returns fileId/URL -> Express saves reference in MongoDB. For private student files, use signed ImageKit URLs."
        )
    ]

    for title, ans in tech_answers:
        card = []
        card.append(Paragraph(f"<b><font color='#ea580c'>●</font> {title}</b>", s_card_h))
        card.append(Spacer(1, 2))
        for line in ans.split('\n'):
            card.append(Paragraph(f"• &nbsp;{line}", s_bullet))
        c_box = Table([[card]], colWidths=[CONTENT_WIDTH])
        c_box.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), C_GRAY_BG),
            ('BOX', (0, 0), (-1, -1), 0.5, C_GRAY_BORDER),
            ('ROUNDEDCORNERS', [6, 6, 6, 6]),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        story.append(c_box)
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # ==========================================
    # SECTION 4: MACHINE CODING & SUBMISSION
    # ==========================================
    sec4_hdr = Table([
        [
            Paragraph("<b><font color='#ffffff' size=11>&nbsp;4&nbsp;</font></b>", ParagraphStyle('HN4', fontName='Helvetica-Bold', fontSize=10, textColor=C_WHITE, alignment=1)),
            Paragraph("<b>Section 4: Machine Coding Round &amp; Submission Guide</b>", s_sec)
        ]
    ], colWidths=[24, CONTENT_WIDTH - 24])
    sec4_hdr.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (0, 0), C_DARK),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(sec4_hdr)
    story.append(Spacer(1, 8))

    mc_summary = [
        Paragraph("<b>Project: Interview Practice Tracker (React + Vite + Tailwind CSS)</b>", s_card_h),
        Spacer(1, 3),
        Paragraph("<b>Core Features Delivered:</b>", s_body),
        Paragraph("• <b>Dashboard Metrics:</b> Real-time visual progress percentage, LeetCode solved counter (3/5), Technical Q&amp;A stats, and Machine Coding status toggle.", s_bullet),
        Paragraph("• <b>Multi-Criteria Filtering:</b> Live title/keyword search, category pills (DSA / Git / Technical / Machine Coding), difficulty filters, and status filters.", s_bullet),
        Paragraph("• <b>Question Management:</b> Add and edit question modals with form validation (min 3 chars, required fields, URL format).", s_bullet),
        Paragraph("• <b>Persistence:</b> Full synchronization with browser LocalStorage (`sheryians_interview_tracker_sheet01`) with reset defaults option.", s_bullet),
        Paragraph("• <b>Sensible UX:</b> Responsive dark theme matching Sheryians aesthetics, empty state, no-results state, detail view modal, and confetti celebration.", s_bullet),
    ]
    mc_box = Table([[mc_summary]], colWidths=[CONTENT_WIDTH])
    mc_box.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_GRAY_BG),
        ('BOX', (0, 0), (-1, -1), 0.5, C_GRAY_BORDER),
        ('ROUNDEDCORNERS', [6, 6, 6, 6]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(mc_box)
    story.append(Spacer(1, 10))

    # WorkDir Submission Checklist
    sub_guide = [
        Paragraph("<b>WorkDir Submission Fields Checklist (learn.sheryians.com/tasks)</b>", s_card_h),
        Spacer(1, 4),
        Paragraph("<b>1. Repository URL:</b> Public GitHub repository URL with full source code, docs, and README.", s_bullet),
        Paragraph("<b>2. Live URL:</b> Deployed application URL on Vercel (https://your-project.vercel.app).", s_bullet),
        Paragraph("<b>3. Google Drive Link:</b> Public folder ('Anyone with the link can view') containing:", s_bullet),
        Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&bull; <code>Sheet 01 - DSA/</code>: 5 Accepted screenshots for LC 1, 26, 283, 189, 15", s_bullet),
        Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&bull; <code>Recordings/</code>: Self-interview video recording + 1-2 min Machine Coding demo video", s_bullet),
        Paragraph("<b>4. Notes:</b> Summary notes for instructor acknowledging completion of all 4 sections.", s_bullet)
    ]
    sub_box = Table([[sub_guide]], colWidths=[CONTENT_WIDTH])
    sub_box.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_ORANGE_LIGHT),
        ('BOX', (0, 0), (-1, -1), 1, C_ORANGE),
        ('ROUNDEDCORNERS', [6, 6, 6, 6]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(sub_box)

    doc.build(story, canvasmaker=SolvedNumberedCanvas)
    print(f"Generated {PDF_FILENAME} successfully!")


if __name__ == '__main__':
    create_handbook_pdf()
