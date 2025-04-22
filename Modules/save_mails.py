import sqlite3

class save_email_address:
    def __init__(self):
        self.create_db_table()
    def create_db_table(self):
        db = sqlite3.connect("email_db.db")
        cursor = db.cursor()
        #CREATE TABLE
        cursor.execute("""CREATE TABLE IF NOT EXISTS email (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL
        );""")
        cursor.close()
        db.commit()
        db.close()

    def add_email(self,*emails):
        db = sqlite3.connect("email_db.db")
        cursor = db.cursor()
        for email in emails:
            cursor.execute("INSERT INTO email(email) VALUES (?);",(email,))
            print(f"{email} başarıyla veri tabanına eklendi")
        db.commit()
        cursor.close()
        db.close()




