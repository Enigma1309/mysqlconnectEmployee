from connection import connect


def convmd5(string):
    import hashlib
    password = hashlib.md5(string.encode('utf-8')).hexdigest()
    return password



mydb = connect()
mycur = mydb.cursor()

def AddEmployee():
    ch = 'y' 
    while ch.lower() != 'n':
        empid = int(input("Enter the employee id: "))
        name = input('Enter employee name: ')
        age = int(input("Enter employee age: "))
        mob_no = int(input("Enter mobile number: "))
        gender = input("Enter the gender (M/F): ")
        fname = input("Enter the father's name: ")
        mname = input ("Enter the mother's name: ")
        salary = int(input("Enter the employee salary: "))
        password = input("Enter the password: ")
        password= convmd5(password)    
        query = "INSERT INTO  empdata values ({},'{}',{},'{}','{}','{}','{}',{},'{}')".format(empid,name,age,mob_no,gender,fname,mname,salary,password)
        mycur.execute(query)
        mydb.commit()
        print("Sucessfully added the data into employee table")

        ch = input("Do you want to add more data ? (y/n): ")

def showemployee(empid,passwd):
    passwd = convmd5(passwd)
    print('Showing the employee details of id:',empid)
    query = "SELECT * from empdata where id = {} and password = '{}'".format(empid,passwd)
    mycur.execute(query)
    print('\n\n')
    print(mycur.fetchall())

def main():

    print('''
    Choose the following opitions:
    1) Add Employee info
    2) Show employee info (by id)
    3) Show all employee info
    4) Exit
    ''')
    ch = int(input("Enter the choice: "))
    if ch ==1 :
        AddEmployee()
        main()
    elif ch == 2 :
        empid = int(input("Enter the employee id: "))
        passwd = input("Enter the employee password: ")
        showemployee(empid,passwd)
        main()
    elif  ch ==3:
        mycur.execute("Select * from empdata;")
        print(mycur.fetchall())

    elif ch ==4 :
        pass
    else:
        print('Choose current option')

main()