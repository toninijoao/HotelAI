from typing import Annotated, Optional, TypedDict
from langgraph.graph.message import add_messages

class HotelState(TypedDict):
    messages: Annotated[list, add_messages]
    intent: Optional[str]
    check_in: Optional[str]
    check_out: Optional[str]
    guests: Optional[int]
    room_type: Optional[str]
    availability: Optional[dict]
    reservation: Optional[dict]
    retrieved_context: Optional[str]
    retrieved_docs: Optional[list]