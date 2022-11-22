
import os

os.system('pkg install git')
os.system('pkg install python')
os.system('rm -rf IG502')
os.system('git clone https://github.com/shubhushubhu99/IG502')
os.system('cd IG502')
os.system('pip install --upgrade pip')
os.system('pip install requests')
os.system('pip install colorama')
os.system('pip install termcolor')
os.system('pip install progressbar')
os.system('pip install rich')
os.system('python Reports.py')
