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
from TikTokLive.types.events import ConnectEvent,  ViewerUpdateEvent , CommentEvent, DisconnectEvent ,LikeEvent ,LiveEndEvent,JoinEvent,ShareEvent,FollowEvent,GiftEvent,EnvelopeEvent
from bidi.algorithm import get_display
from datetime import datetime
import arabic_reshaper
linux = 'clear'
windows = 'cls'
os.system([linux, windows][os.name == 'nt'])
print(Fore.RED+'''
::'###::::'########::'##::::'##:
:'## ##::: ##.... ##: ##:::: ##:
'##:. ##:: ##:::: ##: ##:::: ##:
##:::. ##: ########:: ##:::: ##:
#########: ##.... ##: ##:::: ##:
##.... ##: ##:::: ##: ##:::: ##:
##:::: ##: ########::. #######::
..:::::..::........::::.......:::
##::::::::::'###::::'##:::'##::::'###::::'##::: ##:
##:::::::::'## ##:::. ##:'##::::'## ##::: ###:: ##:
##::::::::'##:. ##:::. ####::::'##:. ##:: ####: ##:
##:::::::'##:::. ##:::. ##::::'##:::. ##: ## ## ##:
##::::::: #########:::: ##:::: #########: ##. ####:
##::::::: ##.... ##:::: ##:::: ##.... ##: ##:. ###:
########: ##:::: ##:::: ##:::: ##:::: ##: ##::. ##:
........::..:::::..:::::..:::::..:::::..::..::::..:: 
''')
print ('''
'''+Fore.BLUE+'''[ + ]'''+Fore.WHITE+''' SnapChat : Devadnan
'''+Fore.BLUE+'''[ + ]'''+Fore.WHITE+''' Insta : Dev.adnan
'''+Fore.BLUE+'''[ + ]'''+Fore.WHITE+''' Tiktok : aama5544
''')

print ('''
'''+Fore.WHITE+'''AAMA554 : '''+Fore.BLUE+'''[ 1 ]
'''+Fore.WHITE+'''OM_ALGAME3 : '''+Fore.BLUE+'''[ 2 ]
'''+Fore.WHITE+'''Other Account : '''+Fore.BLUE+'''[ 3 ]
''')  

choose = int(input(Fore.WHITE+"witch choose you want "+Fore.BLUE+"[ ? ]"+Fore.WHITE+" : "))
if choose == 1:
    client: TikTokLiveClient = TikTokLiveClient(unique_id="@aama5544")
    @client.on("connect")
    async def on_connect(_: ConnectEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+" Connect For id room ] ", client.room_id)
    async def on_comment(event: CommentEvent): 
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Comment from ] "+ green_color+f"{event.user.nickname} -->"+Fore.BLUE +f" {event.comment}")
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
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Like from ] "+ green_color+f"{event.user.nickname}")
    @client.on("live_end")
    async def on_connect(event: LiveEndEvent):
        print(f"Ended Live :(")
    @client.on("join")
    async def on_join(event: JoinEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ join ] "+ green_color+f"{event.user.nickname}")
    @client.on("share")
    async def on_share(event: ShareEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Shareing ] "+ green_color+f"{event.user.nickname}")
    @client.on("follow")
    async def on_follow(event: FollowEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Add ] "+ green_color+f"{event.user.nickname}")
    @client.on("gift")
    async def on_gift(event: GiftEvent):
        # If it's type 1 and the streak is over
        if event.gift.info.type <= 1:
            now = datetime.now()
            current_time = now.strftime("%I:%M:%S")
            print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Sent Gift ] "+ green_color+ f"{event.user.nickname} --> {event.gift.info.name}")
    @client.on("envelope")
    async def on_connect(event: EnvelopeEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Treasure Box ] "+ green_color+f"{event.treasure_box_user.nickname} -> {event.treasure_box_data}") 
    @client.on("viewer_update")
    async def on_connect(event: ViewerUpdateEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Viewer ] "+ green_color, event.viewer_count)
    if __name__ == '__main__':
        client.run()
    print(Style.RESET_ALL)
elif choose == 2:
    client: TikTokLiveClient = TikTokLiveClient(unique_id="@om_algame3")
    @client.on("connect")
    async def on_connect(_: ConnectEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+" Connect For id room ] ", client.room_id)
    async def on_comment(event: CommentEvent): 
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Comment from ] "+ green_color+f"{event.user.nickname} -->"+Fore.BLUE +f" {event.comment}")
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
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Like from ] "+ green_color+f"{event.user.nickname}")
    @client.on("live_end")
    async def on_connect(event: LiveEndEvent):
        print(f"Ended Live :(")
    @client.on("join")
    async def on_join(event: JoinEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ join ] "+ green_color+f"{event.user.nickname}")
    @client.on("share")
    async def on_share(event: ShareEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Shareing ] "+ green_color+f"{event.user.nickname}")
    @client.on("follow")
    async def on_follow(event: FollowEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Add ] "+ green_color+f"{event.user.nickname}")
    @client.on("gift")
    async def on_gift(event: GiftEvent):
        # If it's type 1 and the streak is over
        if event.gift.info.type <= 1:
            now = datetime.now()
            current_time = now.strftime("%I:%M:%S")
            print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Sent Gift ] "+ green_color+ f"{event.user.nickname} --> {event.gift.info.name}")
    @client.on("envelope")
    async def on_connect(event: EnvelopeEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Treasure Box ] "+ green_color+f"{event.treasure_box_user.nickname} -> {event.treasure_box_data}") 
    @client.on("viewer_update")
    async def on_connect(event: ViewerUpdateEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Viewer ] "+ green_color, event.viewer_count)
    if __name__ == '__main__':
        client.run()
    print(Style.RESET_ALL)
elif choose == 3:
    username = input("Username For Client "+Fore.BLUE+"[ ? ]"+Fore.WHITE+" : ")
    client: TikTokLiveClient = TikTokLiveClient(unique_id="@"+username)
    @client.on("connect")
    async def on_connect(_: ConnectEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+" Connect For id room ] ", client.room_id)
    async def on_comment(event: CommentEvent): 
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Comment from ] "+ green_color+f"{event.user.nickname} -->"+Fore.BLUE +f" {event.comment}")
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
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Like from ] "+ green_color+f"{event.user.nickname}")
        
    @client.on("live_end")
    async def on_connect(event: LiveEndEvent):
        print(f"Ended Live :(")
    @client.on("join")
    async def on_join(event: JoinEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ join ] "+ green_color+f"{event.user.nickname}")
    @client.on("share")
    async def on_share(event: ShareEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Shareing ] "+ green_color+f"{event.user.nickname}")
    @client.on("follow")
    async def on_follow(event: FollowEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Add ] "+ green_color+f"{event.user.nickname}")
    @client.on("gift")
    async def on_gift(event: GiftEvent):
        # If it's type 1 and the streak is over
        if event.gift.info.type <= 1:
            now = datetime.now()
            current_time = now.strftime("%I:%M:%S")
            print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Sent Gift ] "+ green_color+ f"{event.user.nickname} --> {event.gift.info.name}")
    @client.on("envelope")
    async def on_connect(event: EnvelopeEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Treasure Box ] "+ green_color+f"{event.treasure_box_user.nickname} -> {event.treasure_box_data}") 
    @client.on("viewer_update")
    async def on_connect(event: ViewerUpdateEvent):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Viewer ] "+ green_color, event.viewer_count)
    if __name__ == '__main__':
        client.run()
    print(Style.RESET_ALL)
