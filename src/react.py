from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

from src.tools.code_translator import translate45, translate63
from src.state import State

load_dotenv()

memory = MemorySaver()
config = {"configurable": {"thread_id": "1"}}
tools = [translate45, translate63]

llm_with_tools = ChatOllama(model="qwen3:8b").bind_tools(tools)

def reasoning(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


graph_builder = StateGraph(State)
graph_builder.add_node("reasoning", reasoning)
graph_builder.add_node("acting", ToolNode(tools))

graph_builder.add_edge(START, "reasoning")
graph_builder.add_conditional_edges("reasoning", tools_condition, {"tools": "acting", "__end__": "__end__"})
graph_builder.add_edge("acting", "reasoning")

graph = graph_builder.compile(checkpointer=memory)


def main():
    from src.ui import print_banner, print_loading, print_ready, print_processing, print_response, print_exit, prompt

    print_banner()
    print_loading()
    graph.get_graph().print_ascii()
    print_ready()

    while True:
        try:
            user_input = prompt()
        except (KeyboardInterrupt, EOFError):
            break
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input.strip():
            continue
        print_processing()
        result = graph.invoke({"messages": [("user", user_input)]}, config=config)
        print_response(result["messages"][-1].content)

    print_exit()
