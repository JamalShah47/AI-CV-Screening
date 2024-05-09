# CV Screening Application

This is a web application built using Flask and OpenAI's GPT-3.5 model, designed to assess a candidate's suitability for a job role based on their CV and a provided job description.

## Project Structure

The project consists of two main components:

- **Backend**:
  - `app.py`: Flask application handling routing and processing of files.
  - `utils/convert.py`: Utility functions for extracting text from PDF and DOCX files.

- **Frontend**:
  - `index.html`: HTML template for the user interface.
  - `script.js`: JavaScript for handling form submission and displaying results.
  - `styles.css`: CSS for styling the UI.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/cv-screening-app.git
   cd cv-screening-app
2. Install dependencies:
   ```bash
pip install -r requirements.txt

3. Set up your OpenAI API key in app.py:
python
Copy code
OpenAI.api_key = "your-api-key"
Usage
Run the Flask application:
bash
Copy code
python app.py
Access the application in your web browser at http://localhost:5000.
Upload both the candidate's CV and the job description.
Click the "Submit" button to assess the candidate's suitability.
The application will display a score and an explanation based on the assessment.
Expected Output
Score: A numerical score representing the candidate's suitability for the role.
Explanation: A detailed explanation of the assessment, including factors considered and feedback.
