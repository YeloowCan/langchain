from langchain.tools import tool

@tool
def sum(a: int, b: int) -> int:
  """sum two number"""
  return a + b

@tool("web_search")
def search(query: str) -> int:
  """search web information"""
  return f"Results for :{query}"

@tool("calculator", description="Performs arithmetic calculations. Use this for any math problems.")
def calc(expression: str) -> str:
    """Evaluate mathematical expressions."""
    return str(eval(expression))