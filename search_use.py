from langchain_community.tools import DuckDuckGoSearchRun

# 初始化工具
search = DuckDuckGoSearchRun()

# 直接运行搜索
result = search.invoke("2026年世界杯举办地")

print(result)