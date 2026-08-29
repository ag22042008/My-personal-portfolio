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
    "email": "coonect2adityagupta@gmail.com",
    "phone": "+91 7985152841",
    "resume_drive_url": "https://drive.google.com/file/d/1xGEF4Q5dwljepgGmCLXG1fkbF8s5OMh6/view?usp=sharing",
    "resume_file_id": "1xGEF4Q5dwljepgGmCLXG1fkbF8s5OMh6",
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
            "github": "https://github.com/ag22042008/multi-agent-resarch-pipeline",
            "demo": "",
        },
        {
            "title": "Python ML Assistant",
            "period": "2025",
            "summary": (
                "A dataset-aware coding assistant: upload a CSV/Excel file and it profiles "
                "the shape, dtypes, and missing values, then a dual-chain LangChain LCEL "
                "pipeline generates commented Python/ML code tailored to your real columns "
                "and, in parallel, a plain-language explanation of what the code does — all "
                "from a single query, in a chat-style Streamlit UI."
            ),
            "impact": "Code + explanation from one query",
            "tags": ["LangChain", "Mistral AI", "Streamlit", "Pandas"],
            "github": "https://github.com/ag22042008/Ml-Ai-Helpful-Assistant",
            "demo": "",
        },
        {
            "title": "City Assistant",
            "period": "2025",
            "summary": (
                "A LangChain/LangGraph agent answering weather, AQI, and local news "
                "questions for any city through a Streamlit chat UI, with human-in-the-loop "
                "approval required before every tool call using LangGraph's interrupt/resume "
                "support, plus per-session conversation memory via MemorySaver."
            ),
            "impact": "Human approval gates every tool call",
            "tags": ["LangChain", "LangGraph", "Streamlit", "Tavily"],
            "github": "https://github.com/ag22042008/CITY-AGENT-ASSISTANT-TOOL-WITH-CREATE-AGENT-FUNCTION",
            "demo": "",
        },
        {
            "title": "CourseMate-AI College Assistant",
            "period": "2026",
            "summary": (
                "An upgraded college assistant built on LangGraph conditional RAG: a "
                "classifier node routes each question to the right retriever — academic "
                "handbook, fee structure, or general knowledge — before generating a "
                "programme-personalized answer with page-level citations. Documents are "
                "chunked and indexed into FAISS, with configurable chunk size/overlap and "
                "a CLI mode alongside the Streamlit UI."
            ),
            "impact": "Routes each query to the right document set automatically",
            "tags": ["LangGraph", "FAISS", "RAG", "Streamlit"],
            "github": "https://github.com/ag22042008/Course-mate-AI-College-Assistant",
            "demo": "",
        },
        {
            "title": "Stock News Sentiment Analyzer",
            "period": "2025",
            "summary": (
                "A live financial-news sentiment dashboard: pulls headlines for any ticker "
                "via the Finnhub API with a rate-limited, day-by-day fetch loop, classifies "
                "each headline with FinBERT — a BERT model fine-tuned on financial text — "
                "and combines the label with its confidence into a weighted sentiment score "
                "from -1 to +1, visualized with Plotly."
            ),
            "impact": "Weighted sentiment score, not just a label",
            "tags": ["Hugging Face", "FinBERT", "Finnhub API", "Plotly"],
            "github": "https://github.com/ag22042008/Stock_news_sentiment_analysis_web_app",
            "demo": "",
        },
        {
            "title": "Order a Java",
            "period": "2025",
            "summary": (
                "A café-themed Java code generator: describe what you need, and a LangChain "
                "LCEL pipeline built around RunnablePassthrough runs code generation and a "
                "plain-language explanation in parallel, delivered as an order ticket with "
                "separate 'Ticket' and 'Barista's Notes' tabs."
            ),
            "impact": "Code + explanation generated in parallel",
            "tags": ["LangChain", "LCEL", "Streamlit", "Mistral AI"],
            "github": "https://github.com/ag22042008/Ai-code-reviewer-with-explanation-implementation-of-runnablepassthrough",
            "demo": "",
        },
        {
            "title": "AI Agent Studio",
            "period": "2025",
            "summary": (
                "Three standalone chatbot experiments merged into one Streamlit app: a "
                "comic chatbot, a mood-adaptive chatbot whose entire system prompt swaps "
                "with the selected mood, and a movie-detail extractor with both structured "
                "(Pydantic) and prose-report output modes — sharing one router and a "
                "dark/gold theme."
            ),
            "impact": "3 chatbot experiments, 1 shared UI",
            "tags": ["LangChain", "Streamlit", "Pydantic"],
            "github": "https://github.com/ag22042008/Ai-AGENT-STUDIO",
            "demo": "",
        },
        {
            "title": "AI Financial Advisor",
            "period": "2025",
            "summary": (
                "A RAG-based investment analyzer: upload annual reports or 10-K filings and "
                "it retrieves the relevant sections via Mistral embeddings and Chroma, then "
                "returns document-grounded analysis of revenue, profitability, debt, and "
                "cash flow with a Buy/Hold/Sell recommendation and page-level citations."
            ),
            "impact": "Cites the source page for every claim",
            "tags": ["RAG", "ChromaDB", "Mistral AI", "Streamlit"],
            "github": "https://github.com/ag22042008/financial-web-analyzer",
            "demo": "",
        },
        {
            "title": "MinuteMind",
            "period": "2025",
            "summary": (
                "Turns a meeting recording into a full digest: Whisper transcription, "
                "map-reduce summarization so long meetings never hit token limits, "
                "extracted action items/decisions/open questions, and a RAG chatbot that "
                "answers follow-up questions about what was actually discussed."
            ),
            "impact": "Map-reduce summarization avoids token limits",
            "tags": ["LangChain", "Groq Whisper", "RAG", "Streamlit"],
            "github": "https://github.com/ag22042008/Minute_Mind",
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

# Viridis-inspired palette, adapted for a dark theme
COLORS = {
    "bg": "#120E1F",
    "surface": "#1C1730",
    "ink": "#EDEAF8",
    "muted": "#A79FC7",
    "accent_1": "#C4A7FF",  # lightened violet
    "accent_2": "#5FD4F0",  # lightened blue
    "accent_3": "#4ADE80",  # lightened green
    "accent_4": "#FDE725",  # yellow
    "card_border": "rgba(196,167,255,0.20)",
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
    --surface: {COLORS['surface']};
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
        linear-gradient(rgba(196,167,255,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(196,167,255,0.05) 1px, transparent 1px);
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
    color: var(--ink) !important;
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
    font-weight: 600;
    background: linear-gradient(120deg, var(--a1), var(--a2));
    color: var(--bg) !important;
    text-decoration: none !important;
    transition: transform .15s ease, filter .15s ease;
}}
.link-chip:hover {{
    filter: brightness(1.12);
    transform: translateY(-2px);
}}

.notebook-cell {{
    border: 1.4px solid var(--border);
    border-left: 4px solid var(--a1);
    border-radius: 10px;
    padding: 20px 22px;
    margin-bottom: 18px;
    background: var(--surface);
    color: var(--ink);
    box-shadow: 0 2px 14px rgba(0,0,0,0.25);
    transition: transform .15s ease, box-shadow .15s ease;
}}
.notebook-cell:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 26px rgba(0,0,0,0.4);
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
    color: var(--ink);
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
    border: 2px solid var(--bg);
}}

