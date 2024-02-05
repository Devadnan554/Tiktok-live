import sys , os 
import argparse
import json
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
from TikTokLive.types.events import ConnectEvent,  ViewerUpdateEvent , CommentEvent, DisconnectEvent ,LikeEvent ,LiveEndEvent,JoinEvent,ShareEvent,FollowEvent,GiftEvent,EnvelopeEvent,MoreShareEvent,IntroMessageEvent
from bidi.algorithm import get_display
from datetime import datetime
import arabic_reshaper
linux = 'clear'
windows = 'cls'
os.system([linux, windows][os.name == 'nt'])

def parse_args():
    
    parser = argparse.ArgumentParser(description="Tiktok Live tool")
    parser.add_argument("-u", help="profile username", required=True, nargs=1)
    return parser.parse_args()


def main():
    args = parse_args()
    user = args.u
    client: TikTokLiveClient = TikTokLiveClient(unique_id="@"+user[0])
    os.system([linux, windows][os.name == 'nt'])
    print(Fore.BLUE+Style.DIM+ '''
 _______                         ______         __                               
|       \                       /      \       |  \                              
| $$$$$$$\  ______   __     __ |  $$$$$$\  ____| $$ _______    ______   _______  
| $$  | $$ /      \ |  \   /  \| $$__| $$ /      $$|       \  |      \ |       \ 
| $$  | $$|  $$$$$$\ \$$\ /  $$| $$    $$|  $$$$$$$| $$$$$$$\  \$$$$$$\| $$$$$$$
| $$  | $$| $$    $$  \$$\  $$ | $$$$$$$$| $$  | $$| $$  | $$ /      $$| $$  | $$
| $$__/ $$| $$$$$$$$   \$$ $$  | $$  | $$| $$__| $$| $$  | $$|  $$$$$$$| $$  | $$
| $$    $$ \$$     \    \$$$   | $$  | $$ \$$    $$| $$  | $$ \$$    $$| $$  | $$
 \$$$$$$$   \$$$$$$$     \$     \$$   \$$  \$$$$$$$ \$$   \$$  \$$$$$$$ \$$   \$$
                                                                                 
 
    ''')
    print ('''
    '''+Fore.BLUE+Style.DIM+'''[ + ]'''+Fore.WHITE+''' SnapChat : Devadnan'''+Fore.BLUE+'''         [ + ]'''+Fore.WHITE+''' Insta : Dev.adnan           '''+Fore.BLUE+'''[ + ]'''+Fore.WHITE+''' Tiktok : aama5544
    '''+Style.RESET_ALL)
    @client.on("connect")
    async def on_connect(_: ConnectEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+" ================== Connect For id room ==================> ] ", client.room_id)
        #print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+" ================== Connect For id room ==================> ] ", client.room_info)
        top = client.room_info
        owner = top.get("owner")
        print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+" ================== owner ==================> ] ")
        print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+owner["nickname"]+ "  "+owner["bio_description"] + "]")
        users = top.get("top_fans")
        print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+" ================== top_fans ==================> ] ")
        for x in users:
            user_adnan = x["user"]
            print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+user_adnan["nickname"]+ "  "+user_adnan["bio_description"] + "]")

    async def on_comment(event: CommentEvent): 
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] [ 🗯️ Comment from ] "+f"{event.user.unique_id}"+" | "+f"{event.user.nickname}-->  "+Fore.WHITE +f" {event.comment}")
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
        print(Fore.BLUE+"["+current_time+"] "+"[ 😍 Like from ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
    @client.on("live_end")
    async def on_connect(event: LiveEndEvent):
        print(f"Ended Live :(")
    @client.on("join")
    async def on_join(event: JoinEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+"[ 🏃‍♂️ join ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
    @client.on("share")
    async def on_share(event: ShareEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+"[ 🚀 Shareing ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
    @client.on("follow")
    async def on_follow(event: FollowEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+"[ 🫂 Add ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
    @client.on("gift")
    async def on_gift(event: GiftEvent):
        if event.gift.info.type <= 1:
            now = datetime.now()
            current_time = now.strftime("%I:%M:%S")
            print(Fore.BLUE+"["+current_time+"] "+"[ 🎁 Sent Gift ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname} --> {event.gift.info.name}")
    @client.on("viewer_update")
    async def on_connect(event: ViewerUpdateEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] [  👀  Viewer ] "+ Fore.WHITE, event.viewer_count)
    
    @client.on("more_share")
    async def on_connect(event: MoreShareEvent):
        print(f"More than {event.amount} users have joined from {event.user.unique_id}'s share link!")
    @client.on("intro_message")
    async def on_connect(event: IntroMessageEvent):
        print(f"Message: {event.message}")
    if __name__ == '__main__':
        client.run()
        print(Style.RESET_ALL)


if __name__ == '__main__':
    main()
