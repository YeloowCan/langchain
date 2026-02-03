from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. 定义模型
model = ChatOpenAI(model="gpt-4o")
# 2. 定义提示词
prompt = ChatPromptTemplate.from_template("请用幽默的语气讲一个关于{topic}的故事")
# 3. 链式组合 (LCEL)
chain = prompt | model | StrOutputParser()

# 调用
response = chain.invoke({"topic": "人工智能"})
print(response)