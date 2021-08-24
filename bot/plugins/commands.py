#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@cv_updatez"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝙐𝙥𝙙𝙖𝙩𝙚 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭  നിങ്ങൾക് സിനിമകൾ വെന്നോ? അതിനായി അത്യം ങ്ങളുടെ മെയിൻ ചാനലിൽ ജോയിൻ ചെയ്യണം... 😁  Join ചെയതത്തിനു ശേഷം വീണ്ടും ബോട്ട് /start ആക്കൂ.😁 </b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 🔰JOIN OUR UPDATE CHANNEL🔰 ", url=f"https://t.me/cv_updatez")]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'ɴᴇᴡ ᴍᴏᴠɪᴇꜱ', url="https://t.me/joinchat/nO3dDangBz81N2Q1"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('🗣️ɢʀᴏᴜᴘ', url='https://t.me/Cinema_Beacon_Group'),
        InlineKeyboardButton('📺ᴄʜᴀɴɴᴇʟ', url ='https://t.me/CB_PSARIPS2')
    ],[
        InlineKeyboardButton('📌ᴄʀᴇᴀᴛᴏʀ', url='https://t.me/Cv_groupAdmin2')
    ],[
        InlineKeyboardButton('📦 ᴊᴏɪɴ', url="https://t.me/cb_psarips1")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph//file/53b667116e3ee6b0249e5.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home 🏃‍♂️', callback_data='start'),
        InlineKeyboardButton('About 🗞️', callback_data='about')
    ],[
        InlineKeyboardButton('Close ❌️', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
       
  await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
  await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
