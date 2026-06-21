# Intermediate Recommender App

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)

An intelligent, web-based decision-support tool designed to help students transition seamlessly from Matriculation to Intermediate education. Built using **Python and Flask**, this application evaluates a student's Matric marks, subject background, personal interests, and long-term career goals to generate highly tailored, logical suggestions for their FSc or ICS academic pathway.

**Live Demo:** [https://shadowdev1.pythonanywhere.com](https://shadowdev1.pythonanywhere.com/)

---

## Why This Project Matters

This application represents a shift from theoretical, isolated practice projects toward building intentional, user-centric tools that solve real-world problems. 

Navigating academic choices after Matriculation can be overwhelming for students due to conflicting advice and a lack of structured guidance. By combining robust backend logic with clean, user-friendly forms, this project demonstrates the potential to create practical, impactful applications that bridge the gap between user data and actionable insights.

---

## Key Features

* **Tailored Academic Matching:** Generates personalized FSc/ICS stream recommendations based on user performance, strengths, and alignment with target engineering, medical, or computational goals.
* **Intuitive Form Interface:** Clean, minimalist UI that simplifies data entry for student marks, subject selection, and qualitative career aspirations.
* **Instant Analytical Feedback:** Evaluates input criteria dynamically to deliver precise, structured recommendations.

---

## Project Structure

* `app.py`: The main Flask application file handling routing and core recommendation logic.
* `requirements.txt`: Contains the list of Python dependencies required to run the application.
* `static/`: Contains public-facing static assets:
    * `css/style.css`: Custom stylesheets defining the visual layout and tech-minimalist design.
    * `js/script.js`: Client-side scripts managing form validation and interactivity.
* `templates/`: **Jinja2** templates for rendering HTML:
    * `index.html`: The primary dashboard and form template for user interaction.

---

## Prerequisites

To run this project locally, ensure you have **Python 3.x** installed on your system. Using a virtual environment is highly recommended to manage dependencies.

## Local Installation & Setup

Copy and run these commands in your terminal to set up the project locally:

```bash
# 1. Clone the repository to your local machine
git clone https://github.com

# 2. Navigate into the project directory
cd intermediate_course_recommender_app

# 3. Create and activate a virtual environment
# For Windows:
python -m venv venv
venv\Scripts\activate

# For macOS/Linux:
python3 -m venv venv && source venv/bin/activate

# 4. Install the required dependencies
pip install -r requirements.txt

# 5. Start the local development server
python app.py
```

Once the server initializes, open your web browser and navigate to the local address provided in your terminal (typically `http://127.0.0`).
