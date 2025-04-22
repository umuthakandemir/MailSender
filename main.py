import os.path

from Modules import mail_sender
import argparse
class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="emil göndermek için parametre")
        self.parser.add_argument("-o", "--options", type=str, help="anlaşılır menu kullanımı için -o menu veya --options menu yazın.")
        self.parser.add_argument("-l", "--list", type=str, help="email listesi yolu. Satır satır okunacaktır.")
        self.parser.add_argument("-p", "--password",type=str,help="email hesabınızın şifresi")
        self.parser.add_argument("-t", "--to", type=str, help="tekli veya çoklu gönderim(,) ile ayırın -e xyz@xyz.com, zyx@zyx.com or --email xyz@xyz.com, zyx@zyx.com")
        self.parser.add_argument("-m", "--message", type=str, help="emailin içeriğği")
        self.parser.add_argument("-s", "--subject", type=str, help="emailin konusu")
        self.parser.add_argument("-f", "--from_email", type=str, help="Sizin email hesabınız. xyz@xyz.com ")
        self.parser.add_argument("-c", "--file", type=str, help="emaile ekstra içerik elkleme. Dosya yolu")
        self.args = self.parser.parse_args()

    def check_args(self):
        args = self.args
        if args.options == "menu":
            from Modules import Menu
            obj1 = Menu.Menu()
            while obj1.durum:
                obj1.show_options()
        else:
            if args.from_email and args.password and args.to and args.subject and args.subject:
                email_list = [e.strip() for e in args.to.split(",")]
                sender = mail_sender.Send_Mail(
                    args.from_email,
                    args.password,
                    email_list,
                    args.subject,
                    args.message,
                    file=args.file
                )
                sender.send()
                print(email_list)
            elif args.from_email and args.password and args.subject and args.subject and args.list and os.path.exists(args.list):
                with open(args.list,"r") as email_list:
                    emails = tuple(line.split() for line in email_list.readlines())
                    sender = mail_sender.Send_Mail(
                        args.from_email,
                        args.password,
                        emails,
                        args.subject,
                        args.message,
                        file=args.file
                    )
                    sender.send()
                    print(emails)
            else:
                print("Kimden, kime, konu ve mesaj zorunludur. -f -t -s -m parametrelerini kontrol edin.")
if __name__=="__main__":
    CLI().check_args()
