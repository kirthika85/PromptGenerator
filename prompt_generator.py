import streamlit as st
import openai
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def generate_prompt(topic,genre):
    print("Entered the function")
    prompt = f"Write a {genre} story about {topic}"
    print(prompt)
    llm=OpenAI(api_key=openai_api_key,temperature=0.5)
    input=ChatPromptTemplate.from_template({prompt})
    chain = input | llm
    response=chain.invoke({input})
    print(response)
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
            print({topic})
            print({genre})
            prompt1=generate_prompt(topic,genre)
            st.write(f"**Prompt:** {prompt1}")
        else:
            st.error("Please enter a topic.")
