import os
import random
import discord
import requests
import json
import asyncio
from discord.ext import commands

from replit import db
#db["totalRPS"] = 0
currentRPS = db["totalRPS"]


intents = discord.Intents.all()

helpCommand = commands.DefaultHelpCommand(no_category = "commands")

bot = commands.Bot(command_prefix = "!audrey", intents = intents)

@bot.event
async def on_connect():
  print("your bot is online")

@bot.command(brief = "have the bot say hello!")
async def audrey(ctx):
  await ctx.reply("hello from audrey's bot")

@bot.command(brief = "be greeted")
async def hello(ctx, name): # ctx and name are separated by space, add as many as needed
  await ctx.send("hello, " + name.upper() + "!")

@bot.command(brief = "add two numbers, separated by a space")
async def add(ctx, one, two): 
  three = int(one) + int(two)
  await ctx.send("" + one + " + " + two + " = " + str(three))


emojiexpressions = [":grinning:", ":smiley:", ":smile:", ":grin:", ":laughing:", ":sweat_smile:", ":joy:", ":rofl:", ":relaxed:", ":blush:", ":innocent:", ":slight_smile:", ":upside_down:", ":wink:", ":relieved:", ":smiling_face_with_tear:", ":heart_eyes:", ":smiling_face_with_3_hearts:", ":kissing_heart:", ":kissing:", ":kissing_smiling_eyes:", ":kissing_closed_eyes:", ":yum:", ":stuck_out_tongue:", ":stuck_out_tongue_closed_eyes:", ":stuck_out_tongue_winking_eye:", ":zany_face:", ":face_with_raised_eyebrow:", ":face_with_monocle:", ":nerd:", ":sunglasses:", ":star_struck:", ":partying_face:", ":smirk:", ":unamused:", ":disappointed:", ":pensive:", ":worried:", ":confused:", ":slight_frown:", ":frowning2:", ":persevere:", ":confounded:", ":tired_face:", ":weary:", ":pleading_face:", ":cry:", ":sob:", ":triumph:", ":face_exhaling:", ":angry:", ":rage:", ":face_with_symbols_over_mouth:", ":exploding_head:", ":face_in_clouds:", ":cold_face:", ":scream:", ":fearful:", ":cold_sweat:", ":disappointed_relieved:", ":sweat:", ":hugging:", ":thinking:", ":face_with_hand_over_mouth:", ":yawning_face:", ":shushing_face:", ":lying_face:", ":no_mouth:", ":neutral_face:", ":expressionless:", ":grimacing:", ":rolling_eyes:", ":hushed:", ":frowning:", ":open_mouth:", ":astonished:", ":sleeping:", ":drooling_face:", ":sleepy:", ":dizzy_face:", ":face_with_spiral_eyes:", ":zipper_mouth:", ":woozy_face:", ":nauseated_face:", ":face_vomiting:", ":sneezing_face:", ":mask:", ":thermometer_face:", ":head_bandage:", ":money_mouth:", ":cowboy:", ":disguised_face:", ":smiling_imp:", ":imp:", ":japanese_ogre:", ":japanese_goblin:", ":clown:", ":ghost:", ":skull:", ":skull_crossbones:", ":alien:", ":space_invader:", ":robot:", ":jack_o_lantern:"]



@bot.command(brief = "get a random facial emoji")
async def emoji(ctx): 
  emoji = random.choice(emojiexpressions)
  await ctx.send(emoji)


@bot.command(brief = "input a time from 1-12 and am/pm separated by a space")
async def time(ctx, time, day):
  time = int(time)
  if day.lower() == "pm":
    if time == 12:
      await ctx.send("it's noon!")
    elif time < 5:
      await ctx.send("good afternoon!")
    elif time < 8:
      await ctx.send("good evening!")
    else:
      await ctx.send("good night!")
  elif day.lower() == "am":
    if time == 12:
      await ctx.send("it's midnight!")
    else:
      await ctx.send("good morning!")

@bot.command(brief = "a dumpster fire picture")
async def dumpsterfire(ctx):
  await ctx.send("https://i.kym-cdn.com/entries/icons/original/000/021/521/DumpsterFire2.jpg")


