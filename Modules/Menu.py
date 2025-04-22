from Modules import save_mails
from Modules import delete_email_addresses as del_address
from Modules import mail_sender
import sqlite3

class Menu:
    def __init__(self):
        self.durum = True
    def send_mail(self):
        print("""
        1-2 arasında seçim yapın
        
        1-Eposta adreslerini ben gireceğim.
        2-eposta adreslerini veritabanı'ndan çek""")

        option = self.user_choice()
        from_email = input("E posta adresiniz")
        password = input("Şifreniz")
        subject = input("konu: ")
        message = input("mesaj: ")
        file_path = input("Dosya eklemek istersen(boş bırakabilirsin), dosya yolu: ")

        if option == 1:
            to = input("eposta adresi gir. örn xyz@xyz.com veya çoklu gönderim (,) ile ayır")
            email_list = [e.strip() for e in to.split(",")]
            print(type(email_list))
            sender = mail_sender.Send_Mail(
                from_email,
                password,
                email_list,
                subject,
                message,
                file=file_path
            )
            sender.send()
        elif option == 2:
            email_addresses = self.get_email_addresses()
            sender = mail_sender.Send_Mail(
                from_email,
                password,
                email_addresses,
                subject,
                message,
                file=file_path
            )
            sender.send()
            print(type(email_addresses))

    def save_mail_address(self):
        user_email_address = input("Aralarında virgül (,) ile epostaları ayırarak veya tek bir eposta girerek işlemi başlatın.:")
        email_list = tuple(user_email_address.split(","))
        func = save_mails.save_email_address()
        func.add_email(*email_list)

    def delete_mail_addres(self):
        print("""
        1-tablonun tamamını sil
        2-email girerek sil""")
        option = self.user_choice()
        if option == 1:
            del_address.delete_All_address()
        elif option == 2:
            user_email_address = input("Aralarında virgül (,) ile epostaları ayırarak veya tek bir eposta girerek işlemi başlatın.:")
            email_list = tuple(user_email_address.split(","))
            del_address.delete_address(*email_list)

    def exit_app(self):
        self.durum = False
        print("güle güle")

    def show_options(self):
        print("""
        1-4 arasında seçim yapın.
        1-mail gönder
        2-mail adresi kaydet
        3-mail adresi sil
        4-kayıtlı maiiler
        5-çık
        """)
        self.check_user_choice()

    def user_choice(self):
        choice = int(input("Seçiminiz.:"))
        return choice

    def check_user_choice(self):
        option = self.user_choice()
        if option == 1:
            self.send_mail()
        elif option == 2:
            self.save_mail_address()
        elif option == 3:
            self.delete_mail_addres()
        elif option == 4:
            mail_addresses = self.get_email_addresses()
            [print(email) for email in mail_addresses]
        elif open() == 5:
            self.exit_app()

    def get_email_addresses(self):
        db = sqlite3.connect("email_db.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM email")
        data = cursor.fetchall()
        emails = [d[1] for d in data]
        cursor.close()
        db.close()
        return emails

