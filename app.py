"""
=============================================================
 DATA SCIENCE / ML PORTFOLIO — Streamlit App
=============================================================

HOW TO RUN
    1) pip install -r requirements.txt
    2) streamlit run app.py

HOW TO CUSTOMIZE
    Everything you need to change lives in the CONFIG
    dictionary right below the imports — name, bio, links,
    skills, projects, experience, education. Edit the values
    and save; Streamlit hot-reloads automatically.

    Want a résumé download button? Drop a file named
    "resume.pdf" next to this script and uncomment the
    block marked "RESUME DOWNLOAD" in the hero section below.
=============================================================
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
from urllib.parse import quote

# -------------------------------------------------------------------------
# CONFIG — edit everything below to make this your own
# -------------------------------------------------------------------------
CONFIG = {
    "name": "Aditya Gupta",
    "role": "Machine Learning Developer · Agentic AI & NLP",
    "location": "Noida, India",
    "email": "connect2adityagupta@gmail.com",
    "phone": "+91 7985152841",
    "tagline": "I build multi-agent AI systems that research, reason, and remember.",
    "bio": (
        "I'm a machine learning developer focused on agentic AI systems and applied "
        "NLP/ML in Python. I've built a multi-agent LangChain/LangGraph research "
        "pipeline with tool-calling search and reader agents, and a unified AI "
        "student assistant combining document RAG, meeting intelligence, and "
        "Socratic tutoring. Proficient in Python, SQL, LangChain, LangGraph, "
        "TensorFlow, Keras, and Streamlit — and I've solved 350+ DSA problems along the way."
    ),
    "focus_areas": ["Agentic AI Systems", "RAG & LLM Tooling", "NLP", "Multi-Agent Orchestration"],
    "grad_year": "2027",
    "dsa_solved": "350+",
    "links": {
        "GitHub": "https://github.com/ag22042008",
        "LinkedIn": "https://linkedin.com/in/aditya-gupta-205ba9281",
    },
    "skills": {
        "Languages & Databases": ["Python", "Java", "SQL (MySQL)"],
        "Agentic AI & Orchestration": ["LangChain", "LangGraph", "Multi-Agent Systems", "Tool-Calling", "Human-in-the-Loop"],
        "ML & Deep Learning": ["Scikit-learn", "TensorFlow", "Keras", "Hugging Face", "Logistic Regression"],
        "Generative AI / RAG": ["RAG", "ChromaDB", "Mistral AI", "Prompt Engineering"],
        "Data & Tools": ["Pandas", "NumPy", "Plotly", "Streamlit", "Git/GitHub", "EDA", "SMOTE"],
    },
    "projects": [
        {
            "title": "Unified AI Student Assistant",
            "period": "2026",
            "summary": (
                "A unified Streamlit dashboard combining three AI consoles: CourseMate-AI, "
                "a RAG pipeline ingesting PDFs and live URLs into ChromaDB with switchable "
                "Gemini/Mistral backends for grounded, page-cited answers; MinuteMind, which "
                "transcribes audio/video via the Groq Whisper API and extracts action items "
                "and decisions; and a Socratic AI tutor that guides students with follow-up "
                "questions instead of direct answers."
            ),
            "impact": "3 AI consoles, one unified app",
            "tags": ["LangChain", "ChromaDB", "Groq Whisper", "Gemini", "Streamlit"],
            "github": "https://github.com/ag22042008/AI-SudentAssistant",
            "demo": "",
        },
        {
            "title": "Multi-Agent Research Pipeline",
            "period": "2025",
            "summary": (
                "A 4-stage multi-agent pipeline (Search → Read → Write → Critique) that "
                "turns a research topic into a structured, source-cited report. A LangChain "
                "Search Agent uses Tavily-backed web search; a Reader Agent scrapes the most "
                "relevant URL via requests/BeautifulSoup; Writer and Critic components then "
                "produce a structured report and score it out of 10, all coordinated through "
                "a shared, inspectable state dict."
            ),
            "impact": "Auto-scores generated reports out of 10",
            "tags": ["LangChain", "LangGraph", "Tavily", "Mistral AI", "BeautifulSoup"],
            "github": "https://github.com/ag22042008/multi-agent-research-pipeline",
            "demo": "",
        },
    ],
    "experience": [
        {
            "role": "ML Developer Intern",
            "company": "Cognify Systems",
            "period": "January 2026 — Present",
            "bullets": [
                "Built and shipped AI-powered web application features with integrated ML "
                "functionality, collaborating with cross-functional engineering and product teams.",
                "Performed model training, data preprocessing, and feature engineering on "
                "production datasets; owned the end-to-end handoff from Jupyter notebook to "
                "deployed feature in live web applications.",
            ],
        },
    ],
    "education": [
        {
            "degree": "B.Tech, Computer Science (Data Science) — GPA 7.61/10",
            "school": "JSS Academy of Technical Education, Noida",
            "period": "2023 — 2027",
        },
    ],
    "certifications": [
        {"name": "Programming in Java", "issuer": "NPTEL, IIT Kharagpur (Elite, 90%)", "year": "2026"},
        {"name": "IBM Data Science with Python and MySQL", "issuer": "IBM / Coursera", "year": "2025"},
        {"name": "Applied Deep Learning", "issuer": "NIT Kurukshetra", "year": "2025"},
    ],
    "achievements": [
        "Selected for the internal round of Smart India Hackathon (SIH) for a team-based ML problem-solving project.",
        "Solved 350+ Data Structures and Algorithms problems across Codeforces and competitive programming platforms.",
    ],
}

# Viridis-inspired palette — a small nod to the default matplotlib colormap
COLORS = {
    "bg": "#FCFBFF",
    "ink": "#1B1730",
    "muted": "#6B678A",
    "accent_1": "#440154",  # deep violet
    "accent_2": "#31688E",  # blue
    "accent_3": "#35B779",  # green
    "accent_4": "#FDE725",  # yellow
    "card_border": "#E7E3F5",
}

st.set_page_config(
    page_title=f"{CONFIG['name']} — {CONFIG['role']}",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------------------------------------------------------
# STYLE
# -------------------------------------------------------------------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

:root {{
    --bg: {COLORS['bg']};
    --ink: {COLORS['ink']};
    --muted: {COLORS['muted']};
    --a1: {COLORS['accent_1']};
    --a2: {COLORS['accent_2']};
    --a3: {COLORS['accent_3']};
    --a4: {COLORS['accent_4']};
    --border: {COLORS['card_border']};
}}

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    color: var(--ink);
}}

.stApp {{
    background-color: var(--bg);
    background-image:
        linear-gradient(rgba(75,46,131,0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(75,46,131,0.035) 1px, transparent 1px);
    background-size: 34px 34px;
}}

#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
header {{background: transparent !important;}}

.block-container {{
    padding-top: 2.2rem;
    max-width: 1100px;
}}

h1, h2, h3, h4 {{
    font-family: 'Space Grotesk', sans-serif !important;
    letter-spacing: -0.01em;
}}

.eyebrow {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    color: var(--a2);
    letter-spacing: 0.03em;
    margin-bottom: 0.3rem;
}}

.gradient-text {{
    background: linear-gradient(100deg, var(--a1) 0%, var(--a2) 40%, var(--a3) 75%, var(--a4) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.hero-name {{
    font-size: 3.1rem;
    font-weight: 700;
    line-height: 1.05;
    margin-bottom: 0.3rem;
}}

.hero-tagline {{
    font-size: 1.2rem;
    color: var(--a1);
    font-weight: 600;
    margin-bottom: 0.6rem;
}}

.chip {{
    display: inline-block;
    padding: 5px 13px;
    margin: 3px 6px 3px 0;
    border-radius: 999px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    font-weight: 500;
    border: 1.4px solid var(--a2);
    color: var(--a1);
    background: rgba(53,183,121,0.07);
    text-decoration: none !important;
}}
.chip:hover {{
    background: var(--a3);
    color: #0d1b12;
}}

.link-chip {{
    display: inline-block;
    padding: 7px 16px;
    margin: 3px 8px 3px 0;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    font-weight: 500;
    background: var(--ink);
    color: #fff !important;
    text-decoration: none !important;
    transition: transform .15s ease, background .15s ease;
}}
.link-chip:hover {{
    background: var(--a1);
    transform: translateY(-2px);
}}

.notebook-cell {{
    border: 1.4px solid var(--border);
    border-left: 4px solid var(--a1);
    border-radius: 10px;
    padding: 20px 22px;
    margin-bottom: 18px;
    background: #ffffff;
    box-shadow: 0 2px 14px rgba(75,46,131,0.05);
    transition: transform .15s ease, box-shadow .15s ease;
}}
.notebook-cell:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 26px rgba(75,46,131,0.1);
}}

.cell-prompt {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    color: var(--a2);
    margin-bottom: 8px;
}}

.impact-badge {{
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    font-weight: 500;
    color: #0d1b12;
    background: var(--a4);
    padding: 4px 10px;
    border-radius: 6px;
    margin-top: 4px;
}}

.timeline-item {{
    border-left: 3px solid var(--a2);
    padding-left: 20px;
    margin-bottom: 26px;
    position: relative;
}}
.timeline-item::before {{
    content: '';
    position: absolute;
    left: -7px;
    top: 4px;
    width: 11px;
    height: 11px;
    border-radius: 50%;
    background: var(--a3);
    border: 2px solid #fff;
}}

.stTabs [data-baseweb="tab-list"] {{
    gap: 6px;
}}
.stTabs [data-baseweb="tab"] {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
}}
.stTabs [aria-selected="true"] {{
    color: var(--a1) !important;
    border-bottom-color: var(--a1) !important;
}}

.stButton>button {{
    font-family: 'JetBrains Mono', monospace;
    border-radius: 8px;
    border: 1.4px solid var(--a1);
    color: var(--a1);
}}
.stButton>button:hover {{
    background: var(--a1);
    color: white;
    border-color: var(--a1);
}}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------------------------------
# HELPERS
# -------------------------------------------------------------------------
def chips(items):
    return " ".join(f'<span class="chip">{item}</span>' for item in items)


def hero_chart():
    """A small 'training curve' — the portfolio's signature visual moment."""
    epochs = np.arange(1, 31)
    rng = np.random.default_rng(7)
    acc = 1 - np.exp(-epochs / 9) + rng.normal(0, 0.012, size=len(epochs))
    acc = np.clip(acc, 0, 0.985)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=epochs, y=acc,
        mode="lines+markers",
        line=dict(width=3, color=COLORS["accent_2"]),
        marker=dict(size=6, color=acc, colorscale="Viridis", showscale=False),
        hovertemplate="epoch %{x}<br>val_accuracy %{y:.3f}<extra></extra>",
    ))
    fig.update_layout(
        height=230,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(title="epoch", gridcolor="rgba(75,46,131,0.08)", zeroline=False),
        yaxis=dict(title="val_accuracy", gridcolor="rgba(75,46,131,0.08)", zeroline=False, range=[0, 1]),
        font=dict(family="JetBrains Mono", size=11, color=COLORS["muted"]),
    )
    return fig


