from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool

from rich import print

#1 creating a tool

def get_text_length(text: str) -> int:
    """Returns the numbers of characters in the given Text"""
    return len(text)

llm = ChatMistralAI(model="mistral-small-2506")

# 2 Tool binding with LLM
llm_with_tool = llm.bind_tools([get_text_length])

result1 = llm.invoke("Hello, my dog is cute")
print(result1)

result2 = llm_with_tool.invoke("Hello, my dog is cute. Please tell me the length of this text using the tool.")
print(result2)
