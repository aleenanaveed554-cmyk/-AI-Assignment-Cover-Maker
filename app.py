import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import date
import base64
import textwrap

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI Assignment Cover Maker",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------
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
        background: #0b1b31;
        border-right: 1px solid #1c3554;
    }

    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: white;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #9fb2ca;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .section-title {
        color: #ffffff;
        font-size: 20px;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .info-card {
        background: #0d2038;
        border: 1px solid #1c3b5f;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 18px;
    }

    .preview-card {
        background: #10243d;
        border: 1px solid #244768;
        border-radius: 20px;
        padding: 20px;
    }

    .stTextInput input,
    .stDateInput input,
    .stSelectbox div[data-baseweb="select"] {
        background: #10243d !important;
        color: white !important;
        border: 1px solid #2b4d70 !important;
        border-radius: 10px !important;
    }

    .stTextInput label,
    .stDateInput label,
    .stSelectbox label,
    .stFileUploader label {
        color: #dce8f5 !important;
        font-weight: 600 !important;
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #1677ff, #0b4ecb);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 13px 20px;
        font-size: 16px;
        font-weight: 700;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #3289ff, #1260e5);
        transform: translateY(-1px);
    }

    .download-row {
        margin-top: 15px;
    }

    .small-note {
        color: #8fa8c4;
        font-size: 13px;
    }

    div[data-testid="stMetric"] {
        background: #10243d;
        border: 1px solid #244768;
        border-radius: 15px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# DEFAULT DATA
# ---------------------------------------------------------
if "generated" not in st.session_state:
    st.session_state.generated = False

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("## 🎓 AI Assignment")
    st.markdown("### Cover Maker")
    st.markdown("---")

    st.markdown("### 🎨 Cover Theme")

    theme = st.selectbox(
        "Choose Theme",
        [
            "Blue",
            "Dark Blue",
            "Purple",
            "Green",
            "Minimal Black & White"
        ]
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
        '<div class="small-note">Professional academic cover generator for school, college and university assignments.</div>',
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# MAIN HEADER
# ---------------------------------------------------------
st.markdown(
    '<div class="main-title">AI Assignment Cover Maker</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Create a premium academic assignment cover in seconds.</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# INPUT AREA
# ---------------------------------------------------------
left, right = st.columns(2)

with left:
    st.markdown('<div class="section-title">🏫 Institution Information</div>', unsafe_allow_html=True)

    university = st.text_input(
        "University / School Name",
        placeholder="e.g. ABC University"
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
    st.markdown('<div class="section-title">👨‍🎓 Student Information</div>', unsafe_allow_html=True)

    student_name = st.text_input(
        "Student Name",
        placeholder="e.g. Ali Ahmed"
    )

    roll_no = st.text_input(
        "Roll Number",
        placeholder="e.g. CS-101"
    )

    course = st.text_input(
        "Course",
        placeholder="e.g. BS Computer Science"
    )

    semester = st.text_input(
        "Semester",
        placeholder="e.g. 5th Semester"
    )

    session = st.text_input(
        "Session",
        placeholder="e.g. 2026-27"
    )

# ---------------------------------------------------------
# SUBMISSION INFORMATION
# ---------------------------------------------------------
st.markdown('<div class="section-title">📚 Submission Information</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    faculty = st.text_input(
        "Faculty / Teacher Name",
        placeholder="e.g. Dr. Muhammad Ahmed"
    )

with c2:
    submission_date = st.date_input(
        "Submission Date",
        value=date.today()
    )

# ---------------------------------------------------------
# GENERATE BUTTON
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

if st.button("✨ GENERATE ASSIGNMENT COVER", use_container_width=True):
    st.session_state.generated = True

# ---------------------------------------------------------
# COLOR THEMES
# ---------------------------------------------------------
THEMES = {
    "Blue": {
        "primary": "#1769E0",
        "secondary": "#0B3D91",
        "accent": "#EAF2FF"
    },
    "Dark Blue": {
        "primary": "#102A56",
        "secondary": "#06152E",
        "accent": "#E8EEF8"
    },
    "Purple": {
        "primary": "#6C3EDB",
        "secondary": "#3E1F75",
        "accent": "#F0EBFF"
    },
    "Green": {
        "primary": "#17834B",
        "secondary": "#0B5130",
        "accent": "#E8F7EF"
    },
    "Minimal Black & White": {
        "primary": "#222222",
        "secondary": "#000000",
        "accent": "#F2F2F2"
    }
}

colors = THEMES[theme]

# ---------------------------------------------------------
# HELPERS
# ---------------------------------------------------------
def load_font(size, bold=False):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"
    ]

    for path in paths:
        try:
            return ImageFont.truetype(path, size)
        except:
            pass

    return ImageFont.load_default()


def center_text(draw, text, y, font, fill, width):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) / 2
    draw.text((x, y), text, font=font, fill=fill)


def rounded_rectangle(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(
        box,
        radius=radius,
        fill=fill,
        outline=outline,
        width=width
    )


# ---------------------------------------------------------
# COVER GENERATOR
# ---------------------------------------------------------
def create_cover():
    W, H = 1654, 2339

    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    primary = colors["primary"]
    secondary = colors["secondary"]
    accent = colors["accent"]

    # Fonts
    university_font = load_font(64, True)
    department_font = load_font(30, False)
    assignment_font = load_font(92, True)
    subject_font = load_font(38, True)
    section_font = load_font(27, True)
    label_font = load_font(25, True)
    value_font = load_font(25, False)
    small_font = load_font(21, False)

    # -----------------------------------------------------
    # BACKGROUND
    # -----------------------------------------------------
    draw.rectangle([0, 0, W, H], fill="white")

    # -----------------------------------------------------
    # GEOMETRIC CORNERS
    # -----------------------------------------------------
    draw.polygon(
        [(0, 0), (480, 0), (0, 480)],
        fill=secondary
    )

    draw.polygon(
        [(0, 0), (320, 0), (0, 320)],
        fill=primary
    )

    draw.polygon(
        [(W, H), (W - 500, H), (W, H - 500)],
        fill=secondary
    )

    draw.polygon(
        [(W, H), (W - 330, H), (W, H - 330)],
        fill=primary
    )

    # Decorative lines
    draw.line(
        [(65, 510), (65, H - 510)],
        fill=primary,
        width=5
    )

    draw.line(
        [(W - 65, 510), (W - 65, H - 510)],
        fill=primary,
        width=5
    )

    # -----------------------------------------------------
    # LOGO
    # -----------------------------------------------------
    logo_y = 145

    if university_logo:
        try:
            logo = Image.open(university_logo).convert("RGBA")
            logo.thumbnail((180, 180))
            x = (W - logo.width) // 2
            img.paste(logo, (x, logo_y), logo)
            logo_y += 205
        except:
            pass

    # -----------------------------------------------------
    # UNIVERSITY NAME
    # -----------------------------------------------------
    university_text = university.upper() if university else "UNIVERSITY / SCHOOL NAME"

    center_text(
        draw,
        university_text,
        logo_y,
        university_font,
        secondary,
        W
    )

    department_y = logo_y + 90

    department_text = (
        department.upper()
        if department
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

    # Small divider
    divider_y = department_y + 70

    draw.line(
        [(W // 2 - 180, divider_y), (W // 2 + 180, divider_y)],
        fill=primary,
        width=4
    )

    # -----------------------------------------------------
    # ASSIGNMENT
    # -----------------------------------------------------
    assignment_y = divider_y + 85

    center_text(
        draw,
        "ASSIGNMENT",
        assignment_y,
        assignment_font,
        secondary,
        W
    )

    subject_y = assignment_y + 125

    subject_text = (
        subject.upper()
        if subject
        else "SUBJECT / COURSE NAME"
    )

    center_text(
        draw,
        subject_text,
        subject_y,
        subject_font,
        primary,
        W
    )

    # -----------------------------------------------------
    # ASSIGNMENT TITLE
    # -----------------------------------------------------
    title_y = subject_y + 100

    title_text = (
        assignment_title
        if assignment_title
        else "Assignment Title"
    )

    title_lines = textwrap.wrap(title_text, width=35)

    current_y = title_y

    for line in title_lines[:3]:
        center_text(
            draw,
            line,
            current_y,
            section_font,
            secondary,
            W
        )
        current_y += 45

    # -----------------------------------------------------
    # STUDENT DETAILS CARD
    # -----------------------------------------------------
    card_x1 = 190
    card_x2 = W - 190
    card_y1 = 1050
    card_y2 = 1510

    rounded_rectangle(
        draw,
        [card_x1, card_y1, card_x2, card_y2],
        24,
        fill="white",
        outline=primary,
        width=4
    )

    # Header strip
    draw.rounded_rectangle(
        [card_x1, card_y1, card_x2, card_y1 + 75],
        radius=24,
        fill=accent
    )

    draw.rectangle(
        [card_x1, card_y1 + 45, card_x2, card_y1 + 75],
        fill=accent
    )

    draw.text(
        (card_x1 + 35, card_y1 + 22),
        "STUDENT DETAILS",
        font=section_font,
        fill=secondary
    )

    student_data = [
        ("Name", student_name or "____________________________"),
        ("Roll No", roll_no or "____________________________"),
        ("Course", course or "____________________________"),
        ("Semester", semester or "____________________________"),
        ("Session", session or "____________________________")
    ]

    y = card_y1 + 115

    for label, value in student_data:
        draw.text(
            (card_x1 + 40, y),
            f"{label}:",
            font=label_font,
            fill=secondary
        )

        draw.text(
            (card_x1 + 230, y),
            value,
            font=value_font,
            fill="#333333"
        )

        y += 65

    # -----------------------------------------------------
    # SUBMITTED TO CARD
    # -----------------------------------------------------
    submitted_y1 = 1580
    submitted_y2 = 1825

    rounded_rectangle(
        draw,
        [card_x1, submitted_y1, card_x2, submitted_y2],
        24,
        fill="white",
        outline=primary,
        width=4
    )

    draw.rounded_rectangle(
        [card_x1, submitted_y1, card_x2, submitted_y1 + 75],
        radius=24,
        fill=accent
    )

    draw.rectangle(
        [card_x1, submitted_y1 + 45, card_x2, submitted_y1 + 75],
        fill=accent
    )

    draw.text(
        (card_x1 + 35, submitted_y1 + 22),
        "SUBMITTED TO",
        font=section_font,
        fill=secondary
    )

    faculty_value = faculty or "____________________________"

    draw.text(
        (card_x1 + 40, submitted_y1 + 125),
        "Faculty / Teacher Name:",
        font=label_font,
        fill=secondary
    )

    draw.text(
        (card_x1 + 430, submitted_y1 + 125),
        faculty_value,
        font=value_font,
        fill="#333333"
    )

    # -----------------------------------------------------
    # DATE
    # -----------------------------------------------------
    date_y = 1910

    draw.text(
        (card_x1, date_y),
        "Submission Date:",
        font=label_font,
        fill=secondary
    )

    formatted_date = submission_date.strftime("%d %B %Y")

    draw.text(
        (card_x1 + 300, date_y),
        formatted_date,
        font=value_font,
        fill="#333333"
    )

    # -----------------------------------------------------
    # STUDENT PHOTO
    # -----------------------------------------------------
    if student_photo:
        try:
            photo = Image.open(student_photo).convert("RGB")
            photo.thumbnail((170, 170))

            photo_x = W - 190 - photo.width
            photo_y = 1920

            draw.rounded_rectangle(
                [
                    photo_x - 8,
                    photo_y - 8,
                    photo_x + photo.width + 8,
                    photo_y + photo.height + 8
                ],
                radius=18,
                fill=primary
            )

            img.paste(photo, (photo_x, photo_y))
        except:
            pass

    # -----------------------------------------------------
    # FOOTER
    # -----------------------------------------------------
    footer_y = H - 160

    center_text(
        draw,
        "ACADEMIC ASSIGNMENT • PROFESSIONAL COVER",
        footer_y,
        small_font,
        secondary,
        W
    )

    return img


# ---------------------------------------------------------
# PREVIEW
# ---------------------------------------------------------
if st.session_state.generated:

    st.markdown("---")
    st.markdown(
        '<div class="section-title">📄 Assignment Cover Preview</div>',
        unsafe_allow_html=True
    )

    cover = create_cover()

    preview_col, info_col = st.columns([2, 1])

    with preview_col:
        st.image(
            cover,
            caption="Generated Assignment Cover",
            use_container_width=True
        )

    with info_col:
        st.markdown(
            """
            <div class="preview-card">
                <h3 style="color:white;">✨ Cover Ready</h3>
                <p style="color:#a8bdd4;">
                Your professional academic assignment cover has been generated.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # PNG
        png_buffer = BytesIO()
        cover.save(png_buffer, format="PNG")
        png_data = png_buffer.getvalue()

        st.download_button(
            label="⬇️ Download PNG",
            data=png_data,
            file_name="assignment_cover.png",
            mime="image/png",
            use_container_width=True
        )

        # PDF
        pdf_buffer = BytesIO()
        cover.save(pdf_buffer, format="PDF", resolution=150.0)
        pdf_data = pdf_buffer.getvalue()

        st.download_button(
            label="📄 Download PDF",
            data=pdf_data,
            file_name="assignment_cover.pdf",
            mime="application/pdf",
            use_container_width=True
        )

        st.markdown(
            """
            <div class="small-note">
            Tip: For best printing results, download the PDF version.
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### 🎓 Academic")
        st.markdown(
            "Designed for university, college and school assignments."
        )

    with c2:
        st.markdown("### 🎨 Professional")
        st.markdown(
            "Premium layouts, geometric shapes and multiple themes."
        )

    with c3:
        st.markdown("### 📥 Export")
        st.markdown(
            "Download your finished cover as PNG or PDF."
        )
