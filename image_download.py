import asyncio
import requests
from bs4 import BeautifulSoup

# This below is the main function 
async def function1():
    url = 'https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/6620ec7544fa3849c3cb27fc_party_wumpus.gif'
    r = requests.get(url, allow_redirects=True)
    open('discordgifgif2.gif', 'wb').write(r.content)
    print("Image 1 is downloaded")

async def function2():
    url = 'https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/6620ec7544fa3849c3cb27fc_party_wumpus.gif'
    r = requests.get(url, allow_redirects=True)
    open('discordgif2.gif', 'wb').write(r.content)
    print("Image 2 is downloaded")

async def function3():
    url = 'https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/6620ec7544fa3849c3cb27fc_party_wumpus.gif'
    r = requests.get(url, allow_redirects=True)
    open('discordgif3.gif', 'wb').write(r.content)
    print("Image 3 is downloaded")

async def main():
    a = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )

asyncio.run(main())

# This below checks the links that is link is able to be downloaded
# url = "https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/662630272724e61320fb7ee2_WUMPUS.webp"
# r = requests.get(url)

# print(r.headers["Content-Type"])

# This below will parse the images and etc linkes which we can download it 
# url = "https://www.discord.com"
# r = requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")

# # find all <img> tags
# for img in soup.find_all("img"):
#     print(img.get("src"))