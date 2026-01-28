import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse

load_dotenv()

deepseek_model = ChatOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    model="deepseek-chat", 
)

doubao_model = ChatOpenAI(
    api_key=os.getenv("DOUBAO_API_KEY"),
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    model="doubao-seed-1-6-251015"
)

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model"""
    message_count = len(request.state["messages"])

    if message_count < 10:
        model = deepseek_model
    else:
        model = doubao_model

    return handler(request.override(model=model))

agent = create_agent(
    model=deepseek_model,
    middleware=[dynamic_model_selection]
)

result = agent.invoke({"messages": [{"role": "user", "content": "你是谁"}]})

print(result)