def feedback(missing_skills):

    tips = []

    if "machine learning" in missing_skills:
        tips.append(
        "Consider adding Machine Learning projects like prediction models or data analysis projects."
        )

    if "sql" in missing_skills:
        tips.append(
        "Learn SQL for database management and data querying. Add a project using MySQL or PostgreSQL."
        )

    if "python" in missing_skills:
        tips.append(
        "Python is essential for data science roles. Add Python-based projects to strengthen your resume."
        )

    if "pandas" in missing_skills:
        tips.append(
        "Use Pandas for data manipulation and show projects involving data cleaning and analysis."
        )

    if len(tips) == 0:
        tips.append("Great! Your resume already contains most of the required skills.")

    return tips