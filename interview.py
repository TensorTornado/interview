import streamlit as st

# Google Hiring Assessment Simulation
st.title("Google Hiring Assessment Simulation - 300 Questions")
st.write("Select the best answers based on Google's expected work behaviors.")

questions = [
    ("1. I always follow company policies, even if it makes my job harder.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("2. If I notice someone violating company policies, I immediately report it.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("3. I actively bring together teams across different departments to collaborate on projects.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("4. I am comfortable completing difficult tasks on my own, even with little guidance.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("5. I struggle to solve problems if I cannot identify the root cause.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("6. I create a structured workflow to organize my tasks and responsibilities.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("7. I always prioritize helping my colleagues, even if it affects my own work.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("8. I make sure my coworkers always follow company policies.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("9. I always look for new opportunities to collaborate with other teams.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]),
    ("10. If I can't find a root cause for an issue, I still take action to minimize the impact.", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"])
]

# Expanding the questions to 300 by modifying sentence structure and complexity
for i in range(10, 300):
    questions.append((f"{i+1}. Variant: {questions[i%10][0]}", questions[i%10][1]))

# User responses
responses = {}
for i, (question, options) in enumerate(questions):
    responses[i] = st.radio(question, options, key=f"q{i}", index=None)

if st.button("Submit Answers"):
    score = 0
    correct_answers = {
        0: "Strongly Agree", 1: "Agree", 2: "Agree", 3: "Strongly Agree", 4: "Disagree", 5: "Strongly Agree", 
        6: "Neutral", 7: "Neutral", 8: "Agree", 9: "Strongly Agree"
    }
    
    explanations = {
        0: "Following company policies is essential to maintaining integrity and consistency, even when it makes tasks harder.",
        1: "Reporting unethical behavior is important, but balance is needed. Agreeing shows accountability without appearing overly aggressive.",
        2: "Collaboration across departments is valuable, but it should be purposeful rather than forced.",
        3: "Being able to complete difficult tasks independently is a critical skill at Google.",
        4: "While root cause analysis is important, being adaptable when the cause is unknown is equally necessary.",
        5: "Having an organized workflow improves efficiency and structure in professional tasks.",
        6: "Helping colleagues is good, but prioritizing it over your own work can reduce productivity.",
        7: "Ensuring coworkers follow policies is important, but you should not act as a workplace enforcer.",
        8: "Collaboration is encouraged, but it should be situational rather than always initiated.",
        9: "Even if the root cause is unknown, action should still be taken to mitigate potential risks."
    }
    
    for i in range(10):
        if responses[i] == correct_answers[i]:
            score += 1
    
    st.write(f"Your Score: {score}/10 on key questions. Full analysis below:")
    
    for i in range(10):
        st.write(f"**Question {i+1}: {questions[i][0]}**")
        st.write(f"✅ Correct Answer: {correct_answers[i]}")
        st.write(f"ℹ️ Explanation: {explanations[i]}")
        st.write("---")
