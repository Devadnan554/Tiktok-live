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

username = input(green_color+"ادخل اسم المستخدم ==> "+detect_color)

client: TikTokLiveClient = TikTokLiveClient(unique_id="@"+username)

@client.on("connect")
async def on_connect(_: ConnectEvent):
    print(green_color+"تم الاتصال بجلسة :"+detect_color, client.room_id)

async def on_comment(event: CommentEvent): 
    print(green_color+f"{event.user.nickname} ==>"+detect_color+f" {event.comment}")

client.add_listener("comment", on_comment)

@client.on("disconnect")
async def on_disconnect(event: DisconnectEvent):
    print(detect_color+"Disconnected")

@client.on("like")
async def on_like(event: LikeEvent):
    print(green_color+f"{event.user.nickname}"+detect_color+" كبس")

@client.on("live_end")
async def on_connect(event: LiveEndEvent):
    print(f"توقف البث:(")

@client.on("join")
async def on_join(event: JoinEvent):
    print(green_color+f"{event.user.nickname}"+detect_color+" دخل البث")

@client.on("share")
async def on_share(event: ShareEvent):
    print(green_color+f"{event.user.nickname}"+detect_color+" شير البث")

@client.on("follow")
async def on_follow(event: FollowEvent):
     print(green_color+f"{event.user.nickname}"+detect_color+" اضاف المضيف")

if __name__ == '__main__':
    client.run()