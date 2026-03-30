import os
import pdfplumber
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')  
nltk.download('stopwords')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize                                                                                                                           

# -------------------------
# Extract text from PDF
# -------------------------
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + " "
    return text


# -------------------------
# Preprocess text
# -------------------------
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())

    filtered = [
        word for word in tokens
        if word.isalnum() and word not in stop_words
    ]

    return " ".join(filtered)


# -------------------------
# Skill extraction
# -------------------------
def extract_skills(text):
    skills_db = {
    "python": ["python"],
    "machine learning": ["machine learning", "ml"],
    "data analysis": ["data analysis", "data analytics"],
    "sql": ["sql", "mysql", "postgres"],
    "nlp": ["nlp", "natural language processing"],
    "pandas": ["pandas"],
    "scikit-learn": ["scikit", "sklearn"],
}

    found = []
    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return found


# -------------------------
# Similarity
# -------------------------
def compute_similarity(resume, job_desc):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, job_desc])
    return cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

# -------------------------
# Load Job Description from file
# -------------------------
def load_job_description(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Load job description
job_description = load_job_description("job_description.txt")

job_clean = preprocess(job_description)


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":

    job_description = """
    Looking for a Python developer with experience in machine learning,
    data analysis, NLP, and SQL.
    """

    job_clean = preprocess(job_description)

    folder = "resume"
    results = []

    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            path = os.path.join(folder, file)

            resume_text = extract_text_from_pdf(path)
            resume_clean = preprocess(resume_text)

            score = compute_similarity(resume_clean, job_clean)
            skills = extract_skills(resume_clean)

            results.append((file, score, skills))

    # Sort by score
    results.sort(key=lambda x: x[1], reverse=True)

    print("\n===== Resume Screening Results =====\n")

    for file, score, skills in results:
        print(f"{file}")
        print(f"Match Score: {round(score * 100, 2)}%")
        print(f"Skills Found: {skills}")
        print("-" * 40)