import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.pdfgen import canvas

PDF_FILENAME = "Sheryians_Weekly_Interview_Preparation_Sheet_01.pdf"

# Dimensions
PAGE_WIDTH, PAGE_HEIGHT = A4  # 595.27 x 841.89
MARGIN = 36
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN

# Colors matching Sheryians PDF
C_ORANGE = colors.HexColor("#ea580c")
C_ORANGE_LIGHT = colors.HexColor("#fff7ed")
C_ORANGE_BORDER = colors.HexColor("#fed7aa")
C_DARK = colors.HexColor("#0f172a")
C_DARK_CARD = colors.HexColor("#18181b")
C_GRAY_BG = colors.HexColor("#f8fafc")
C_GRAY_BORDER = colors.HexColor("#e2e8f0")
C_TEXT_DARK = colors.HexColor("#1e293b")
C_TEXT_MUTED = colors.HexColor("#64748b")
C_GREEN_BG = colors.HexColor("#dcfce7")
C_GREEN_TEXT = colors.HexColor("#15803d")
C_WHITE = colors.HexColor("#ffffff")


class NumberedCanvas(canvas.Canvas):
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
        # Footer
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(C_TEXT_MUTED)
        self.drawString(MARGIN, 22, "Weekly Interview Preparation Program")
        self.drawRightString(
            PAGE_WIDTH - MARGIN,
            22,
            f"Sheryians Coding School · Page {self._pageNumber}"
        )
        self.restoreState()


