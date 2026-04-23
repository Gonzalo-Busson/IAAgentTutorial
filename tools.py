from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from datetime import datetime
from langchain.tools import tool

search = DuckDuckGoSearchRun()
search_tool = tool(name="DuckDuckGo Search", 
                   func=search.run, 
                   description="use this tool to search the web for recent information")