bearList = ["https://nationalzoo.si.edu/sites/default/files/animals/slothbear-001.jpg", "https://files.worldwildlife.org/wwfcmsprod/images/Polar_bear_on_ice_in_Svalbard_Norway_WW294883/story_full_width/42ny6cwj8t_Polar_bear_on_ice_in_Svalbard_Norway_WW294883.jpg", "https://cdn.britannica.com/52/162652-050-6A676116/Polar-bears-ice-floe-Norway.jpg", "https://cdn.audleytravel.com/3994/2849/79/1340901-polar-bear-churchill.jpg", "https://www.vitalground.org/wp-content/uploads/2021/06/i-362880_griz_cubs.jpg", "https://ewscripps.brightspotcdn.com/dims4/default/aaeb01c/2147483647/strip/true/crop/1280x720+0+0/resize/1280x720!/quality/90/?url=http%3A%2F%2Fewscripps-brightspot.s3.amazonaws.com%2Fc8%2Fec%2Fa2916d3748ddbb24cf767b4d7806%2Fap20191697142470.jpg", "https://therevelator.org/wp-content/uploads/2021/11/Grizzly-road-Jim-Peaco-NPS.jpg", "https://i.insider.com/606196da8e71b3001851939d?width=1200&format=jpeg", "https://wildwnc.org/wp-content/uploads/2020/01/IMG_7457_byCaseyWillis-6t04.jpg"]

@bot.command(brief = "get a random bear picture")
async def bear(ctx):
  pic = random.choice(bearList)
  await ctx.send(pic)

outcomes = ["certainly", "certainly not", "perhaps", "never", "no way", "without a doubt", "doubtful", "perhaps", "if hell freezes over", "of course!!!"]
@bot.command(aliases = ["8ball"], brief = "ask a question, recieve a completely accurate answer")
async def eightball(ctx, *, phrase: str): # phrase is the whole remaining message
  reply = random.choice(outcomes)
  await ctx.send("**" + phrase + "**: " + reply)

rpsList = ["rock", "paper", "scissors"]




currentRPS = db["totalRPS"]

@bot.command(aliases = ["RPS", "Rps"], brief = "play rock, paper, scissors with the bot")
async def rps(ctx, choice):
  currentRPS = db["totalRPS"]
  currentRPS += 1
  db["totalRPS"] = currentRPS
  
  
  botChoice = random.choice(rpsList)
  choice = choice.lower()
  if botChoice == choice:
    outcome = "tie!"
  
  elif choice == "rock":
    if botChoice == "scissors":
      outcome = "you win!"
    elif botChoice == "paper":
      outcome = "you lose!"
  elif choice == "paper":
    if botChoice == "rock":
      outcome = "you win!"
    elif botChoice == "scissors":
      outcome = "you lose!"
  elif choice == "scissors":
    if botChoice == "paper":
      outcome = "you win!"
    elif botChoice == "rock":
      outcome = "you lose!"

  else:
    await ctx.send("that's not a valid option, please try again")
    pass
  
  #await ctx.send("you played: " + choice + "\nbot played: " + botChoice + "\n" + outcome)
  await ctx.send("you played " + choice + "\nbot played " + botChoice + "\n" + outcome)
  await ctx.send("_rps game # " + str(currentRPS) + "_")








@bot.command(brief = "get a random joke from an API")
async def joke(ctx): 
  # create a variable for the joke api url
  url = "https://official-joke-api.appspot.com/random_joke"

  # contact the url
  req = requests.get(url)

  # get data from joke url
  data = req.json()

  setup = data["setup"]
  
  await ctx.send(setup)

  punchline = data["punchline"]
  await asyncio.sleep(1)
  await ctx.send(punchline)

@bot.command(brief = "find the weather by inputting a zip code")
async def weather(ctx, zip): #they put in a zip code 
  # create a variable for the weather api url
  currentAPI = os.environ['willisWeather']
  url = "https://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",US&appid=" + currentAPI
  
  # contact the url
  req = requests.get(url)
  
  # get data from joke url
  data = req.json()
  
  # description for weather
  weather = data["weather"][0]["description"]
  
  # temp for weather
  temperature = data["main"]["temp"]
  # change to f
  temperature = (temperature - 273.15) * (9/5) + 32 
  # round to 2 decimal places
  temperature = round(temperature, 1)
  await ctx.send(weather + ", " + str(temperature) + " °F")







