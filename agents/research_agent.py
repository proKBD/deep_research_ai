from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import Tool
import os

class ResearchAgent:
    def __init__(self):
        api_key = os.getenv('TAVILY_API_KEY')
        if not api_key:
            raise ValueError("TAVILY_API_KEY environment variable not set")
        self.tool = TavilySearchResults(api_key=api_key)

    def search(self, query):
        return self.tool.run(query)

