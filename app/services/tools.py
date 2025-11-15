from langchain_community.tools.tavily_search import TavilySearchResults


def get_web_search_tool(api_key: str) -> TavilySearchResults:
    tavily_tool = TavilySearchResults(openai_api_key=api_key)
    return tavily_tool