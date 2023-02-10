from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import streamlit as st
from streamlit_option_menu import option_menu
import os

routes = os.environ["ROUTE"]

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["About","Katonic_GPT_Prompt Generator"]
    )

st.image('katonic_logo.png')
if selected == "About":
    st.title("Katonic-GPT Prompt Generator App")
    st.write("""This Katonic_GPT Prompt generator generates ChatGPT prompts, it's based on a BART model trained on [this dataset](https://huggingface.co/datasets/fka/awesome-chatgpt-prompts). 📓 You Simply enter a persona that you want and it'll generate the Prompt🤩
    """)

tokenizer = AutoTokenizer.from_pretrained("merve/chatgpt-prompts-bart-long")
model = AutoModelForSeq2SeqLM.from_pretrained("merve/chatgpt-prompts-bart-long", from_tf=True)

if selected == "Katonic_GPT_Prompt Generator":

    input_component = st.text_input("Enter the Persona e.g. Photographer")
    if st.button("Submit"):
        print(input_component)
        batch = tokenizer(input_component, return_tensors="pt")
        generated_ids = model.generate(batch["input_ids"], max_new_tokens=150)
        output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        st.code(output[0])



