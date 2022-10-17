from email.policy import default
from multiprocessing.connection import answer_challenge
import os
import openai
import streamlit as st
from streamlit_chat import message
from Bot import mises, session_prompt

openai.api_key = os.getenv('OPENAI_API_KEY')

start_sequence = "\nAI:"
restart_sequence = "\n\Humano:"

st.set_page_config(
    page_icon='🏢',
    page_title='Chat Bot de Enología',
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "This is a chatbot created using OPENAI's Advance GPT-3 model",
        'Get Help': 'mailto:mpolanco@feylibertad.org',
        'Report a bug': "mailto:mpolanco@feylibertad.org",
    }
)
st.title("Chat Bot de Enología")

st.sidebar.title("🏢 Chat Bot de Enología")
st.sidebar.markdown("""
**Feedback/Questions**:
[DIVIAPPS.COM](https://diviapps.com)
""")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'chat_log' not in st.session_state:
    st.session_state['chat_log'] = session_prompt

chat_log = st.session_state['chat_log']

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'


question = st.text_input("Pregunta sobre vinos:",
                         value='¿Qué es una variedad?')
message(question, is_user=False,
       avatar_style="personas",
       seed="456")

answer = mises(question, chat_log)

# printing the Answer
chat_log = append_interaction_to_chat_log(question, answer, chat_log)
message(answer)

with st.expander("¿No está seguro de qué preguntar?"):
    st.markdown("""
Pruebe con alguna de estas preguntas:
```
1. ¿A qué temperatura se debe servir el vino tinto?
2. ¿Qué es un tempranillo?
3. ¿Vino tinto con carnes rojas y blanco con carnes blancas?
```
    """)

