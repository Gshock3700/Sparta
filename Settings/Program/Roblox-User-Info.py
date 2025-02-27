from Config.Util import *
from Config.Config import *

try:
    import requests
except Exception as e:
   ErrorModule(e)

Title("Roblox User Info")

try:
    username_input = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Username -> {color.RESET}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")
    try:
        response = requests.post("https://users.roblox.com/v1/usernames/users", json={
            "usernames": [username_input],
            "excludeBannedUsers": "true"
        })

        data = response.json()

        user_id = data['data'][0]['id']

        user_info_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        user_info = user_info_response.json()

        try:
            userid = user_info['id']
        except:
            userid = "None"
        
        try:
            display_name = user_info['displayName']
        except:
            display_name = "None"
        
        try:
            username = user_info['name']
        except:
            username = "None"

        try:
            description = user_info['description']
        except:
            description = "None"

        try:
            created_at = user_info['created']
        except:
            created_at = "None"
        
        try:
            is_banned = user_info['isBanned']
        except:
            is_banned = "None"
        
        try:
            external_app_display_name = user_info['externalAppDisplayName']
        except:
            external_app_display_name = "None"

        try:
            has_verified_badge = user_info['hasVerifiedBadge']
        except:
            has_verified_badge = "None"

        print(f"""
    {INFO_ADD} Username       : {white}{username}{red}
    {INFO_ADD} Id             : {white}{userid}{red}
    {INFO_ADD} Display Name   : {white}{display_name}{red}
    {INFO_ADD} Description    : {white}{description}{red}
    {INFO_ADD} Created        : {white}{created_at}{red}
    {INFO_ADD} Banned         : {white}{is_banned}{red}
    {INFO_ADD} External Name  : {white}{external_app_display_name}{red}
    {INFO_ADD} Verified Badge : {white}{has_verified_badge}{red}
    """)
        Continue()
        Reset()
    except:
        ErrorUsername()
except Exception as e:
    Error(e)
