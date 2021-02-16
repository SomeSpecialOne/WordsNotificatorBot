import sqlite3
import time
import random

from loader import bot

db = sqlite3.connect('dictionaryENG-RUS.db')

stickers_good_night = [
    "CAACAgIAAxkBAAIbL2Aq2MicAAFcuIXYQJlHgUmBmJN1cgACbAUAAj-VzAqM14T6d4Dvfh4E",
    "CAACAgIAAxkBAAIbMWAq2dz5Fdga0iMxkMI8zbK2rCe8AAINBwACRvusBN8Cnez2hqJjHgQ",
    "CAACAgIAAxkBAAIbMmAq2et7zXydMsnwHU0F2U_SN93PAAIkCQACGELuCHBUENT4WrkWHgQ",
    "CAACAgIAAxkBAAIbM2Aq2fBKG-NpRtxIG38MFs783cssAAJZAgACVp29Cg8vC9H6xdhQHgQ",
    "CAACAgIAAxkBAAIbNGAq2fI1y6kT2L3w3dOHqH07ccF5AALuAgACtXHaBoqPS1j4HCdTHgQ",
    "CAACAgIAAxkBAAIbNWAq2fRa19da37d0LtPtkDJ6lUEAA94CAALz474LyKdCKmKTwW4eBA",
    "CAACAgIAAxkBAAIbNmAq2fpo03SURUShRM5OFV5Gwk1-AAKtAQACVp29Cp3wQF4LF9WgHgQ",
    "CAACAgIAAxkBAAIbN2Aq2gH6BK1aTbIwfXA8hTKQasZkAAJDAAOtZbwU_-iXZG7hfLseBA",
    "CAACAgIAAxkBAAIbOGAq2gZtuO1AIiXLWc3mWEuY1_hQAAIwAQACMNSdESHpeB_6BbiqHgQ",
    "CAACAgIAAxkBAAIbOWAq2hnEnUb2Os93tw7lt9SRMKmkAAKKBQAC-gu2CI_Pbhb6Txq1HgQ",
    "CAACAgIAAxkBAAIbOmAq2jTomMdIqnwsVfLhNU_cGMvEAAI5AAOvxlEaqBfSb56eXbQeBA",
    "CAACAgIAAxkBAAIbO2Aq2kEpnmU2hIgd_4__ietQ2YUJAAKKAAMWQmsKT4OpWS5wU_4eBA",
    "CAACAgIAAxkBAAIbPGAq2kyMJjBQFvlPWnPAXK6JGmiIAAI5AANZu_wlNOHiKh4gqp0eBA",
    "CAACAgIAAxkBAAIbPWAq2lFs85BlwO5x4jk1_bVGWXrDAAJ6AAOmysgMVHaw3_p6rtseBA",
    "CAACAgIAAxkBAAIbPmAq2nLiJ4RXOBvuSBji0akv0LAkAAJKAwACbbBCA4xyA8CaotsVHgQ"
]

