import streamlit as st
from prompt_engine import build_prompt
from ai_engine import generate_response

st.set_page_config(page_title="AI Tech Communicator", layout="centered")

st.title("AI Technical Communication Assistant")
st.write(
    "Improve clarity and effectiveness of developer communication using AI."
)

communication_type = st.selectbox(
    "Select communication type",
    [
        "Commit Message",
        "Code Comment",
        "Pull Request Explanation",
        "Technical Chat Message"
    ]
)

user_input = st.text_area(
    "Enter your technical message or description",
    height=180
)

if st.button("Improve with AI"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        prompt = build_prompt(communication_type, user_input)
        ai_output = generate_response(prompt)

        st.subheader("Improved Communication")
        st.success(ai_output)

        st.subheader("What was improved")
        st.info(
            "Clarity, technical accuracy, and professional tone were enhanced."
        )

