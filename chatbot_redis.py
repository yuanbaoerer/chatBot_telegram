from telegram import Update
from telegram.ext import (Updater, CommandHandler,MessageHandler,Filters,CallbackContext)

import configparser
import logging
import redis

global redis1
def main():
    # Load token and create an Updater for the bot
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    global redis1
    redis1 = redis.Redis(host=(config['REDIS']['HOST'])
                         , port=(config['REDIS']['REDIS_PORT'])
                         , password=(config['REDIS']['PASSWORD'])
                         , decode_responses=(config['REDIS']['DECODE_RESPONSE'])
                         , username=(config['REDIS']['USER_NAME']))
    # set logging module
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

    # register a dispatcher to handle message: here we register an echo dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("add",add))
    dispatcher.add_handler(CommandHandler("help",help_command))
    #start the bot:
    updater.start_polling()
    updater.idle()

def echo(update, context):
    reply_message = update.message.text.upper()
    logging.info("Update: "+str(update))
    logging.info("Context: "+str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)

'''
define a few command handlers. These usually take the two arguments update and 
context. Error handlers also receive the raised TelegramError object in error.
'''
def help_command(update: Update, context: CallbackContext) -> None:
    '''Send a message when the command /help is issued.'''
    update.message.reply_text('Help!')

def add(update: Update, context: CallbackContext) -> None:
    '''Send a message when the command /add is issued.'''
    try:
        global redis1
        logging.info(context.args[0])
        msg = context.args[0] # /add keyword <-- this should store the keyword

        redis1.incr(msg)

        # 从 Redis 数据库中获取该关键词对应的值，并将其解码为字符串
        count_str = redis1.get(msg)
        # 构造回复消息，告知用户该关键词被提及的次数
        update.message.reply_text(f'You have said {msg} for {count_str} times.')
        #
        # update.message.reply_text('You have said ' + msg + ' for '+ redis1.get(msg).decode('UTF-8') + ' times.')
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <keyword>')

if __name__ == '__main__':
    main()
