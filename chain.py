from operator import itemgetter
from pathlib import Path

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import Runnable, RunnablePassthrough

from llm import get_language_model


def read_template(name: str) -> str:
    template_path = Path(__file__).parent / "templates" / f"{name}.txt"
    return template_path.read_text()


def get_pipeline() -> Runnable:
    llm = get_language_model()

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", read_template("instructions")),
            MessagesPlaceholder("history"),
            ("user", "{input}"),
        ]
    )

    context_variables = {
        "history": itemgetter("history"),
        "input": RunnablePassthrough(),
    }

    pipeline = context_variables | prompt_template | llm | StrOutputParser()

    return pipeline
