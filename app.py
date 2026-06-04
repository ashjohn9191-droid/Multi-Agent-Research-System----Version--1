import streamlit as st
from crew import crew
from datetime import datetime

st.set_page_config(
    page_title="Ashley AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

/* Main App */
.stApp{
    background-color:#F5F7FA;
}

/* Title */
.main-title{
    text-align:center;
    font-size:52px;
    font-weight:800;
    color:#2563EB;
    margin-bottom:5px;
}

/* Subtitle */
.sub-title{
    text-align:center;
    font-size:18px;
    color:#4B5563;
    margin-bottom:20px;
}

/* Report Box */
.report-box{
    background:white;
    color:black;
    padding:25px;
    border-radius:15px;
    border:1px solid #E5E7EB;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:white;
}

/* Input */
.stTextInput input{
    background:white !important;
    color:black !important;
    border-radius:10px;
}

/* Buttons */
.stButton > button{
    width:100%;
    border-radius:12px;
    height:50px;
    font-weight:bold;
}

/* History */
.stAlert{
    background:white !important;
    color:black !important;
}

/* Success Message */
.stSuccess{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.title("🤖 Ashley AI")

    st.markdown("### Features")

    st.markdown("""
    ✅ AI Research

    ✅ Fast Responses

    ✅ CrewAI Powered

    ✅ Report Generation

    ✅ Download Reports
    """)

    st.markdown("---")

    st.info("Powered by CrewAI + Groq")

# ==========================
# HEADER
# ==========================

st.markdown(
    "<div class='main-title'>Ashley AI Research Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>AI Powered Research System</div>",
    unsafe_allow_html=True
)

st.divider()

# ==========================
# SESSION STATE
# ==========================

if "history" not in st.session_state:
    st.session_state.history = []

# ==========================
# INPUT
# ==========================

topic = st.text_input(
    "🔍 Enter Research Topic",
    placeholder="Example: Agentic AI, Machine Learning, Data Science"
)

col1, col2 = st.columns(2)

with col1:
    start_btn = st.button("🚀 Start Research")

with col2:
    clear_btn = st.button("🗑 Clear History")

# ==========================
# CLEAR HISTORY
# ==========================

if clear_btn:
    st.session_state.history = []
    st.rerun()

# ==========================
# START RESEARCH
# ==========================

if start_btn:

    if topic.strip():

        with st.spinner("🔎 Ashley AI is researching..."):

            result = crew.kickoff(
                inputs={
                    "topic": topic
                }
            )

        report = str(result)

        st.session_state.history.append({
            "topic": topic,
            "time": datetime.now().strftime("%H:%M:%S")
        })

        st.success("✅ Research Completed!")

        st.markdown("## 📄 Final Report")

        st.markdown(
            f"<div class='report-box'>{report}</div>",
            unsafe_allow_html=True
        )

        st.download_button(
            label="⬇ Download Report",
            data=report,
            file_name=f"{topic}_report.txt",
            mime="text/plain"
        )

# ==========================
# HISTORY
# ==========================

if st.session_state.history:

    st.divider()

    st.subheader("🕒 Research History")

    for item in reversed(st.session_state.history):

        st.info(
            f"📌 {item['topic']} | {item['time']}"
        )