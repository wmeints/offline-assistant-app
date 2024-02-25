from typing import List, Union

import chainlit as cl
from langchain_core.messages import AIMessage, HumanMessage

from chain import get_pipeline

pipeline = get_pipeline()


def parse_message(message: cl.Message) -> Union[HumanMessage, AIMessage]:
    print(message.author)

    if message.author == "User":
        return HumanMessage(content=message.content)
    else:
        return AIMessage(content=message.content)


def parse_history(chat_history: List[cl.Message]) -> Union[HumanMessage, AIMessage]:
    return [parse_message(message) for message in chat_history]


@cl.on_chat_start
def start_chat():
    cl.user_session.set("chat_history", [])


@cl.on_message
async def main(message: cl.Message) -> cl.Message:
    # Append the user message to the chat history
    chat_history = cl.user_session.get("chat_history")
    chat_history.append(message)

    response = cl.Message(content="")
    await response.send()

    stream = pipeline.astream(
        {"history": parse_history(chat_history), "input": message.content}
    )

    async for chunk in stream:
        await response.stream_token(chunk)

    # Update the chat history
    chat_history.append(response)
    cl.user_session.set("chat_history", chat_history)

    await response.update()
