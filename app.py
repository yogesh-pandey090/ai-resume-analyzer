from flask import Flask, render_template, request
import PyPDF2
from job_recommender import recommend_job
from skills import skills_list, job_roles
from ai_feedback import feedback
from keyword_analyzer import analyze_keywords

app = Flask(__name__)


def extract_text_from_pdf(file):

    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text.lower()


def extract_skills(text):

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def analyze_resume(found_skills, job_role):

    required_skills = job_roles[job_role]

    matched = []
    missing = []

    for skill in required_skills:

        if skill in found_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (len(matched) / len(required_skills)) * 100

    return matched, missing, score


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():

    file = request.files['resume']
    job_role = request.form['jobrole']

    text = extract_text_from_pdf(file)

    skills = extract_skills(text)

    recommended_job = recommend_job(skills)

    keywords_found = analyze_keywords(text)

    # analyze resume
    matched, missing, score = analyze_resume(skills, job_role)

    # generate AI feedback
    tips = feedback(missing)

    return render_template(
        'result.html',
        skills=skills,
        matched=matched,
        missing=missing,
        tips=tips,   # PASSING FEEDBACK TO HTML
        score=round(score, 2),
        recommended_job = recommended_job,
        keywords_found=keywords_found
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)