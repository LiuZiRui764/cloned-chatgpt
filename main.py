import streamlit as st
from util import generate_script

st.title("📽 Video Script Generator")

with st.sidebar:
    openai_api_key = st.text_input("Please input your OpenaiAPI",type="password")
    st.write("""Methods of getting API keys:
             'https://api.aigc369.com/register?aff=87kh'""")
subject = st.text_input("💡 Topic of the video")
video_length = st.number_input("⏰ Video Duration(min)",min_value=0.1,step = 0.5)
creativity = st.slider("""🕹 Video creativity 
                        (the smaller the creativity, the more rigorous the result; the higher the creativity, the more flexible the result)""",
                       min_value=0.0,max_value=1.5,step=0.1,value=0.2)
submit = st.button("generate script")
if submit and not openai_api_key:
    st.write("🔒 Warning : Please input your openai key.")
    st.stop()
if submit and not subject:
    st.write("🔒 Warning : Please input your subject.")
    st.stop()
if submit and video_length < 0.1:
    st.write("🔒 Warning : The video duration should be more than 0.1 minutes.")
    st.stop()
if submit:
    with st.spinner(("Loading...")):
        title,script = generate_script(subject,video_length,creativity,openai_api_key)
    st.write("Loading completed")
    st.subheader("✍ Title:")
    st.write(title)
    st.subheader("📜 Script:")
    st.write(script)