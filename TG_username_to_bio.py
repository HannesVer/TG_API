from telethon import TelegramClient
from collections import namedtuple
from telethon.tl.functions.users import GetFullUserRequest
import pandas as pd
import numpy as np

api_id = int(xx)
api_hash = 'xx'
phone = '+xx'
limit = xx


client = TelegramClient('xx', api_id, api_hash)
teledata = pd.read_excel(r"./your_list_of_usernames")
teledata["Bio"] = ""
usernames = teledata["Username"]
print(len(usernames))

for i in range(len(usernames)):
    async def main():
        try:
            full = await client(GetFullUserRequest(usernames.iloc[i]))
            teledata["Bio"].iloc[i] = str(full.full_user.about)
        except:
            teledata["Bio"].iloc[i] = "N/A"
    with client:
        client.loop.run_until_complete(main())

print(teledata["Bio"])
teledata.to_excel("youroutputfile.xlsx")  

