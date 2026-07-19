import streamlit as st
from parser import extract_text
from skill_extractor import extract_skills
from ats_score import calculate_score

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Screening Agent")

st.write("Upload your Resume and Job Description")

# Upload files
resume = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.file_uploader(
    "📋 Upload Job Description",
    type=["pdf", "docx", "txt"]
)

# Button appears only after both files are uploaded
if resume and job_description:

    if st.button("🚀 Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            # Extract text
            resume_text = extract_text(resume)
            jd_text = extract_text(job_description)

            # Extract skills
            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(jd_text)

            # ATS Score
            score = calculate_score(resume_skills, jd_skills)

            matched = sorted(
                list(set(resume_skills).intersection(jd_skills))
            )

            missing = sorted(
                list(set(jd_skills) - set(resume_skills))
            )

        st.success("✅ Analysis Completed!")

        st.header("📊 ATS Score")
        st.metric("Match Percentage", f"{score}%")

        st.progress(score / 100)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Resume Skills")
            st.write(resume_skills)

        with col2:
            st.subheader("📋 Required Skills")
            st.write(jd_skills)

        col3, col4 = st.columns(2)

        with col3:
            st.subheader("🟢 Matched Skills")
            st.success(", ".join(matched) if matched else "None")

        with col4:
            st.subheader("🔴 Missing Skills")
            st.error(", ".join(missing) if missing else "None")

        with st.expander("📄 Resume Text"):
            st.write(resume_text)

        with st.expander("📋 Job Description Text"):
            st.write(jd_text)

else:
    st.info("Please upload both Resume and Job Description.")