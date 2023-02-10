# Katonic_GPT_Prompt_Generator

This App is based on BART Model, which can be able to generate Prompts based on persona you wish to go with.

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
Type your Persona -> Submitt it -> Copy the Prompt generated -> Paste in ChatGPT.
