import operator
from typing_extensions import Annotated, TypedDict
from langgraph.checkpoint.memory import InMemorySaver

from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model ="llama-3.3-70b-versatile", temperature = 0)

from langchain_core.messages import(
    AnyMessage,
    HumanMessage,
    SystemMessage,
    AIMessage,
) 