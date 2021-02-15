import time
from loader import db


class User:

    def __init__(self, chat_id: int, first_name: str, last_name: str, username: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.id = chat_id
        self.time_zone = 0
        self.sleep_from = 0
        self.sleep_to = 0
        self.period = 0

    def create_user(self):
        """
        Save user to db
        """
        sql = db.cursor()
        sql.execute('''SELECT COUNT() FROM ENGRUS''')
        end = sql.fetchone()[0]
        sql.execute('''INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?, ?);''',
                    (self.id, self.first_name, self.last_name, self, 1, 3, 0, 0, 0))
        sql.execute(f'''CREATE TABLE IF NOT EXISTS [{self.id}] 
                        (Word_id INTEGER PRIMARY KEY ON CONFLICT REPLACE,
                        Notificated BOOLEAN);''')

        for i in range(1, end + 1):
            sql.execute(f'''INSERT INTO [{self.id}] VALUES (?, ?);''', (i, 0))
        db.commit()
        sql.close()

    def update_time_zone(self, time_zone: int):
        self.time_zone = time_zone

    def update_time_sleep_from(self, sleep_from: int):
        self.sleep_from = sleep_from

    def update_time_sleep_to(self, sleep_to: int):
        self.sleep_to = sleep_to

    def update_period(self, period: int):
        self.period = period

    def save_settings(self):
        sql = db.cursor()
        sql.execute(f'''UPDATE Users SET [Time_zone] = {self.time_zone}, [Period] = {self.period}, 
                        [Sleep_from] = {self.sleep_from}, [Sleep_to] = {self.sleep_to}, 
                        [Period] = {self.period} WHERE [User_id] == {self.id};''')
        db.commit()
        sql.close()

    def get_time_to_send(self) -> str:
        time_to_send = time.gmtime(time.time() + (3600 * (self.time_zone + 1)))  # nearest hour
        if self.sleep_from > self.sleep_to:  # from 21,22, or 23 to 6,7,8 or 9
            if time_to_send.tm_hour in range(self.sleep_to + 1, self.sleep_from + 1):
                return time.strftime("%H:00", time_to_send)
            else:
                return f'0{self.sleep_to}:00\nСпокойной ночи ✨'
        else:  # for 00:00 to ...
            if time_to_send.tm_hour not in range(self.sleep_from + 1, self.sleep_to + 1):
                return time.strftime("%H:00", time_to_send)
            else:
                return f'0{self.sleep_to}:00\nСпокойной ночи ✨'

    def get_current_time(self):
        current_time = time.strftime("%H:%M", time.gmtime(time.time() + (self.time_zone * 3600)))
        return current_time

    def off_on(self, val: int):
        sql = db.cursor()
        sql.execute(f'''UPDATE Users SET [On] = {val} WHERE [User_id] == {self.id};''')
        db.commit()
        sql.close()
