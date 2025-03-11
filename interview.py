import streamlit as st
import plotly.express as px
import pandas as pd

# App Title and Intro
st.title("**GOOGLE PRACTICE INTERVIEW QUESTIONS**")
st.write("Conquer Google’s interview with 1000 questions across 10 sessions. Master 7 key workplace behaviors with detailed feedback and visuals.")

# Constants
QUESTIONS_PER_SESSION = 100
TOTAL_QUESTIONS = 1000
TOTAL_SESSIONS = TOTAL_QUESTIONS // QUESTIONS_PER_SESSION
RESPONSE_OPTIONS = ["Strongly Agree", " Agree", "Neutral", "Disagree", "Strongly Disagree"]
DEFAULT_RESPONSE = "Neutral"
PASS_THRESHOLD = 70

# Question pool (Session 1 fully populated, sample for Session 2, framework for 3–10)
questions = [
    # Integrity (Session 1: 1–14)
    "1. I do what’s right when nobody is watching.",
    "2. I always follow company policies, even if it’s harder.",
    "3. I refuse to take shortcuts that break rules.",
    "4. My actions align with company values consistently.",
    "5. I’d delay a task rather than violate policy.",
    "6. I uphold standards without supervision.",
    "7. I stick to guidelines under pressure.",
    "8. I prioritize integrity over convenience.",
    "9. I never bend rules for efficiency.",
    "10. I respect protocols in all situations.",
    "11. I maintain honesty even when unpopular.",
    "12. I act with integrity on tight deadlines.",
    "13. I avoid unethical shortcuts at all costs.",
    "14. I align my work with company principles.",

    # Ethics (Session 1: 15–28)
    "15. I call out unethical behavior when I see it.",
    "16. If someone violates policy, I report it promptly.",
    "17. I feel responsible for ethical standards.",
    "18. I hold others accountable for company rules.",
    "19. I address unfair actions I observe.",
    "20. I report breaches, even if it’s a friend.",
    "21. I challenge unethical decisions calmly.",
    "22. I ensure fairness without overstepping.",
    "23. I speak up about policy violations.",
    "24. I encourage ethical conduct in my team.",
    "25. I report issues to uphold honesty.",
    "26. I address unethical acts decisively.",
    "27. I avoid policing others’ every move.",
    "28. I balance reporting with workplace harmony.",

    # Cross-Team Collaboration (Session 1: 29–42)
    "29. I facilitate collaboration across teams when needed.",
    "30. I bring people together for key projects.",
    "31. I connect departments for practical outcomes.",
    "32. I enjoy teamwork across disciplines when useful.",
    "33. I initiate collaboration for shared goals.",
    "34. I foster synergy when it makes sense.",
    "35. I seek inter-team solutions as required.",
    "36. I build bridges for project success.",
    "37. I collaborate across groups when necessary.",
    "38. I pursue teamwork opportunities selectively.",
    "39. I align teams for effective results.",
    "40. I support inter-departmental efforts.",
    "41. I connect colleagues for mutual benefit.",
    "42. I promote collaboration without forcing it.",

    # Responsible Autonomy (Session 1: 43–56)
    "43. I handle ambiguous tasks comfortably.",
    "44. I complete difficult work without guidance.",
    "45. I thrive independently on complex tasks.",
    "46. I take ownership of my assignments.",
    "47. I manage tough tasks solo confidently.",
    "48. I excel with minimal oversight.",
    "49. I act decisively without direction.",
    "50. I finish solo tasks effectively.",
    "51. I don’t rely on others to succeed.",
    "52. I tackle challenges independently.",
    "53. I perform well with unclear instructions.",
    "54. I take initiative without prompting.",
    "55. I navigate ambiguity on my own.",
    "56. I succeed solo under pressure.",

    # Problem-Solving Skills (Session 1: 57–70)
    "57. It’s hard to solve problems without a root cause.",
    "58. I act to minimize issues without a root cause.",
    "59. I adapt when causes aren’t clear.",
    "60. I mitigate risks despite uncertainty.",
    "61. I solve problems in ambiguous situations.",
    "62. I stop the bleeding without full insight.",
    "63. I experiment to resolve unclear issues.",
    "64. I reduce impacts without knowing why.",
    "65. I stay calm solving vague problems.",
    "66. I tackle challenges creatively.",
    "67. I take risks to fix issues quickly.",
    "68. I don’t freeze if the cause is unknown.",
    "69. I resolve issues despite missing details.",
    "70. I act fast to limit problem damage.",

    # Organizational Skills (Session 1: 71–84)
    "71. I create a structured workflow for myself.",
    "72. I plan my tasks systematically.",
    "73. I prioritize work for efficiency.",
    "74. I keep my workload organized.",
    "75. I design clear plans for my tasks.",
    "76. I maintain structure in my work.",
    "77. I track my progress methodically.",
    "78. I adapt plans for unexpected changes.",
    "79. I organize tasks to meet deadlines.",
    "80. I break projects into manageable steps.",
    "81. I sort my responsibilities well.",
    "82. I plan ahead to stay on track.",
    "83. I manage time with clear systems.",
    "84. I streamline my own work processes.",

    # Reliability (Session 1: 85–98)
    "85. I help colleagues when they ask me.",
    "86. I’m dependable when needed.",
    "87. I deliver on my commitments consistently.",
    "88. I support peers when approached.",
    "89. I meet deadlines reliably.",
    "90. I step up when others need me.",
    "91. I balance help with my own tasks.",
    "92. I assist in team crises when asked.",
    "93. I fulfill promises to my team.",
    "94. I offer help when it’s sought.",
    "95. I stay reliable under stress.",
    "96. I keep my word to colleagues.",
    "97. I complete tasks on time for others.",
    "98. I aid teammates when they need support.",

    # Mixed Focus (Session 1: 99–100)
    "99. I uphold policies while working solo.",
    "100. I help ethically collaborate across teams.",

    # Session 2 Sample (Integrity: 101–114)
    "101. I act with honesty when unsupervised.",
    "102. I follow rules even when it slows me down.",
    "103. I reject rule-breaking shortcuts.",
    "104. My choices reflect company ethics always.",
    "105. I’d pause work to stay compliant.",
    "106. I maintain standards alone.",
    "107. I adhere to policies under stress.",
    "108. I value integrity above ease.",
    "109. I never skirt rules for speed.",
    "110. I honor protocols every time.",
    "111. I stay true even if it’s tough.",
    "112. I keep integrity on rushed tasks.",
    "113. I shun unethical quick fixes.",
    "114. I sync my work with company values."
    # Sessions 3–10 follow: 201–300, 301–400, ..., 901–1000
]

