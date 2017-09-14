#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to send random images to Telegram messages.
# This program is dedicated to the public domain under the MIT license.
import config
from ImgUrls import ImgUrls
import telebot
from telebot import types

def main():

    imgUrls = ImgUrls()

    # Telegram Bot Authorization Token
    bot = telebot.TeleBot(config.token)

    @bot.message_handler(commands=['start'])
    def send_cat(message):
        # bot.send_message(message.chat.id, "Cat")
        bot.send_message(message.chat.id, 'Hello, I\'am bot, who can send a random photo girl or cats:) Write me /girl or /cat')

    @bot.message_handler(commands=['cat', 'Cat'])
    def send_cat(message):
        # bot.send_message(message.chat.id, "Cat")
        bot.send_photo(message.chat.id, imgUrls.getImgUrl('cats'))

    @bot.message_handler(commands=['girl', 'Girl'])
    def send_girl(message):
        bot.send_message(message.chat.id, imgUrls.getImgUrl('girls'))

    bot.polling()


if __name__ == '__main__':
    main()