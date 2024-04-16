from openai import OpenAI
import streamlit as st


# Read the API Key and Setip an OpenAI Client
f = open(r"C:\Users\lavak\OneDrive\Desktop\DataScience Course\internship\TASKS\Task 5 - Building Your First GenAI App - AI Code Reviewer\.openai_api_key.txt") 
key = f.read()
client = OpenAI(api_key=key)

# Set colored page title
st.title("Python Code Review with OpenAI")

# User input section
st.header("Enter Your Python Code")
prompt = st.text_area("Enter your Python code here:", height=200)


# If the button is clicked, generate responses
if st.button("Generate") == True:
     st.markdown("<h2>Review Result</h2>", unsafe_allow_html=True)
     response=client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "user", "content": "Review the given python code and generate the correct code "},
            {"role": "user", "content": prompt}
        ],
    )
# Print the response on the web app
     st.write(response.choices[0].message.content)
