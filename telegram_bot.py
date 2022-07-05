import time
import os
from tkinter import Button
from tkinter.tix import ButtonBox
from unittest import result
import telepot
from telepot.loop import MessageLoop       
from telepot.namedtuple import InlineKeyboardMarkup as MU, InlineKeyboardButton as BT

access_token = os.environ["BOT_TOKEN"]
token = (access_token)
mc = '699099967'
bot = telepot.Bot(token)

def btn_show(msg):
    btn1 = BT(text = "1. WALLET(월렛)", callback_data = "1")
    btn2 = BT(text = "2. 코인입금주소", callback_data = "2")
    btn3 = BT(text = "3. 공지", callback_data = "3")
    btn4 = BT(text = "4. 지갑", callback_data = "4")
    btn5 = BT(text = "5. ASTA", callback_data = "5")
    btn6 = BT(text = "6. MYCE", callback_data = "6")
    mu = MU(inline_keyboard = [[btn1, btn2],[btn3, btn4],[btn5, btn6]])
    bot.sendMessage(mc, "선택하세요", reply_markup = mu)

def query_ans(msg):
    btn7 = BT(text = "We-Fi wallet(위파이)", callback_data = "7")
    btn8 = BT(text = "Today-Wallet(투데이)", callback_data = "8")
    mu1 = MU(inline_keyboard = [[btn7, btn8]])
    btn9 = BT(text = "QR코드", callback_data = "9")
    btn10 = BT(text = "지갑주소", callback_data = "10")
    mu2 = MU(inline_keyboard = [[btn9, btn10]])
    query_data = msg["data"]
    if query_data == "1":
        bot.sendMessage(mc, "월렛을 선택하세요", reply_markup = mu1)  
    elif query_data == "2":
        bot.sendMessage(mc, "타입을 선택하세요", reply_markup = mu2) 
    elif query_data == "3":
        bot.sendMessage(mc, text = "무슨양식?")
    elif query_data == "4":
        bot.sendMessage(mc, text = "0x8f2d166eCF5742f77fEdb339dFd3dD20b91Bcc14")
    elif query_data == "5":
        bot.sendMessage(mc, text = "본부장님1,913,824")
    elif query_data == "6":
        bot.sendMessage(mc, text = "평단 2.2")
    elif query_data == "7":
        bot.sendMessage(mc, text= "http://wefi-financial.com 추천인코드 202101")
    elif query_data == "8":
        bot.sendMessage(mc, text = "http://today-wallet.com 추천인코드 202201")

        
access_token = os.environ["BOT_TOKEN"]
TOKEN = (access_token)
mc = '699099967'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': btn_show, "callback_query" : query_ans}).run_as_thread()

print('Listening ...')

while 1: 
    time.sleep(10)
    
# "5003695944:AAFOz4oy4Kpv9uCBy8SxNsmqBfgRddQHHd8" #
