
import mysql.connector as db
import pandas as pd

class connectivity:
    def __init__(self):
        mydb = db.connect(host = "localhost", user = "root", password = "c0d3r123")
        cur = mydb.cursor()
        query = '''create database if not exists rohan;'''
        cur.execute(query)
        cur.execute("commit;")
        mydb.close()
    def create_table(self):
        mydb = db.connect(host = "localhost", user = "root", password = "c0d3r123", database = "rohan")
        cur = mydb.cursor()
        query = '''create table school(roll_no int,name varchar(30),contact bigint,loc varchar(30))'''
        cur.execute(query)
        cur.execute("commit;")
        mydb.close()
        return "Table Created"
    def insert_values(self,roll_no,name,contact,loc):
        mydb = db.connect(host = "localhost", user = "root" ,password = "c0d3r123",database = "rohan")
        cur = mydb.cursor()
        query = f'''insert into school(roll_no,name,contact,loc)values({roll_no},"{name}",{contact},"{loc}")'''
        cur.execute(query)
        cur.execute("commit;")
        mydb.close()
        return "value inserted"
    def update_value(self,location,roll_no):
        mydb = db.connect(host = "localhost",user = "root",password = "c0d3r123",database = "rohan")
        cur = mydb.cursor()
        query = f'''update school set loc = "{location}" where roll_no = {roll_no};'''
        cur.execute(query)
        cur.execute("commit;")
        mydb.close()
        return "Location Updated"
    def access_info(self):
        mydb = db.connect(host = "localhost",user = "root",password = "c0d3r123", database = "rohan")
        cur = mydb.cursor()
        query = '''select * from school;'''
        cur.execute(query)
        data = cur.fetchall()
        mydb.close()
        return data

if __name__ == "__main__":
    
    app = connectivity()
    print(app.access_info()[0])

    # print(app.create_table())


    # insert value


    # roll_no = int(input("Enter Your Roll number : "))
    # name = input("Enter The Name : ")
    # contact = int(input("Enter Your contact number : "))
    # loc = input("Enter your location : ")
    
    # print(app.insert_values(roll_no,name,contact,loc))


    # update value

    # roll_no = int(input("Enter the roll number : "))
    # location = input("Enter the new location : ")
    # print(app.update_value(location,roll_no))




    # Access Info


    # info = app.access_info()
    # print(info)
    # a,b,c,d = zip(*info)
    # print(a)
    # print(b)
    # print(c)
    # print(d)

    # df = pd.DataFrame(info,columns = ["roll_no", "name" ,"contact","location"])
    # print(df)
'''
    create table order1(o_id int unique not null auto_increment,order varchar(30),order_no int auto_increment,amount int,date_time datetime,c_id int,primary key (o_id),foreign key(c_id) references customer1(c_id));   
    '''