# Correct answers (Session 1 fully defined, Session 2 sample)
correct_answers = {
    # Integrity (Session 1)
    1: "Strongly Agree", 2: "Strongly Agree", 3: "Strongly Agree", 4: "Strongly Agree", 5: "Strongly Agree",
    6: "Strongly Agree", 7: "Strongly Agree", 8: "Strongly Agree", 9: "Strongly Agree", 10: "Strongly Agree",
    11: "Strongly Agree", 12: "Strongly Agree", 13: "Strongly Agree", 14: "Strongly Agree",
    # Ethics (Session 1)
    15: " Agree", 16: " Agree", 17: "Strongly Agree", 18: "Neutral", 19: " Agree", 20: "Neutral",
    21: " Agree", 22: "Neutral", 23: " Agree", 24: "Strongly Agree", 25: " Agree", 26: " Agree",
    27: "Neutral", 28: "Neutral",
    # Collaboration (Session 1)
    29: " Agree", 30: " Agree", 31: " Agree", 32: " Agree", 33: " Agree", 34: " Agree",
    35: " Agree", 36: " Agree", 37: " Agree", 38: "Neutral", 39: " Agree", 40: " Agree",
    41: " Agree", 42: "Neutral",
    # Autonomy (Session 1)
    43: "Strongly Agree", 44: "Strongly Agree", 45: "Strongly Agree", 46: "Strongly Agree", 47: "Strongly Agree",
    48: "Strongly Agree", 49: "Strongly Agree", 50: "Strongly Agree", 51: "Strongly Agree", 52: "Strongly Agree",
    53: "Strongly Agree", 54: "Strongly Agree", 55: "Strongly Agree", 56: "Strongly Agree",
    # Problem-Solving (Session 1)
    57: "Disagree", 58: "Strongly Agree", 59: "Strongly Agree", 60: "Strongly Agree", 61: "Strongly Agree",
    62: "Strongly Agree", 63: "Strongly Agree", 64: "Strongly Agree", 65: "Strongly Agree", 66: "Strongly Agree",
    67: " Agree", 68: "Disagree", 69: "Strongly Agree", 70: "Strongly Agree",
    # Organizational (Session 1)
    71: "Strongly Agree", 72: "Strongly Agree", 73: "Strongly Agree", 74: "Strongly Agree", 75: "Strongly Agree",
    76: "Strongly Agree", 77: "Strongly Agree", 78: "Strongly Agree", 79: "Strongly Agree", 80: "Strongly Agree",
    81: "Strongly Agree", 82: "Strongly Agree", 83: "Strongly Agree", 84: "Strongly Agree",
    # Reliability (Session 1)
    85: " Agree", 86: "Strongly Agree", 87: "Strongly Agree", 88: " Agree", 89: "Strongly Agree", 90: " Agree",
    91: "Neutral", 92: " Agree", 93: "Strongly Agree", 94: " Agree", 95: "Strongly Agree", 96: "Strongly Agree",
    97: "Strongly Agree", 98: " Agree",
    # Mixed (Session 1)
    99: "Strongly Agree", 100: " Agree",
    # Integrity (Session 2 sample)
    101: "Strongly Agree", 102: "Strongly Agree", 103: "Strongly Agree", 104: "Strongly Agree", 105: "Strongly Agree",
    106: "Strongly Agree", 107: "Strongly Agree", 108: "Strongly Agree", 109: "Strongly Agree", 110: "Strongly Agree",
    111: "Strongly Agree", 112: "Strongly Agree", 113: "Strongly Agree", 114: "Strongly Agree"
}

