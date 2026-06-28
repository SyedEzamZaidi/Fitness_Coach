import operator
from typing import TypedDict, Literal, Annotated
from pydantic import BaseModel

from langchain_core.messages import(
    AnyMessage,
    HumanMessage,
    SystemMessage,
    AIMessage,
) 

class Profile(BaseModel):
    name: str
    age: int
    gender: Literal["Male","Female"]
    weight: float
    height: int
    diseases: list[str]
    coach: Literal["Soft","Moderate","Intense","Brutal"]
    food_pref: Literal["Veg","Non-Veg","Vegan","Eggetarian","Halal","Jain"]


class state(TypedDict):
    profile: Profile
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int


