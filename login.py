import os
import os.path
from getpass import getpass
os.system("clear")
def banner():
	print("\033[1;36;40m_                                 
   print(  "    ,_> `.   ,';      ")
               ,-`'      `'   '`'._
            ,,-) ---._   |   .---''`-),.
          ,'      `.  \  ;  /   _,'     `,
       ,--' ____       \   '  ,'    ___  `-,
      _>   /--. `-.              .-'.--\   \__
     '-,  (    `.  `.,`~ \~'-. ,' ,'    )    _\
     _<    \     \ ,'  ') )   `. /     /    <,.
  ,-'   _,  \    ,'    ( /      `.    /        `-,
  `-.,-'     `.,'       `         `.,'  `\    ,-'
   ,'       _  /   ,,,      ,,,     \     `-. `-._
  /-,     ,'  ;   ' _ \    / _ `     ; `.     `(`-\
   /-,        ;    (o)      (o)      ;          `'`,
 ,~-'  ,-'    \     '        `      /     \      <_
 /-. ,'        \                   /       \     ,-'
   '`,     ,'   `-/             \-' `.      `-. <
    /_    /      /   (_     _)   \    \          `,
      `-._;  ,' |  .::.`-.-' :..  |       `-.    _\
        _/       \  `:: ,^. :.:' / `.        \,-'
      '`.   ,-'  /`-..-'-.-`-..-'\            `-.
        >_ /     ;  (\/( ' )\/)  ;     `-.    _<
        ,-'      `.  \`-^^^-'/  ,'        \ _<
         `-,  ,'   `. `"""""' ,'   `-.   <`'
           ')        `._.,,_.'        \ ,-'
            '._        '`'`'   \       <
               >   ,'       ,   `-.   <`'
                `,/          \      ,-`
                 `,   ,' |   /     /
                  '; /   ;        (
                   _)|   `       (
                   `')         .-'
                     <_   \   /    
                       \   /\(
                        `;/  `\033[0m")
	print("                \033[1;34;40m authorRRR by \033[1;33;40mWANI YAMIN\033[0m")
	print("")
banner()

def reset():
	os.remove("/data/data/com.termux/files/usr/share/user.txt")
	os.remove("/data/data/com.termux/files/usr/etc/bash.bashrc")
	os.system("mv /data/data/com.termux/files/usr/etc/a /data/data/com.termux/files/usr/etc/bash.bashrc")
if not os.path.exists("/data/data/com.termux/files/usr/share/user.txt"):
	os.system("cp /data/data/com.termux/files/usr/etc/bash.bashrc /data/data/com.termux/files/usr/etc/a")
	f=open("/data/data/com.termux/files/usr/etc/bash.bashrc","a")
	f.write("cd Login ; python login.py")
	f.close()
	user=input("\033[1;33;40mSET YOUR USERNAME :\033[0m \033[1;32;40m")
	print("")                                                        
	print("")
	print("")
	print("")
	passwd=getpass("\033[1;33;40mSET YOUR PASSWORD :\033[0m \033[1;32;40m")
	f=open("/data/data/com.termux/files/usr/share/user.txt","w")                                            
	f.write(f"{user}\n")
	f.write(passwd)                                           
	f.close()
else:
	while(1):
		try:
			f=open("/data/data/com.termux/files/usr/share/user.txt","r")
			username=f.readline()
			username=username.strip()
			password=f.readline()
			password=password.strip()
			f.close()
			usr=input("\033[1;33;40mEnter username -: \033[0m \033[1;32;40m")
			if usr==username:
				pas=getpass("\033[1;33;40mEnter password -: \033[0m \033[1;32;40m")
				if pas==password:
					os.system("clear")
					banner()
					break
				else :
					print("")
					print("")
					print("")
					print("")
					print("\033[1;31;40m try again\033[0m")
					print("")
					print("")
					print("")
					print("")
			elif(usr=="forget" or usr=="reset" or pas=="forget" or pas=="reset"):
				reset()
				break
			else:
				print("")
				print("")
				print("")
				print("")
				print("")
				print("\033[1;31;40m try again\033[0m")
				print("")
				print("")
				print("")
				print("")
		except :
			print("")
			print("")
			print("")
			print("")
			print("\033[1;31;40mtry again\033[0m")
			print("")
			print("")
			print("")
			print("")
