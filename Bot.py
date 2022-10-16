import os
from unittest.util import _MAX_LENGTH
import openai
import streamlit as st
openai.api_key = os.getenv('OPENAI_API_KEY')


start_sequence = "\nAI:"
restart_sequence = "\n\Humano:"

session_prompt = "Lo que sigue es una conversación con un asistente de AI experto en vinos. El asistente es servicial, creativo, inteligente y muy amable.\n\nHumano: Hola, ¿quién eres?\nAI: Soy un bot de AI experto en enología. ¿En qué puedo ayudarle hoy? \nHumano: ¿Qué debo buscar  en un vino tinto?\nAI: Al buscar un vino tinto, querrá asegurarse de encontrar una buena variedad que se adapte a sus gustos. También es importante considerar el precio y el tipo de vino que está buscando.\nHumano: ¿Qué es el proseco?\nAI: El proseco es un tipo de vino espumoso que se produce en Italia. Tiene un sabor dulce y afrutado, y suele ser más ligero que otros tipos de vino espumoso.\n"

def mises(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=prompt_text,
        temperature=0.7,
        # max_length=250,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
