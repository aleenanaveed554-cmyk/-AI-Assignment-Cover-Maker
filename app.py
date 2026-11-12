import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import date
import textwrap

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="AI Assignment Cover Maker",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #07111f;
}

[data-testid="stSidebar"] {
    background: #091a30;
    border-right: 1px solid #1d395a;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.main-title {
    font-size: 44px;
    font-weight: 800;
    color: white;
    margin-bottom: 4px;
}

.subtitle {
    font-size: 17px;
    color: #9eb5d0;
    margin-bottom: 28px;
}

.section-title {
    color: white;
    font-size: 21px;
    font-weight: 800;
    margin: 18px 0 14px 0;
}

.stTextInput input,
.stDateInput input,
[data-baseweb="select"] {
    background: #10243d !important;
    color: white !important;
    border: 1px solid #315274 !important;
    border-radius: 10px !important;
}

.stTextInput label,
.stDateInput label,
.stSelectbox label,
.stFileUploader label {
    color: #dbe8f6 !important;
    font-weight: 600 !important;
}

.stButton > button {
    width: 100%;
    min-height: 52px;
    background: linear-gradient(135deg, #1677ff, #0b4fc4);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 17px;
    font-weight: 800;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #318cff, #1260e2);
}

.info-box {
    background: #10243d;
    border: 1px solid #294966;
    border-radius: 18px;
    padding: 22px;
}

.small-note {
    color: #8fa8c2;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# THEMES
# =========================================================
THEMES = {
    "Blue": {
        "primary": "#1769E0",
        "dark": "#0B3275",
        "light": "#EAF2FF"
    },
    "Dark Blue": {
        "primary": "#123E7A",
        "dark": "#061B3A",
        "light": "#E8EEF7"
    },
    "Purple": {
        "primary": "#6C3EDB",
        "dark": "#351C70",
        "light": "#F0EBFF"
    },
    "Green": {
        "primary": "#16834B",
        "dark": "#074B2D",
        "light": "#E8F7EF"
    },
    "Minimal Black & White": {
        "primary": "#222222",
        "dark": "#000000",
        "light": "#F1F1F1"
    }
}

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    st.markdown("## 🎓 AI Assignment")
    st.markdown("### Cover Maker")

    st.markdown("---")

    st.markdown("### 🎨 Cover Theme")

    theme = st.selectbox(
        "Choose Theme",
        list(THEMES.keys())
    )

    st.markdown("---")

    st.markdown("### 🖼️ Branding")

    university_logo = st.file_uploader(
        "University / School Logo",
        type=["png", "jpg", "jpeg"]
    )

    student_photo = st.file_uploader(
        "Student Photo / Logo (Optional)",
        type=["png", "jpg", "jpeg"]
    )

    st.markdown("---")

    st.markdown(
        """
        <div class="small-note">
        Create a premium academic assignment cover
        for school, college and university projects.
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# HEADER
# =========================================================
st.markdown(
    '<div class="main-title">AI Assignment Cover Maker</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Create a professional academic cover page in seconds.</div>',
    unsafe_allow_html=True
)

# =========================================================
# INSTITUTION + STUDENT
# =========================================================
left, right = st.columns(2)

with left:

    st.markdown(
        '<div class="section-title">🏫 Institution Information</div>',
        unsafe_allow_html=True
    )

    university = st.text_input(
        "University / School Name",
        placeholder="e.g. Imran Public School and College"
    )

    department = st.text_input(
        "Department / Faculty",
        placeholder="e.g. Department of Computer Science"
    )

    assignment_title = st.text_input(
        "Assignment Title",
        placeholder="e.g. Artificial Intelligence"
    )

    subject = st.text_input(
        "Subject / Course Name",
        placeholder="e.g. Generative AI"
    )

with right:

    st.markdown(
        '<div class="section-title">👨‍🎓 Student Information</div>',
        unsafe_allow_html=True
    )

    student_name = st.text_input(
        "Student Name",
        placeholder="e.g. Aleena Naveed"
    )

    roll_no = st.text_input(
        "Roll Number",
        placeholder="e.g. CS-102"
    )

    course = st.text_input(
        "Course",
        placeholder="e.g. DIT / Computer Science"
    )

    semester = st.text_input(
        "Semester",
        placeholder="e.g. 1st Semester"
    )

    session = st.text_input(
        "Session",
        placeholder="e.g. 2026-27"
    )

# =========================================================
# SUBMISSION
# =========================================================
st.markdown(
    '<div class="section-title">📚 Submission Information</div>',
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:
    faculty = st.text_input(
        "Faculty / Teacher Name",
        placeholder="e.g. Muhammad Sir"
    )

with c2:
    submission_date = st.date_input(
        "Submission Date",
        value=date.today()
    )

st.markdown("<br>", unsafe_allow_html=True)

generate = st.button(
    "✨ GENERATE ASSIGNMENT COVER",
    use_container_width=True
)

# =========================================================
# FONT HELPER
# =========================================================
def get_font(size, bold=False):

    if bold:
        paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"
        ]
    else:
        paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"
        ]

    for path in paths:
        try:
            return ImageFont.truetype(path, size)
        except:
            continue

    return ImageFont.load_default()


# =========================================================
# CENTER TEXT
# =========================================================
def center_text(draw, text, y, font, fill, width):

    box = draw.textbbox((0, 0), text, font=font)

    text_width = box[2] - box[0]

    x = (width - text_width) / 2

    draw.text(
        (x, y),
        text,
        font=font,
        fill=fill
    )


# =========================================================
# FIT TITLE
# =========================================================
def draw_wrapped_center(draw, text, y, font, fill, width, max_chars=32):

    lines = textwrap.wrap(text, width=max_chars)

    current_y = y

    for line in lines[:2]:

        center_text(
            draw,
            line,
            current_y,
            font,
            fill,
            width
        )

        current_y += 62

    return current_y


# =========================================================
# CREATE COVER
# =========================================================
def create_cover():

    W = 1654
    H = 2339

    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    colors = THEMES[theme]

    primary = colors["primary"]
    dark = colors["dark"]
    light = colors["light"]

    # -----------------------------------------------------
    # FONTS - MUCH BIGGER
    # -----------------------------------------------------
    university_font = get_font(62, True)
    department_font = get_font(32, True)

    cover_font = get_font(92, True)
    subject_font = get_font(38, True)

    title_font = get_font(43, True)

    card_header_font = get_font(31, True)
    label_font = get_font(27, True)
    value_font = get_font(27, False)

    footer_font = get_font(20, False)

    # -----------------------------------------------------
    # WHITE BACKGROUND
    # -----------------------------------------------------
    draw.rectangle(
        [0, 0, W, H],
        fill="white"
    )

    # =====================================================
    # TOP GEOMETRIC DESIGN
    # =====================================================

    # Large dark triangle
    draw.polygon(
        [
            (0, 0),
            (570, 0),
            (0, 570)
        ],
        fill=dark
    )

    # Blue triangle
    draw.polygon(
        [
            (0, 0),
            (385, 0),
            (0, 385)
        ],
        fill=primary
    )

    # Small accent triangle
    draw.polygon(
        [
            (0, 385),
            (170, 215),
            (170, 385)
        ],
        fill=light
    )

    # Right top accent
    draw.polygon(
        [
            (W, 0),
            (W - 230, 0),
            (W, 230)
        ],
        fill=light
    )

    # =====================================================
    # TOP DECORATIVE LINES
    # =====================================================

    draw.line(
        [(120, 610), (W - 120, 610)],
        fill=primary,
        width=5
    )

    draw.line(
        [(260, 625), (W - 260, 625)],
        fill=dark,
        width=2
    )

    # =====================================================
    # LOGO
    # =====================================================

    logo_y = 100

    if university_logo:

        try:

            logo = Image.open(
                university_logo
            ).convert("RGBA")

            logo.thumbnail((190, 190))

            logo_x = (W - logo.width) // 2

            img.paste(
                logo,
                (logo_x, logo_y),
                logo
            )

            logo_y += 210

        except:
            pass

    # =====================================================
    # UNIVERSITY NAME
    # =====================================================

    university_text = (
        university.upper()
        if university.strip()
        else "UNIVERSITY / SCHOOL NAME"
    )

    center_text(
        draw,
        university_text,
        logo_y,
        university_font,
        dark,
        W
    )

    # =====================================================
    # DEPARTMENT
    # =====================================================

    department_y = logo_y + 88

    department_text = (
        department.upper()
        if department.strip()
        else "DEPARTMENT / FACULTY"
    )

    center_text(
        draw,
        department_text,
        department_y,
        department_font,
        primary,
        W
    )

    # =====================================================
    # MAIN HEADING
    # =====================================================

    heading_y = department_y + 100

    center_text(
        draw,
        "ASSIGNMENT",
        heading_y,
        cover_font,
        dark,
        W
    )

    # COVER
    center_text(
        draw,
        "COVER",
        heading_y + 105,
        cover_font,
        primary,
        W
    )

    # =====================================================
    # SUBJECT
    # =====================================================

    subject_y = heading_y + 225

    subject_text = (
        subject.upper()
        if subject.strip()
        else "SUBJECT / COURSE NAME"
    )

    center_text(
        draw,
        subject_text,
        subject_y,
        subject_font,
        dark,
        W
    )

    # =====================================================
    # ASSIGNMENT TITLE BOX
    # =====================================================

    title_box_y = subject_y + 90

    draw.rounded_rectangle(
        [
            270,
            title_box_y,
            W - 270,
            title_box_y + 155
        ],
        radius=22,
        fill=light,
        outline=primary,
        width=4
    )

    title_label_font = get_font(22, True)

    center_text(
        draw,
        "ASSIGNMENT TITLE",
        title_box_y + 20,
        title_label_font,
        primary,
        W
    )

    assignment_text = (
        assignment_title
        if assignment_title.strip()
        else "Assignment Title"
    )

    draw_wrapped_center(
        draw,
        assignment_text,
        title_box_y + 57,
        title_font,
        dark,
        W,
        36
    )

    # =====================================================
    # STUDENT DETAILS CARD
    # =====================================================

    card_x1 = 175
    card_x2 = W - 175

    student_y1 = 1080
    student_y2 = 1545

    draw.rounded_rectangle(
        [
            card_x1,
            student_y1,
            card_x2,
            student_y2
        ],
        radius=25,
        fill="white",
        outline=primary,
        width=5
    )

    # Header
    draw.rounded_rectangle(
        [
            card_x1,
            student_y1,
            card_x2,
            student_y1 + 90
        ],
        radius=25,
        fill=dark
    )

    draw.rectangle(
        [
            card_x1,
            student_y1 + 55,
            card_x2,
            student_y1 + 90
        ],
        fill=dark
    )

    draw.text(
        (card_x1 + 35, student_y1 + 25),
        "STUDENT DETAILS",
        font=card_header_font,
        fill="white"
    )

    student_data = [
        (
            "Name",
            student_name if student_name.strip()
            else "____________________________"
        ),
        (
            "Roll No",
            roll_no if roll_no.strip()
            else "____________________________"
        ),
        (
            "Course",
            course if course.strip()
            else "____________________________"
        ),
        (
            "Semester",
            semester if semester.strip()
            else "____________________________"
        ),
        (
            "Session",
            session if session.strip()
            else "____________________________"
        )
    ]

    y = student_y1 + 125

    for label, value in student_data:

        draw.text(
            (card_x1 + 45, y),
            f"{label}:",
            font=label_font,
            fill=dark
        )

        draw.text(
            (card_x1 + 250, y),
            value,
            font=value_font,
            fill="#333333"
        )

        y += 65

    # =====================================================
    # SUBMITTED TO
    # =====================================================

    submit_y1 = 1610
    submit_y2 = 1855

    draw.rounded_rectangle(
        [
            card_x1,
            submit_y1,
            card_x2,
            submit_y2
        ],
        radius=25,
        fill="white",
        outline=primary,
        width=5
    )

    draw.rounded_rectangle(
        [
            card_x1,
            submit_y1,
            card_x2,
            submit_y1 + 90
        ],
        radius=25,
        fill=dark
    )

    draw.rectangle(
        [
            card_x1,
            submit_y1 + 55,
            card_x2,
            submit_y1 + 90
        ],
        fill=dark
    )

    draw.text(
        (card_x1 + 35, submit_y1 + 25),
        "SUBMITTED TO",
        font=card_header_font,
        fill="white"
    )

    faculty_value = (
        faculty
        if faculty.strip()
        else "____________________________"
    )

    draw.text(
        (card_x1 + 45, submit_y1 + 125),
        "Faculty / Teacher Name:",
        font=label_font,
        fill=dark
    )

    draw.text(
        (card_x1 + 480, submit_y1 + 125),
        faculty_value,
        font=value_font,
        fill="#333333"
    )

    # =====================================================
    # SUBMISSION DATE
    # =====================================================

    date_y = 1940

    draw.text(
        (card_x1, date_y),
        "Submission Date:",
        font=label_font,
        fill=dark
    )

    formatted_date = submission_date.strftime(
        "%d %B %Y"
    )

    draw.text(
        (card_x1 + 310, date_y),
        formatted_date,
        font=value_font,
        fill="#333333"
    )

    # =====================================================
    # STUDENT PHOTO
    # =====================================================

    if student_photo:

        try:

            photo = Image.open(
                student_photo
            ).convert("RGB")

            photo.thumbnail((145, 145))

            photo_x = W - card_x2 + card_x2 - photo.width - 40
            photo_x = W - 300

            photo_y = 1890

            draw.rounded_rectangle(
                [
                    photo_x - 8,
                    photo_y - 8,
                    photo_x + photo.width + 8,
                    photo_y + photo.height + 8
                ],
                radius=15,
                fill=primary
            )

            img.paste(
                photo,
                (photo_x, photo_y)
            )

        except:
            pass

    # =====================================================
    # BOTTOM GEOMETRIC DESIGN
    # =====================================================

    draw.polygon(
        [
            (W, H),
            (W - 570, H),
            (W, H - 570)
        ],
        fill=dark
    )

    draw.polygon(
        [
            (W, H),
            (W - 390, H),
            (W, H - 390)
        ],
        fill=primary
    )

    draw.polygon(
        [
            (W - 390, H),
            (W - 210, H),
            (W - 390, H - 180)
        ],
        fill=light
    )

    # =====================================================
    # FOOTER
    # =====================================================

    center_text(
        draw,
        "ACADEMIC ASSIGNMENT • PROFESSIONAL COVER",
        H - 115,
        footer_font,
        dark,
        W
    )

    return img


# =========================================================
# GENERATE
# =========================================================
if generate:

    st.markdown("---")

    st.markdown(
        '<div class="section-title">📄 Generated Assignment Cover</div>',
        unsafe_allow_html=True
    )

    cover = create_cover()

    preview_col, download_col = st.columns([2.1, 1])

    # -----------------------------------------------------
    # PREVIEW
    # -----------------------------------------------------
    with preview_col:

        st.image(
            cover,
            use_container_width=True
        )

    # -----------------------------------------------------
    # DOWNLOAD AREA
    # -----------------------------------------------------
    with download_col:

        st.markdown(
            """
            <div class="info-box">
                <h2 style="color:white;">✨ Cover Ready</h2>
                <p style="color:#a9bfd8;">
                Your premium academic assignment cover
                has been successfully generated.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # PNG
        png_buffer = BytesIO()

        cover.save(
            png_buffer,
            format="PNG"
        )

        st.download_button(
            "⬇️ DOWNLOAD PNG",
            data=png_buffer.getvalue(),
            file_name="AI_Assignment_Cover.png",
            mime="image/png",
            use_container_width=True
        )

        # PDF
        pdf_buffer = BytesIO()

        cover.save(
            pdf_buffer,
            format="PDF",
            resolution=150.0
        )

        st.download_button(
            "📄 DOWNLOAD PDF",
            data=pdf_buffer.getvalue(),
            file_name="AI_Assignment_Cover.pdf",
            mime="application/pdf",
            use_container_width=True
        )

        st.markdown(
            """
            <p class="small-note">
            PDF is recommended for printing and university submission.
            </p>
            """,
            unsafe_allow_html=True
        )

else:

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### 🎓 Academic Design")
        st.write(
            "Professional layouts suitable for school, college and university assignments."
        )

    with c2:
        st.markdown("### 🎨 Multiple Themes")
        st.write(
            "Blue, Dark Blue, Purple, Green and Minimal Black & White themes."
        )

    with c3:
        st.markdown("### 📥 Export")
        st.write(
            "Download your finished cover as a high-quality PNG or PDF."
        )