stickers_good_morning = [
    "CAACAgIAAxkBAAIbP2Aq283vLmD8Q1qoC2f6NhafOxRjAAKaAAP3AsgP0dUG8v161DgeBA"
    "CAACAgIAAxkBAAIbQGAq29GNRTbOC7AXPgAB1a3CzL6_yAACEQMAAvPjvgsZbp8lnswsJB4E"
    "CAACAgIAAxkBAAIbQWAq29Q39TJyVTOUUQRpM1to_azNAAIeCQACGELuCPlY2e4dIZwhHgQ"
    "CAACAgIAAxkBAAIbQmAq29vYYXNJdRYooNKNoD2F6QABSQACVQIAAladvQqsSyyCT6MV3x4E"
    "CAACAgIAAxkBAAIbQ2Aq2-mOT94OsuDY4PEvZ3Wahw06AAIEBwACRvusBEPY1ijiqT2DHgQ"
    "CAACAgIAAxkBAAIbRGAq2_FmveURmfaJ_zOjd-sV7v9HAAJdAANEDc8Xx77nXM4YAjweBA"
    "CAACAgIAAxkBAAIbRWAq2_MTC9tDbxHQIPy2gijDYRgSAAJBAAOvxlEakmwMdNAnIj4eBA"
    "CAACAgIAAxkBAAIbRmAq2_ay6mGWxELH072OQHRJLDiwAAJuBQACP5XMCoY62V2IvLc1HgQ"
    "CAACAgEAAxkBAAIbR2Aq2_2gHPbDLlp7OL7MTHL4e6dbAAIPAQACOA6CEbXMTX_iFJGCHgQ"
    "CAACAgIAAxkBAAIbSGAq3AiVwPFMfmxsx0OmHoQVE3ozAAKSAQACVp29Cp_QLQhCLtUFHgQ"
    "CAACAgIAAxkBAAIbSWAq3At42p5z5A2TjcEjRJp6RBYiAAJcAANZu_wlj1s_8uLbhRAeBA"
    "CAACAgIAAxkBAAIbSmAq3B3Y6igPhu_StA5sspQw4lQcAAKCAAOmysgMnFoH8pxBBGceBA"
    "CAACAgIAAxkBAAIbS2Aq3C-fBSFgDDRg3vyWdDnVT1bTAAIcAAP3AsgPcBxyLW2TGHgeBA"
    "CAACAgIAAxkBAAIbTGAq3Dd2PXrSCs4Xetari0lWjhogAAJuAAPANk8TbYftSrN4mZceBA"
]


class User:
    def __init__(self, id: int, first_name: str, time_zone: int,
                 sleep_from: int, sleep_to: int, period: int, word):
        self.id = id
        self.first_name = first_name
        self.time_zone = time_zone
        self.sleep_from = sleep_from
        self.sleep_to = sleep_to
        self.period = period

        self.word = word

    class Word:
        def __init__(self, id: int, word: str, translation: str, context_en, context_ru: str):
            self.id = id
            self.word = word
            self.translation = translation
            self.context_en = context_en
            self.context_ru = context_ru


