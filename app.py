import streamlit as st
from resume_parser import parse_resume
from github_analyzer import analyze_github
from mentor_brain import get_mentor_advice
from emailer import send_email_report
import os

# Set page config
st.set_page_config(page_title="CareerWise AI", layout="wide")

# Load custom CSS
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title and header
st.title("CareerWise AI")
st.markdown("Your personalized career mentor for students.")

# Sidebar for inputs
with st.sidebar:
    st.header("Profile Inputs")
    resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"], key="resume")
    github_username = st.text_input("GitHub Username", placeholder="e.g., octocat", key="github")
    email_address = st.text_input("Email for Weekly Report", placeholder="e.g., student@example.com", key="email")
    analyze_button = st.button("Analyze My Profile", key="analyze")
    send_report = st.button("Send Weekly Report", key="report")

# Main content
col1, col2 = st.columns([2, 1])
with col1:
    if analyze_button and resume_file and github_username:
        # Save uploaded resume temporarily
        temp_path = "temp_resume.pdf"
        with open(temp_path, "wb") as f:
            f.write(resume_file.read())

        # Parse resume
        with st.spinner("Parsing resume..."):
            resume_data = parse_resume(temp_path)
            st.subheader("Resume Summary")
            if "error" in resume_data:
                st.error(resume_data["error"])
            else:
                st.markdown(f"**Name**: {resume_data.get('name', 'N/A')}")
                st.markdown(f"**Skills**: {', '.join(resume_data.get('skills', [])) or 'None'}")
                st.markdown(f"**Education**: {resume_data.get('education', 'N/A')}")
                if resume_data.get("warnings"):
                    st.warning("\n".join(resume_data.get("warnings", [])))

        # Analyze GitHub
        with st.spinner("Analyzing GitHub..."):
            github_summary = analyze_github(github_username)
            st.subheader("GitHub Summary")
            if "error" in github_summary:
                st.error(github_summary["error"])
            else:
                st.markdown(f"**Repositories**: {github_summary.get('repo_count', 0)}")
                st.markdown(f"**Languages**: {', '.join(github_summary.get('languages', [])) or 'None'}")
                st.markdown(f"**Total Stars**: {github_summary.get('total_stars', 0)}")
                st.markdown(f"**README Quality**: {github_summary.get('readme_quality', 'N/A')}")

        # Get mentor advice
        with st.spinner("Generating recommendations..."):
            advice = get_mentor_advice(resume_data, github_summary)
            st.subheader("Career Recommendations")
            st.markdown(advice)

        # Clean up temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)

with col2:
    if send_report and email_address and github_username:
        with st.spinner("Sending email report..."):
            github_summary = analyze_github(github_username)
            if "error" in github_summary:
                st.error(github_summary["error"])
            else:
                report_sent = send_email_report(email_address, github_summary)
                if report_sent:
                    st.success("Weekly report sent successfully!")
                else:
                    st.error("Failed to send email. Check credentials.")