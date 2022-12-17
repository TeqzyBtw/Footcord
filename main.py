import nextcord
import requests
import asyncio
import http.client

conn = http.client.HTTPConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapikey': "API KEY HERE"
}

client = nextcord.Client()


@client.event
async def on_ready():
    #await asyncio.sleep(2)
    print(f"bot is online, ping: {client.latency}")
    #while True:
        #await asyncio.sleep(15)



@client.slash_command(description="Sends The Current Countrys That Are Still Not Eliminated")
async def countrys(interaction: nextcord.Interaction):
    conn.request("GET", "/countries", headers=headers)
    res = conn.getresponse()
    data = res.read()
    stringcounter = data.decode("utf-8")
    embed = nextcord.Embed(title="Current Countrys That Are Still In", description=f"{stringcounter}", color=nextcord.Color.green)

@client.slash_command(description="Get A List Of Available Leagues And Cups")
async def leagues(interaction: nextcord.Interaction):
    conn.request("GET", "/leagues", headers=headers)
    res = conn.getresponse()
    data = res.read()
    stringcounter = data.decode("utf-8")
    embed = nextcord.Embed(title="List Of Available Leagues And Cups", description=f"{stringcounter}", color=nextcord.Color.red)

client.run("TOKEN HERE")
