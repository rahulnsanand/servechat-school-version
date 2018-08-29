"""Y:/R.A XII-A/"""
# -*- coding: cp1252 -*-
import sqlite3 as lite
import sys
from time import localtime, strftime
print ("")
print ("--------------------------------------------------------------------------------")
print ("+++++++++++++++++++++++++++SERVECHAT-Alpha Version 3.0++++++++++++++++++++++++++")
print ("+                                                                              +")
print ("+                                                   By-R.A™                    +")
print ("+                                                   All Rights Reserved(2014)© +")
print ("+                                                                              +")
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print ("--------------------------------------------------------------------------------")

reg="Y"
refresh="S"
log="Y"
Ch=""
n1="\n"
con = lite.connect('Y:/R.A XII-A/ServeChat.db')
con.execute("CREATE TABLE IF NOT EXISTS Contacts(Name TEXT,password TEXT);")
cur = con.cursor()
cur.execute("INSERT INTO Contacts VALUES ('Admintest','admin' );")

def LOGINPAGE(x):
    if(x=='1'):
            
            username= raw_input("ENTER YOUR USERNAME  :")
            password=raw_input ("ENTER YOUR PASSWORD  :")
            print ("================================================================================")

            cursor=con.execute("SELECT Name,Password from Contacts")
            for row in cursor:
                name=row[0]
                passw=row[1]
                
                if(name==username and passw==password):
                    print "LOGGED IN SUCCESSFULLY"
                    con1= lite.connect('Y:/R.A XII-A/Servechatout.db')
                    j='1'
                    if(j=='1'):
                        
                        print ("================================================================================")
                        print  '                         WELCOME TO SERVECHAT,',username
                        print ("================================================================================")
                        print ("")
                        username=username+" :"
                        fob=open('Y:/R.A XII-A/Chat.txt','a')
                        fob.write(username)
                        welcome="has JOINED the group"
                        ter=strftime(" %I:%M.", localtime())
                        n1='\n'
                        
                        fob.write(welcome)
                        fob.write(ter)
                        fob.write(n1)
                        fob.close()
                        fob=open('Y:/R.A XII-A/record.txt','a')
                        fob.write(username)
                        
                        fob.write("LOGIN TIME :")
                        ter=strftime("%a,%d %b %I:%M :", localtime())
                        fob.write(ter)
                        fob.write(n1)
                        fob.close()
                        refresh="S"
                
                        while refresh=="S":
                            usrcho=raw_input("CHECK MY INBOX      (1)\nWRITE A NEW MESSAGE (2)\nLOGOUT AND EXIT     (3)\n")
                            if (usrcho=='1'):
                                    print ("")
                                    print ("================================================================================")
                            
                                    fob=open('Y:/R.A XII-A/Chat.txt','r')
                                    msg=fob.read()
                                
                                    print msg
                                
                                    print ("================================================================================")
                                    print ("")

                            elif (usrcho=='2'):
                                
                                print ("")
                                print ("================================================================================")
                                messg=raw_input("ENTER YOUR MESSAGE :")
                                fob=open('Y:/R.A XII-A/Chat.txt','a')
                                n=('\n')
                                a=strftime(" %a:%I:%M :", localtime())
                                sp=(" ")
                                quot=('"')
                                fob.write(username)
                                fob.write(a )
                                fob.write(sp)
                                fob.write(quot)
                                fob.write(messg)
                                fob.write(quot)
                                fob.write(n)
                                fob.close()
                                print ("MESSAGE SENT SUCCESSFULLY")
                                print ("================================================================================")
                                print ("")

                            elif (usrcho=='3'):
                                print("SUCCESSFULLY LOGGED OUT")
                                fob=open('Y:/R.A XII-A/Chat.txt','a')
                                fob.write(username)
                                ter=strftime(" %I:%M.", localtime())
                                welcome="has LEFT the group"
                                
                                n1='\n'
                                fob.write(welcome)
                                fob.write(ter)
                                fob.write(n1)
                                fob.close()
                            
                                return
                            else:
                                print ("================================================================================")
                                print "ERROR 404: YOU'VE SERIOSULY GOT NO BRAINS!\nKINDLY GET THAT FIRST!"
                                print ("================================================================================")
                                raw_input("PRESS <Enter> TO RETRY")
                                print ("================================================================================")
            else:
                print ("================================================================================")
                print ("          INVALID USERNAME AND PASSWORD! MAKE SURE YOU HAVE AN ACCOUNT          ")
                print ("================================================================================")
                return


