import subprocess
import paramiko
import time
import time as mm
import sys as n
import optparse
import os
from pip._vendor.colorama import Fore, Style
parser = optparse.OptionParser()
parser.add_option("-p", "--path",dest="path", help="path you save file in ")
parser.add_option("-t", "--target",dest="target", help="put target ip")
(options, arguments) = parser.parse_args()
G = Fore.LIGHTGREEN_EX + Style.BRIGHT
R = Fore.LIGHTRED_EX + Style.BRIGHT
W = Fore.LIGHTWHITE_EX + Style.BRIGHT
B = Fore.LIGHTBLUE_EX + Style.BRIGHT
def slow(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 20)


def slow2(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 25)


def slow1(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 2000)
meun = f'''
 {W}[1]{G}Show-apps-list
 {W}[2]{G}Dump-app
 {W}[00]exit
'''
logo = '''
   ▄▀█ █▀█ █▄▀ ▄▄ █▀▄ █░█ █▀▄▀█ █▀█
   █▀█ █▀▀ █░█ ░░ █▄▀ █▄█ █░▀░█ █▀▀
                 Code By: @codeone1
              https://github.com/xcodeon1   
'''
shpe = G+f'''
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$_______________$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$___________________$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$____$$$_________$$$____$$$$$$$$$$$$$
$$$$$$$$$$$$$_____$$$_________$$$_____$$$$$$$$$$$$
$$$$$$$$$$$$___________________________$$$$$$$$$$$
$$$$$$$$$$$$___________________________$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$_____$$$____________________________$$$____$$$
$$$$_____$$$____________________________$$______$$  
$$$$_____$$$____________________________$$______$$
$$$$_____$$$____________________________$$______$$
$$$$_____$$$____________________________$$______$$   {R}{logo}{G}
$$$$_____$$$____________________________$$______$$       
$$$$_____$$$____________________________$$______$$
$$$$______$$____________________________$$______$$
$$$$_____$$$____________________________$$______$$
$$$$$___$$$$____________________________$$$___$$$$
$$$$$$$$$$$$____________________________$$$$$$$$$$
$$$$$$$$$$$$____________________________$$$$$$$$$$
$$$$$$$$$$$$___________________________$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
'''
slow1(shpe)
try:
    host = options.target
    username = 'root'
    password = 'alpine'
    port = '8022'
    # connect to server
    con = paramiko.SSHClient()
    con.load_system_host_keys()
    con.connect(host, username=username, password=password, port=port)
    stdin, stdout, stderr = con.exec_command('cd /data/app/;ls')
    slow(W + "Now it show all Apps")
    slow("-" * 40)
    if stderr.read() == b'':
        for line in stdout.readlines():
            commane = line.strip()
            print(commane + '\n')
    else:
        print(stderr.read())
    dump = str(input(f"{W}[~]Do you want dump app y/n >> "))
    if dump == 'y':
        os.system('clear')
        slow1(shpe)
        app_path = str(input(f"{W}[~] Enter App path >> "))
        str(subprocess.run(
                ["sshpass", "-p", "alpine", "scp", "-P", "8022", "-r",
                 f"root@{options.target}:/data/app/{app_path}", f"{options.path}"]))
        slow1(f"{G}Now you have dump App in{W} %s \n" %options.path)
        slow(f"Don't Forget follow me in {B}Twitter: {W}@xcodeone1")
    else:
        slow(f"\n{W}See you Later Don't Forget follow me in {B}Twitter: {W}@xcodeone1")
except AttributeError:
    pass