.stTabs [data-baseweb="tab-list"] {{
    gap: 6px;
}}
.stTabs [data-baseweb="tab"] {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: var(--muted) !important;
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
    color: var(--bg);
    border-color: var(--a1);
}}

.stDownloadButton>button {{
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    border-radius: 8px;
    border: 1.4px solid var(--a1);
    color: var(--a1);
    background: transparent;
}}
.stDownloadButton>button:hover {{
    background: var(--a1);
    color: var(--bg);
    border-color: var(--a1);
}}

/* --- Hard overrides so nothing can silently inherit an invisible color ---
   (this is what broke: some elements relied on inherited color, which a
   viewer's OS/browser dark mode was allowed to override to near-white) --- */
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] strong {{
    color: var(--ink) !important;
}}
[data-testid="stMetricValue"] {{ color: var(--ink) !important; }}
[data-testid="stMetricLabel"] {{ color: var(--muted) !important; }}
label, .stTextInput label, .stTextArea label {{ color: var(--ink) !important; }}
.stTextInput input, .stTextArea textarea {{
    color: var(--ink) !important;
    background: var(--surface) !important;
    border-color: var(--border) !important;
}}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------------------------------
# HELPERS
# -------------------------------------------------------------------------
def chips(items):
    return " ".join(f'<span class="chip">{item}</span>' for item in items)


@st.cache_data(show_spinner=False, ttl=3600)
def fetch_drive_file_bytes(file_id):
    """Downloads a publicly-shared Google Drive file's raw bytes.
    Handles the 'file too large to scan for viruses' confirmation step
    Google adds for larger files. Cached for an hour so it's only
    fetched once per session, not on every rerun."""
    import requests
    session = requests.Session()
    base_url = "https://drive.google.com/uc"
    resp = session.get(base_url, params={"id": file_id, "export": "download"}, stream=True)
    token = next((v for k, v in resp.cookies.items() if k.startswith("download_warning")), None)
    if token:
        resp = session.get(base_url, params={"id": file_id, "export": "download", "confirm": token}, stream=True)
    resp.raise_for_status()
    return resp.content


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
        xaxis=dict(title="epoch", gridcolor="rgba(196,167,255,0.15)", zeroline=False),
        yaxis=dict(title="val_accuracy", gridcolor="rgba(196,167,255,0.15)", zeroline=False, range=[0, 1]),
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

    # --- RESUME DOWNLOAD ---
    # Fetches the actual file from the Google Drive link in CONFIG each session.
    # If that ever fails (link permissions changed, no internet, etc.) it
    # falls back to a plain "open in Drive" button instead of breaking the page.
    st.write("")
    try:
        resume_bytes = fetch_drive_file_bytes(CONFIG["resume_file_id"])
        st.download_button(
            "⬇ Download Résumé",
            data=resume_bytes,
            file_name=f"{CONFIG['name'].replace(' ', '_')}_Resume.pdf",
            mime="application/pdf",
        )
    except Exception:
        st.markdown(
            f'<a class="link-chip" href="{CONFIG["resume_drive_url"]}" target="_blank">Résumé ↗</a>',
            unsafe_allow_html=True,
        )

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
    st.markdown(
        "<p style='color:var(--muted); font-size:0.88rem; margin-top:-4px;'>"
        "MinuteMind also lives here as a standalone repo — an earlier build of the "
        "console now folded into the Unified AI Student Assistant. CourseMate-AI's "
        "College Assistant version below supersedes an earlier, simpler build.</p>",
        unsafe_allow_html=True,
    )
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
                <div class="cell-prompt">In [{i + 4}]: load_project("{proj['title']}")</div>
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
    st.markdown('<div class="eyebrow">In [14]: experience()</div>', unsafe_allow_html=True)
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
    st.markdown('<div class="eyebrow">In [15]: certifications()</div>', unsafe_allow_html=True)
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
