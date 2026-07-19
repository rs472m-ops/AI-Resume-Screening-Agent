def calculate_score(resume_skills, jd_skills):
    """
    Calculate ATS Match Score
    """

    if len(jd_skills) == 0:
        return 0

    matched_skills = set(resume_skills).intersection(set(jd_skills))

    score = (len(matched_skills) / len(jd_skills)) * 100

    return round(score, 2)