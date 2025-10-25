from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

user_message = HumanMessage(content="今天的天气怎么样")

system_message = SystemMessage(content="你是一个幽默的助手")

chat_template = ChatPromptTemplate.from_messages([
    system_message,
    user_message,
])

print(user_message)