# Explanations (Session 1 fully defined, Session 2 sample)
explanations = {
    # Integrity (Session 1)
    1: "Google demands uncompromised honesty without supervision.",
    2: "Policy adherence is a Google non-negotiable.",
    3: "Shortcuts breaking rules erode trust.",
    4: "Consistency with values is a Google must.",
    5: "Integrity trumps deadlines—Google agrees.",
    6: "Standards hold firm without oversight.",
    7: "Pressure doesn’t sway guideline adherence.",
    8: "Integrity over convenience is Google’s way.",
    9: "Rules aren’t bent for efficiency.",
    10: "Protocols are respected always.",
    11: "Honesty shines even when unpopular.",
    12: "Integrity under deadlines is key.",
    13: "Shortcuts violating standards are out.",
    14: "Alignment with principles builds trust.",
    # Ethics (Session 1)
    15: "Calling out unethical acts is expected, but Agree balances action with tact.",
    16: "Prompt reporting upholds ethics.",
    17: "Ethical responsibility is a Google trait.",
    18: "Neutral—over-policing others isn’t Google’s style.",
    19: "Addressing unfairness shows ethical awareness.",
    20: "Neutral—context matters with friends.",
    21: "Calm challenges to unethical acts are smart.",
    22: "Neutral—fairness shouldn’t overstep.",
    23: "Speaking up maintains standards.",
    24: "Encouraging ethics strengthens teams.",
    25: "Reporting for honesty is proactive.",
    26: "Decisive ethical action is valued.",
    27: "Neutral—avoid being the rule police.",
    28: "Neutral—harmony matters alongside ethics.",
    # Collaboration (Session 1)
    29: "Collaboration when needed is Google-ready.",
    30: "Bringing teams together for projects is smart.",
    31: "Practical outcomes drive team connections.",
    32: "Useful collaboration is a strength.",
    33: "Initiating for goals is effective.",
    34: "Synergy when sensible is key.",
    35: "Solutions across teams are practical.",
    36: "Bridges for success are Google-like.",
    37: "Necessary collaboration is balanced.",
    38: "Neutral—forcing new initiatives isn’t always needed.",
    39: "Aligning teams yields results.",
    40: "Supporting efforts is collaborative.",
    41: "Connecting for benefit is strategic.",
    42: "Neutral—don’t over-push collaboration.",
    # Autonomy (Session 1)
    43: "Ambiguity doesn’t faze Google candidates.",
    44: "Independent task completion is a must.",
    45: "Thriving solo on complexity shines.",
    46: "Ownership is Google’s autonomy core.",
    47: "Tough tasks don’t need hand-holding.",
    48: "Minimal oversight success is elite.",
    49: "Decisiveness without guidance wins.",
    50: "Solo effectiveness is key.",
    51: "No reliance on others is Google-ready.",
    52: "Independent challenges are handled well.",
    53: "Vague instructions don’t stop you.",
    54: "Initiative is a Google strength.",
    55: "Ambiguity navigation is clutch.",
    56: "Solo pressure success is top-tier.",
    # Problem-Solving (Session 1)
    57: "Disagree—Google wants adaptability over root cause reliance.",
    58: "Minimizing without root cause is proactive.",
    59: "Adapting to unclear causes is smart.",
    60: "Risk mitigation despite uncertainty is key.",
    61: "Ambiguous problem-solving is Google-like.",
    62: "Stopping bleeding without insight is effective.",
    63: "Experimentation tackles uncertainty.",
    64: "Impact reduction without why is practical.",
    65: "Calmness in vagueness is a strength.",
    66: "Creative solutions are Google-valued.",
    67: "Risk-taking for speed is balanced.",
    68: "Disagree—freezing isn’t an option.",
    69: "Resolution despite gaps is resourceful.",
    70: "Fast action limits damage.",
    # Organizational (Session 1)
    71: "Self-structure is a Google efficiency.",
    72: "Systematic planning drives success.",
    73: "Prioritization boosts productivity.",
    74: "Order keeps work on track.",
    75: "Clear plans enhance focus.",
    76: "Structure avoids chaos.",
    77: "Methodical tracking is smart.",
    78: "Adapting plans shows flexibility.",
    79: "Deadline organization is clutch.",
    80: "Steps make projects manageable.",
    81: "Sorting tasks is efficient.",
    82: "Planning ahead prevents slips.",
    83: "Time systems are Google-tier.",
    84: "Streamlining is personal efficiency.",
    # Reliability (Session 1)
    85: " Agree—helping when asked is reliable.",
    86: "Dependability is a Google cornerstone.",
    87: "Consistency builds trust.",
    88: "Support when approached is solid.",
    89: "Reliable deadlines are expected.",
    90: "Stepping up when needed is key.",
    91: "Neutral—balance is Google’s way.",
    92: "Crisis help when asked is strong.",
    93: "Promises kept are non-negotiable.",
    94: "Help when sought is dependable.",
    95: "Stress doesn’t break reliability.",
    96: "Your word matters at Google.",
    97: "Timeliness for others is clutch.",
    98: "Support when needed builds teams.",
    # Mixed (Session 1)
    99: "Policy and solo work align perfectly.",
    100: "Ethical team collaboration is Google-ready.",
    # Integrity (Session 2 sample)
    101: "Google expects uncompromised honesty alone.",
    102: "Rules hold even when they slow progress.",
    103: "Shortcuts breaking ethics are rejected.",
    104: "Ethics guide my every choice.",
    105: "Compliance trumps rushing tasks.",
    106: "Standards shine without watchers.",
    107: "Stress doesn’t bend my adherence.",
    108: "Ease never tops integrity.",
    109: "Speed doesn’t justify rule-breaking.",
    110: "Protocols are my constant.",
    111: "Tough choices don’t sway honesty.",
    112: "Deadlines respect my integrity.",
    113: "Quick fixes stay ethical.",
    114: "Values sync my every task."
}

