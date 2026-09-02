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
    "resume_drive_url": "https://drive.google.com/file/d/1pX9MCidXtukasJaiwodc7Z5XKxPlfKln/view?usp=sharing",
    "resume_file_id": "1pX9MCidXtukasJaiwodc7Z5XKxPlfKln",
    "avatar_url": "data:image/jpeg;base64,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",  # embedded photo (base64) so it works with no external dependency
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
            "demo": "https://ai-sudentassistant-cjeybzvunzppshmbucctkj.streamlit.app/",
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
            "demo": "https://multi-agent-resarch-pipeline-6n4dy7ebqkrkkxnbbse7hw.streamlit.app/",
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
            "demo": "https://course-mate-ai-college-assistant-qigo5th7xe6ubjrww9gw3v.streamlit.app/",
        },
        {
            "title": "CourseMate-AI",
            "period": "2025",
            "summary": (
                "The original retrieval-augmented PDF chatbot that answers questions "
                "grounded only in an uploaded document: chunks and embeds the text with "
                "Mistral, stores the vectors in Chroma, retrieves with MMR search for a "
                "balance of relevance and diversity, and shows exactly which passages were "
                "used for every answer."
            ),
            "impact": "Answers grounded only in the source PDF",
            "tags": ["RAG", "ChromaDB", "Mistral AI", "Streamlit"],
            "github": "https://github.com/ag22042008/Course-mate-AI",
            "demo": "https://course-mate-ai-33fkzywiggeuztfz7hgdgh.streamlit.app/",
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
            "demo": "https://financial-web-analyzer-hgaen5ufudneuc6pmacywz.streamlit.app/",
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
                "Built and shipped MinuteMind, an AI meeting-intelligence tool using the Groq Whisper API, saving 30+ minutes of manual review time per meeting across 15+ meetings processed during the internship",
"Designed a map-reduce summarization pipeline capable of processing meetings up to 3 hours long without hitting LLM token limits, and built a RAG-based chatbot layer letting users query meeting transcripts directly instead of re-watching recordings.",
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
    st.markdown(
        f"""
        <div style="width:104px; height:104px; border-radius:50%; padding:3px;
                    background:linear-gradient(135deg, var(--a1), var(--a2), var(--a3), var(--a4));
                    margin-bottom:16px;">
            <img src="{CONFIG['avatar_url']}" style="width:100%; height:100%; border-radius:50%;
                       object-fit:cover; display:block; border:3px solid var(--bg);" />
        </div>
        """,
        unsafe_allow_html=True,
    )
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
        "College Assistant version is the newer, more capable rebuild of the original.</p>",
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
    st.markdown('<div class="eyebrow">In [15]: experience()</div>', unsafe_allow_html=True)
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
    st.markdown('<div class="eyebrow">In [16]: certifications()</div>', unsafe_allow_html=True)
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
