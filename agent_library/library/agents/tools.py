from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()

# Search tool to look up current information on the internet
search_tool = Tool(
    name="Search",
    func=search.run,
    description="Useful for when you need to look up current information on the internet"
)


