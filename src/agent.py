import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

def synthesize(query, results):
    if not results:
        return "No results found."

    formatted_results = ""
    for i, result in enumerate(results, 1):
        formatted_results += f"Source {i}: {result['title']}\nURL: {result['url']}\nContent: {result['content']}\n\n"

    # Mock response for now, replace with real API call later
    return f"[MOCK RESPONSE] Here is what I found for: '{query}'\n\n{formatted_results}"