class Notificator:
    """
    Main functions
    """
    def __init__(self, period: int):
        """
        Getting all users and words
        """
        sql = db.cursor()
        sql.execute(f'''SELECT [User_id], [First_name], [Time_zone], [Sleep_from], 
                        [Sleep_to] FROM Users WHERE [Period] == {period};''')
        ans = sql.fetchall()
        self.users = []
        if ans:
            for tup in ans:
                sql.execute(f'''SELECT [Word_id] FROM [{tup[0]}] WHERE [Notificated] == 0
                                ORDER BY random() LIMIT 1;''')
                word_id = sql.fetchone()[0]
                sql.execute(f'''SELECT [Word], [Translation], [ContextEN], [ContextRU] FROM ENGRUS WHERE [ID] == {word_id};''')
                word_tup = sql.fetchone()
                word = User.Word(word_id, word_tup[0], word_tup[1], word_tup[2], word_tup[3])
                user = User(tup[0], tup[1], tup[2], tup[3], tup[4], period, word)
                self.users.append(user)
                sql.execute(f'''UPDATE [{tup[0]}] SET [Notificated] = 1 WHERE [Word_id] == {word_id};''')
            db.commit()
        sql.close()

    async def start(self):
        """
        Start sending
        """
        for user in self.users:
            current_hour = time.gmtime(time.time() + (3600 * user.time_zone)).tm_hour
            if user.period == 3600:
                if self.time_check(user) is True:
                    if current_hour == user.sleep_from:
                        try:
                            await bot.send_sticker(chat_id=user.id, sticker=random.choice(stickers_good_night))
                        except Exception as e:
                            self.logging(e, user)
                    elif current_hour == user.sleep_to:
                        try:
                            await bot.send_sticker(chat_id=user.id, sticker=random.choice(stickers_good_morning))
                        except Exception as e:
                            self.logging(e, user)
                    msg_word = f'<b>{user.word.word}</b> 🇬🇧 - <b>{user.word.translation}</b> 🇷🇺'
                    msg_context = f'{user.word.context_en} 🇬🇧\n' \
                                  f'{user.word.context_ru} 🇷🇺'
                    msg_context = msg_context.replace(user.word.word, f'<b>{user.word.word}</b>')\
                        .replace(user.word.translation, f'<b>{user.word.translation}</b>')
                    try:
                        await bot.send_message(chat_id=user.id, text=msg_word, parse_mode='HTML')
                        await bot.send_message(chat_id=user.id, text=msg_context, parse_mode='HTML')
                    except Exception as e:
                        self.logging(e, user)

            elif user.period == 7200:
                if self.time_check(user) is True:
                    if (user.sleep_to - current_hour) % 2 == 0:
                        if current_hour == user.sleep_from:
                            try:
                                await bot.send_sticker(chat_id=user.id, sticker=random.choice(stickers_good_night))
                            except Exception as e:
                                self.logging(e, user)
                        elif current_hour == user.sleep_to:
                            try:
                                await bot.send_sticker(chat_id=user.id, sticker=random.choice(stickers_good_morning))
                            except Exception as e:
                                self.logging(e, user)
                        msg_word = f'<b>{user.word.word}</b> 🇬🇧 - <b>{user.word.translation}</b> 🇷🇺'
                        msg_context = f'{user.word.context_en} 🇬🇧\n' \
                                      f'{user.word.context_ru} 🇷🇺'
                        msg_context = msg_context.replace(user.word.word, f'<b>{user.word.word}</b>') \
                            .replace(user.word.translation, f'<b>{user.word.translation}</b>')
                        try:
                            await bot.send_message(chat_id=user.id, text=msg_word, parse_mode='HTML')
                            await bot.send_message(chat_id=user.id, text=msg_context, parse_mode='HTML')
                        except Exception as e:
                            self.logging(e, user)

            elif user.period == 10800:
                if self.time_check(user) is True:
                    if (user.sleep_to - current_hour) % 3 == 0:
                        if current_hour == user.sleep_from:
                            try:
                                await bot.send_sticker(chat_id=user.id, sticker=random.choice(stickers_good_night))
                            except Exception as e:
                                self.logging(e, user)
                        elif current_hour == user.sleep_to:
                            try:
                                await bot.send_sticker(chat_id=user.id, sticker=random.choice(stickers_good_morning))
                            except Exception as e:
                                self.logging(e, user)
                        msg_word = f'<b>{user.word.word}</b> 🇬🇧 - <b>{user.word.translation}</b> 🇷🇺'
                        msg_context = f'{user.word.context_en} 🇬🇧\n' \
                                      f'{user.word.context_ru} 🇷🇺'
                        msg_context = msg_context.replace(user.word.word, f'<b>{user.word.word}</b>') \
                            .replace(user.word.translation, f'<b>{user.word.translation}</b>')
                        try:
                            await bot.send_message(chat_id=user.id, text=msg_word, parse_mode='HTML')
                            await bot.send_message(chat_id=user.id, text=msg_context, parse_mode='HTML')
                        except Exception as e:
                            self.logging(e, user)

    @staticmethod
    def time_check(user: User) -> bool:
        """
        Checking if current time is True or False to send message
        """
        current_hour = time.gmtime(time.time() + (3600 * user.time_zone)).tm_hour
        if user.sleep_from > user.sleep_to:
            if current_hour in range(user.sleep_to, user.sleep_from + 1):
                return True
            else:
                return False
        else:
            if current_hour not in range(user.sleep_from + 1, user.sleep_to):
                return True
            else:
                return False

    @staticmethod
    def logging(text: Exception, user: User):
        with open('logs.txt', 'a') as logs:
            logs.write(f'[{time.strftime("%H:%M", time.gmtime(time.time() + (3600 * 3)))}] {text} for {user.first_name} [{user.sleep_from}-{user.sleep_to}, {user.period}]\n')




        

