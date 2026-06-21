# app.py
from flask import Flask, request, jsonify, render_template
import traceback

app = Flask(__name__)

# Constants for subject total marks (adjust if your specific board differs)
SUBJECT_TOTAL_MARKS = 150

@app.route('/')
def index():
    """Renders the main HTML page."""
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Receives user data from the frontend, processes it, and returns a recommendation.
    """
    try:
        data = request.json
        print(f"--- Flask: Received data from frontend ---\n{data}\n---")

        total_matric_marks = data.get('totalMatricMarks', 0)
        math_marks_raw = data.get('mathMarks', 0)
        physics_marks_raw = data.get('physicsMarks', 0)
        chemistry_marks_raw = data.get('chemistryMarks', 0)
        bio_or_comp_option = data.get('bioOrCompOption', '')
        biology_marks_raw = data.get('biologyMarks', 0)
        computer_marks_raw = data.get('computerMarks', 0)
        
        selected_interests = [str(i).lower() for i in data.get('interests', [])]
        selected_career_goals = [str(g).lower() for g in data.get('careerGoals', [])]

        print(f"--- Flask: Processed Input ---\nTotal Matric Marks: {total_matric_marks}\nMath: {math_marks_raw}, Physics: {physics_marks_raw}, Chemistry: {chemistry_marks_raw}\nBio/Comp Option: {bio_or_comp_option}\nBiology: {biology_marks_raw}, Computer: {computer_marks_raw}\nInterests: {selected_interests}\nCareer Goals: {selected_career_goals}\n---")

        overall_percentage = (total_matric_marks / 1200) * 100 if total_matric_marks > 0 else 0

        math_percentage = (math_marks_raw / SUBJECT_TOTAL_MARKS) * 100 if SUBJECT_TOTAL_MARKS > 0 else 0
        physics_percentage = (physics_marks_raw / SUBJECT_TOTAL_MARKS) * 100 if SUBJECT_TOTAL_MARKS > 0 else 0
        chemistry_percentage = (chemistry_marks_raw / SUBJECT_TOTAL_MARKS) * 100 if SUBJECT_TOTAL_MARKS > 0 else 0
        biology_percentage = (biology_marks_raw / SUBJECT_TOTAL_MARKS) * 100 if SUBJECT_TOTAL_MARKS > 0 else 0
        computer_percentage = (computer_marks_raw / SUBJECT_TOTAL_MARKS) * 100 if SUBJECT_TOTAL_MARKS > 0 else 0

        print(f"--- Flask: Calculated Percentages ---\nOverall: {overall_percentage:.2f}%\nMath: {math_percentage:.2f}%, Physics: {physics_percentage:.2f}%, Chemistry: {chemistry_percentage:.2f}%\nBiology: {biology_percentage:.2f}%, Computer: {computer_percentage:.2f}%\n---")

        excellent_percent_overall = 80
        good_percent_overall = 70
        average_percent_overall = 60
        
        high_subject_percent = 80
        good_subject_percent = 70
        average_subject_percent = 60

        med_keywords = ["medical", "doctor", "health", "biology", "research", "helping people", "dentist", "pharmacist", "physiotherapist"]
        eng_keywords = ["engineering", "engineer", "physics", "math", "problem-solving", "design", "innovation", "mechanical engineering", "electrical engineering", "civil engineering"]
        ics_keywords = ["technology", "programming", "computer science", "software", "it", "coding", "data science", "web development", "cybersecurity", "game development"]
        icom_keywords = ["business", "commerce", "finance", "accounting", "management", "economics", "entrepreneurship", "marketing", "auditor"]
        fa_keywords = ["arts", "humanities", "social sciences", "creativity", "writing", "design", "journalism", "psychology", "history", "literature", "teaching", "law"]

        is_interested_in_med = any(k in selected_interests or k in selected_career_goals for k in med_keywords)
        is_interested_in_eng = any(k in selected_interests or k in selected_career_goals for k in eng_keywords)
        is_interested_in_ics = any(k in selected_interests or k in selected_career_goals for k in ics_keywords)
        is_interested_in_icom = any(k in selected_interests or k in selected_career_goals for k in icom_keywords)
        is_interested_in_fa = any(k in selected_interests or k in selected_career_goals for k in fa_keywords)

        recommendation = "Based on your input, we recommend exploring various intermediate options."
        details = ["Please fill out all sections thoroughly for a more specific recommendation."]

        if overall_percentage >= excellent_percent_overall:
            if is_interested_in_med and bio_or_comp_option == 'biology' and biology_percentage >= high_subject_percent and physics_percentage >= good_subject_percent and chemistry_percentage >= good_subject_percent:
                recommendation = "FSc Pre-Medical"
                details = [
                    "Excellent foundation for MBBS, BDS, Pharmacy, DPT, and other allied health sciences.",
                    "Focuses on Physics, Chemistry, and Biology. Strong analytical and memorization skills are key.",
                    "Typical career paths: Doctor, Dentist, Pharmacist, Physiotherapist, Medical Researcher."
                ]
            elif is_interested_in_eng and math_percentage >= high_subject_percent and physics_percentage >= good_subject_percent and chemistry_percentage >= good_subject_percent:
                recommendation = "FSc Pre-Engineering"
                details = [
                    "Ideal for pursuing various engineering disciplines (e.g., Software, Electrical, Civil, Mechanical).",
                    "Focuses on Physics, Chemistry, and Mathematics. Strong problem-solving and logical reasoning are crucial.",
                    "Typical career paths: All types of Engineers, Mathematician, Architect (often after a foundation year)."
                ]
            elif is_interested_in_ics and bio_or_comp_option == 'computer' and computer_percentage >= high_subject_percent and math_percentage >= good_subject_percent and physics_percentage >= average_subject_percent:
                recommendation = "ICS (Intermediate in Computer Science)"
                details = [
                    "Great for careers in software development, data science, cybersecurity, and IT.",
                    "Subject combinations usually include Computer Science, Mathematics, and Physics or Statistics. Combines logical thinking with practical computer skills.",
                    "Typical career paths: Software Developer, Data Scientist, Network Administrator, IT Professional, Web Developer."
                ]
            elif is_interested_in_icom:
                recommendation = "ICom (Intermediate in Commerce)"
                details = [
                    f"While your overall marks ({overall_percentage:.2f}%) are high, your strong interest in business makes ICom a solid foundation.",
                    "Focuses on Accounting, Business Mathematics, Economics, and Commercial Geography/Banking. Leads to BBA, BCom, ACCA, CA.",
                    "Typical career paths: Accountant, Banker, Business Manager, Auditor, Marketing Specialist."
                ]
            else:
                recommendation = "FSc (Pre-Engineering/Pre-Medical) or ICS"
                details = [
                    f"Your marks ({overall_percentage:.2f}%) are outstanding! Consider clarifying your specific interests (e.g., practical application vs. theoretical study, problem-solving vs. memorization) to narrow down between Pre-Medical, Pre-Engineering, or ICS.",
                    "All these streams offer strong pathways to professional degrees and diverse career opportunities."
                ]
        
        elif overall_percentage >= good_percent_overall:
            if is_interested_in_ics and bio_or_comp_option == 'computer' and computer_percentage >= good_subject_percent and math_percentage >= average_subject_percent:
                recommendation = "ICS (Intermediate in Computer Science)"
                details = [
                    "A good choice for technology-related fields. Focus on strengthening your analytical and programming skills.",
                    "Subject focus: Computer Science, Mathematics, Physics/Statistics.",
                    "Opens doors to various IT and software-related bachelor's degrees."
                ]
            elif is_interested_in_icom:
                recommendation = "ICom (Intermediate in Commerce)"
                details = [
                    "A strong option if you have an aptitude and interest in business, finance, and economics.",
                    "It's a direct pathway to BBA, BCom, and related fields."
                ]
            elif is_interested_in_eng and math_percentage >= good_subject_percent and physics_percentage >= average_subject_percent and chemistry_percentage >= average_subject_percent:
                recommendation = "FSc Pre-Engineering"
                details = [
                    "Achievable with good effort. Focus on strengthening your concepts in Physics, Chemistry, and Math.",
                    "Still provides a pathway to various engineering and science degrees."
                ]
            elif is_interested_in_med and bio_or_comp_option == 'biology' and biology_percentage >= good_subject_percent and physics_percentage >= average_subject_percent and chemistry_percentage >= average_subject_percent:
                recommendation = "FSc Pre-Medical"
                details = [
                    "Achievable with dedication. Concentrate on Biology, Physics, and Chemistry. Be prepared for rigorous study.",
                    "Leads to medical and allied health fields, but competition for MBBS/BDS may be higher."
                ]
            else:
                recommendation = "FSc General Science, ICom, or FA"
                details = [
                    f"Your marks ({overall_percentage:.2f}%) are good. Explore options based on your specific subject strengths and long-term career interests.",
                    "FSc General Science provides a broader science background. ICom focuses on commerce, and FA on arts and humanities. Consider your strongest subjects in Matric."
                ]

        elif overall_percentage >= average_percent_overall:
            if is_interested_in_icom:
                recommendation = "ICom (Intermediate in Commerce)"
                details = [
                    "Suitable for students with an interest in business, accounting, and economics.",
                    "It offers a practical pathway to careers in the business sector and leads to BBA, BCom, etc."
                ]
            elif is_interested_in_fa:
                recommendation = "FA (Faculty of Arts / Humanities)"
                details = [
                    "Offers a wide range of subjects like Psychology, Economics, Statistics, Fine Arts, Journalism, etc.",
                    "Good for those interested in social sciences, humanities, creative fields, or civil services.",
                    "Leads to degrees like BA, B.Ed, LLB, Mass Communication."
                ]
            elif is_interested_in_ics and bio_or_comp_option == 'computer' and computer_percentage >= average_subject_percent and math_percentage >= (average_subject_percent - 5):
                    recommendation = "ICS (Intermediate in Computer Science)"
                    details = [
                        "If you have a genuine interest in computers and average marks, ICS can still be a good choice.",
                        "You'll need to work hard on Mathematics and Computer Science to excel.",
                        "Can lead to various IT-related diplomas and degrees."
                    ]
            else:
                recommendation = "FA (Faculty of Arts) or ICom"
                details = [
                    f"Your marks ({overall_percentage:.2f}%) suggest exploring non-science-intensive fields. Focus on subjects where you have a natural aptitude or strong interest.",
                    "Consider your strongest subjects in Matric and what kind of career aligns with your personality and skills."
                ]

        else:
            if is_interested_in_fa:
                recommendation = "FA (Faculty of Arts / Humanities)"
                details = [
                    f"With marks below {average_percent_overall:.0f}%, FA is often the most accessible path, offering diverse subjects without heavy science/math requirements.",
                    "It provides a foundation for many bachelor's degrees in arts, humanities, and social sciences."
                ]
            elif is_interested_in_icom:
                recommendation = "ICom (Intermediate in Commerce)"
                details = [
                    "If your interest is strongly in commerce, ICom can still be an option, but you may need to work extra hard to build foundational concepts.",
                    "Consider seeking academic support."
                ]
            else:
                recommendation = "Exploring vocational diplomas (DAE) or reconsideration of interests."
                details = [
                    f"Traditional intermediate streams might be challenging with marks below {average_percent_overall:.0f}%.",
                    "Consider vocational diplomas (DAE - Diploma of Associate Engineer) which offer practical skills for specific trades (e.g., Civil, Electrical, IT trades). These can lead to job opportunities or a pathway to technical degrees.",
                    "Also, revisit your interests to find a field where you can truly excel."
                ]

        print(f"--- Flask: Recommendation Generated ---\nStream: {recommendation}\nDetails: {details}\n---")

        return jsonify({
            'recommendation': recommendation,
            'details': details
        })

    except Exception as e:
        print(f"--- Flask: An error occurred in /recommend route ---")
        print(f"Error: {e}")
        traceback.print_exc()
        return jsonify({'error': 'An internal server error occurred', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)