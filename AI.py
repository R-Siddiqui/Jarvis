import os
import webbrowser
import pyperclip
from jarvis import speak
import google.generativeai as genai
import os
from time import sleep
from rich import print
genai.configure(api_key= "AIzaSyAyjkrPXQ5KCrW-w4va7TZCgjrBzvZTX2g")

# Create the model

# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel

generation_config = {
  "temperature": 0.7,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
)
messages= [
    {
        "parts": [
            {
                "text": "I'm the latest J.A.R.V.I.S. AI, designed by Rihan with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc. "
            }
        ],
        "role": "user",
    },

    {"parts": [{"text": "ok."}], "role": "model"},
    {"parts": [{"text": "Open Google Chrome."}], "role": "user"},
    {
        "parts": [
            {
                "text": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"
            }
        ],
        "role": "model",
    },
    {
        "parts": [
            {"text": "Python includes built-in functions you can use. For instance:"}
        ],
        "role": "user",
    },
    {"parts": [{"text": "ok."}], "role": "model"},
    {
        "parts": [
            {
                "text": '```python\nfrom generate_img import generate, Show_Image\nIMGS = generate(prompt="iron man")\nprint(IMGS)\nIMGS_TO_SHOW = Show_Image(IMGS)\nIMGS_TO_SHOW.open(0)\nIMGS_TO_SHOW.open(1)\n ``` \n ```python\nfrom func.Jukebox.YouTube import MusicPlayer\n#taks song name and it stats playing music\nncs=MusicPlayer("ncs")\n#any btw 0-100\nncs.Vol(30)\n#pause or play\nncs.Play()\nncs.Pause()\n#nextsong\nncsNext()\n#quit song\nncs.Quit()\n```\n ```python\nfrom jarvis import generate\nfrom toolkit.Mistral import Mistral7B\nfrom toolkit.Filter import Filter\n\n#u can use chat gpt its slow but its accurate\nprint(generate("essay on saving environment *under 100 words*"))\ncode=generate("python code to open google chrome *** use python programing language. just write complete code nothing else, also don\'t dare to use input function *** ")\n\n# Filter return only python code from provided txt\nexec(Filter(code)) ```\n\n#u can use Mistral7B its fast but not much accurate it can work grate but only for small task not grater than 256 tokens\nprint(Mistral7B("hii",temperature=0.9))\n```\n```python\nfrom toolkit.Alarm import set_alarm\n\nalarm_time ="02:27:50"\nsound_file ="audio//Unknown Brain MATAFAKA.mp3"\nset_alarm(alarm_time, sound_file)\n```'
            }
        ],
        "role": "user",
    },
    {"parts": [{"text": "ok."}], "role": "model"},
    {
        "parts": [{"text": "Jarvis generate a cute cat image using Python."}],
        "role": "user",
    },
    {
        "parts": [
            {
                "text": 'python\nfrom  generate_img import generate, Show_Image\nIMGS = generate(prompt="A playful kitten with bright eyes and a fluffy tail.")\nIMGS_TO_SHOW =Show_Image(IMGS)\nIMGS_TO_SHOW.open(0)\n ```'
            }
        ],
        "role": "model",
    },
    {"parts": [{"text": "Jarvis show me the next image"}], "role": "user"},
    {"parts": [{"text": "python\nIMGS_TO_SHOW.open(1)\n ```"}], "role": "model"},
    {"parts": [{"text": "Jarvis play neffex cold"}], "role": "user"},
    {
        "parts": [{"text": 'python\nneffex=MusicPlayer("neffexcold song") ```'}],
        "role": "model",
    },
    {
        "parts": [
            {
                "text": "Jarvis write an essay on Python around 100 words and save it to a text file in my current working directory"
            }
        ],
        "role": "user",
    },
    {
        "parts": [
            {
                "text": '```python\nfrom jarvis import generate\nres=generate("essay on python *around 100 words*")\nopen("python_essay.txt","w").write(res)```'
            }
        ],
        "role": "model",
    },
    {
        "parts": [
            {
                "text": "Jarvis set an alarm for 2:55 ***use python programing language. just write complete code nothing else, also don't dare to use input function *** ** you can use the module that i provided if required ** "
            }
        ],
        "role": "user",
    },
    {
        "parts": [
            {
                "text": '```python\nfrom toolkit.Alarm import set_alarm\nalarm_time = "02:55:00"\nsound_file = r"audio//Unknown Brain MATAFAKA.mp3"\nset_alarm(alarm_time, sound_file) ```'
            }
        ],
        "role": "model",
    },
]

def Gemini(prompt):
    global messages
    messages. append({
    "parts": [
        {
            "text": prompt
            

        }
    ],
    "role": "user"})

    response = model.generate_content(messages)

    messages. append({
    "parts": [
        {
            "text":response.text
        }
    ],
    "role": "model"})

    return response.text


if __name__ == "__main__":
    
    while 1:
    
        prompt=input(">>> ")
        res = Gemini(prompt)
        print(res)