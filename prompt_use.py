from langchain_openai import ChatOpenAI
from langchain.tools import tool

llm = ChatOpenAI(
  api_key="sk-f9a354e4af734c1d90c42f8c6d9997b4",
  base_url="https://api.deepseek.com",
  model="deepseek-chat", 
)

print(llm.invoke("你好").content)

for chunk in llm.stream("给我讲一个笑话"):
  print(chunk.text)

# responses = llm.batch([
#   "你是谁",
#   "上海今天的天气怎么样",
#   "利物浦和曼联哪支球队更厉害"
# ])

# for response in responses:
#   print(response)

for item in llm.batch_as_completed([
  "夸一下我",
  "祝福一下我"
]):
  print(item)

@tool
def get_weather(location: str) -> str:
    """Get the weather at a location."""
    return f"It's sunny in {location}."

model_with_tool = llm.bind_tools([get_weather])

response = model_with_tool.invoke("What's the weather like in Boston?")

print(response)
