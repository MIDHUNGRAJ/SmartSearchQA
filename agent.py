import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Get API keys
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Ensure API keys are available
if not TAVILY_API_KEY or not GOOGLE_API_KEY:
    raise ValueError("Please set TAVILY_API_KEY and GOOGLE_API_KEY in your .env file.")

# Setup Tavily search tool
search = TavilySearchResults()
tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description="Useful for answering questions using web search.",
    )
]

# Setup Google Generative AI (Gemini)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GOOGLE_API_KEY)

# Create the agent
agent = initialize_agent(
    tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True
)


def run_query(query: str) -> str:
    return agent.run(query)

