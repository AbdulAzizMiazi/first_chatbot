import streamlit as st          # type:ignore
from google import genai
import os
from dotenv import load_dotenv  # type:ignore

st.title("Simple AI App :robot:", anchor=False)
st.divider()

qsn = st.text_input("Ask me anything you want :slightly_smiling_face::", placeholder="Ask the question")
is_sent = st.button("Send:arrow_forward:", type="primary")


load_dotenv()
key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key = key)

if is_sent and qsn !="":
    with st.spinner('Loading...'):
        interaction = client.interactions.create(
            model="gemini-3-flash-preview",
            input= f"{qsn} Answer briefly."
        )
        print(interaction.output_text)
        st.markdown(interaction.output_text)