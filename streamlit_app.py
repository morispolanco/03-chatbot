from email.policy import default
from multiprocessing.connection import answer_challenge
import os
import openai
import streamlit as st
from streamlit_chat import message
from Bot import mises, session_prompt

from streamlit_option_menu import option_menu

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1


def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Projects", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")
    
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
