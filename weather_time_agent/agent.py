from google.adk.agents import Agent
from dotenv import load_dotenv
load_dotenv()

MODEL_NAME = "gemini-2.0-flash"

def get_current_weather(city: str)->str:
    """
    Provides the current weather for a given city

    """
    if city.lower() in ["kolkata", "kolkata west bengal"]:
        return f"The current weather in Kolkata is: Humid with moderate heat, with temperature around 35C"
    else:
        return "No weather detail found for the entered city"
    

def get_current_time(city: str)-> str:
    """
    Provides the current time for a given city.
    """

    if city.lower() in ["kolkata", "kolkata west bengal"]:
        return f"Current time is 02:00 PM"
    else:
        return "No time information found for the city"
    
manager_agent =  Agent(
    name="root_weather_time_agent",
    model=MODEL_NAME,
    description="provides the weather and time information",
    instruction="You have access to the get_current_time tool and the get_current_weather tool.Always use these tools to answer to the user question about weather and time information in a given city. please do not answer to any other questions",
    tools=[get_current_weather, get_current_time]
)

root_agent = manager_agent