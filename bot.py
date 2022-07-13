from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from data import chapter_one

import os
from dotenv import load_dotenv

load_dotenv()

updater = Updater(token=os.getenv('token'))

current_algo_index = 0


def menu_keyboard():
    return ReplyKeyboardMarkup([
        [KeyboardButton('Chapter 1'), KeyboardButton('Chapter 2'), KeyboardButton('Chapter 3')],
        [KeyboardButton('Chapter 4'), KeyboardButton('Chapter 5'), KeyboardButton('Chapter 6')],
    ], resize_keyboard=True, one_time_keyboard=True)


def submenu_keyboard():
    return ReplyKeyboardMarkup([
        [KeyboardButton('Previous'), KeyboardButton('Next')],
    ], resize_keyboard=True, one_time_keyboard=True)


def start_handle(update: Update, context: CallbackContext):
    global current_algo_index
    current_algo_index = 0
    update.message.reply_text(f'Hello {update.effective_user.first_name}🖖\n\n'
                              f'Welcome to the community of engineers who love algorithms and data structure.\n\n'
                              f'Here below you can see our roadmap to start solving problems ⬇️',
                              reply_markup=menu_keyboard())


def chapter_one_handle(update: Update, context: CallbackContext):
    update.message.reply_text(f"🟢 Name: {chapter_one[current_algo_index]['name']}\n"
                              f"⚙️ Level: {chapter_one[current_algo_index]['level']}\n"
                              f"📄 Topics: {''.join(chapter_one[current_algo_index]['topics'])}\n"
                              f"🔗 Link: {chapter_one[current_algo_index]['link']}",
                              reply_markup=submenu_keyboard())


def next_handle(update: Update, context: CallbackContext):
    global current_algo_index
    current_algo_index += 1

    if len(chapter_one) == current_algo_index:
        current_algo_index -= 1

    update.message.reply_text(f"🟢 Name: {chapter_one[current_algo_index]['name']}\n"
                              f"⚙️ Level: {chapter_one[current_algo_index]['level']}\n"
                              f"📄 Topics: {''.join(chapter_one[current_algo_index]['topics'])}\n"
                              f"🔗 Link: {chapter_one[current_algo_index]['link']}",
                              reply_markup=submenu_keyboard())


def prev_handle(update: Update, context: CallbackContext):
    global current_algo_index

    if current_algo_index != 0:
        current_algo_index -= 1

    update.message.reply_text(f"🟢 Name: {chapter_one[current_algo_index]['name']}\n"
                              f"⚙️ Level: {chapter_one[current_algo_index]['level']}\n"
                              f"📄 Topics: {''.join(chapter_one[current_algo_index]['topics'])}\n"
                              f"🔗 Link: {chapter_one[current_algo_index]['link']}",
                              reply_markup=submenu_keyboard())


# Sample for context:
# def location_handle(update: Update, context: CallbackContext):
#     context.bot.send_location(chat_id=update.effective_user.id, latitude=51.121, longitude=22.1341)


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_handle))
# dispatcher.add_handler(MessageHandler(Filters.text('Manzil'), location_handle))
dispatcher.add_handler(MessageHandler(Filters.text('Chapter 1'), chapter_one_handle))
dispatcher.add_handler(MessageHandler(Filters.text('Next'), next_handle))
dispatcher.add_handler(MessageHandler(Filters.text('Previous'), prev_handle))
dispatcher.add_handler(MessageHandler(Filters.all, start_handle))

updater.start_polling()
updater.idle()