# Session state
if "page" not in st.session_state:
    st.session_state.page = 1
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Navigation
st.write(f"**Session {st.session_state.page} of {TOTAL_SESSIONS}**")
progress = st.progress(st.session_state.page / TOTAL_SESSIONS)

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.session_state.page > 1 and not st.session_state.submitted:
        if st.button("⬅️ Previous"):
            st.session_state.page -= 1
            st.session_state.submitted = False
with col2:
    if st.session_state.page < TOTAL_SESSIONS and not st.session_state.submitted:
        if st.button("Next ➡️"):
            st.session_state.page += 1
            st.session_state.submitted = False
with col3:
    if st.button("Reset Assessment"):
        st.session_state.page = 1
        st.session_state.responses = {}
        st.session_state.submitted = False

# Questions
start_idx = (st.session_state.page - 1) * QUESTIONS_PER_SESSION
end_idx = min(start_idx + QUESTIONS_PER_SESSION, TOTAL_QUESTIONS)  # Cap at 1000
current_questions = [(q, RESPONSE_OPTIONS) for q in questions[start_idx:end_idx]]

with st.expander(f"Questions {start_idx + 1} - {end_idx}", expanded=not st.session_state.submitted):
    for i, (question, options) in enumerate(current_questions, start=start_idx):
        st.session_state.responses[i] = st.radio(
            question, 
            options, 
            key=f"q{i}", 
            index=RESPONSE_OPTIONS.index(DEFAULT_RESPONSE) if i not in st.session_state.responses else options.index(st.session_state.responses[i])
        )

