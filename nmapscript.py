import os
import subprocess
import sys

RED='\033[91m'
BLUE='\33[94m'
END='\033[0m'

if len(sys.argv) < 2:
	os.system('cls||clear')
	sys.stdout.write(RED+"""\t\t\t
			 _______  _______  _______  ___   _______  _______ 
			|       ||       ||       ||   | |       ||   _   |
			|   _   ||    _  ||_     _||   | |       ||  |_|  |
			|  | |  ||   |_| |  |   |  |   | |       ||       |
			|  |_|  ||    ___|  |   |  |   | |      _||       |
			|       ||   |      |   |  |   | |     |_ |   _   |
			|_______||___|      |___|  |___| |_______||__| |__|


	\n"""+END)
else:
	sys.exit("Usage : python3 nmapscript.py ")
	os.system("cls||clear")

def mainMenu():
	print(BLUE+"*"*80)
	print(RED+"\t\t\t SCANNER")
	print(BLUE+"*"*80)
	print("\t\t\t 1) Host Discovery")
	print("\t\t\t 2) OS Discovery")
	print("\t\t\t 3) Port Discovery")
	print("\t\t\t 4) Port Range Discovery")
	print("\t\t\t 5) clear terminal")
	print("\t\t\t 6) Quit!!")
	print("")
	choice=int(input("\t\t\tselect the option : "+RED))
	if choice==1:
		hostDiscovery()
		mainMenu()
	elif choice==2:
		osDiscovery()
		mainMenu()
	elif choice==3:
		portDiscovery()
		mainMenu()
	elif choice==4:
		portRange()
		mainMenu()
	elif choice==5:
		clearTer()
		mainMenu()
	elif choice==6:
		clearTer()
		quitp()
	else:
		print("invalid choice")
		mainMenu()
	
def hostDiscovery():
	host = input(RED+"Enter the target Ip Address/Name: "+BLUE)
	print("-"*80)
	subprocess.check_call(['nmap','-n','-v','-Pn','-sn','-sL','-PE',
	'-PP','-oN','hostdicovery.txt',host])
	print("-"*80)

def osDiscovery():
	os = input(RED+"Enter the target Ip Address: "+BLUE)
	print("-"*80)
	print(RED+"")
	subprocess.check_call(['nmap','-n','-F','-A','-Pn','-sS','-O',
	'-oN','osdicovery.txt',os])
	print("-"*80)

def portDiscovery():
	port = input(RED+"Enter the target Ip Address: "+BLUE)
	print("-"*80)
	print(RED+"")
	subprocess.check_call(['nmap','-n','-v','-sV','-oN','portdicovery.txt',port])
	print("-"*80)

def portRange():
	port = input(RED+"Enter the target Ip Address: "+BLUE)
	print("-"*80)
	print(RED+"")
	subprocess.check_call(['nmap','-p','1-100','-oN','portdicovery.txt',port])
	print("-"*80)
	print(''+END)
def clearTer():
	os.system('cls||clear')

def quitp():
	quit()
	
if __name__== "__main__":
	mainMenu()
