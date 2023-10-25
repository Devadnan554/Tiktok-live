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
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent , LikeEvent ,DisconnectEvent , LikeEvent , JoinEvent , GiftEvent , ShareEvent , UnknownEvent
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
developer : Abu Layan
developer_snapchat : devadnan                                                                                                                        
##### ##### ##### ##### ##### ##### ##### ##### ##### #####  
''')

username = input(green_color+"insert username for Client ==> "+detect_color)


client: TikTokLiveClient = TikTokLiveClient(unique_id="@"+username)


# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print(green_color+"Connected to Room ID:"+detect_color, client.room_id)


# Notice no decorator?
async def on_comment(event: CommentEvent):
   # user = event.user.nickname
    #comment = event.comment
    #reshaped_user = arabic_reshaper.reshape(user)    # correct its shape
    #bidi_user = get_display(reshaped_user)
    #reshaped_comment = arabic_reshaper.reshape(comment)    # correct its shape
    #bidi_comment = get_display(reshaped_comment)    
    print(green_color+f"{event.user.nickname} ->"+detect_color+f" {event.comment}")
   # print(green_color+bidi_user+"  ==> "+detect_color+bidi_comment)

# Define handling an event via a "callback"
client.add_listener("comment", on_comment)


@client.on("disconnect")
async def on_disconnect(event: DisconnectEvent):
    print(detect_color+"Disconnected")

@client.on("like")
async def on_like(event: LikeEvent):
    print(green_color+f"{event.user.nickname}"+detect_color+" has like the live !")




@client.on("join")
async def on_join(event: JoinEvent):
    print(green_color+f"{event.user.nickname}"+detect_color+" joined the stream!")
    #userjoin = event.user.unique_id
    #reshaped_userjoin = arabic_reshaper.reshape(userjoin)    # correct its shape
    #bidi_userjoin = get_display(reshaped_userjoin)
    #print(green_color+ bidi_userjoin +" ==> "+detect_color+"join the room")

@client.on("share")
async def on_share(event: ShareEvent):
    print(green_color+f"@{event.user.nickname}  "+detect_color+"shared the stream!")


    


@client.on("error")
async def on_connect(error: Exception):
    # Handle the error
    if isinstance(error, SomeRandomError):
        print(green_color+"Handle some error!")
        return
     # Otherwise, log the error
    # You can use the internal method, but ideally your own
    client._log_error(error)
if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()
