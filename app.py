
import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🚀 GPT-Powered Spam Mail Detector")

uploaded_file = st.file_uploader("Upload an email text file", type="txt")

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.write("### Email content:")
    st.write(content)

    with st.spinner("Asking GPT..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert spam classifier. "
                        "Reply only with SPAM or NOT SPAM for the following email."
                    )
                },
                {
                    "role": "user",
                    "content": content
                }
            ]
        )

        result = response.choices[0].message.content.strip()
        st.subheader(f"Prediction: **{result}**")
