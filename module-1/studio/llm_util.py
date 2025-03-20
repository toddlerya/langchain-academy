import os

from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langgraph.types import Command, interrupt  # noqa: F401

# 加载 .env 文件中的环境变量
# 默认加载项目根目录下的 .env 文件
load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    # qwq-32b model only support stream mode
    # model="qwq-32b",
    model="qwen2.5-14b-instruct-1m",
    temperature=0.7,
)

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
search_tool = TavilySearchResults(max_results=2)
