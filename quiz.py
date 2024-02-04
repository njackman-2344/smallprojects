#quiz
print("A+ Certification Review: 4 questions")


count=0

def quest1():
    global count
    print("POP3 protocol is used for: ")
    choices1 = ["1. Name Resolution", "2. Sending Email", "3. File Notification", "4. Email Retrieval"]
    print(choices1)
    answer1=int(input("Which one? 1-4: "))
    correct1=4
    if answer1 !=correct1: 
        print("Wrong Answer. Number 4")
    else:
        print(" Correct. Next question")
    if answer1==4:
        count =count + 1
    else: return count


def quest2():
    global count
    print("The function of the NetBT protocol is to allow NetBios services to be used over TCP/IP Networks: ")
    choices2 = ["1.True ", "2.False "]
    print(choices2)
    answer2=int(input("Which one? 1 or 2: "))
    correct2=1
    if answer2 !=correct2: 
        print("Wrong Answer. It's True.")
    else: print(" Correct. Next question")
    if answer2==1:
        count= count + 1
    else: return count
        
    
        

def quest3():
    global count
    print("A type of protocol used in network management systems for monitoring network-attached devices is called: ")
    choices3 = ["1. SMB", "2. NTP", "3. SNMP", "4. RDP"]
    print(choices3)
    answer3=int(input("Which one? 1-4: "))
    correct3=3
    if answer3 !=correct3: 
        print("Wrong Answer. Number 3")
    else: print(" Correct. Next question")
    if answer3==3:
        count= count + 1
    else: return count
    
    
       

def quest4():
    global count
    print("LDAP is an example of: ")
    choices4 = ["1. Authentication Protocol", "2. Address Resolution Protocol", "3. Directory Access Protocol", "4. File Exchange Protocol"]
    print(choices4)
    answer4=int(input("Which one? 1-4: "))   
    correct4=3
    if answer4 !=correct4: 
        print("Wrong Answer. Number 3")
    else: print("Correct. Next Question.")
    if answer4==3:
        count= count + 1
    else: return count
        
quest1()
quest2()
quest3()
quest4()

if count ==4:
     print("Congrats! You got 4 questions right!")
elif count ==3:
     print("Great Job! You got 3 out of 4 questions right. Try it again!")
elif count ==2:
     print("Oh No! 2 out of 4 questions right! Try again!")
elif count ==1:
     print("You got 1 right. Study up!")
else: print("0 out of 4. Study more!")





         