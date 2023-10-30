import sys , os 
normal_color = "\033[0;31m"
info_color = "\033[0;31m"
red_color = "\033[0;31m"
green_color = "\033[1;32m"
whiteB_color = "\033[0;31m"
detect_color = "\033[0;31m"
banner_color="\033[0;31m"
end_banner_color="\033[0;31m"
from colorama import Fore, Back, Style
from TikTokLive  import TikTokLiveClient
from TikTokLive.types.events import ConnectEvent,  ViewerUpdateEvent , CommentEvent, DisconnectEvent ,LikeEvent ,LiveEndEvent,JoinEvent,ShareEvent,FollowEvent
from bidi.algorithm import get_display
from datetime import datetime
import arabic_reshaper
linux = 'clear'
windows = 'cls'
os.system([linux, windows][os.name == 'nt'])
print(detect_color+'''
              █████████   █████                   █████                                                
  ███░░░░░███ ░░███                   ░░███                                                 
 ░███    ░███  ░███████  █████ ████    ░███         ██████   █████ ████  ██████   ████████  
 ░███████████  ░███░░███░░███ ░███     ░███        ░░░░░███ ░░███ ░███  ░░░░░███ ░░███░░███ 
 ░███░░░░░███  ░███ ░███ ░███ ░███     ░███         ███████  ░███ ░███   ███████  ░███ ░███ 
 ░███    ░███  ░███ ░███ ░███ ░███     ░███      █ ███░░███  ░███ ░███  ███░░███  ░███ ░███ 
 █████   █████ ████████  ░░████████    ███████████░░████████ ░░███████ ░░████████ ████ █████
░░░░░   ░░░░░ ░░░░░░░░    ░░░░░░░░    ░░░░░░░░░░░  ░░░░░░░░   ░░░░░███  ░░░░░░░░ ░░░░ ░░░░░ 
                                                              ███ ░███                      
                                                             ░░██████                       
                                                              ░░░░░░                        
          
''')
print ('''
##### ##### ##### ##### ##### ##### ##### ##### ##### #####                                                                                                                                                                                                                                                 
                المبرمج : ابو ليان
                 السناب : devadnan                                                                                                                        
##### ##### ##### ##### ##### ##### ##### ##### ##### #####  
''')  
username = input(green_color+"UserName For Client--> "+detect_color)
client: TikTokLiveClient = TikTokLiveClient(unique_id="@"+username)
@client.on("connect")
async def on_connect(_: ConnectEvent):
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")
    print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+" Connect For id room ] ", client.room_id)
async def on_comment(event: CommentEvent): 
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")
    print(Fore.LIGHTBLUE_EX+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Comment from ] "+ green_color+f"{event.user.nickname} -->"+Fore.BLUE +f" {event.comment}")
client.add_listener("comment", on_comment)
@client.on("disconnect")
async def on_disconnect(event: DisconnectEvent):
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")
    print(detect_color+"Disconnected")
@client.on("like")
async def on_like(event: LikeEvent):
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")
    print(Fore.LIGHTBLUE_EX+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Like from ] "+ green_color+f"{event.user.nickname}")
@client.on("live_end")
async def on_connect(event: LiveEndEvent):
    print(f"Ended Live :(")
@client.on("join")
async def on_join(event: JoinEvent):
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")
    print(Fore.LIGHTBLUE_EX+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ join ] "+ green_color+f"{event.user.nickname}")
@client.on("share")
async def on_share(event: ShareEvent):
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")
    print(Fore.LIGHTBLUE_EX+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Shareing ] "+ green_color+f"{event.user.nickname}")
@client.on("follow")
async def on_follow(event: FollowEvent):
     now = datetime.now()
     current_time = now.strftime("%I:%M:%S")
     print(Fore.LIGHTBLUE_EX+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Add ] "+ green_color+f"{event.user.nickname}")
if __name__ == '__main__':
    client.run()
print(Style.RESET_ALL)