import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.checkpoint.postgres import PostgresSaver 

load_dotenv()

model = ChatOpenAI(
  api_key=os.getenv("DEEPSEEK_API_KEY"),
  base_url="https://api.deepseek.com",
  model="deepseek-chat", 
)

@tool
def search(query: str) -> str:
  """Search for information"""
  return f"Result for: {query}"

@tool
def get_weather(location: str) -> str:
  """Get weather"""
  return f"Weather in {location}: 30℃"


DB_URI = "postgresql://postgres:postgres@localhost:5442/postgres?sslmode=disable"

with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    checkpointer.setup() # auto create tables in PostgresSql
    agent = create_agent(
        model, 
        tools=[search, get_weather],
        checkpointer=InMemorySaver()
    )


