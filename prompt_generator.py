import streamlit as st
from langchain.llms import OpenAI

# Set up OpenAI API
# OpenAI.api_key = "your-api-key"  # Replace with your OpenAI API key


def generate_prompt(topic, genre, length):
    prompt = f"Write a {genre} story about {topic}. It should be {length} words long."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
         max_tokens=100
    #   response=OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("WriteGenie: Creative Writing Prompt Generator")
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Input fields
topic = st.text_input("Enter topic:")
genre = st.selectbox("Select genre:", ["Science Fiction", "Fantasy", "Mystery", "Romance", "Thriller"])
length = st.slider("Select prompt length (words):", min_value=50, max_value=200, step=10, value=100)
generate_button = st.button("Generate Prompt")

     
# Validation api_key
with st.form('my_form'):
     submitted = st.form_submit_button('Submit')
     if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
            if submitted and openai_api_key.startswith('sk-'):
                # Generate prompt on button click
                if generate_button:
                    if topic:
                        st.write("Generating prompt...")
                        prompt = generate_prompt(topic, genre, length)
                        st.write(f"**Prompt:** {prompt}")
                else:
                        st.error("Please enter a topic.")
