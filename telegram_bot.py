import time
import os
import telepot
from telepot.loop import MessageLoop       
from telepot.namedtuple import InlineKeyboardMarkup as MU, InlineKeyboardButton as BT

access_token = os.environ["BOT_TOKEN"]
token = (access_token)
mc = '699099967'
bot = telepot.Bot(token)

def btn_show(msg):
    btn1 = BT(text = "1. Hello", callback_data = "1")
    btn2 = BT(text = "2. Bye", callback_data = "2")
    btn3 = BT(text = "3. 양식", callback_data = "3")
    btn4 = BT(text = "4. 지갑", callback_data = "4")
    btn5 = BT(text = "5. ASTA", callback_data = "5")
    btn6 = BT(text = "6. MYCE", callback_data = "6")
    mu = MU(inline_keyboard = [[btn1, btn2],[btn3, btn4],[btn5, btn6]])
    bot.sendMessage(mc, "선택하세요", reply_markup = mu)

def query_ans(msg):
    query_data = msg["data"]
    if query_data == "1":
        bot.sendMessage(mc, text = "안녕하세요")
    elif query_data == "2":
        bot.sendMessage(mc, text = "안녕히 계세요")
    elif query_data == "3":
        bot.sendMessage(mc, text = "무슨양식?")
    elif query_data == "4":
        bot.sendMessage(mc, text = "0x8f2d166eCF5742f77fEdb339dFd3dD20b91Bcc14")
    elif query_data == "5":
        bot.sendMessage(mc, text = "본부장님1,913,824")
    elif query_data == "6":
        bot.sendMessage(mc, text = "평단 2.2")

        
access_token = os.environ["BOT_TOKEN"]
TOKEN = (access_token)
mc = '699099967'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': btn_show, "callback_query" : query_ans}).run_as_thread()

print('Listening ...')

while 1: 
    time.sleep(10)
