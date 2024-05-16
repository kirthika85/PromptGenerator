import streamlit as st
import openai
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
  
# Streamlit UI
st.title("Creative Writing Prompt")
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')


# Input fields
topic = st.text_input("Enter topic:")
genre = st.selectbox("Select genre:", ["Science Fiction", "Fantasy", "Mystery", "Romance", "Thriller"])
#length = st.slider("Select prompt length (words):", min_value=50, max_value=200, step=10, value=100)
generate_button = st.button("Generate Story")
concatenated_content = ""

     
# Validation api_key
if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
if generate_button and openai_api_key.startswith('sk-'):
    # Generate prompt on button click
    if generate_button:
        if topic:
            st.write("Generating prompt...")                
            prompt=f"Write a {genre} story about {topic}"
            print(prompt)
            llm=ChatOpenAI(api_key=openai_api_key,temperature=0.8,model_name="gpt-3.5-turbo")
            response=llm.stream(prompt)
            for chunk in response:
                content_without_timestamps = ''.join(filter(lambda x: not x.isdigit(), chunk.content))
                #print(content_without_timestamps, end="", flush=True)
                concatenated_content += content_without_timestamps
            st.write(f"**Prompt:** {concatenated_content}")
        else:
            st.error("Please enter a topic.")
