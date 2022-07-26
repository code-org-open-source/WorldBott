from imports import *

# This file contains all of the Variables that the bot Uses.

# ~~ Oraganization ~~

# Why does Python not have a #DEFINE statement?

load_dotenv()
USER = os.getenv('NAME')
PASS = os.getenv('ME')
API = os.getenv('KEY')

# API KEY
key = API

# Username and Password
username = USER
password = PASS

# Starting Message.
starting_message = "Bot is up as @" + username

# Window Names
WINDOW_PROMPT = "WorldBott Prompt"
WINDOW_USERNAME = "Username Input"
WINDOW_PASSWORD = "Password Input"
WINDOW_CLOSE_VS_CODE = "This will close VS Code."
WINDOW_RELOAD = "This will reload the browser."
WINDOW_TEST_TIME = "This will stop the bot from waiting 24 hours."
WINDOW_QUIT = "This will close the Application and the Bot will Stop."
WINDOW_CUSTOM = "This will change the custom message."

# Upcoming Features
TODO = [
    "Add a way to change the username and password using a GUI",
    "Add a way to change the starting message using a GUI",
    "Add a way to change the API key using a GUI",
    "Give the bot the ability to read comments.",
    "Give the bot the ability to read posts.",
    "Give the bot the ability to read messages.",
    "Give the bot the ability to read likes.",
    "Have the bot grab its own link, communicate with a Discord bot, and send messages to a Discord channel.",
    "Discord Integration?",
    "Get the bot a custom nameplate.",
    "Get the bot a 'bot' role.",
    "Get the bot to follow other users.",
    "Have the bot communicate with another bot."
]

# Completed Features
COMPLETED = [
    "The Bot can close VS Code.",
    "The Bot can reload the page.",
    "The Bot can test the time values.",
    "The Bot can go to a specific field.",
    "The Bot can log itself in.",
    "The Bot can send messages, and custom images.",
    "The Bot can send custom messages.",
    "The Bot can use API's to get information, then post about that information.",
    "The Bot can like, and comment on its own posts.",
    "The Bot has its own GUI. (SomeWhat Completed)",
    "The Bot can select text, and delete it.",
    "The Bot has a developer mode.",
    "Add new custom messages using a GUI"
]

# Prompts
prompts = [
    "Hi there, I'm WorldBott!",
    "I'm WorldBott!",
    "Today, I was communicating with some APIs and I got this message.",
    "I really like Visual Studio code because: ",
    "Today I was wondering",
    "I'm currently thinking about",
    "I was talking to",
    "I'm currently talking to",
    "I might have done",
]

# NamePlate List
nameplate_list = [
    "Blue",
    "Red",
    "Green",
    "Yellow",
    "Purple",
    "Blue Text",
    "Red Text",
    "Green Text",
    "Yellow Text",
    "Purple Text",
    "Pink Text",
    "Neon Blue",
    "Neon Red",
    "Neon Green",
    "Neon Yellow",
    "Neon Purple",
    "Gold",
    "Silver",
    "Bronze",
    "License Plate",
    "Blue to Pink",
    "Yellow to Green",
    "Green to Blue",
    "Pink to Orange",
    "TikTok",
    "Instagram",
    "Blue Border",
    "Red Border",
    "Green Border",
    "Purple Border",
    "USA Flag",
    "Japan Flag",
    "Germany Flag",
    "Italy Flag",
    "France Flag",
    "Pride Flag",
    "Ukraine Flag",
    "OG",
    "Mod",
    "Water",
    "Fire",
    "Earth",
    "Air",
    "Rick Astley",
    "R O A C H E S"
]

# Maximum Values
MAX_POSTS = 100
MAX_LIKES = 100
MAX_COMMENTS = 100
MAX_TEXT = 500

# Minimum Values
MIN_POSTS = 1
MIN_LIKES = 1
MIN_COMMENTS = 1
MIN_TEXT = 3

# Number Values
LOW_RAND = 1
HIGH_RAND = 15

# Time Values
WAIT_TIME = 86400
RELOAD_TIME = 10
HIGH_TIME = 5.5
LOW_TIME = 1.5
QUICK_TIME = 0.5

# Title of the Window
TITLE = "WorldBott"

# Window Size
WINDOW_X = 100
WINDOW_Y = 50

# Default Element Sizes
DEFAULT_WIDTH = 20
DEFAULT_HEIGHT = 2

# Current Version of the Bot.
version = "3.0"
num_version = 3.0

# Source
source_code = "https://github.com/code-org-open-source/WorldBott"

# Defaults
default_comment = "Default WorldBott Comment"
default_status = "WorldBott " + version + "\nMade by Colack and Friends\n\n" + source_code
default_message = ":)"

# Custom Messages 
custom_message = [

]

# Default Messages
default2 = "Easy Dubs Gamers"
default4 = "✌(ツ)"
default5 = "🤖"
default6 = "My name is WorldBott Hartwell White. I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession."
defaultPrevious = ":D"
defaultRandom = "Here is a random image: "
defaultRandString = " <-- My new favorite word!"

# Josuke Laugh Meme
josuke_laugh = "https://i.kym-cdn.com/photos/images/original/001/177/975/e0e.gif"

# GUI WILL BE IMPLEMENTED SOON!
# Just wait ~1-Week

# Window Layout
layout = [
    [sg.Text("WorldBott Version " + version)],
    [sg.Button("Start")], [sg.Button("Exit")],
    [sg.Text("Username"), sg.InputText(key="username")],
    [sg.Text("Password"), sg.InputText(key="password")],
    [sg.Button("Submit"), sg.Button("Submit")],
]
