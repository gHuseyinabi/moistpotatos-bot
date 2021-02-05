#a simple bot using the discord api
#this bot will reply with a random insult when someone sends !insult
import discord
import random
import logging
import time
import googlesearch
import requests
import json

logging.basicConfig()
logging.getLogger('discord')
client = discord.Client()
GreetList = ['Greetings!', 'Hello!', 'Hi!', 'Hey!']
version = '0.92'

@client.event
async def on_ready():
    print(f'Joined as {client.user}')

@client.event
async def on_message(msg):
    if msg.author ==  client.user:
        return

    if msg.content.startswith('%' + 'help'):
        print(f'{time.asctime()}: We received "!help" command!')
        await msg.channel.send(f'''Commands for version `{version}`:
        **%help** - sends this list of commands
        **%greet** - says hello
        **%search** - finds and retrieves ten urls based on your search query''')

    if msg.content.startswith('%' + 'greet'):
        print(f'{time.asctime()}: We received the "%greet" command!')
        await msg.channel.send(GreetList[random.randrange(0, 4, 1)])

    if msg.content.startswith('%' + 'search'):
        fetchedURLS = []
        print(f'{time.asctime()}: We received the "%search" command!')
        query = msg.content[8:]
        await msg.channel.send(f'Finding ten URLS with the search query `{query}`')

        for search_results in googlesearch.search(query, tld="com", num=10, stop=10, pause=2):
            fetchedURLS.append(search_results)

        await msg.channel.send(f'''Here are ten URLS based on your search `{query}`:''')
        
        for url in fetchedURLS:
            await msg.channel.send(url)

    if msg.content.startswith('%' + 'r/memes'):
        hot_posts = requests.get(f'http://www.reddit.com/user/lechocolatfroid/posts.json', {'User-agent': 'u/lechocolatfroid'})
        txt = hot_posts.text
        print(hot_posts.text)
        data = json.loads(txt)

        
        for post in data['data']['children']:
            await msg.channel.send(post['data']['id'], "", post['data']['author'], post['data']['body'])

        


client.run('token')