@bot.command(brief = "find the expected age for a name")
async def nameage(ctx, name): #they put in a name
  # create a variable for the name api url
  url = "https://api.agify.io/?name=" + name
  
  
  
  # contact the url
  req = requests.get(url)
  
  # get data from name url
  data = req.json()


  # age given by database
  age = data["age"]
  
  await ctx.send("your expected age is " + str(age))



@bot.command(brief = "input two names separated by a space to check compatiblity")
async def love(ctx, name1, name2): #they put in a name
  url = "https://love-calculator.p.rapidapi.com/getPercentage"
  
  querystring = {"sname":name1,"fname":name2}
  
  love_API = os.environ['loveAPI']
  headers = {
	  "X-RapidAPI-Key": love_API,
	  "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = response.json()
  percentage = data["percentage"]
  result = data["result"]
  await ctx.send("You are " + percentage + "% compatible. " + result)
  #await ctx.send(response.text)



@bot.command(brief = "input a language code (ex: fr, es) followed by a space, then a message to translate")
async def translate(ctx, lang, *, content: str):
  url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
  translate_API = os.environ['loveAPI']
  payload = "q=" + content + "&target=" + lang + "&source=en"
  headers = {
	  "content-type": "application/x-www-form-urlencoded",
	  "Accept-Encoding": "application/gzip",
	  "X-RapidAPI-Key": translate_API,
	  "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
  }
  
  response = requests.request("POST", url, data=payload, headers=headers)
  data = response.json()
  response = data["data"]["translations"][0]["translatedText"]
  
  new = ""
  i = 0
  while i < (len(response) - 4):
    
    if response[i:i+5] == "&#39;":
      new += "'"
      i += 5
    else:
     new += response[i]
     i += 1
  if response[len(response)-4:len(response)] == "#39;":
    new += ""
  else:
    new += response[len(response)-4:len(response)]
  
  await ctx.send(new)
  #print(response.text)




@bot.command(brief = "get a random cat fact")
async def catfact(ctx):
  url = "https://catfact.ninja/fact"
  
  req = requests.get(url)
  
  data = req.json()
  
  fact = data["fact"]
  
  await ctx.send(fact)


@bot.command(brief = "get a random dog picture")
async def dog(ctx):
  url = "https://dog.ceo/api/breeds/image/random"
  
  req = requests.get(url)
  
  data = req.json()
  
  pic = data["message"]
  
  await ctx.send(pic)



@bot.command()
async def spotifySearch(ctx, *, query:str):
  url = "https://api.apilayer.com/spotify/search?q=" + query
  await ctx.send("searching spotify for " + query)
  payload = {}
  headers= {
    "apikey": "Q6tJHtYFYAHPoFF95EfYbuDI5YRmVM2Z"
  }
  
  response = requests.request("GET", url, headers=headers, data = payload)
  
  status_code = response.status_code
  #result = response.text
  data = response.json()
  #print(response)

  #print(data)
  #print("\n\n\n\n\n\n\n\n\nthis is it")
  #print(data["albums"]["items"][0]["data"])
  #print("\n\n\n\n\n\n\n\n\nthis is it")
  await ctx.send(data["albums"]["items"][0]["data"]["name"] + "by" +data["albums"]["items"][0]["data"]["artists"]["items"][0]["profile"]["name"])
  #print(data["albums"]["items"][0]["data"]["coverArt"]["sources"][0]["url"])
  uri = data["albums"]["items"][0]["data"]["uri"]
  
  uri = uri[14:len(uri)]
  url = "https://open.spotify.com/album/" + uri
  await ctx.send(url)
  
  #print("\n\n\n\n\n\n\n\n\nthis is it")
  #print(data["playlists"]["items"][0]["data"])
  #print("\n\n\n\n\n\n\n\n\nthis is it")
  await ctx.send(data["playlists"]["items"][0]["data"]["name"])
  uri = data["playlists"]["items"][0]["data"]["uri"]
  uri = uri[17:len(uri)]
  url = "https://open.spotify.com/playlist/" + uri
  await ctx.send(url)




my_secret = os.environ['token']
bot.run(my_secret)

#bot.run("MTAzNDEzMjE2MTkwMjY3NDA0MA.G8tpcL.M5HoFDhCbgXxyScJuUd2h4X-X24W-n6yaF9NcY")