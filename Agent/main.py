# goal is to get the current weather of karachi or any area of the world using 
#  open ai apikey chat inference

from openai import OpenAI
from dotenv import load_dotenv
import json
import requests
load_dotenv()

client = OpenAI()

def get_weather(city:str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
       return f"The weather in {city} is {response.text}."
    else:
        return "Unable to fetch weather data."

tools = [
    {
        "tool_name": "get_weather",
        "description": "Find live weather for any city.",
        "function": get_weather,
        "input": "city-name"
    }
]


SYSTEM_PROMPT=f"""
    you are an help full assititnace whose job is to answer the query of user.

    follow the flow for any type of query you have to go thogut each step dont skip any.
    1. analyze : understand what user wants to say or identify the users goal.
    2. plan    : make a possible plan to achive user's goal.
    3. action  : take steps to complete the plan use tools given to you if you think tools will help you to have that 
    the given tools are in this list {tools}  
    4. observe : after taking action what you get the result are goan be part of observatoin you have to 

    Rules:
    - Follow the Output JSON Format.
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query

    
    Output JSON Format:
    {{
        "step": "string",
        "content": "string",
        "function": "The name of function if the step is action",
        "input": "The input parameter for the function",
    }}

    EXample:
    you must follow the same order for all the user query and follow the output format strictly.

    User Query = "What is the weather of xyz city"
    OUPUT: {{"step":"plan" , "content" : "the user is asking to check the weather of xyz"}}
    OUPUT: {{"step":"plan" , "content":"from the avable tools i need to use the get_weather tool to get the  live weahter info"}}
    OUPUT: {{"step":"action", "function":"get_weather" ,"input":"xyz"}}
    OUTPUT: {{"step":"observe", "output":"45deg"}}
    OUTPUT:{{"step":"ouput","content":"The weather of xyz city is 45 deg"}}

    


"""

messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
         ]

query = input("...........")
messages.append({"role":"user","content":query})


while True:

    res = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=messages,
        response_format={"type":"json_object"}
        
    )

    messages.append({"role":"assistant" ,"content":res.choices[0].message.content})  

    parsed_json_message = json.loads(res.choices[0].message.content) 

    if parsed_json_message.get("step") == "plan":
        print("\n🤖 ",parsed_json_message.get("content"))
        continue

    if parsed_json_message.get("step") == "action":
        tool_name = parsed_json_message.get("function")
        tool_input = parsed_json_message.get("input")
        print(f"\n🤖 I will use {tool_name} tool with input {tool_input}")
        print(f"\n🤖: Executing {tool_name} tool...")

        for obj in tools:
            if obj.get("tool_name") == tool_name:
                output = obj.get("function")(tool_input)
                print(f"\n🤖: The data that i got from {tool_name} tool  is  {output}")

                messages.append({"role":"user","content":json.dumps({"step":"observe", "output":output})})
                print(f"\n🤖: validating the output...")

        continue

    if parsed_json_message.get("step") == "output":
            print(f"\n🤖: {parsed_json_message.get("content")}")
            break

        
  