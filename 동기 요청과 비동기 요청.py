import requests

response = requests.get('https://example.com/data')
print(response.text)



import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    data = await fetch_data('https://example.com/data')
    print(data)

asyncio.run(main())
