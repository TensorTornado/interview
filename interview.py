import streamlit as st

# Google Hiring Assessment Simulation
st.title("Google Hiring Assessment Simulation - 300 Questions")
st.write("Select the best answers based on Google's expected work behaviors.")

# Define how many questions per page
QUESTIONS_PER_PAGE = 10

# Base questions
base_questions = [
    "I always follow company policies, even if it makes my job harder.",
    "If I notice someone violating company policies, I immediately report it.",
    "I actively bring together teams across different departments to collaborate on projects.",
    "I am comfortable completing difficult tasks on my own, even with little guidance.",
    "I struggle to solve problems if I cannot identify the root cause.",
    "I create a structured workflow to organize my tasks and responsibilities.",
    "I always prioritize helping my colleagues, even if it affects my own work.",
    "I make sure my coworkers always follow company policies.",
    "I always look for new opportunities to collaborate with other teams.",
    "If I can't find a root cause for an issue, I still take action to minimize the impact."
]

# Generate 300 questions by creating variations
questions = [(f"{i+1}. {base_questions[i % 10]}", ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"])
             for i in range(300)]

# Pagination logic
total_pages = len(questions) // QUESTIONS_PER_PAGE
page = st.number_input("Select Page", min_value=1, max_value=total_pages, value=1, step=1)

# Calculate question range for the selected page
start_idx = (page - 1) * QUESTIONS_PER_PAGE
end_idx = start_idx + QUESTIONS_PER_PAGE
current_questions = questions[start_idx:end_idx]

# User responses dictionary
responses = {}

# Display the questions for the selected page
for i, (question, options) in enumerate(current_questions, start=start_idx):
    responses[i] = st.radio(question, options, key=f"q{i}", index=None)

# Submit button
if st.button("Submit Answers"):
    score = 0
    correct_answers = {
        0: "Strongly Agree", 1: "Agree", 2: "Agree", 3: "Strongly Agree", 4: "Disagree",
        5: "Strongly Agree", 6: "Neutral", 7: "Neutral", 8: "Agree", 9: "Strongly Agree"
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
    
    # Evaluate answers only for the displayed page
    for i in range(start_idx, end_idx):
        if i % 10 in correct_answers and responses[i] == correct_answers[i % 10]:
            score += 1
    
    st.write(f"Your Score for this page: {score}/{QUESTIONS_PER_PAGE}")
    
    # Display review section
    for i in range(start_idx, end_idx):
        if i % 10 in correct_answers:
            st.write(f"**Question {i+1}: {questions[i][0]}**")
            st.write(f"✅ Correct Answer: {correct_answers[i % 10]}")
            st.write(f"ℹ️ Explanation: {explanations[i % 10]}")
            st.write("---")
