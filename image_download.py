import asyncio
import requests
from bs4 import BeautifulSoup

print("Welcome to Image/GIF download services")
print("1. for Manual download\n2. for Pinterest download\n3. Single download")
user_ask = input("Enter number to chose medium to download image/gif: ")

if("1" in user_ask):
    def manual_download():
        print("You chose manual download.....")
        async def function1():
            url = input("Enter URL of your choice: ") # Here we are entering the URL 
            response = requests.get(url) # Get request has been sended
            file_name = input("Enter name to save the file: ") # Asking for file name to be saved
            ext_name = input("Enter ext name: ") # Asking for extension name
            open(f"{file_name}.{ext_name}", "wb").write(response.content)
            print(f"{file_name} is downloaded") # The content is being downlaoded and saved in the folder from the file name given

        async def function2():
            url = input("Enter URL of your choice: ") # Here we are entering the URL
            response = requests.get(url) # Get request has been sended
            file_name = input("Enter name to save the file: ") # Asking for file name to be saved
            ext_name = input("Enter ext name: ") # Asking for extension name
            open(f"{file_name}.{ext_name}", "wb").write(response.content)
            print(f"{file_name} is downloaded") # The content is being downlaoded and saved in the folder from the file name given

        async def function3():
            url = input("Enter URL of your choice: ") # Here we are entering the URL
            response = requests.get(url) # Get request has been sended
            file_name = input("Enter name to save the file: ") # Asking for file name to be saved
            ext_name = input("Enter ext name: ") # Asking for extension name
            open(f"{file_name}.{ext_name}", "wb").write(response.content)
            print(f"{file_name} is downloaded") # The content is being downlaoded and saved in the folder from the file name given

        async def main():
            l = await asyncio.gather(
                function1(),
                function2(),
                function3()
            )
        asyncio.run(main())
    manual_download()

elif("2" in user_ask):
    def pinteres_download():
        print("You chose pinterest download.....")
        url = input("enter url here: ") # Here we are giving the URL
        headers = {"User-Agent": "Mozilla/5.0"}  # Pretend to be a browser
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        # Try to get the image URL
        og_image = soup.find("meta", property="og:image")
        if og_image:
            print("Image URL:", og_image["content"])

        # Try to get the video URL (in case it's a GIF-like video)
        og_video = soup.find("meta", property="og:video")
        if og_video:
            print("Video/GIF URL:", og_video["content"])

        url = input("Enter url here: ") # Here we are giving the URL
        response = requests.get(url) # Get request has beend made
        file_name = input("Enter the name of the file: ") # Asking for file name to be saved
        ext_name = input("Enter ext name: ") # Asking for extension name
        open(f"{file_name}.{ext_name}", "wb").write(response.content)
        print("Download Successful") # Here the content has been saved in the folder from the file name given
    pinteres_download()

elif("3" in user_ask):
    def single_download():
        print("You chose single download.....")
        url = input("Enter url here: ") # Here we are giving the URL
        file_name = input("Enter the name of the file: ") # Get request has beend made
        response = requests.get(url) # Asking for file name to be saved
        ext_name = input("Enter ext name: ") # Asking for extension name
        open(f"{file_name}.{ext_name}", "wb").write(response.content)
        print("Download Successful") # Here the content has been saved in the folder from the file name given
    single_download()

else:
    print("Something went wrong")