# Intermediate Recommender App

An intelligent web-based decision-support tool designed to help student's transition seamlessly from Matriculation to Intermediate education. By evaluating a student's Matric marks, subject background, personal interests, and long-term career goals, the application generates highly tailored, logical suggestions for their FSc/ICS academic pathway.

Live Demo: [https://shadowdev1.pythonanywhere.com/](https://shadowdev1.pythonanywhere.com/)[span_0](start_span)[span_0](end_span)

---

## Why This Project Matters

This application represents a shift from theoretical, isolated practice projects toward building intentional, user-centric tools that solve real-world problems. 

Navigating academic choices after Matriculation can be overwhelming for students due to conflicting advice and a lack of structured guidance. By combining robust logical structures on the backend with clean, user-friendly forms on the frontend, this project demonstrates the potential to create highly practical, impactful applications that bridge the gap between user data and actionable insights.

---

## Key Features

*   **Tailored Academic Matching:** Generates personalized FSc/ICS stream recommendations based on user performance, strengths, and alignment with target engineering, medical, or computational goals.
*   **Intuitive Form Interface:** Clean, minimalist UI that simplifies data entry for student marks, subject selection, and qualitative career aspirations.
*   **Instant Analytical Feedback:** Evaluates input criteria dynamically to deliver precise, structured recommendations.

---

## Project Structure

*   `app.py`: The main Flask application file handling routing and core recommendation logic[span_1](start_span)[span_1](end_span).
*   `requirements.txt`: Contains the list of Python dependencies required to run the application[span_2](start_span)[span_2](end_span).
*   `static/`: Contains public-facing static assets[span_3](start_span)[span_3](end_span):
    *   `css/style.css`: Custom stylesheets defining the visual layout and user interface design[span_4](start_span)[span_4](end_span).
    *   `js/script.js`: Client-side scripts managing form validation and interactivity[span_5](start_span)[span_5](end_span).
*   `templates/`: Jinja2 templates for rendering HTML[span_6](start_span)[span_6](end_span):
    *   `index.html`: The primary dashboard and form template for user interaction[span_7](start_span)[span_7](end_span).
*   `venv/`: Project virtual environment[span_8](start_span)[span_8](end_span).

---

## Prerequisites

To run this project locally, ensure you have **Python 3.x** installed on your system. Using a virtual environment is highly recommended to manage dependencies.

## Local Installation

1.  Clone the repository to your local machine:
```bash
    git clone [https://github.com/yourusername/intermediate_recommender_app.git](https://github.com/yourusername/intermediate_recommender_app.git)
    ```
2.  Navigate to the project directory:
```bash
    cd intermediate_recommender_app
    ```
3.  Create and activate a virtual environment:
```bash
    # On Windows
    python -m venv venv
    venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  Install the required dependencies:
```bash
    pip install -r requirements.txt
    ```

## Usage

Start the local development server using the following command:

```bash
python app.py
