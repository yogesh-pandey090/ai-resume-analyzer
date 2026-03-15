def ats_score(found_skills, required_skills):

    matched = set(found_skills).intersection(required_skills)

    score = (len(matched) / len(required_skills)) * 100

    return round(score,2)