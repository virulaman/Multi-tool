import random
import os
import time
import hashlib

def banner():
    print("======================================================================")
    print(" _________                             __              __   .__.     ")
    print("\______   \_____    ______ ______     |__|__ __  ____ |  | _|__| ____") 
    print(" |     ___/\__  \  /  ___//  ___/     |  |  |  \/    \|  |/ /  |/ __ \ ")
    print(" |    |     / __ \_\___ \ \___ \      |  |  |  /   |  \    <|  \  ___/ ")
    print(" |____|    (____  /____  >____  > /\__|  |____/|___|  /__|_ \__|\___  >")
    print("                \/     \/     \/  \______|          \/     \/       \/ ")
    print("")
    print("=========================================================================")
banner()
print("by virulaman")

print("1) for creating a password press 1")
print("2) for cracking a password press 2")
print("3) press 3 for help and for an about file")
print("4) press 4 for exiting")
a = int(input())

def genpass():   
     if a == 1:      
        g = int(input("Enter the desired length of the password: "))  
        password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(g))
        print("Your generated password is:", password)

genpass()
def crackpass():
    if a == 2:
        correct_password = input("Enter the password to crack (for test): ")
        wordlist_file = input("Enter the path to your wordlist file: ")

        try:
            with open(wordlist_file, "r") as f:
                for line in f:
                    guess = line.strip()
                    print("Trying:", guess)
                    if guess == correct_password:
                        print("Password cracked! It was:", guess)
                        return
                print(f"Password {correct_password} not found in wordlist.")
        except FileNotFoundError:
            print("Wordlist file not found.")

crackpass()


def readme():
    if a == 3:
        print("This tool is in a Alfa early acces version please report any problems or suggestions at the followint email (it's a bit unserius): wazaaa345chad@gmail.com")
        print("Here are some of the next functions:")
        print("external password cracking (for pentesting and cracking websites)")
        print("wifi cracking password cracking")
        print("pingin host")
        print("nmap")
        print("SQL infection")
        print("Press 3 for reading legal info (VERY IMPORTANT)")
        u = int(input())
        if u == 3:
            print("This tool is only used for ETHICAL use.")
            print("The coder that makes this tool completly demacrates of iligal use.")

readme()

def exit():
    if a == 4:     
        for i in range(5, 0, -1):
            print(i, end='\r')
            
            time.sleep(1)

            print("")
            for i in range(100):
                print("                                                                                            ") 


exit()
