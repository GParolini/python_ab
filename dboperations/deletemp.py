import mysql.connector;

def delete(id):
    conn = mysql.connector.connect(host = 'localhost', database ='mydb', user='root', password = "xxx")

    if conn.is_connected():
        print("Connected to mysql db")
        cursor = conn.cursor()
        str = "delete from emp where id ='%d'"
        args = (id)
        try:
            cursor.execute(str % args)
            conn.commit()
            print("Employee deleted")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

empID = int(input('Enter Emp id:'))
delete(empID)
