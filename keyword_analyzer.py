keywords = [
"project",
"experience",
"internship",
"certification",
"achievement"
]

def analyze_keywords(text):

    found = []

    for word in keywords:

        if word in text:
            found.append(word)

    return found