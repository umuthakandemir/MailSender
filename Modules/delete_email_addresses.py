import sqlite3
def delete_address(*address_list):
    db = sqlite3.connect("email_db.db")
    cursor = db.cursor()
    for address in address_list:
        cursor.execute("DELETE FROM email WHERE email=?;", (address,))
        print(f"{address} başarıyla silindi.")
    db.commit()
    cursor.close()
    db.close()

def delete_All_address():
    db = sqlite3.connect("email_db.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM email ;")
    print("Tamamı başarıyla silindi.")
    db.commit()
    cursor.close()
    db.close()

