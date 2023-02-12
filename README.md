# Katonic_GPT_Prompt_Generator

This App is based on BART Model, which can be able to generate Prompts based on persona you wish to go with.

### About Repository
- This repository contains Katonic-app.py file contains streamlit UI code app code.with all the used data/images in respective folders.
- Dockerfile for deployment.
- app.py file contains gradio UI code.

## Product Overview

This Application is created using Hugging face BART model which is trained on awesome-chatgpt-prompts dataset.The dataset consist of act/role-player and their prompts in .csv file format. 

### About BART Model:
- Bart uses a standard seq2seq/machine translation architecture with a bidirectional encoder (like BERT) and a left-to-right decoder (like GPT).

- The pretraining task involves randomly shuffling the order of the original sentences and a novel in-filling scheme, where spans of text are replaced with a single mask token.

- BART is particularly effective when fine tuned for text generation but also works well for comprehension tasks. It matches the performance of RoBERTa with comparable training resources on GLUE and SQuAD, achieves new state-of-the-art results on a range of abstractive dialogue, question answering, and summarization tasks, with gains of up to 6 ROUGE.

### About Prompt-Engineering

Prompt engineering or prompting is an AI (artificial intelligence) concept of how to talk to an AI system like ChatGPT and get a desired response. For example, instead of giving the AI a simple prompt like "define a computer," you could add additional information to the prompt to get a better result. In other words, you could give a prompt like "define a computer in one paragraph as if I was five years old" and get more of a result of what you want.

Hence using This Application You can make awesome prompts for your ChatGPT Usage with detailed description of your usecase.

### User-Guide
About
![image](https://user-images.githubusercontent.com/124993015/218325957-772812de-15b6-41ff-94ad-cf7c42036ae2.png)

Type The Persona e.g teacher
![image](https://user-images.githubusercontent.com/124993015/218326225-c733eb27-e29a-443a-bb4e-85209d4840d9.png)

Let's copy the prompt and see what chatgpt replied
1. before using our generated prompts
![image](https://user-images.githubusercontent.com/124993015/218328534-cdd0fb20-56a1-49d1-869a-2356d951d115.png)



3. After using generated prompts
![image](https://user-images.githubusercontent.com/124993015/218326400-938f7a6e-d48e-4ea6-acfb-86390041aa5a.png)

we can see the difference i.e. we get more detailed and relevant information using prompts.

##### To play around this application:
use git clone 
