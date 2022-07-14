from email.mime import image
import os
import time
from tkinter import Button
from tkinter.tix import ButtonBox
from unittest import result
from telegram import ChatAction
from telegram import InlineKeyboardButton as BT, InlineKeyboardMarkup as MU
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
 
TOKEN='5003695944:AAFOz4oy4Kpv9uCBy8SxNsmqBfgRddQHHd8'
 
updater = Updater( token=TOKEN, use_context=True )
dispatcher = updater.dispatcher
 
def cmd_task_buttons(update, context):
    
    btn1 = BT(text = "1. WALLET(월렛)", callback_data = "1")
    btn2 = BT(text = "2. 코인입금주소", callback_data = "2")
    btn3 = BT(text = "3. 공지", callback_data = "3")
    btn4 = BT(text = "4. 지갑", callback_data = "4")
    btn5 = BT(text = "5. ASTA", callback_data = "5")
    btn6 = BT(text = "6. MYCE", callback_data = "6")
    
    reply_markup = MU(inline_keyboard = [[btn1, btn2],[btn3, btn4],[btn5, btn6]] )
    
    context.bot.send_message(
        chat_id=update.message.chat_id
        , text='작업을 선택해주세요.'
        , reply_markup=reply_markup
    )
    
def cb_button(update, context):
    query = update.callback_query
    data = query.data
    
    context.bot.send_chat_action(
        chat_id=update.effective_user.id
        , action=ChatAction.TYPING
    )

    btn7 = BT(text = "We-Fi wallet(위파이)", callback_data = "7")
    btn8 = BT(text = "Today-Wallet(투데이)", callback_data = "8")
    btn80 = BT(text = "CANCEL", callback_data = "80")
    mu1 = MU(inline_keyboard = [[btn7, btn8],[btn80]])
    btn9 = BT(text = "QR코드", callback_data = "9")
    btn10 = BT(text = "지갑주소", callback_data = "10")
    btn90 = BT(text = "CANCEL", callback_data = "90")
    mu2 = MU(inline_keyboard = [[btn9, btn10],[btn90]])
    

    if data == '1':
        context.bot.edit_message_text(
            text="월렛을 선택하세요"
            , reply_markup = mu1
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )

    elif data == '7':
        context.bot.edit_message_text(
            text="http://wefi-financial.com 추천인코드 202101"
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )

    elif data == '8':
        context.bot.edit_message_text(
            text="http://today-wallet.com 추천인코드 202201"
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )

    elif data == '80':
        context.bot.edit_message_text(
        text='작업을 취소하였습니다.'.format( data )
        , chat_id=query.message.chat_id
        , message_id=query.message.message_id
        
        )
            

    elif data == '2':
        context.bot.edit_message_text(
            text="입금주소 방식을 선택하세요_WORKIT(워킷)"
            , reply_markup = mu2
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )

    elif data == '9':
        context.bot.send_photo(
            chat_id=query.message.chat_id
            , photo=open(r'C:\Users\spero\OneDrive\바탕 화면\python\qrcode.png','rb')
        )


    elif data == '10':
        context.bot.edit_message_text(
            text="0x2d2a2b7c29feb628f4da5b4e06ba01b86ffe6c51"
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )

    
    elif data == '90':
        context.bot.edit_message_text(
        text='작업을 취소하였습니다.'.format( data )
        , chat_id=query.message.chat_id
        , message_id=query.message.message_id
        
        )


    
    
task_buttons_handler = CommandHandler( 'kdax', cmd_task_buttons )
button_callback_handler = CallbackQueryHandler( cb_button )    
 
dispatcher.add_handler( task_buttons_handler )
dispatcher.add_handler( button_callback_handler )
 
updater.start_polling()
updater.idle()

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)