# -------------------------------------------------------------------------
# HERO
# -------------------------------------------------------------------------
col1, col2 = st.columns([1.3, 1], gap="large")

with col1:
    st.markdown('<div class="eyebrow">In [1]: whoami()</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hero-name">{CONFIG["name"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hero-tagline">{CONFIG["role"]}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<p style="font-size:1.05rem; color:var(--ink); max-width:520px;">{CONFIG["tagline"]}</p>',
        unsafe_allow_html=True,
    )
    st.markdown(chips(CONFIG["focus_areas"]), unsafe_allow_html=True)
    st.write("")
    link_html = " ".join(
        f'<a class="link-chip" href="{url}" target="_blank">{label} ↗</a>'
        for label, url in CONFIG["links"].items()
    )
    st.markdown(link_html, unsafe_allow_html=True)

    # --- RESUME DOWNLOAD (optional) ---
    # Uncomment the block below after adding a "resume.pdf" file next to app.py
    # st.write("")
    # with open("resume.pdf", "rb") as f:
    #     st.download_button("Download résumé", f, file_name="resume.pdf", mime="application/pdf")

with col2:
    st.markdown(
        '<div class="eyebrow">Out [1]: sample training run (demo data)</div>',
        unsafe_allow_html=True,
    )
    st.plotly_chart(hero_chart(), use_container_width=True, config={"displayModeBar": False})

