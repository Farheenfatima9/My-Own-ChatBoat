import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
# from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage, 
    HumanMessage,
    AIMessage
)
def init():
    load_dotenv()
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY")=="":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

 
    st.set_page_config(
        page_title="Your own GPT", 
            page_icon="🐸️"    
    )

def main():
    
    init()
    chat=ChatOpenAI(temperature=0)

    # BUffer memory
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content='You are a helpful assistant.')
        ]


    st.header( "Your Own ChatGPt 🐸️")

    # message("Hello how are you?")
    # message("I am good", is_user=True)
    with st.sidebar:
        user_input=st.text_input("Your Message: ", key="user_input")

        if user_input:
            # message(user_input, is_user=True)
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Thinking..."):
                response = chat(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))
            # message(response.content, is_user=False)

    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i%2==0:
            message(msg.content, is_user=True, key=str(i)+'_user')
        else:
            message(msg.content, is_user=False, key=str(i)+'_AI')

if __name__=='__main__':
    main()