from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv

load_dotenv()

main_agent = Agent(
    name="simple_search_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions using Google Search",
    instruction="You are an expert researcher. You always stick to facts.",
    tools=[google_search]
)

root_agent=main_agent