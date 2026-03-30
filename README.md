# CSA-PROJECT
# Resume Screening Tool (NLP-Based)

## Overview

This project is an NLP-based Resume Screening Tool that compares resumes with a given job description and ranks candidates based on their relevance.

The system automates the initial screening process by analyzing textual data from resumes and identifying how well they match job requirements.

---

## Problem Statement

Recruiters often have to manually screen a large number of resumes, which is time-consuming and inefficient. There is also a risk of missing suitable candidates due to human limitations.

This project aims to solve this problem by automating resume evaluation using Natural Language Processing techniques.

---

## Solution

The system:

* Extracts text from resume PDFs
* Cleans and preprocesses the text
* Converts text into numerical form using TF-IDF
* Compares resumes with job descriptions using cosine similarity
* Extracts relevant skills
* Ranks resumes based on match score

---

## Features

* Resume parsing (PDF support)
* NLP-based preprocessing (tokenization, stopword removal)
* TF-IDF vectorization
* Cosine similarity scoring
* Multiple resume ranking
* Skill extraction with synonym matching

---

## Tech Stack

* Python
* NLTK
* Scikit-learn
* pdfplumber

---

## Project Structure

resume-screening-nlp/
│── app.py
│── requirements.txt
│── job_description.txt
│── resumes/
│   │── resume1.pdf
│   │── resume2.pdf

---

## How to Run the Project

### 1. Clone the repository

git clone repo link- (https://github.com/vaishali-07743/CSA-PROJECT.git)
cd resume-screening-nlp

### 2. Install dependencies

pip install -r requirements.txt

### 3. Add resumes

Place your resume PDFs inside the resumes/ folder.

### 4. Edit job description

Modify job_description.txt with your desired job role.

### 5. Run the project

python app.py

---

## Output

The system will display:

* Match Score (%)
* Extracted Skills
* Ranked resumes

### Example:

resume1.pdf
Match Score: 89.2%
Skills: ['python', 'machine learning', 'sql']
----------------------------------------

---

## Development Process

This project was built step-by-step:

1. Started with basic project setup
2. Implemented PDF text extraction
3. Added NLP preprocessing using NLTK
4. Applied TF-IDF and cosine similarity
5. Extended to handle multiple resumes
6. Added skill extraction
7. Improved skill matching using synonyms and regex

---

## Challenges Faced

### 1. PDF Text Extraction

Some resumes did not extract properly because they were image-based. This was handled by using text-based PDFs.

### 2. NLTK Errors

There were issues with missing resources such as punkt_tab, which required manual downloading of additional datasets.

### 3. Skill Matching Accuracy

Initially, the system used simple keyword matching, which was not very accurate. This was improved by adding synonyms and using regex-based matching.

### 4. Time Constraints

Due to limited time, the focus was kept on implementing core functionality rather than adding a graphical interface or advanced models.

---

## Limitations

* Does not understand deep semantic meaning
* Skill matching depends on predefined dictionary
* Cannot process image-based resumes
* No graphical interface

---

## Future Improvements

* Use advanced NLP models like BERT
* Add a web interface using Flask
* Improve skill extraction using machine learning
* Support more file formats

---

## What I Learned

* Practical use of NLP in real-world applications
* Importance of preprocessing in text analysis
* Understanding TF-IDF and cosine similarity
* Handling real-world data issues
* Using GitHub for version control

---

## Conclusion

This project demonstrates how NLP can be applied to automate resume screening. While simple, it provides a functional and scalable solution to a real-world problem.

---

## Author 
Vaishali Sukhnani
25BCE11353
