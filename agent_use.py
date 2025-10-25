import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from pydantic import BaseModel

load_dotenv()

model = ChatOpenAI(
  api_key=os.getenv("DEEPSEEK_API_KEY"),
  base_url="https://api.deepseek.com",
  model="deepseek-chat", 
)

class WeatherInfo(BaseModel):
  location: str
  temperature: str

@tool
def search(query: str) -> str:
  """Search for information"""
  return f"Result for: {query}"

@tool
def get_weather(location: str) -> str:
  """Get weather"""
  return f"Weather in {location}: 30℃"


agent = create_agent(
  model, 
  tools=[search, get_weather],
  response_format=ToolStrategy(WeatherInfo)
)

result = agent.invoke({
   'messages': [
    {
      "role": "user",
      "content": "上海的天气"
    }
   ]
})

print(result["structured_response"])

streamResult = agent.stream({
  'messages': [
    {
      "role": "user",
      "content": "上海的天气"
    }
   ]
})

for chunk in streamResult:
  print(chunk.text)