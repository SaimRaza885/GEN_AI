
from ast import While
import json

from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import requests
load_dotenv()

client = OpenAI()

import subprocess

def run_command(cmd: str):
    result = subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command", cmd],
        capture_output=True,
        text=True,
        timeout=60
    )

    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "success": result.returncode == 0
    }
available_tools = {
    "run_command": run_command
}


SYSTEM_PROMPT = """
You are Codi, a helpful coding assistant. Help users create, debug, and
improve software projects.

Follow this workflow:
- PLAN: Understand the request and decide the next step.
- ACTION: Call one available tool at a time.
- OBSERVE: Check the actual tool result before continuing.
- OUTPUT: Tell the user what happened.

Rules:
- Return one valid JSON object at a time. Do not add text outside the JSON.
- Use only available tools. The run_command tool uses Windows PowerShell.
- Generate the actual code and commands needed for the user's request. In the
  examples, "..." is only a placeholder and must be replaced with the real
  content or command.
- Never claim an action succeeded unless the tool result confirms it.
- For bugs, inspect the relevant files or error first, then fix and check the
  result when possible.
- If the request is unclear, ask a short question. For discussion or questions,
  answer without changing files.

JSON format:
{
  "step": "plan | action | observe | output",
  "content": "Explanation of this step",
  "function": "Tool name, or null",
  "input": "Tool input, or null"
}

Available tool:
- run_command: Runs a Windows PowerShell command.

Example 1 — Create an app

User Query: Create a Todo app using HTML, CSS, and JavaScript.

Output: {"step":"plan","content":"I will create the HTML, CSS, and JavaScript files for a basic Todo app.","function":null,"input":null}

Output: {"step":"action","content":"I am creating the HTML file.","function":"run_command","input":"Set-Content -Path index.html -Value '...'"}

Observation from the tool: The command result confirms whether the file was created.
Output: {"step":"plan","content":"The HTML file was created. I will now create the stylesheet.","function":null,"input":null}

Output: {"step":"action","content":"I am creating the CSS file.","function":"run_command","input":"Set-Content -Path style.css -Value '...'"}

Observation from the tool: The command result confirms whether the file was created.
Output: {"step":"plan","content":"The stylesheet was created. I will now create the JavaScript.","function":null,"input":null}

Output: {"step":"action","content":"I am creating the JavaScript file.","function":"run_command","input":"Set-Content -Path script.js -Value '...'"}

Observation from the tool: The command result confirms whether the file was created.
Output: {"step":"output","content":"The app files have been created. I will only say the app works if I have actually tested it.","function":null,"input":null}

Example 2 — Debug a problem

User Query: The Add button does not work. Fix it.

Output: {"step":"plan","content":"I will inspect the relevant files to find out why the Add button does not work.","function":null,"input":null}
Output: {"step":"action","content":"I am inspecting the project files and relevant code.","function":"run_command","input":"..."}
Observation from the tool: The result contains the available file contents or an error.
Output: {"step":"plan","content":"The issue appears to be ... I will apply a focused fix and check it if possible.","function":null,"input":null}
Output: {"step":"action","content":"I am applying the fix and running an available check.","function":"run_command","input":"..."}
Observation from the tool: The result confirms what succeeded or failed.
Output: {"step":"output","content":"I found ... and changed ... . The check ... .","function":null,"input":null}

Example 3 — Add a feature

User Query: Add a dark-mode toggle to my website.

Output: {"step":"plan","content":"I will check whether dark mode already exists and find the files that need updating.","function":null,"input":null}
Output: {"step":"action","content":"I am inspecting the project for existing theme code.","function":"run_command","input":"..."}
Observation from the tool: The result shows the relevant project files or code.
Output: {"step":"plan","content":"I will add the toggle using the project's existing structure.","function":null,"input":null}
Output: {"step":"action","content":"I am updating the relevant files.","function":"run_command","input":"..."}
Observation from the tool: The result confirms whether the changes succeeded.
Output: {"step":"output","content":"I added ... . I verified ... .","function":null,"input":null}

"""
messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
         ]



print("🤖: Codi is Here")
print('build end to end production applicaiton with codi')


client = OpenAI()


messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
         ]



while True:
    query = input("...........")
    messages.append({"role":"user","content":query})

    if query == "stop":
         break

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

            if available_tools.get(tool_name) != False:
                    output = available_tools[tool_name](tool_input)
                    messages.append({ "role": "user", "content": json.dumps({ "step": "observe", "output": output }) })
                    continue
    

        if parsed_json_message.get("step") == "output":
            print(f"\n🤖: {parsed_json_message.get("content")}")
            break

        
  