from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Faculty-related chatbot dataset
responses = {
    "hello": "Hello, professor! How can I assist you today?",
    "hi": "Hi there! How is your class going?",
    "how are you": "I'm here and ready to assist with teaching-related queries!",
    "good morning": "Good morning! Hope you have a great day with your students.",
    "good night": "Good night! Rest well for another productive teaching day.",
    "who are you": "I am a faculty assistant chatbot, here to help with teaching and student management!",
    "what is your name": "You can call me FacultyBot!",

    # Faculty responsibilities
    "how to prepare a lesson plan": "Start with objectives, outline key topics, and include activities for engagement.",
    "how to make lectures more engaging": "Use interactive discussions, real-world examples, and multimedia.",
    "how to handle large classes": "Use structured lessons, classroom management techniques, and technology.",
    "how to evaluate students fairly": "Use rubrics, give constructive feedback, and assess with diverse methods.",
    "how to improve student participation": "Encourage questions, use group activities, and apply active learning.",
    "how to deal with disruptive students": "Stay calm, set clear expectations, and address issues privately.",
    "how to support struggling students": "Offer extra help, suggest resources, and provide encouragement.",
    "how to manage grading efficiently": "Use online tools, set clear deadlines, and maintain consistency.",
    "how to balance research and teaching": "Plan ahead, delegate tasks, and integrate research into teaching.",
    "how to handle academic dishonesty": "Set clear policies, educate students on ethics, and use plagiarism detection tools.",
    
    # Student support & mentorship
    "how to be an effective mentor": "Listen actively, guide students, and provide career advice.",
    "how to motivate students": "Recognize achievements, set realistic goals, and create an inclusive environment.",
    "how to help students with anxiety": "Be supportive, provide resources, and encourage a healthy mindset.",
    "how to guide students in research": "Help with topic selection, provide sources, and review drafts.",
    "how to prepare students for exams": "Use revision sessions, practice tests, and stress-relief strategies.",
    "how to address student complaints": "Listen carefully, remain professional, and resolve issues fairly.",
    "how to write a recommendation letter": "Highlight strengths, give specific examples, and keep it professional.",
    
    # Classroom technology & online teaching
    "how to use technology in teaching": "Use LMS platforms, interactive tools, and digital assessments.",
    "best tools for online teaching": "Zoom, Google Classroom, Moodle, and interactive whiteboards.",
    "how to make online classes engaging": "Use polls, breakout rooms, and gamification techniques.",
    "how to manage student attendance": "Use digital attendance tools or QR-based check-in systems.",
    "how to create effective online quizzes": "Make them interactive, time-bound, and aligned with objectives.",
    
    # Faculty development
    "how to improve as a faculty member": "Attend workshops, collaborate with peers, and seek student feedback.",
    "how to publish academic research": "Choose a relevant journal, follow guidelines, and revise based on feedback.",
    "how to write a research proposal": "Define objectives, justify significance, and include methodology details.",
    "how to apply for faculty grants": "Find funding sources, write a compelling proposal, and meet deadlines.",
    "how to get tenure as a professor": "Publish research, demonstrate teaching excellence, and contribute to the institution.",
    
    # Work-life balance for faculty
    "how to manage faculty workload": "Prioritize tasks, set boundaries, and use time management strategies.",
    "how to handle faculty stress": "Take breaks, seek peer support, and practice mindfulness.",
    "how to balance teaching and personal life": "Schedule time wisely and set limits on work commitments.",
    
    # Student behavior & discipline
    "how to handle late submissions": "Have a clear policy, offer leniency when necessary, and encourage responsibility.",
    "how to prevent cheating in exams": "Use multiple versions, randomize questions, and monitor carefully.",
    "how to address bullying in class": "Create a safe environment, enforce policies, and report serious cases.",
    "how to deal with unmotivated students": "Understand their struggles, set achievable goals, and offer encouragement.",
    
    # Career progression
    "how to become a great professor": "Be passionate, continuously learn, and inspire students.",
    "what makes a good lecturer": "Clear communication, subject mastery, and student engagement.",
    "how to transition from faculty to administration": "Gain leadership experience, pursue additional training, and network.",
    
    # AI in education
    "how can AI help in teaching": "AI can personalize learning, automate grading, and assist in content creation.",
    "will AI replace teachers": "No, AI can support teaching, but human interaction remains essential.",
    "how to integrate AI in the classroom": "Use AI tutors, automate tasks, and analyze student performance data.",
    
    # Default response
    "default": "I'm here to assist with faculty and student management. Can you clarify your question?"
}

# Generate additional faculty-related responses dynamically
for i in range(30, 101):
    responses[f"faculty question {i}"] = f"This is an automated response for faculty-related question {i}."

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route for chatbot response
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    bot_response = responses.get(user_message, responses["default"])
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
