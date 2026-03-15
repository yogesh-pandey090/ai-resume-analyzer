job_roles = {

"Data Scientist":[
"python","machine learning","pandas","numpy","data analysis"
],

"Web Developer":[
"html","css","javascript","react","flask"
],

"Data Analyst":[
"python","sql","pandas","data analysis"
]

}


def recommend_job(found_skills):

    best_role = None
    max_match = 0

    for role,skills in job_roles.items():

        match = len(set(found_skills).intersection(skills))

        if match > max_match:

            max_match = match
            best_role = role

    return best_role