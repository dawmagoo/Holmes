import discord
from discord.ext import commands
import requests

# Tworzymy obiekt klienta Discord
client = commands.Bot(command_prefix='/wiki', intents=discord.Intents.all())

# Tworzymy komendę, która pozwala użytkownikowi wyszukać informacje w MediaWiki
@client.command()
async def search(ctx, *, query):
    # Wysyłamy zapytanie do MediaWiki API
    response = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={query}&utf8=1&formatversion=2')
    data = response.json()

    # Pobieramy pierwszy wynik wyszukiwania
    result = data['query']['search'][0]

    # Tworzymy wiadomość z odpowiedzią
    message = f'Znaleziono artykuł o tytule "{result["title"]}": https://en.wikipedia.org/wiki/{result["title"].replace(" ", "_")}'

    # Wysyłamy wiadomość na czacie
    await ctx.send(message)

    # Wyświetlamy pytanie na konsoli
    print(f'Zadano pytanie: {query}')


# Token bota Discord
TOKEN = 'YOUR_BOT_TOKEN'

# Uruchamiamy bota
client.run(TOKEN)
