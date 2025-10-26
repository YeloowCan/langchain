import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

load_dotenv()

class Movie(BaseModel):
  """A Movie with details"""
  title: str = Field(..., description="The title of the movie")
  year: int = Field(..., description="The year of the movie")

model = ChatOpenAI(
  api_key=os.getenv("DEEPSEEK_API_KEY"),
  base_url="https://api.deepseek.com",
  model="deepseek-chat", 
)

model_with_structure = model.with_structured_output(Movie)

repsonse = model_with_structure.invoke("Provide details about the movie Inception")

print(repsonse)