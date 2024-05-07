from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from utils.convert import extract_text_from_docx, extract_text_from_pdf
import re

app = Flask(__name__)

OpenAI.api_key = "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"

#openai client
client = OpenAI(api_key=OpenAI.api_key)

# Maximum tokens per message to stay within the maximum context length
MAX_TOKENS_PER_MESSAGE = 100

# Define route for root URL
@app.route('/')
def index():
    return render_template('index.html')

def truncate_text(text):
    # Truncate the text if it exceeds the maximum token length
    tokens = text.split()[:MAX_TOKENS_PER_MESSAGE]
    return ' '.join(tokens)

@app.route('/process-files', methods=['POST'])
def process_files():
    cv_file = request.files['cv']
    job_description_file = request.files['jobDescription']

    # Convert CV and job description files to text
    cv_text = extract_text_from_docx(cv_file) if cv_file.filename.endswith('.docx') else extract_text_from_pdf(cv_file)
    job_description_text = extract_text_from_docx(job_description_file) if job_description_file.filename.endswith('.docx') else extract_text_from_pdf(job_description_file)

    # Truncate input text to stay within the maximum token length
    cv_truncated = truncate_text(cv_text)
    job_description_truncated = truncate_text(job_description_text)

    # Call OpenAI API
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "CV: " + cv_truncated},
            {"role": "system", "content": "Job Description: " + job_description_truncated},
            {"role": "user", "content": "Assess the candidate's suitability for the role against the job description. Imagine you're the hiring manager reviewing the candidate's CV. Compare the candidate's qualifications and experience to the requirements outlined in the job description. Provide feedback on whether the CV effectively aligns with the job requirements"},
            {"role": "user", "content": "On a scale of 1 to 10, rate the candidate's CV based on its effectiveness in showcasing their qualifications and suitability for the role. Consider factors such as alignment with the job description, clarity, relevance, and overall impact."}
        ]
    )

    # Access the completion message content
    try:
        explanation = completion.choices[0].message.content
        # Extract the score from the explanation
        score = extract_score(explanation)
    except Exception as e:
        # Handle the error
        return jsonify({'error': 'Failed to access completion message: {}'.format(str(e))}), 400

    # Return the score and explanation
    return jsonify({'score': score, 'explanation': explanation})


def extract_score(explanation):
    score_pattern = r'(\d+(\.\d+)?) out of 10'
    match = re.search(score_pattern, explanation)
    if match:
        score = float(match.group(1))
        return score
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
