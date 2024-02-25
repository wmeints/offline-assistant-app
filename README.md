# Offline copywriting assistant with Gemma 7B

Welcome to this experiment! In this experiment, I'm testing out how to integrate Gemma 7B into a copywriting assistant.

## 🥅 Goals

- Experiment with open-source large language models as an alternative to GPT-\* from OpenAI
- Learn how to combine [Hugging Face](https://huggingface.co/) models with [Langchain](https://python.langchain.com/docs/get_started/introduction)
- Learn how to configure [Chainlit](https://docs.chainlit.io/get-started/overview) as a fully functional chat frontend for large language models

## ❗ System requirements

- A machine with a proper GPU of sorts (Mac M2/M3 or Nvidia RTX4080)
- Plenty of memory (I tested it with 32GB of memory)
- Python 3.11

## 🚀 Getting started

Please run this example in a dedicated virtual environment. Follow these steps to configure the project:

```bash
python -m venv .venv
pip install -r requirements.txt
pip install -r dev-requirements.txt
```

Next, run the project using the following command:

```bash
chainlit run app.py
```

## 🧑‍💻 Developer documentation

The following sections cover how to work on the code in the project.

### Project structure

| Directory/File | Description                                           |
| -------------- | ----------------------------------------------------- |
| .chainlit      | The configuration directory for the chainlit frontend |
| templates      | The directory containing the prompt templates         |
| app.py         | Contains the code for the frontend                    |
| chain.py       | Contains the LLM chain code                           |
| llm.py         | Contains code to configure Gemma 7B                   |

### Modifying prompt templates

You can turn this assistant into another one by editing the `templates/instructions.txt` file. Feel free to experiment.
