import smtplib
from email.message import EmailMessage

class Send_Mail:
    def __init__(self,email,password,to,subject,message,file=None):
        self.email = email
        self.password = password
        self.to = to
        self.subject = subject
        self.message = message
        self.file = file

    def send(self):
        try:
            # Gönderme
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(self.email, self.password)
                # Dosya ekle (isteğe bağlı)

                for address in self.to:
                    print(address,"adresine mail gönderiliyor..")
                    msg = EmailMessage()
                    msg["Subject"] = self.subject
                    msg["From"] = self.email
                    msg["To"] = address
                    msg.set_content(self.message)
                    if self.file:
                        import mimetypes, os
                        with open(self.file, 'rb') as f:
                            mime_type, _ = mimetypes.guess_type(self.file)
                            maintype, subtype = mime_type.split('/') if mime_type else ('application', 'octet-stream')
                            msg.add_attachment(f.read(), maintype=maintype, subtype=subtype,
                                           filename=os.path.basename(self.file))
                    smtp.send_message(msg)
                    print("E-posta gönderildi.")

        except Exception as e:
            print(f"Hata olustu eposta gönderilmedi.Hata: {e}")