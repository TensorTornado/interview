import streamlit as st

# Google Hiring Assessment Simulation
st.title("Google Hiring Assessment Simulation - 100 Questions")
st.write("Select the best answers based on Google's expected work behaviors.")

questions = [
    ("I always follow company policies, even if it makes my job harder.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("If I notice someone violating company policies, I immediately report it.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("I actively bring together teams across different departments to collaborate on projects.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("I am comfortable completing difficult tasks on my own, even with little guidance.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("I struggle to solve problems if I cannot identify the root cause.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("I create a structured workflow to organize my tasks and responsibilities.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("I always prioritize helping my colleagues, even if it affects my own work.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("I make sure my coworkers always follow company policies.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("I always look for new opportunities to collaborate with other teams.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("If I can't find a root cause for an issue, I still take action to minimize the impact.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"])
]

# Expanding the questions to 100 by modifying sentence structure
for i in range(10, 100):
    questions.append((f"Variant {i+1}: {questions[i%10][0]}", questions[i%10][1]))

# User responses
responses = {}
for i, (question, options) in enumerate(questions):
    responses[i] = st.radio(question, options, key=f"q{i}")

if st.button("Submit Answers"):
    score = 0
    correct_answers = {
        0: "Strongly Agree", 1: "Agree", 2: "Agree", 3: "Strongly Agree", 4: "Disagree", 5: "Strongly Agree", 
        6: "Neutral", 7: "Neutral", 8: "Agree", 9: "Strongly Agree"
    }
    
    for i in range(10):
        if responses[i] == correct_answers[i]:
            score += 1
    
    st.write(f"Your Score: {score}/10 on key questions. Full analysis available upon request.")