def create_sheet_pdf():
    doc = SimpleDocTemplate(
        PDF_FILENAME,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=28,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom typography styles
    style_title = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=C_DARK
    )
    style_subtitle = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=C_TEXT_MUTED
    )
    style_section_title = ParagraphStyle(
        'SectionTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=16,
        textColor=C_DARK
    )
    style_section_sub = ParagraphStyle(
        'SectionSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=C_TEXT_MUTED
    )
    style_card_title = ParagraphStyle(
        'CardTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=C_DARK
    )
    style_card_prompt = ParagraphStyle(
        'CardPrompt',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=C_TEXT_DARK
    )
    style_card_bullet = ParagraphStyle(
        'CardBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=C_TEXT_DARK
    )
    style_callout = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#9a3412")
    )
    style_darkbox = ParagraphStyle(
        'DarkBoxText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=C_WHITE
    )

    story = []

    # =========================================================================
    # PAGE 1: Overview & Section 1 (DSA)
    # =========================================================================
    # Brand row
    header_table_data = [
        [
            Paragraph("<b><font color='#ea580c' size=14>■</font> SHERYIANS</b> CODING SCHOOL", ParagraphStyle('Brd', fontName='Helvetica-Bold', fontSize=10, textColor=C_DARK)),
            Paragraph("<font color='#ffffff'><b>SHEET 01</b></font>", ParagraphStyle('Pill', fontName='Helvetica-Bold', fontSize=9, alignment=2, textColor=C_WHITE))
        ]
    ]
    header_table = Table(header_table_data, colWidths=[CONTENT_WIDTH - 80, 80])
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

    # Big Title
    story.append(Paragraph("Weekly Interview <font color='#ea580c'><b>Preparation</b></font>", style_title))
    story.append(Spacer(1, 3))
    story.append(Paragraph("DSA + Git &amp; GitHub + Full-Stack Technical Interview + Frontend Machine Coding", style_subtitle))
    story.append(Spacer(1, 6))

    # Tag pills
    pills_text = "<font color='#ea580c'>●</font> DSA — LeetCode &nbsp;&nbsp;&nbsp;&nbsp; <font color='#ea580c'>●</font> Git &amp; GitHub &nbsp;&nbsp;&nbsp;&nbsp; <font color='#ea580c'>●</font> Full-Stack Technical &nbsp;&nbsp;&nbsp;&nbsp; <font color='#ea580c'>●</font> Machine Coding"
    story.append(Paragraph(pills_text, ParagraphStyle('Pills', fontName='Helvetica-Bold', fontSize=8, textColor=C_TEXT_DARK)))
    story.append(Spacer(1, 8))

    # Objective Callout Box
    obj_text = "<b><font color='#ea580c'>Objective —</font></b> Practice how to solve, explain, build, communicate and document. Not how to memorize answers."
    obj_table = Table([[Paragraph(obj_text, style_callout)]], colWidths=[CONTENT_WIDTH])
    obj_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_ORANGE_LIGHT),
        ('LINELEFT', (0, 0), (0, -1), 3, C_ORANGE),
        ('BOX', (0, 0), (-1, -1), 0.5, C_ORANGE_BORDER),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(obj_table)
    story.append(Spacer(1, 10))

    # Section Overview Table
    ov_data = [
        [
            Paragraph("<b>SECTION</b>", ParagraphStyle('TH1', fontName='Helvetica-Bold', fontSize=8, textColor=C_WHITE)),
            Paragraph("<b>WEEKLY WORK</b>", ParagraphStyle('TH2', fontName='Helvetica-Bold', fontSize=8, textColor=C_WHITE)),
            Paragraph("<b>EVIDENCE</b>", ParagraphStyle('TH3', fontName='Helvetica-Bold', fontSize=8, textColor=C_WHITE))
        ],
        [
            Paragraph("<b><font color='#ea580c'>1</font> DSA (LeetCode)</b>", ParagraphStyle('TD1', fontName='Helvetica', fontSize=8)),
            Paragraph("5 problems", ParagraphStyle('TD2', fontName='Helvetica', fontSize=8)),
            Paragraph("Accepted screenshots + Drive folder", ParagraphStyle('TD3', fontName='Helvetica', fontSize=8))
        ],
        [
            Paragraph("<b><font color='#ea580c'>2</font> Git &amp; GitHub</b>", ParagraphStyle('TD1', fontName='Helvetica', fontSize=8)),
            Paragraph("5 scenario-based questions", ParagraphStyle('TD2', fontName='Helvetica', fontSize=8)),
            Paragraph("Recorded answers for selected questions", ParagraphStyle('TD3', fontName='Helvetica', fontSize=8))
        ],
        [
            Paragraph("<b><font color='#ea580c'>3</font> Full-Stack Technical</b>", ParagraphStyle('TD1', fontName='Helvetica', fontSize=8)),
            Paragraph("5 interview questions", ParagraphStyle('TD2', fontName='Helvetica', fontSize=8)),
            Paragraph("Recorded answers for selected questions", ParagraphStyle('TD3', fontName='Helvetica', fontSize=8))
        ],
        [
            Paragraph("<b><font color='#ea580c'>4</font> Machine Coding</b>", ParagraphStyle('TD1', fontName='Helvetica', fontSize=8)),
            Paragraph("1 frontend task", ParagraphStyle('TD2', fontName='Helvetica', fontSize=8)),
            Paragraph("GitHub repo + live link + demo", ParagraphStyle('TD3', fontName='Helvetica', fontSize=8))
        ],
    ]
    ov_table = Table(ov_data, colWidths=[150, 150, CONTENT_WIDTH - 300])
    ov_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_DARK),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [C_WHITE, C_GRAY_BG]),
        ('GRID', (0, 0), (-1, -1), 0.5, C_GRAY_BORDER),
    ]))
    story.append(ov_table)
    story.append(Spacer(1, 14))

    # Section 1 Header
    sec1_hdr = Table([
        [
            Paragraph("<b><font color='#ffffff' size=11>&nbsp;1&nbsp;</font></b>", ParagraphStyle('HdrNum', fontName='Helvetica-Bold', fontSize=10, textColor=C_WHITE, alignment=1)),
            Paragraph("<b>DSA (LeetCode)</b><br/><font color='#64748b' size=7>SECTION 1</font>", style_section_title)
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
    story.append(Spacer(1, 6))

    sec1_desc = "Solve all 5 directly on LeetCode. Do not copy a solution before attempting the problem yourself. After an Accepted submission, upload proof to your weekly Drive folder."
    story.append(Paragraph(sec1_desc, style_section_sub))
    story.append(Spacer(1, 8))

    # DSA Problem Table
    dsa_data = [
        [
            Paragraph("<b>#</b>", ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=8, textColor=C_ORANGE)),
            Paragraph("<b>PROBLEM</b>", ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=8, textColor=C_ORANGE)),
            Paragraph("<b>LEVEL</b>", ParagraphStyle('H3', fontName='Helvetica-Bold', fontSize=8, textColor=C_ORANGE)),
            Paragraph("<b>LEETCODE</b>", ParagraphStyle('H4', fontName='Helvetica-Bold', fontSize=8, textColor=C_ORANGE))
        ],
        [
            Paragraph("01", ParagraphStyle('P1', fontName='Helvetica', fontSize=8)),
            Paragraph("<b>Two Sum</b>", ParagraphStyle('P2', fontName='Helvetica', fontSize=8)),
            Paragraph("<font color='#16a34a'><b>Easy</b></font>", ParagraphStyle('P3', fontName='Helvetica-Bold', fontSize=8)),
            Paragraph("LC 1", ParagraphStyle('P4', fontName='Helvetica', fontSize=8))
        ],
        [
            Paragraph("02", ParagraphStyle('P1', fontName='Helvetica', fontSize=8)),
            Paragraph("<b>Remove Duplicates from Sorted Array</b>", ParagraphStyle('P2', fontName='Helvetica', fontSize=8)),
            Paragraph("<font color='#16a34a'><b>Easy</b></font>", ParagraphStyle('P3', fontName='Helvetica-Bold', fontSize=8)),
            Paragraph("LC 26", ParagraphStyle('P4', fontName='Helvetica', fontSize=8))
        ],
        [
            Paragraph("03", ParagraphStyle('P1', fontName='Helvetica', fontSize=8)),
            Paragraph("<b>Move Zeroes</b>", ParagraphStyle('P2', fontName='Helvetica', fontSize=8)),
            Paragraph("<font color='#16a34a'><b>Easy</b></font>", ParagraphStyle('P3', fontName='Helvetica-Bold', fontSize=8)),
            Paragraph("LC 283", ParagraphStyle('P4', fontName='Helvetica', fontSize=8))
        ],
        [
            Paragraph("04", ParagraphStyle('P1', fontName='Helvetica', fontSize=8)),
            Paragraph("<b>Rotate Array</b>", ParagraphStyle('P2', fontName='Helvetica', fontSize=8)),
            Paragraph("<font color='#ea580c'><b>Medium</b></font>", ParagraphStyle('P3', fontName='Helvetica-Bold', fontSize=8)),
            Paragraph("LC 189", ParagraphStyle('P4', fontName='Helvetica', fontSize=8))
        ],
        [
            Paragraph("05", ParagraphStyle('P1', fontName='Helvetica', fontSize=8)),
            Paragraph("<b>3Sum</b>", ParagraphStyle('P2', fontName='Helvetica', fontSize=8)),
            Paragraph("<font color='#ea580c'><b>Medium</b></font>", ParagraphStyle('P3', fontName='Helvetica-Bold', fontSize=8)),
            Paragraph("LC 15", ParagraphStyle('P4', fontName='Helvetica', fontSize=8))
        ],
    ]
    dsa_table = Table(dsa_data, colWidths=[35, CONTENT_WIDTH - 205, 80, 90])
    dsa_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_ORANGE_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, C_ORANGE_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [C_WHITE, C_GRAY_BG]),
    ]))
    story.append(dsa_table)
    story.append(Spacer(1, 10))

    # Submission callout
    dsa_sub_text = "<b><font color='#ea580c'>DSA submission:</font></b> Upload one screenshot per accepted problem showing the problem/solution result and your accepted status. Put all 5 screenshots in the <b>Sheet 01 → DSA</b> Drive folder and submit that folder link."
    dsa_sub_box = Table([[Paragraph(dsa_sub_text, style_callout)]], colWidths=[CONTENT_WIDTH])
    dsa_sub_box.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_ORANGE_LIGHT),
        ('BOX', (0, 0), (-1, -1), 1, C_ORANGE),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(dsa_sub_box)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: Section 2 (Git & GitHub)
    # =========================================================================
    sec2_hdr = Table([
        [
            Paragraph("<b><font color='#ffffff' size=11>&nbsp;2&nbsp;</font></b>", ParagraphStyle('HdrNum2', fontName='Helvetica-Bold', fontSize=10, textColor=C_WHITE, alignment=1)),
            Paragraph("<b>Git &amp; GitHub</b><br/><font color='#64748b' size=7>SECTION 2</font>", style_section_title)
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
    story.append(Spacer(1, 4))
    story.append(Paragraph("Answer these like an interview. First explain what you would do, then explain why. Be ready for the follow-ups.", style_section_sub))
    story.append(Spacer(1, 10))

    git_scenarios = [
        (
            "1",
            "Wrong Branch, Correct Work",
            "You accidentally made 4 commits on main instead of your feature branch. How would you move the work to the correct branch without losing it?",
            [
                "Would your approach change if the commits were already pushed to the remote?",
                "When would you use cherry-pick here?",
                "What would you do if teammates were already using main?"
            ]
        ),
        (
            "2",
            "Merge Conflict During PR",
            "Your feature branch has a merge conflict with main just before the PR is merged. Walk through the complete process of resolving it safely.",
            [
                "How do you verify that the conflict resolution did not break existing functionality?",
                "Would you merge main into the feature branch or rebase? Explain the trade-off.",
                "What should you do before pushing the resolved branch?"
            ]
        ),
        (
            "3",
            "Secret Accidentally Committed",
            "A developer committed an API key to GitHub and immediately realizes the mistake. What steps should they take?",
            [
                "Why is deleting the commit/file not enough?",
                "What should happen to the exposed key itself?",
                "How would you prevent similar secrets from being committed again?"
            ]
        ),
        (
            "4",
            "PR Review With New Changes",
            "A reviewer asks for changes on your pull request after you have already pushed several commits. How would you update the PR while keeping the review understandable?",
            [
                "Would you create a new commit or amend/squash?",
                "When can force-push become risky?",
                "How would you communicate a significant change to the reviewer?"
            ]
        ),
        (
            "5",
            "Recovering Lost Local Work",
            "You ran a Git command incorrectly and your local branch no longer points to the commit containing yesterday's work. How would you investigate and recover it?",
            [
                "What is git reflog and why can it help?",
                "How would you verify the recovered commit before changing the branch?",
                "What habit would reduce the chance of permanent loss?"
            ]
        ),
    ]

    for num, title, prompt, bullets in git_scenarios:
        card_content = []
        card_content.append(Paragraph(f"<b><font color='#ea580c'>● {num}</font> &nbsp;{title}</b>", style_card_title))
        card_content.append(Spacer(1, 3))
        card_content.append(Paragraph(f"<b><font color='#ea580c'>SCENARIO</font></b> &nbsp;{prompt}", style_card_prompt))
        card_content.append(Spacer(1, 3))
        for b in bullets:
            card_content.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;• &nbsp;{b}", style_card_bullet))

        card_table = Table([[card_content]], colWidths=[CONTENT_WIDTH])
        card_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), C_GRAY_BG),
            ('BOX', (0, 0), (-1, -1), 0.5, C_GRAY_BORDER),
            ('ROUNDEDCORNERS', [6, 6, 6, 6]),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(card_table)
        story.append(Spacer(1, 7))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: Section 3 (Full-Stack Technical)
    # =========================================================================
    sec3_hdr = Table([
        [
            Paragraph("<b><font color='#ffffff' size=11>&nbsp;3&nbsp;</font></b>", ParagraphStyle('HdrNum3', fontName='Helvetica-Bold', fontSize=10, textColor=C_WHITE, alignment=1)),
            Paragraph("<b>Full-Stack Technical Interview</b><br/><font color='#64748b' size=7>SECTION 3 · CUMULATIVE</font>", style_section_title)
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
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "This section is cumulative. Questions can come from JavaScript, React, Node.js, Express, REST APIs, MongoDB/Mongoose, authentication/authorization, ImageKit and — once taught — TypeScript, Next.js and other full-stack topics. This week's questions stay within topics already taught, while the bank expands as the course progresses.",
        style_section_sub
    ))
    story.append(Spacer(1, 8))

    tech_questions = [
        (
            "1",
            "JavaScript — Async Flow",
            "You call an API using fetch(), update the UI after the response, and also have a setTimeout() in the same flow. Explain how JavaScript's event loop affects the order of execution.",
            [
                "What is the difference between a microtask and a macrotask?",
                "Where do Promise callbacks fit?",
                "Why can blocking synchronous JavaScript make the UI feel frozen?"
            ]
        ),
        (
            "2",
            "React — Unnecessary Re-render",
            "A React page becomes slow because a parent component re-renders frequently and several child components also re-render. How would you investigate and improve it?",
            [
                "When would React.memo help?",
                "What are useMemo and useCallback actually solving?",
                "Why should you avoid adding memoization everywhere?"
            ]
        ),
        (
            "3",
            "REST API + Express — Request Flow",
            "A protected GET /api/profile endpoint is returning 401 for a logged-in user. Explain the complete request flow and how you would debug it.",
            [
                "Where should authentication middleware run?",
                "How would you distinguish an authentication failure from an authorization failure?",
                "Which HTTP status codes would you use for 401 and 403?"
            ]
        ),
        (
            "4",
            "MongoDB + Mongoose — Duplicate Data",
            "Your registration API is allowing two users to register with the same email under a race condition. How would you prevent and handle duplicate records?",
            [
                "Would application-level checking alone be sufficient?",
                "How can a unique index help?",
                "How should the API respond when a duplicate-key error occurs?"
            ]
        ),
        (
            "5",
            "Authentication + Authorization + ImageKit",
            "A student is authenticated but should not be allowed to access another student's private resource or upload area. Design the checks you would apply before allowing the request, and explain where ImageKit fits into the upload flow.",
            [
                "What is the difference between authentication and authorization?",
                "What information should the server trust from the client?",
                "How would you prevent a user from changing an ID in the URL and accessing someone else's data?"
            ]
        ),
    ]

    for num, title, prompt, bullets in tech_questions:
        card_content = []
        card_content.append(Paragraph(f"<b><font color='#ea580c'>● {num}</font> &nbsp;{title}</b>", style_card_title))
        card_content.append(Spacer(1, 2))
        card_content.append(Paragraph(f"<b><font color='#ea580c'>QUESTION</font></b> &nbsp;{prompt}", style_card_prompt))
        card_content.append(Spacer(1, 2))
        for b in bullets:
            card_content.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;• &nbsp;{b}", style_card_bullet))

        card_table = Table([[card_content]], colWidths=[CONTENT_WIDTH])
        card_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), C_GRAY_BG),
            ('BOX', (0, 0), (-1, -1), 0.5, C_GRAY_BORDER),
            ('ROUNDEDCORNERS', [6, 6, 6, 6]),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(card_table)
        story.append(Spacer(1, 5))

    # Bottom Callout
    fut_text = "<b><font color='#ea580c'>Future technical topics —</font></b> As TypeScript, Next.js, advanced React, Redis, deployment, system design or other modules are taught, they will be added to the cumulative interview rotation. Students are expected to revise older topics rather than study only the newest topic."
    fut_box = Table([[Paragraph(fut_text, style_callout)]], colWidths=[CONTENT_WIDTH])
    fut_box.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_ORANGE_LIGHT),
        ('BOX', (0, 0), (-1, -1), 0.5, C_ORANGE_BORDER),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(Spacer(1, 3))
    story.append(fut_box)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: Section 4 (Frontend Machine Coding Round)
    # =========================================================================
    sec4_hdr = Table([
        [
            Paragraph("<b><font color='#ffffff' size=11>&nbsp;4&nbsp;</font></b>", ParagraphStyle('HdrNum4', fontName='Helvetica-Bold', fontSize=10, textColor=C_WHITE, alignment=1)),
            Paragraph("<b>Frontend Machine Coding Round</b><br/><font color='#64748b' size=7>SECTION 4</font>", style_section_title)
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

    # Meta badges: Time limit, Stack, Backend
    badges_text = "<b>⏱ Time limit:</b> 2.5 hours &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>⚙ Stack:</b> HTML/CSS/JS or React &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>🚫 Backend not required</b>"
    story.append(Paragraph(badges_text, ParagraphStyle('Badges', fontName='Helvetica', fontSize=8.5, textColor=C_DARK)))
    story.append(Spacer(1, 8))

    build_prompt = "<b>Build:</b> Interview Practice Tracker — a responsive dashboard where a student can track their weekly interview-preparation work."
    story.append(Paragraph(build_prompt, ParagraphStyle('Build', fontName='Helvetica', fontSize=9, leading=12, textColor=C_DARK)))
    story.append(Spacer(1, 10))

    # Features Grid (2 columns)
    col1 = [
        Paragraph("<b><font color='#ea580c'>▸</font> Dashboard</b> — total questions, completed DSA problems, completed interview questions, machine-coding status.", style_card_prompt),
        Spacer(1, 6),
        Paragraph("<b><font color='#ea580c'>▸</font> Question tracker</b> — add questions with category (DSA / Git / Technical), difficulty, status (Pending / In Progress / Completed).", style_card_prompt),
        Spacer(1, 6),
        Paragraph("<b><font color='#ea580c'>▸</font> Search + filters</b> — filter by category, status and difficulty.", style_card_prompt),
        Spacer(1, 6),
        Paragraph("<b><font color='#ea580c'>▸</font> Progress</b> — visual completion percentage based on stored questions.", style_card_prompt),
    ]

    col2 = [
        Paragraph("<b><font color='#ea580c'>▸</font> Persistence</b> — LocalStorage so data remains after refresh.", style_card_prompt),
        Spacer(1, 6),
        Paragraph("<b><font color='#ea580c'>▸</font> Responsive UI</b> — desktop + mobile layouts.", style_card_prompt),
        Spacer(1, 6),
        Paragraph("<b><font color='#ea580c'>▸</font> States</b> — empty state, no-search-results state, form validation.", style_card_prompt),
        Spacer(1, 6),
        Paragraph("<b><font color='#ea580c'>▸</font> Polish</b> — clean component structure, readable code, sensible UX.", style_card_prompt),
    ]

    features_table = Table([[col1, col2]], colWidths=[CONTENT_WIDTH / 2, CONTENT_WIDTH / 2])
    features_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(features_table)
    story.append(Spacer(1, 12))

    # Deliverables Box
    deliv_text = "<b><font color='#ea580c'>Deliverables —</font></b> GitHub repository + live deployed link + 1–2 minute demo video. README should contain setup steps, features and any assumptions."
    deliv_box = Table([[Paragraph(deliv_text, style_callout)]], colWidths=[CONTENT_WIDTH])
    deliv_box.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_ORANGE_LIGHT),
        ('BOX', (0, 0), (-1, -1), 1, C_ORANGE),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(deliv_box)
    story.append(Spacer(1, 12))

    # AI Rule Box (Dark)
    ai_text = "<b><font color='#ea580c'>AI rule —</font></b> AI/GPT may be used to understand concepts, debug, compare approaches or get hints. The final implementation must be understood by you. You should be able to explain your code in an interview."
    ai_box = Table([[Paragraph(ai_text, style_darkbox)]], colWidths=[CONTENT_WIDTH])
    ai_box.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_DARK_CARD),
        ('ROUNDEDCORNERS', [6, 6, 6, 6]),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(ai_box)
    story.append(Spacer(1, 10))

    # Core Rule Box (Dark)
    core_text = "<b><font color='#ea580c'>Core rule —</font></b> This is practice, not a competition for who can copy fastest. Use AI/GPT as a learning assistant, not as a replacement for thinking. If you cheat on practice, the only person you cheat is yourself."
    core_box = Table([[Paragraph(core_text, style_darkbox)]], colWidths=[CONTENT_WIDTH])
    core_box.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_DARK_CARD),
        ('ROUNDEDCORNERS', [6, 6, 6, 6]),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(core_box)

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Generated {PDF_FILENAME} successfully!")


if __name__ == '__main__':
    create_sheet_pdf()
