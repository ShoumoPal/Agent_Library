from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

search = DuckDuckGoSearchRun()

# Search tool to look up current information on the internet
search_tool = Tool(
    name="Search",
    func=search.run,
    description="Useful for when you need to look up current information on the internet"
)

def image_search(query: str) -> str:

    print(query)
    import requests
    import os

    PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
    if not PEXELS_API_KEY:
        raise ValueError("PEXELS_API_KEY not found in environment variables.")

    url = "https://api.pexels.com/v1/search"
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    params = {
        "query": query
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching image: {response.status_code}, {response.text}")
    data = response.json()
    if 'photos' in data and len(data['photos']) > 0:
        return data['photos'][0]['src']['medium']
    else:
        return "No image found"
    
image_search_tool = Tool(
    name="Image_Search",
    func=image_search,
    description="Useful for when you need to find an image related to a topic. Use the titles of the books as the paramenter for this function."
)