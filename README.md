Resume Analyzer

Overview

Resume Analyzer is a Python-based application that analyzes resumes and provides an ATS-style evaluation. The program extracts important information such as contact details and technical skills from PDF, DOCX, or TXT resume files, then calculates a basic resume score and generates feedback to help improve the resume.

Features

- Upload and analyze PDF, DOCX, and TXT resumes.
- Extract email address and phone number.
- Identify technical skills from the resume.
- Generate a basic ATS (Applicant Tracking System) score.
- Provide feedback based on the resume score.
- Simple command-line interface for easy use.

Technologies Used

- Python
- Regular Expressions (Regex)
- PDFPlumber
- Python-Docx
- File Handling

Project Structure

- "resume_analyzer.py" – Main application source code.
- "sample_resume.docx" – Sample resume for testing.
- "README.md" – Project documentation.

How to Run

1. Install Python 3.
2. Install the required libraries:
   pip install pdfplumber python-docx
3. Run the application:
   python resume_analyzer.py
4. Enter the path of a PDF, DOCX, or TXT resume file when prompted.
5. View the extracted information, detected skills, ATS score, and resume analysis.

Future Improvements

- Web-based interface using Streamlit or Flask.
- AI-powered resume scoring and suggestions.
- Job description matching.
- Resume keyword optimization.
- Experience and education extraction using NLP.
- Support for more resume formats.

Learning Outcomes

This project demonstrates Python programming concepts including file handling, text processing, regular expressions, PDF and DOCX parsing, basic NLP techniques, and rule-based data analysis. It serves as a practical project for understanding resume parsing and ATS-style evaluation systems.