# Submit
if not st.session_state.submitted:
    if st.button("Submit Answers"):
        st.session_state.submitted = True

# Grading and Feedback
if st.session_state.submitted:
    weights = {
        "Integrity": 20, "Ethics": 20, "Collaboration": 15, "Autonomy": 15, 
        "Problem": 10, "Organizational": 10, "Reliability": 10
    }
    area_counts = {area: 0 for area in weights}
    area_correct = {area: 0 for area in weights}
    total_correct = 0
    total_graded = 0

    for i in range(start_idx, end_idx):
        q_num = i + 1
        if q_num in correct_answers:
            total_graded += 1
            area = (
                "Integrity" if q_num % 100 <= 14 else "Ethics" if q_num % 100 <= 28 else
                "Collaboration" if q_num % 100 <= 42 else "Autonomy" if q_num % 100 <= 56 else
                "Problem" if q_num % 100 <= 70 else "Organizational" if q_num % 100 <= 84 else
                "Reliability" if q_num % 100 <= 98 else "Mixed"
            )
            if area != "Mixed":
                area_counts[area] += 1
                if st.session_state.responses.get(i) == correct_answers[q_num]:
                    area_correct[area] += 1
                    total_correct += 1

    score = 0
    for area in weights:
        if area_counts[area] > 0:
            score += weights[area] * (area_correct[area] / area_counts[area])
    mixed_correct = sum(1 for i in range(start_idx + 98, end_idx) if i in st.session_state.responses and i + 1 in correct_answers and st.session_state.responses[i] == correct_answers[i + 1])
    mixed_total = min(2, end_idx - (start_idx + 98))
    if mixed_total > 0:
        score += (mixed_correct / mixed_total) * 10

    percentage = (total_correct / total_graded) * 100 if total_graded > 0 else 0
    if percentage >= PASS_THRESHOLD:
        st.success(f"Session {st.session_state.page}: PASSED ({int(score)}/100, {percentage:.1f}%)")
    else:
        st.error(f"Session {st.session_state.page}: FAILED ({int(score)}/100, {percentage:.1f}%)")

    # Graphical Feedback
    st.subheader("Performance Breakdown")
    area_data = {area: (area_correct[area] / area_counts[area] * 100) if area_counts[area] > 0 else 0 for area in weights}
    df = pd.DataFrame(list(area_data.items()), columns=["Focus Area", "Percentage Correct"])
    fig_bar = px.bar(df, x="Focus Area", y="Percentage Correct", title="Performance by Focus Area", range_y=[0, 100])
    st.plotly_chart(fig_bar)

    pie_data = {"Correct": total_correct, "Incorrect": total_graded - total_correct}
    fig_pie = px.pie(values=list(pie_data.values()), names=list(pie_data.keys()), title="Overall Correctness")
    st.plotly_chart(fig_pie)

    # Review
    with st.expander("Review Your Answers", expanded=True):
        for i in range(start_idx, end_idx):
            q_num = i + 1
            if q_num in correct_answers:
                user_answer = st.session_state.responses.get(i, "No Answer")
                correct_answer = correct_answers[q_num]
                explanation = explanations[q_num]
                st.write(f"**Question {q_num}: {questions[i]}**")
                st.write(f"Your Answer: {user_answer}")
                if user_answer == correct_answer:
                    st.write(f"✅ Correct Answer: {correct_answer}")
                    st.write(f"ℹ️ Why Correct: {explanation}")
                else:
                    st.write(f"❌ Correct Answer: {correct_answer}")
                    st.write(f"ℹ️ Why Incorrect: {explanation} Adjust your approach.")
                st.write("---")