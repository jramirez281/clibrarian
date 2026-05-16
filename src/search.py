import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

def search(query):
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    response = client.search(query, max_results=5)
    results = []
    for result in response["results"]:
        results.append({
            "title": result["title"],
            "url": result["url"],
            "content": result["content"]
        })
    return results