while (log=="Y"):
    
    print ("================================================================================")
    Ch=raw_input("ALREADY REGISTERED?     (1)\nREGISTER A NEW ACCOUNT? (2)\nEXIT ?                  (3)\n")
    
    print ("================================================================================")
    
    if (Ch=='1'):
        print ("________________________________________________________________________________")
        print ("                **KINDLY INPUT VALUES AS ASKED TO, WITHOUT USING EXTRA BRAINS.**")
        print ("                             **OTHERWISE THE APPLICATION MIGHT CRASH**          ")
        print ("________________________________________________________________________________")
        LOGINPAGE('1')
                                    
            

    elif(Ch=='2'):
        
        
        print ("================================================================================")
        print ("================================================================================")
        print ("                           WELCOME TO SERVECHAT V3.0                            ")
        print ("================================================================================")
        print ("================================================================================")
        print ("                                             CREATED BY R.A FOR YOUR CONVENIENCE")
        print ("NOTE: ALL CREDENTIALS ARE 'CASE SENSITIVE'                                      ")
        print ("================================================================================")
        print ("================================================================================")
        while reg=="Y":           
            new_username= raw_input    ('TO PROCEED, PLEASE ENTER YOUR NEW USERNAME: ')
            new_password= raw_input    ('ENTER YOUR DESIRED PASSWORD               : ')
            new_passwordre=raw_input   ('CONFIRM YOUR DESIRED PASSWORD             : ')
            if(new_passwordre==new_password):
                createnewdb = raw_input('CONFIRM THE CREDENTIALS? (Y/N)            : ')
                if createnewdb == "Y" or createnewdb=="y":
                    
                    cursor=con.execute("SELECT Name,password from Contacts;")
                    for row in cursor:
                        
                        name=row[0]
                        passw=row[1]
                        if(name!=new_username and passw!=new_password):
                            with con:
                                cur = con.cursor()
                                cur.execute("CREATE TABLE IF NOT EXISTS Contacts (Name TEXT,Password TEXT);")
                                cur.execute("INSERT INTO Contacts VALUES (?, ?);", (new_username ,new_password))
                                print "OUR DATABASE HAS BEEN UPDATED SUCESSFULLY!"
                                jk=raw_input("CONTINUE TO LOGIN? (1)\nEXIT THE APP       (2)")
                                
                                if jk=='1':
                                    LOGINPAGE('1')
                                    break
                                elif jk=='2':
                                    break
                                else:
                                    print"INVALID INPUT! BASIC READING SKILLS REQUIRED TO USE THIS APP!"
                            break   
                            
                        elif(name==new_username):
                            print ("================================================================================")
                            print  "                     SORRY,YOUR USERNAME IS ALREADY BEEN TAKEN!                 "
                            uscho=raw_input("RETRY WITH A DIFFERENT USERNAME?(1)")
                            print ("================================================================================")
                            
                                
                        else:
                            print ("================================================================================")
                            print  "                                    INVALID INPUT!                              "
                            uscho=raw_input("RETRY?(1)")
                            print ("================================================================================")
                                            
                    break
                elif( createnewdb=="N" or createnewdb=="n"):
                    print ("================================================================================")
                    print  "          RE-ENTER YOUR CREDENTIALS.\nTHIS TIME TAKE CARE WITH THE INPUT!       "
                    print ("================================================================================")
                else:
                    print ("================================================================================")
                    print("NOPE, SEEMS YOU'VE GOT NO SENSE OF ENGLISH. COMEON. IT CLEARLY SAYS (Y/N)\nNOW TYPE YOUR DETAILS AGAIN\n")
                    print ("================================================================================")
            else:
                print ("================================================================================")
                print ("                     YOUR PASSWORDS DO NOT MATCH!\nTRY AGAIN!                   ")
                print ("================================================================================")
                
    elif(Ch=='3'):
        
        print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print  "===========================THANKYOU FOR USING THIS APP=========================="
        print  "                            THIS IS AN ALPHA VERSION                            "
        print ("            DEVELOPMENT IS UNDER PROCESS, KINDLY KEEP TRACK OF UPDATES.         ")
        print  "YOU FIND THIS APP OFFENSIVE? WELL, THEN IT HAS DONE WHAT IT WAS SUPPOSED TO :P  "
        print (" IF YOU DON'T, YOU HAVE USED THIS APP JUST AS THE DEVELOPER MEANT IT TO BE USED ")
        print ("================================================================================")
        print ("                              TERMS AND CONDITIONS                              ")
        print ("   THIS APPLICATION IS AN ALPHA BUILD OF THE PREVIOUS VERSION SERVECHAT V2.0.   ")
        print ("================================================================================")       
        print ("            EVERYTHING YOU USE IN THIS APP IS CREATED BY THE DEVELOPER.         ")
        print ("EVENTHOUGH IT MAY SOUND ASTONISHING,")
        print ("                           ***NONE OF THE CODES HAVE BEEN COPIED FROM ANYONE.***")
        print ("      IT TOOK THE DEVELOPER 2 DAYS TO FINISH THE UPGRADE FROM V2.0 TO V3.0.     ")
        print ("================================================================================")    
        print ("                    FEATURES IN THIS UPGRADE (FROM USERS VIEW):                 ")
        print ("1.MAJOR UPGRADES HAVE BEEN MADE BY ADDING UP:")
        print ("2.A REGISTRATION PAGE")
        print ("3.LINKING THE PYTHON WITH MYSQL FOR SUPPPORT OF DATABASE.")
        print ("================================================================================")       
        print ("                 FEATURES IN THIS UPGRADE (FROM DEVELOPERS VIEW):               ")
        print ("1.THERE IS A 'def' FUNCTION BEING USED.")
        print ("2.MYSQL IMPORT, SYSTEM IMPORT")
        print ("3.FILE ACCESS IMPORT.")
        print ("4.THE CODE HAS GONE FROM 114 TO 230 LINES, CLEARLY THAT MEANS SOMETHING.")
        print ("================================================================================")       
        print ("               THIS IS JUST THE BEGINNING OF THE UPCOMING VERSIONS.             ")
        print ("================================================================================")
        print ("V4.0 AIMS TO COME IN WITH")
        print ("1.A 'EDIT' YOUR PASSWORD FEATURE")
        print ("2.CHAT WITH PEOPLE INDIVIDUALLY BASED ON THERE AVAILABILITY FEATURE.")
        print ("================================================================================")
        print ("V5.0 AIMS TO COME WITH")
        print ("1.AUTOMATIC INBOX REFRESHER")
        print ("HOPE YOU'VE FOUND THIS APP USEFULL.")
        print ("================================================================================")
        print ("                     THANKYOU FOR YOU SUPPORT AND APPRECIATION.                 ")
        print ("                                      #PEACE#                                   ")
        print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("================================================================================")
        raw_input("                           Press <Enter> To Exit                              \n")
        print ("================================================================================")
        break

    else:
        print ("================================================================================")
        print ("                           INVALID INPUT! TRY AGAIN!                            ")

    
     

            
