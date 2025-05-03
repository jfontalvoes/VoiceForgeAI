import streamlit as st
import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv(), override=True)
openai_api_key = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
st.title("Text-to-Speech With OpenAI")
st.write("This app uses OpenAI's text-to-speech synthesis API to convert text into speech.")
text = st.text_area("Enter text to synthesize", "Hello, world!" , height=200)
voice = st.selectbox("Select a voice", voices)

if st.button("Generate Speech"):
    if text:
        response = client.audio.speech.create(
            model="tts-1", 
            voice=voice,
            input=text,
        )
        audiopath = "audio.mp3"
        with open(audiopath, "wb") as output_file:
            for chunk in response.iter_bytes():
                if  chunk:
                    output_file.write(chunk)    
        
        st.success("Audio generated successfully!")

        audio_file = open(audiopath, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")