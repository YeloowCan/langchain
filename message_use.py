import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
  api_key=os.getenv("DEEPSEEK_API_KEY"),
  base_url="https://api.deepseek.com",
  model="deepseek-chat", 
)

user_message = HumanMessage(content="今天的天气怎么样")

system_message = SystemMessage(content="你是一个幽默的助手")

messages = [system_message, user_message]

response = model.invoke(messages)

print(response)