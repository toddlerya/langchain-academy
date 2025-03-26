from langchain_core.messages import HumanMessage
from langgraph.graph import END, START, MessagesState, StateGraph
from llm_util import llm

# messages = [
#     AIMessage(content="So you said you were researching ocean mammals?", name="Model")
# ]
# messages.append(HumanMessage(content="Yes, that's right.", name="Lance"))
# messages.append(
#     AIMessage(content="Great, what would you like to learn about.", name="Model")
# )
# messages.append(
#     HumanMessage(
#         content="I want to learn about the best place to see Orcas in the US.",
#         name="Lance",
#     )
# )

# for m in messages:
#     m.pretty_print()


# result = llm.invoke(messages)
# print(f"type(result): {type(result)}")
# print(f"result: {result}")
# print(f"result.response_metadata: {result.response_metadata}")


def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b


llm_with_tools = llm.bind_tools([multiply])
tool_call = llm_with_tools.invoke([HumanMessage(content="2乘3等于多少", name="Lance")])
print(f"tool_call.tool_calls: {tool_call.tool_calls}")


# Node
def tool_calling_llm(state: MessagesState):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


# Build graph
builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_edge(START, "tool_calling_llm")
builder.add_edge("tool_calling_llm", END)
graph = builder.compile()

# View
# print(graph.get_graph().draw_mermaid())
# display(Image(graph.get_graph().draw_mermaid_png()))

# messages = graph.invoke({"messages": HumanMessage(content="2乘以3等于几")})
# for m in messages["messages"]:
#     m.pretty_print()
