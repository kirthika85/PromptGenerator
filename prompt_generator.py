import streamlit as st
import openai
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def generate_prompt(topic, genre):
    prompt = f"Write a {genre} story about {topic}"
    llm = ChatOpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo",temperature=0.5)
    input = ChatPromptTemplate.from_template(prompt)
    chain = input | llm
    response=chain.invoke()
    return(response)
    
# Streamlit UI
st.title("Creative Writing Prompt Generator")
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Input fields
topic = st.text_input("Enter topic:")
genre = st.selectbox("Select genre:", ["Science Fiction", "Fantasy", "Mystery", "Romance", "Thriller"])
#length = st.slider("Select prompt length (words):", min_value=50, max_value=200, step=10, value=100)
generate_button = st.button("Generate Prompt")

     
# Validation api_key
if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
if generate_button and openai_api_key.startswith('sk-'):
    # Generate prompt on button click
    if generate_button:
        if topic:
            st.write("Generating prompt...")
            prompt=generate_prompt(topic, genre)
            st.write(f"**Prompt:** {prompt}")
        else:
            st.error("Please enter a topic.")
