from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}
This is String Session Generator Bot

If you don't trust this bot, 
1) Stop reading this message
2) Delete this chat

Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

Made With ❤ By @TeleRoidGroup.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🍃 Session String Process 🍃", callback_data="generate")],
        [InlineKeyboardButton(text="🏡 Home ", callback_data="home")],
        [
            InlineKeyboardButton("🤖 BotsList 🤖", url="https://t.me/joinchat/t1ko_FOJxhFiOThl")
        ]
    ]

    generate_button = [
        [InlineKeyboardButton(" Start Session String Process", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Updates Channel", url="https://t.me/TeleRoidGroup")],
        [InlineKeyboardButton("Support Group", url="https://t.me/TeleRoid14")],
        [
            InlineKeyboardButton("♻ Help", callback_data="help"),
            InlineKeyboardButton("🛡 About", callback_data="about")
        ],
        [InlineKeyboardButton("🍃 Session String 🍃", callback_data="generate")],
    ]

    # Help Message
    HELP = """
**How to Use the Bot and The Available Commands**
start - Start the Bot
/about - About The Bot
/help - This Message
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
╭────[🔅Session Bot🔅]───⍟
│
├<b>🤖 Bot Name : <a href='https://t.me/TeleRoidSessionBot'>@TeleRoidSessionBot</a></b>
│
├<b>📢 Channel : <a href='https://t.me/TeleRoidGroup'>@TeleRoidGroup</a></b>
│
├<b>👥 Version : <a href='https://t.me/TeleRoidSessionBot'>0.9.2 beta</a></b>
│
├<b>💢 Source : <a href='https://github.com/PredatorHackerzZ'>Click Here</a></b>
│
├<b>🌐 Server : <a href='https://heroku.com'>Heroku</a></b>
│
├<b>📕 Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>
│
├<b>㊙ Language: <a href='https://www.python.org'>Python 3.9.4</a></b>
│
├<b>👨‍💻 Developer : <a href='https://t.me/PredatorHackerZ'>@Pred∆tor</a></b>
│
├<b>🚸 Powered By : <a href='https://t.me/Moviesflixers_DL'>@HindiWebNetwork</a></b>
│
╰──────[Thanks 😊]───⍟
    """
