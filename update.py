# colors 
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
y = r

#----------------modules
from os import system,name
from time import sleep


# -----clear 
system('cls' if name=='nt' else 'clear')

print('''
      \033[91m██\033[93m╗\033[91m ██████\033[93m╗ \033[91m███████\033[93m╗\033[91m ██████\033[93m╗ \033[91m██████\033[93m╗ 
      \033[91m██\033[93m║\033[91m██\033[93m╔════╝ \033[91m██\033[93m╔════╝\033[91m██\033[93m╔═\033[91m████\033[93m╗╚════\033[91m██\033[93m╗
      \033[91m██\033[93m║\033[91m██\033[93m║\033[91m  ███\033[93m╗\033[91m███████\033[93m╗\033[91m██\033[93m║\033[91m██\033[93m╔\033[91m██\033[93m║ \033[91m█████\033[93m╔╝
      \033[91m██\033[93m║\033[91m██\033[93m║\033[91m   ██\033[93m║╚════\033[91m██\033[93m║\033[91m████\033[93m╔╝\033[91m██\033[93m║\033[91m██\033[93m╔═══╝ 
      \033[91m██\033[93m║╚\033[91m██████\033[93m╔╝\033[91m███████\033[93m║╚\033[91m██████\033[93m╔╝\033[91m███████\033[93m╗
      \033[93m╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝''')          

#-------update
system('rm -rf Reports.py')
sleep(0.1)
system('wget https://raw.githubusercontent.com/shubhushubhu99/IG502/main/Reports.py')
sleep(0.1)
print(r+"└─ "+w+"\033[1;37m>> IG502 Updated Sucessfully <<")
sleep(0.5)

# ---------return to Reports.py file 
system('python Reports.py' if name=='nt' else 'python3 Reports.py')
