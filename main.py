from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]

client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)

data = {"小猫咪的坏心眼可多着呢"}
res = wm.send_template(user_id, template_id, data)
print(res)
