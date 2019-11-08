import mysql.connector;

def update(id, salary):
    conn = mysql.connector.connect(host = 'localhost', database ='mydb', user='root', password = "xxx")

    if conn.is_connected():
        print("Connected to mysql db")
        cursor = conn.cursor()
        str = "update emp set sal='%d' where id ='%d'"
        args = (salary, id)
        try:
            cursor.execute(str % args)
            conn.commit()
            print("Salary updated")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


empID = int(input('Enter Emp id:'))
newsal = int(input("Enter new salary:"))
update(empID, newsal)
