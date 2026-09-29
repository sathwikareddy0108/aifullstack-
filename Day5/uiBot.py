import ollama
import streamlit as st
st.title(":violet[My ChatBot🕵️!]")
with st.sidebar:
    personalities = {
        "kid👶" : "give the answers like you are explaining to a 5yrs old kid give answer in 2 lines",
        "professor👩‍🏫": "you are an IIT PROFESSOR .EXPLAIN THE TOPICS USING CORRECT terminology.give the answer in 2 lines",
        "grandparents👵":"you are an old person.explain the topics in telugu.give answer in 2 lines"

    }
    personality = st.selectbox("select a personality",personalities.keys())
    if st.button(":green[clear chat🧹]"):
        st.session_state.messages = []

        st.success("chat cleared sucessfully😭")
    st.header(":blue[chat settings⚙️]")
    uploaded_files = st.file_uploader("upload a file🤔")
    try:
        if uploaded_files:
            st.success("file uploaded successfully👍")
            with st.expander("preview"):
                context=uploaded_files.read().decode()("utf-8")
                st.text(context)
    except:
        st.error("file type not supported")
if "messages" not in st.session_state:
        st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You: ")
if question:
    with st.chat_message("user"):
        st.write("user: ", question)
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )
    with st.spinner("Thinking.."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[{
                "role":"system","content" : personalities[personality]
            }] + st.session_state.messages
        )
    st.session_state.messages.append(
        {
            "role" : "assistant",
            "content":response["message"]["content"]
        }
    )
    with st.chat_message("Assistant"):
        st.write("AI:",response["message"]["content"])

        
    
    


    