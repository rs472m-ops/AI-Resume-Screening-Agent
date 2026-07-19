from skill_extractor import extract_skills
from ats_score import calculate_score

resume = """
Python
SQL
Pandas
Git
Excel
"""

job_description = """
Python
SQL
Power BI
Azure
Excel
Git
"""

resume_skills = extract_skills(resume)
jd_skills = extract_skills(job_description)

score = calculate_score(resume_skills, jd_skills)

matched = list(set(resume_skills).intersection(set(jd_skills)))
missing = list(set(jd_skills) - set(resume_skills))

print("Resume Skills:", resume_skills)
print("Job Skills:", jd_skills)
print("Matched Skills:", matched)
print("Missing Skills:", missing)
print("ATS Score:", score)