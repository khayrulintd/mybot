from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename="bot.log"
                    )

def greet_user(bot, update):
    print('Вызван /старт')
    logging.info("Вызван /старт")
    text = ('Привет, Юзернейм')
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    logging.info("talk_to_me")
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater("822102958:AAHsgSxtLNp1FHMFXih30Rkpkx4DHFsvsFU", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    logging.info("Вызван /старт")
    mybot.idle()

main()