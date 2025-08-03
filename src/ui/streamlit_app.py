import streamlit as st
import os
from pathlib import Path

# Add the src directory to the Python path
import sys
src_path = Path(__file__).parent.parent
sys.path.insert(0, str(src_path))

from core.resume_parser import parse_resume
from core.github_analyzer import analyze_github
from core.mentor_brain import get_mentor_advice
from core.emailer import send_email_report
from utils.config import Config

# Set page config with improved styling
st.set_page_config(
    page_title="CareerWise AI - Your Career Mentor",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS using Streamlit's markdown for minimal styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .sidebar-header {
        color: #1f77b4;
        font-weight: bold;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main header with emoji and better styling
st.markdown('<h1 class="main-header">🎯 CareerWise AI</h1>', unsafe_allow_html=True)
st.markdown("### Your personalized career mentor for students")

# Sidebar with improved layout
with st.sidebar:
    st.markdown('<h3 class="sidebar-header">📋 Profile Inputs</h3>', unsafe_allow_html=True)
    
    # File uploader with better description
    st.markdown("**📄 Upload Your Resume**")
    resume_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        key="resume",
        help="Upload your resume in PDF format for analysis"
    )
    
    # GitHub username input
    st.markdown("**🐙 GitHub Username**")
    github_username = st.text_input(
        "Enter your GitHub username",
        placeholder="e.g., octocat",
        key="github",
        help="We'll analyze your GitHub profile and repositories"
    )
    
    # Email input
    st.markdown("**📧 Email for Weekly Reports**")
    email_address = st.text_input(
        "Enter your email address",
        placeholder="e.g., student@example.com",
        key="email",
        help="Receive weekly career insights and recommendations"
    )
    
    st.markdown("---")
    
    # Action buttons with better styling
    col1, col2 = st.columns(2)
    with col1:
        analyze_button = st.button(
            "🔍 Analyze Profile",
            key="analyze",
            use_container_width=True,
            type="primary"
        )
    
    with col2:
        send_report = st.button(
            "📊 Send Report",
            key="report",
            use_container_width=True
        )

# Main content area
if analyze_button and resume_file and github_username:
    # Progress indicator
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Step 1: Parse resume
    status_text.text("📄 Parsing your resume...")
    progress_bar.progress(25)
    
    temp_path = "temp_resume.pdf"
    with open(temp_path, "wb") as f:
        f.write(resume_file.read())

    resume_data = parse_resume(temp_path)
    
    # Resume results
    st.markdown("## 📄 Resume Analysis")
    if "error" in resume_data:
        st.error(f"❌ Resume parsing failed: {resume_data['error']}")
    else:
        # Create a nice card-like display for resume data
        with st.container():
            st.markdown("### Personal Information")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("👤 Name", resume_data.get('name', 'N/A'))
                st.metric("🎓 Education", resume_data.get('education', 'N/A'))
            with col2:
                skills_list = resume_data.get('skills', [])
                if skills_list:
                    st.markdown("**🛠️ Skills:**")
                    for skill in skills_list[:5]:  # Show first 5 skills
                        st.markdown(f"• {skill}")
                else:
                    st.markdown("**🛠️ Skills:** None detected")
        
        if resume_data.get("warnings"):
            st.warning("⚠️ **Resume Warnings:**")
            for warning in resume_data.get("warnings", []):
                st.markdown(f"• {warning}")
    
    # Step 2: Analyze GitHub
    status_text.text("🐙 Analyzing your GitHub profile...")
    progress_bar.progress(50)
    
    github_summary = analyze_github(github_username)
    
    # GitHub results
    st.markdown("## 🐙 GitHub Analysis")
    if "error" in github_summary:
        st.error(f"❌ GitHub analysis failed: {github_summary['error']}")
    else:
        # Create metrics display for GitHub data
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📦 Repositories", github_summary.get('repo_count', 0))
        with col2:
            st.metric("⭐ Total Stars", github_summary.get('total_stars', 0))
        with col3:
            st.metric("📊 README Quality", github_summary.get('readme_quality', 'N/A'))
        
        # Languages used
        languages = github_summary.get('languages', [])
        if languages:
            st.markdown("**💻 Programming Languages:**")
            lang_cols = st.columns(min(len(languages), 4))
            for i, lang in enumerate(languages[:4]):
                with lang_cols[i]:
                    st.markdown(f"• {lang}")
    
    # Step 3: Get mentor advice
    status_text.text("🧠 Generating personalized recommendations...")
    progress_bar.progress(75)
    
    advice = get_mentor_advice(resume_data, github_summary)
    
    # Career recommendations
    st.markdown("## 🎯 Career Recommendations")
    st.markdown(advice)
    
    # Complete progress
    progress_bar.progress(100)
    status_text.text("✅ Analysis complete!")
    
    # Clean up temp file
    if os.path.exists(temp_path):
        os.remove(temp_path)

# Email report section
if send_report and email_address and github_username:
    st.markdown("## 📧 Weekly Report")
    
    with st.spinner("📤 Sending your weekly report..."):
        github_summary = analyze_github(github_username)
        if "error" in github_summary:
            st.error(f"❌ Failed to analyze GitHub: {github_summary['error']}")
        else:
            report_sent = send_email_report(email_address, github_summary)
            if report_sent:
                st.success("✅ Weekly report sent successfully! Check your email.")
            else:
                st.error("❌ Failed to send email. Please check your credentials.")

# Welcome message when no analysis has been performed
if not analyze_button and not send_report:
    st.markdown("## 🚀 Welcome to CareerWise AI!")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **What we can do for you:**
        
        🔍 **Profile Analysis**: Upload your resume and GitHub username to get a comprehensive analysis of your professional profile.
        
        📊 **GitHub Insights**: We'll analyze your repositories, coding languages, and project quality.
        
        🎯 **Personalized Recommendations**: Get tailored career advice based on your skills and experience.
        
        📧 **Weekly Reports**: Receive regular updates and insights to keep your career on track.
        
        **Ready to get started?** Use the sidebar to upload your resume and enter your GitHub username!
        """)
    
    with col2:
        st.markdown("""
        **💡 Tips for best results:**
        
        • Ensure your resume is in PDF format
        • Use your actual GitHub username
        • Make sure your GitHub profile is public
        • Include a valid email for weekly reports
        """)

# Footer
st.markdown("---")
st.markdown("*Powered by CareerWise AI - Your personal career mentor*")