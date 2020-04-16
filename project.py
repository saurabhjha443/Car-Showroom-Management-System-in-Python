import pymysql as db


conn=db.connect("127.0.0.1","root","pass@123","database1")
cur=conn.cursor()

def viewemployee(cur):
    qry="select * from employee"
    cur.execute(qry)
    rs=cur.fetchall()
    print("userName\tuserPass\tuserType\tfullName\tphone\temail\tstatus\n----------------------")
    for rows in rs:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*rows))

def viewprospect(cur):
    qry="select * from prospect"
    cur.execute(qry)
    rs=cur.fetchall()
    print("prospId\tprospName\tprosPhone\tprospAddress\tinterestedModel\tinterestedColor\tdateOfVisit\thotness\n----------------------")
    for rows in rs:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*rows))
        
#Login
print("Enter username and password to login:")
userName=input("Enter username")
userPass=input("Enter Password")
cur=conn.cursor()
qry="select * from employee where userName=%s and userPass=%s"
cur.execute(qry,(userName,userPass))
result=cur.fetchall()

if result:
    userType=input("Enter your user type")
    cur=conn.cursor()
    qry="select * from employee where userName=%s and userPass=%s and userType=%s"
    cur.execute(qry,(userName,userPass,userType))
    res=cur.fetchall()
    if res:
        if userType=="admin":
            val=int(input("Enter value 1 for Admin module and 2 for Monitor module"))
            if val==1:

                while(True):
                    print("Admin Module Access")
                    print("""************************ADMIN MODULE*********************
                                            1) Create User Account
                                                a) Monitor b)Admin
                                            2)View All User(Employees)
                                            3) View All Prospects
                                            4) Change Password
                                                a) Self b)Others
                                            5) Search Prospect
                                                a)By Hotness b) By Prospect Id
                                            6)Activate/Deactivate Account
                                            7) Sign Out
                                                 """)
                    choice=int(input("Enter your Choice"))
                    if choice==1:
                    #User Account Creation
                        num=int(input("no of records:"))
                        for i in range(num):
                                        userName=input("user name:")
                                        userPass =input("Enter Password:")
                                        userType =input("Type of user:")
                                        fullName=input("Enter full name:")
                                        phone =input("Enter phone number:")
                                        email =input("Email Id ")
                                        status =input("Enter status of employee(Activated or Deactivated):")

                                        qry="insert into employee values(%s,%s,%s,%s,%s,%s,%s)"
                                        cur.execute(qry,(userName,userPass,userType,fullName,phone,email,status))
                                        print("\n")
                        conn.commit()
                        viewemployee(cur)
                    elif choice==2:
                    #view all employee
                            print("view users")
                            cur=conn.cursor()
                            qry="select * from employee"
                            cur.execute(qry,)
                            result=cur.fetchall()
                            for i in result:
                                print(i)
                            conn.commit()
                    elif choice==3:
                    #view all prospect
                            print("view prospect")
                            cur=conn.cursor()
                            qry="select * from prospect"
                            cur.execute(qry,)
                            res=cur.fetchall()
                            for i in res:
                                print(i)
                            conn.commit()
                    elif choice ==4:
                    #Change Password
                            print("Change Password")
                            userName=input("Enter Username")
                            userPass=input("Enter New Password ")
                            cur=conn.cursor()
                            qry="update employee set userPass=%s where userName=%s"
                            cur.execute(qry,(userPass,userName))
                            conn.commit()
                            viewemployee(cur)
                    elif choice==5:
                    #Search Prospect
                            print("Enter either by hotness or ProspectId")
                            value=input("Enter h for hotness or p for prospId")
                            if value=='h':
                                hotness=input("Enter hotness of customer")
                                cur=conn.cursor()
                                qry="select * from prospect where hotness=%s"
                                cur.execute(qry,(hotness))
                                res=cur.fetchall()
                                print(res)
                                conn.commit()
                            elif value =='p':
                                prospId=input("Enter prospect Id")
                                cur=conn.cursor()
                                qry="select * from prospect where prospId=%s"
                                cur.execute(qry,(prospId))
                                res=cur.fetchone()
                                print(res)
                                conn.commit()
                            else:
                                print("!!! Invalid Choice!!!")
                    elif choice==6:
                    #Status of Account
                            print("Activate or Deactivate Account")
                            userName=input("Enter User Name")
                            status=input("Change Status of Account as per your choice")
                            cur=conn.cursor()
                            qry="update employee set Status=%s where userName=%s"
                            cur.execeute(qry,(status,userName))
                            conn.commit()
                            viewemployee(cur)
                    elif choice==7:
                    #Sign Out
                            print("You have sucessfully signed out")
                            break
                    else:
                            print("!!! Invalid Choice!!!")
            elif val==2:

                while(True):
                    print("Employee Module Access")
                    print("""*******************EMPLOYEE MODULE*************************
                                            Login
                                            1)Add New Prospect
                                            2)View All Prospeect
                                            3)Update Prospect
                                                a) -Phone b)-Model c)-Colour d)-Hotness
                                            4)Search
                                                a)By Hotness b) By Prospect Id
                                            5)Change Own paasword
                                            6)Sign Out
                                             """)
                    choice=int(input("Enter Choice"))
                    if choice==1:
                    #Add New Prospect
                        num=int(input("enter no. of records you wanna enter"))
                        for i in range(num):
                                            prospId=input("enter prospect id:")
                                            prospName =input("Enter name:")
                                            prospPhone =input("Enter phone number:")
                                            prospAddress=input("Enter address:")
                                            interestedModel =input("Enter interested model:")
                                            interestedColor =input("Enter interested color")
                                            dateOfVisit =input("Enter date of visit:")
                                            hotness=input("enter hotness as 1) cold,2)warm,3)hot:")

                                            qry="insert into prospect values(%s,%s,%s,%s,%s,%s,%s,%S)"
                                            cur.execute(qry,(prospId,prospName,prospPhone,prospAddress,interestedModel,interestedColor,dateOfVisit,hotness))
                                            print("\n")
                        conn.commit()
                        viewprospect(cur)
                    elif choice==2:
                    #View All Prospect
                        print("view prospect")
                        cur=conn.cursor()
                        qry="select * from prospect"
                        cur.execute(qry)
                        res=cur.fetchall()
                        for i in res:
                            print(i)
                        conn.commit()
                    elif choice==3:
                    #update prospect
                         print("update prospect")
                         prospId=input("Enter prospId")
                         prospPhone=input("Enter new phone number")
                         interestedModel=input("Enter model of car")
                         interestedColour=input("Enter colour of car")
                         hotness=input("Enter hotness of customer")


                         cur=conn.cursor()
                         qry="update prospect set prospPhone=%s,interestedModel=%s,interestedColour=%s,hotness=%s where prospId=%s"
                         cur.execute(qry,(prospPhone,interestedModel,interestedColour,hotness,prospId))
                         conn.commit()
                    elif choice==4:
                    #Search Prospect
                         print("Enter either by hotness or ProspectId")
                         value=input("Enter h for hotness or p for prospId")
                         if value=='h':
                             hotness=input("Enter hotness of customer")
                             cur=conn.cursor()
                             qry="select * from prospect where hotness=%s"
                             cur.execute(qry,(hotness))
                             res=cur.fetchall()
                             print(res)
                             conn.commit()
                         elif value =='p':
                             prospId=input("Enter prospect Id")
                             cur=conn.cursor()
                             qry="select * from prospect where prospId=%s"
                             cur.execute(qry,(prospId))
                             res=cur.fetchone()
                             print(res)
                             conn.commit()
                         else:
                             print("!!! Invalid Choice!!!")
                    elif choice==5:
                    #change password
                        print("Change Password")
                        userName=input("Enter Username")
                        userPass=input("Enter New Password ")
                        cur=conn.cursor()
                        qry="update employee set userPass=%s where userName=%s"
                        cur.execute(qry,(userPass,userName))
                        conn.commit()
                        viewemployee(cur)
                    elif choice==6:
                    #Sign Out
                        print("You Have Signed Out")
                        break
                    else:
                        print("!!!Invalid Choice!!!")
                        continue
                else:
                    print("!!!Invalid Choice!!!")
        elif userType=="employee":

            while(True):
                    print("Employee Module Access")
                    print("""*******************EMPLOYEE MODULE*************************
                                             Login
                                             1)Add New Prospect
                                             2)View All Prospeect
                                             3)Update Prospect
                                                 a) -Phone b)-Model c)-Colour d)-Hotness
                                             4)Search
                                                 a)By Hotness b) By Prospect Id
                                             5)Change Own paasword
                                             6)Sign Out
                                              """)
                    choice=int(input("Enter Choice"))
                    if choice==1:
                    #Add New Prospect
                        num=int(input("enter no. of records you wanna enter"))
                        for i in range(num):
                                            prospId=input("enter prospect id:")
                                            prospName =input("Enter name:")
                                            prospPhone =input("Enter phone number:")
                                            prospAddress=input("Enter address:")
                                            interestedModel =input("Enter interested model:")
                                            interestedColor =input("Enter interested color")
                                            dateOfVisit =input("Enter date of visit:")
                                            hotness=input("enter hotness as 1) cold,2)warm,3)hot:")

                                            qry="insert into prospect values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                            cur.execute(qry,(prospId,prospName,prospPhone,prospAddress,interestedModel,interestedColor,dateOfVisit,hotness))
                                            print("\n")
                        conn.commit()
                        viewprospect(cur)
                    elif choice==2:
                    #View All Prospect
                        print("view prospect")
                        cur=conn.cursor()
                        qry="select * from prospect"
                        cur.execute(qry,)
                        res=cur.fetchall()
                        for i in res:
                            print(i)
                        conn.commit()
                    elif choice==3:
                    #update prospect
                         print("update prospect")
                         prospId=input("Enter prospId")
                         prospPhone=input("Enter new phone number")
                         interestedModel=input("Enter model of car")
                         interestedColour=input("Enter colour of car")
                         hotness=input("Enter hotness of customer")


                         cur=conn.cursor()
                         qry="update prospect set prospPhone=%s,interestedModel=%s,interestedColour=%s,hotness=%s where prospId=%s"
                         cur.execute(qry,(prospPhone,interestedModel,interestedColour,hotness,prospId))
                         conn.commit()
                    elif choice==4:
                    #Search Prospect
                         print("Enter either by hotness or ProspectId")
                         value=input("Enter h for hotness or p for prospId")
                         if value=='h':
                             hotness=input("Enter hotness of customer")
                             cur=conn.cursor()
                             qry="select * from prospect where hotness=%s"
                             cur.execute(qry,(hotness))
                             res=cur.fetchall()
                             print(res)
                             conn.commit()
                         elif value=='p':
                             prospId=input("Enter prospect Id")
                             cur=conn.cursor()
                             qry="select * from prospect where prospId=%s"
                             cur.execute(qry,(prospId))
                             res=cur.fetchone()
                             print(res)
                             conn.commit()
                         else:
                             print("!!! Invalid Choice!!!")
                    elif choice==5:
                    #change password
                        print("Change Password")
                        userName=input("Enter Username")
                        userPass=input("Enter New Password ")
                        cur=conn.cursor()
                        qry="update employee set userPass=%s where userName=%s"
                        cur.execute(qry,(userPass,userName))
                        conn.commit()
                        viewemployee(cur)
                    elif choice==6:
                    #Sign Out
                        print("You Have Signed Out")
                        break
                    else:
                        print("!!!Invalid Choice!!!")
                        continue
    else:
        print("!!!Invalid Choice!!!")
else:
    print("Invalid")
        
                
cur.close()
conn.commit()
conn.close()

