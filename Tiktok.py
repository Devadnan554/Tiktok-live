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
print(Fore.BLUE+Style.DIM+ '''
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
'''+Fore.BLUE+Style.DIM+'''[ + ]'''+Fore.WHITE+''' SnapChat : Devadnan'''+Fore.BLUE+'''         [ + ]'''+Fore.WHITE+''' Insta : Dev.adnan           '''+Fore.BLUE+'''[ + ]'''+Fore.WHITE+''' Tiktok : aama5544
'''+Style.RESET_ALL)

print ('''
        '''+Fore.WHITE+'''AAMA554 : '''+Fore.BLUE+'''[ 1 ]      '''+Fore.WHITE+'''OM_ALGAME3 : '''+Fore.BLUE+'''[ 2 ]       '''+Fore.WHITE+'''Other Account : '''+Fore.BLUE+'''[ 3 ]
''')  

print("""

""")


try:
    while True:
        choose = input(Fore.WHITE+"                         witch choose you want "+Fore.BLUE+"[ ❓ ]"+Fore.WHITE+" : "+Fore.BLUE)
        try:
            def aama5544():
                try:
                    while True:
                        os.system([linux, windows][os.name == 'nt'])
                        client: TikTokLiveClient = TikTokLiveClient(unique_id="@aama5544")
                        @client.on("connect")
                        async def on_connect(_: ConnectEvent):
                            now = datetime.now()
                            current_time = now.strftime("%I:%M:%S")
                            print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+" ================== Connect For id room ================== ] ",client.room_id)
                        async def on_comment(event: CommentEvent): 
                            now = datetime.now()
                            current_time = now.strftime("%I:%M:%S")
                            print(Fore.BLUE+"["+current_time+"] "+"[ 🗯️ Comment from ] "+f"{event.user.unique_id}"+" | "+f"{event.user.nickname}-->  "+Fore.WHITE +f" {event.comment}")
                            #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Comment from ] "+ green_color+f"{event.user.nickname} -->"+Fore.BLUE +f" {event.comment}")
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
                            #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Like from ] "+ green_color+f"{event.user.nickname}")
                        @client.on("live_end")
                        async def on_connect(event: LiveEndEvent):
                            print(f"Ended Live :(")
                        @client.on("join")
                        async def on_join(event: JoinEvent):
                            now = datetime.now()
                            current_time = now.strftime("%I:%M:%S")
                            print(Fore.BLUE+"["+current_time+"] "+"[ 🏃‍♂️ join ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                            #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ join ] "+ green_color+f"{event.user.nickname}")
                        @client.on("share")
                        async def on_share(event: ShareEvent):
                            now = datetime.now()
                            current_time = now.strftime("%I:%M:%S")
                            print(Fore.BLUE+"["+current_time+"] "+"[ 🚀 Shareing ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                            #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Shareing ] "+ green_color+f"{event.user.nickname}")
                        @client.on("follow")
                        async def on_follow(event: FollowEvent):
                            now = datetime.now()
                            current_time = now.strftime("%I:%M:%S")
                            print(Fore.BLUE+"["+current_time+"] "+"[  🫂  Add ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                            #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Add ] "+ green_color+f"{event.user.nickname}")
                        @client.on("gift")
                        async def on_gift(event: GiftEvent):
                            # If it's type 1 and the streak is over
                            if event.gift.info.type <= 1:
                                now = datetime.now()
                                current_time = now.strftime("%I:%M:%S")
                                print(Fore.BLUE+"["+current_time+"] "+"[  🎁 Sent Gift ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname} --> {event.gift.info.name}")
                                #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Sent Gift ] "+ green_color+ f"{event.user.nickname} --> {event.gift.info.name}")
                        @client.on("viewer_update")
                        async def on_connect(event: ViewerUpdateEvent):
                            now = datetime.now()
                            current_time = now.strftime("%I:%M:%S")
                            print(Fore.BLUE+"["+current_time+"] [  👀  Viewer ] "+ Fore.WHITE, event.viewer_count)
                        if __name__ == '__main__':
                            client.run()
                        print(Style.RESET_ALL)
                except KeyboardInterrupt:
                    os.system([linux, windows][os.name == 'nt'])
                    print(Fore.WHITE+"                         I will miss you "+Fore.BLUE+"[ 😞 ]"+Fore.WHITE)    
                finally:
                    print(Fore.WHITE+"                         Don't forget to add me on social media "+Fore.BLUE+"[ 😉 ]"+Fore.WHITE)  
                    print(Fore.BLUE+Style.DIM+ '''
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
                    '''+Fore.BLUE+Style.DIM+'''[ + ]'''+Fore.WHITE+''' SnapChat : Devadnan'''+Fore.BLUE+'''         [ + ]'''+Fore.WHITE+''' Insta : Dev.adnan           '''+Fore.BLUE+'''[ + ]'''+Fore.WHITE+''' Tiktok : aama5544
                    '''+Style.RESET_ALL)       


            def OM_ALGAME3():
                os.system([linux, windows][os.name == 'nt'])
                client: TikTokLiveClient = TikTokLiveClient(unique_id="@OM_ALGAME3")
                @client.on("connect")
                async def on_connect(_: ConnectEvent):
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] "+ green_color+"[ ================== Connect For id room ================== ] ", client.room_id)
                async def on_comment(event: CommentEvent): 
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] "+"[ 🗯️ Comment from ] "+f"{event.user.unique_id}"+" | "+f"{event.user.nickname}-->  "+Fore.WHITE +f" {event.comment}")
                    #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Comment from ] "+ green_color+f"{event.user.nickname} -->"+Fore.BLUE +f" {event.comment}")
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
                    #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Like from ] "+ green_color+f"{event.user.nickname}")
                @client.on("live_end")
                async def on_connect(event: LiveEndEvent):
                    print(f"Ended Live :(")
                @client.on("join")
                async def on_join(event: JoinEvent):
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] "+"[ 🏃‍♂️ join ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                    #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ join ] "+ green_color+f"{event.user.nickname}")
                @client.on("share")
                async def on_share(event: ShareEvent):
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] "+"[  🚀  Shareing ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                    #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Shareing ] "+ green_color+f"{event.user.nickname}")
                @client.on("follow")
                async def on_follow(event: FollowEvent):
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] "+"[  🫂  Add ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                    #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Add ] "+ green_color+f"{event.user.nickname}")
                @client.on("gift")
                async def on_gift(event: GiftEvent):
                    # If it's type 1 and the streak is over
                    if event.gift.info.type <= 1:
                        now = datetime.now()
                        current_time = now.strftime("%I:%M:%S")
                        print(Fore.BLUE+"["+current_time+"] "+"[ 🎁 Sent Gift ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname} --> {event.gift.info.name}")
                        #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Sent Gift ] "+ green_color+ f"{event.user.nickname} --> {event.gift.info.name}")
                @client.on("viewer_update")
                async def on_connect(event: ViewerUpdateEvent):
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] [  👀  Viewer ] "+ Fore.WHITE, event.viewer_count)
                if __name__ == '__main__':
                    client.run()
                print(Style.RESET_ALL)

            def Other():
                username = input(Fore.WHITE+"                         Username For Client "+Fore.BLUE+"[ ❓ ] : ")
                client: TikTokLiveClient = TikTokLiveClient(unique_id="@"+username)
                os.system([linux, windows][os.name == 'nt'])
                @client.on("connect")
                async def on_connect(_: ConnectEvent):
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] "+ green_color+"["+" ================== Connect For id room ==================> ] ", client.room_id)
                async def on_comment(event: CommentEvent): 
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] [ 🗯️ Comment from ] "+f"{event.user.unique_id}"+" | "+f"{event.user.nickname}-->  "+Fore.WHITE +f" {event.comment}")
                    #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Comment from ] "+ green_color+f"{event.user.nickname} -->"+Fore.BLUE +f" {event.comment}")
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
                    #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Like from ] "+ green_color+f"{event.user.nickname}")
                @client.on("live_end")
                async def on_connect(event: LiveEndEvent):
                    print(f"Ended Live :(")
                @client.on("join")
                async def on_join(event: JoinEvent):
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] "+"[ 🏃‍♂️ join ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                    #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ join ] "+ green_color+f"{event.user.nickname}")
                @client.on("share")
                async def on_share(event: ShareEvent):
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] "+"[ 🚀 Shareing ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                    #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Shareing ] "+ green_color+f"{event.user.nickname}")
                @client.on("follow")
                async def on_follow(event: FollowEvent):
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] "+"[ 🫂 Add ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                    #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Add ] "+ green_color+f"{event.user.nickname}")
                @client.on("gift")
                async def on_gift(event: GiftEvent):
                    # If it's type 1 and the streak is over
                    if event.gift.info.type <= 1:
                        now = datetime.now()
                        current_time = now.strftime("%I:%M:%S")
                        print(Fore.BLUE+"["+current_time+"] "+"[ 🎁 Sent Gift ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname} --> {event.gift.info.name}")
                        #print(Fore.BLUE+"["+current_time+"] "+ Fore.LIGHTYELLOW_EX+ "[ Sent Gift ] "+ green_color+ f"{event.user.nickname} --> {event.gift.info.name}")
                @client.on("viewer_update")
                async def on_connect(event: ViewerUpdateEvent):
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S")
                    print(Fore.BLUE+"["+current_time+"] [  👀  Viewer ] "+ Fore.WHITE, event.viewer_count)
                if __name__ == '__main__':
                    client.run()
                print(Style.RESET_ALL)
            choose = int(choose)    
            if choose == 1 :
                aama5544()
            elif choose == 2:
                OM_ALGAME3()
            elif choose == 3 :
                Other()

        except ValueError:
            print(Fore.WHITE+"                         Cant Type String Only Intger "+Fore.BLUE+"[ 😠 ]"+Fore.WHITE)



		
except KeyboardInterrupt:
    os.system([linux, windows][os.name == 'nt'])
    print(Fore.WHITE+"                         I will miss you "+Fore.BLUE+"[ 😞 ]"+Fore.WHITE)    
finally:
    print(Fore.WHITE+"                         Don't forget to add me on social media "+Fore.BLUE+"[ 😉 ]"+Fore.WHITE)  
    print(Fore.BLUE+Style.DIM+ '''
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
    '''+Fore.BLUE+Style.DIM+'''[ + ]'''+Fore.WHITE+''' SnapChat : Devadnan'''+Fore.BLUE+'''         [ + ]'''+Fore.WHITE+''' Insta : Dev.adnan           '''+Fore.BLUE+'''[ + ]'''+Fore.WHITE+''' Tiktok : aama5544
    '''+Style.RESET_ALL)