st.write("")

# -------------------------------------------------------------------------
# TABS
# -------------------------------------------------------------------------
tab_about, tab_skills, tab_projects, tab_experience, tab_certs, tab_contact = st.tabs(
    ["About", "Skills", "Projects", "Experience", "Certifications", "Contact"]
)

with tab_about:
    st.markdown('<div class="eyebrow">In [2]: about()</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1], gap="large")
    with c1:
        st.markdown(f"<div class='notebook-cell'>{CONFIG['bio']}</div>", unsafe_allow_html=True)
    with c2:
        st.metric("Graduating", CONFIG["grad_year"])
        st.metric("DSA problems solved", CONFIG["dsa_solved"])
        st.metric("Based in", CONFIG["location"])

with tab_skills:
    st.markdown('<div class="eyebrow">In [3]: skills()</div>', unsafe_allow_html=True)
    for category, items in CONFIG["skills"].items():
        st.markdown(f"**{category}**")
        st.markdown(f"<div style='margin-bottom:16px;'>{chips(items)}</div>", unsafe_allow_html=True)

with tab_projects:
    st.markdown('<div class="eyebrow">In [4]: projects()</div>', unsafe_allow_html=True)
    cols = st.columns(2, gap="medium")
    for i, proj in enumerate(CONFIG["projects"]):
        with cols[i % 2]:
            links = ""
            if proj.get("github"):
                links += f'<a class="link-chip" href="{proj["github"]}" target="_blank">Code ↗</a>'
            if proj.get("demo"):
                links += f'<a class="link-chip" href="{proj["demo"]}" target="_blank">Demo ↗</a>'
            st.markdown(f"""
            <div class="notebook-cell">
                <div class="cell-prompt">In [{i + 5}]: load_project("{proj['title']}")</div>
                <h4 style="margin:0 0 6px 0;">{proj['title']}
                    <span style="color:var(--muted); font-weight:400; font-size:0.85rem;"> · {proj['period']}</span>
                </h4>
                <p style="color:var(--ink); font-size:0.94rem;">{proj['summary']}</p>
                <div class="impact-badge">{proj['impact']}</div>
                <div style="margin-top:10px;">{chips(proj['tags'])}</div>
                <div style="margin-top:12px;">{links}</div>
            </div>
            """, unsafe_allow_html=True)

with tab_experience:
    st.markdown('<div class="eyebrow">In [9]: experience()</div>', unsafe_allow_html=True)
    for exp in CONFIG["experience"]:
        bullets_html = "".join(f"<li style='margin-bottom:4px;'>{b}</li>" for b in exp["bullets"])
        st.markdown(f"""
        <div class="timeline-item">
            <div style="font-family:'JetBrains Mono',monospace; font-size:0.78rem; color:var(--a2);">{exp['period']}</div>
            <h4 style="margin:2px 0 2px 0;">{exp['role']} · {exp['company']}</h4>
            <ul style="margin-top:6px; padding-left:18px; color:var(--ink); font-size:0.93rem;">{bullets_html}</ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="eyebrow">education</div>', unsafe_allow_html=True)
    for ed in CONFIG["education"]:
        st.markdown(f"**{ed['degree']}** — {ed['school']} ({ed['period']})")

with tab_certs:
    st.markdown('<div class="eyebrow">In [10]: certifications()</div>', unsafe_allow_html=True)
    cert_cols = st.columns(len(CONFIG["certifications"]))
    for col, cert in zip(cert_cols, CONFIG["certifications"]):
        with col:
            st.markdown(f"""
            <div class="notebook-cell">
                <div class="cell-prompt">{cert['year']}</div>
                <h4 style="margin:0 0 4px 0; font-size:1.02rem;">{cert['name']}</h4>
                <p style="color:var(--muted); font-size:0.86rem; margin:0;">{cert['issuer']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="eyebrow" style="margin-top:8px;">achievements</div>', unsafe_allow_html=True)
    for ach in CONFIG["achievements"]:
        st.markdown(f"- {ach}")

with tab_contact:
    st.markdown('<div class="eyebrow">In [∞]: contact()</div>', unsafe_allow_html=True)
    st.markdown(
        f"Reach me directly at **{CONFIG['email']}** or **{CONFIG['phone']}**, "
        f"or send a note below — it opens in your email client, pre-filled."
    )

    with st.form("contact_form"):
        c1, c2 = st.columns(2)
        sender_name = c1.text_input("Your name")
        sender_email = c2.text_input("Your email")
        message = st.text_area("Message", height=140)
        submitted = st.form_submit_button("Prepare email")

    if submitted:
        if not message.strip():
            st.warning("Add a message before sending.")
        else:
            subject = quote(f"Portfolio contact from {sender_name or 'a visitor'}")
            body = quote(f"{message}\n\n— {sender_name} ({sender_email})")
            mailto = f"mailto:{CONFIG['email']}?subject={subject}&body={body}"
            st.markdown(f'<a class="link-chip" href="{mailto}">Open in email client ↗</a>', unsafe_allow_html=True)

    st.write("")
    link_html2 = " ".join(
        f'<a class="link-chip" href="{url}" target="_blank">{label} ↗</a>'
        for label, url in CONFIG["links"].items()
    )
    st.markdown(link_html2, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# FOOTER
# -------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    f"<p style='text-align:center; color:var(--muted); font-family:JetBrains Mono, monospace; "
    f"font-size:0.78rem;'>Built with Streamlit · {CONFIG['name']} © 2026</p>",
    unsafe_allow_html=True,
)
