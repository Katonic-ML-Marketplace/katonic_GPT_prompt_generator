from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import streamlit as st
from streamlit_option_menu import option_menu
import os

routes = os.environ["ROUTE"]
tokenizer = AutoTokenizer.from_pretrained("merve/chatgpt-prompts-bart-long")
model = AutoModelForSeq2SeqLM.from_pretrained("merve/chatgpt-prompts-bart-long", from_tf=True)

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["About","Katonic_GPT_Prompt Generator"]
    )

st.image('katonic_logo.png')
if selected == "About":
    st.title("Katonic-GPT Prompt Generator App🚀")
    st.markdown("""This **Katonic_GPT Prompt generator** generates ChatGPT prompts, it's based on a BART model trained on [awesome-gpt-prompts-dataset](https://huggingface.co/datasets/fka/awesome-chatgpt-prompts). 📓 
    The Prompts will make our and ChatGPT life easier, so to make full-proof and efficient use of ChatGPT, Use this App to generate the Prompts""")
    st.markdown("""You can Follow these steps to generate the prompts👇:""")
    st.markdown("1. Enter the Persona that you want e.g. Photographer,developer 👩‍💻👩🏻‍🚀🧝🏻‍♀️👨🏻‍🏫👨🏻‍⚖️👨🏻‍🎨👨🏻‍🎓")
    st.markdown("2. Enter on the submit button ➖ It'll generate prompts.")
    st.markdown("3. Copy the Prompts and paste it to the ChatGPT [here](https://chat.openai.com/).")

if selected == "Katonic_GPT_Prompt Generator":

    input_component = st.text_input("Enter the Persona e.g. Photographer")
    if st.button("Submit"):
        print(input_component)
        batch = tokenizer(input_component, return_tensors="pt")
        generated_ids = model.generate(batch["input_ids"], max_new_tokens=150)
        output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        st.code(output[0])

        st.markdown("""You can Copy the Prompts👆 and just paste it in [ChatGPT](https://chat.openai.com/) to get the desired result🤩""")



