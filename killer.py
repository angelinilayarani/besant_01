import mysql.connector
import smtplib
import random


my_db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="12345",
      database="cmchospital_db"
)

mycursor=my_db.cursor()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def user_data():
      sql="insert into user_details (fullname,gender,emailid,phone_number,vaccien_1,vaccien_2,patient_status) values (%s,%s,%s,%s,%s,%s,%s)"
 
      fullname=input("enter patient fullname :")
      gender=input("enter patient gender :")
      emailid=input("enter patient emailid :")
      phone_number=input("enter patient phone number :")
      vaccien_1=input("did you get your first vaccine('Yes' or 'No') :")
      vaccien_2=input("did you get your second vaccine('Yes' or 'No') :")
      if vaccien_1=="no":
         print("Warning! vaccien-1 is necessary to prevent from corona virus ")
      elif vaccien_2=="no":
           print("Warning! vaccien-2 is necessary to prevent from corona virus ")
      patient_status=input("patient Normal or Attack virus or Required or Death :")
   
      val=(fullname,gender,emailid,phone_number,vaccien_1,vaccien_2,patient_status)

      mycursor.execute(sql,val)
      my_db.commit()
      print(f"hi {fullname} your details is registered successfully !!!.........")
      

      
      #~~~~~~~~~~~~~~~~mail_code~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      try:
          
         
         # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
 
         # start TLS for security
        s.starttls()
 
         # Authentication
        s.login("ayyanar.2481996@gmail.com", "lipfcigwfeilcurw")
 
         # message to be sent
        message = f"hi {fullname} your details is registered successfully ......."
 
         # sending the mail
        s.sendmail("ayyanar.2481996@gmail.com", emailid, message)

 
         # terminating the session
        s.quit()
        print("******mail send successfully*******")

      except:
        print("********sorry mail not send*****")

      
      var=input("do you want to continue press yes : ")
      if var=="yes":
        main()
      else:
        print("thanks for visiting our app ")
     
      

def admain_view():
    #view data
      mycursor.execute("select * from user_details")
      myresult=mycursor.fetchall()
      for i in myresult:
        print(i)
      var=input("do you want to continue press yes : ")
      if var=="yes":
        main()
      else:
        print("thanks for visiting our app")
def update_data():
    #update data
      sql="update user_details set vaccien_1='Yes' where vaccien_1='no'"
      mycursor.execute(sql)
      my_db.commit()
      print("data updated successfully!..........")
      var=input("do you want to continue press yes : ")
      if var=="yes":
        main()
      else:
        print("thanks for visiting our app")
def delete_data():
    #delete data
      column_name=input("which column you want to delete: ")
      delete_data=input(f"which data you want to delete in {column_name} column:")
      sql=f"DELETE FROM user_details WHERE {column_name}= %s"
      mycursor.execute(sql,(delete_data,))
      my_db.commit()
      print("Data deleted successfully")
      var=input("do you want to continue press yes : ")
      if var=="yes":
        main()
      else:
        print("thanks for visiting our app")

def main():
    print("--------->COVID-19 DATA SURVEY<------------'")
    print("-------------->Year- ' 2022-2023 '<-----------")
    print("********MATHURAI (disticte)->DATA SURVEY-'2023'*******")
    print("1->user data")
    print("2->admain view")
    print("3->update data")
    print("4->delete data")
    
    user=int(input("Enter your number: "))
    if user==1:
        user_data()
    elif user==2:
        admain_view()
    elif user==3:
       update_data()
    elif user==4:
       delete_data()
       


main()