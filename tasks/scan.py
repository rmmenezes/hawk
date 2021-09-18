import nmap
import sys
import os
import multiprocessing
from extras import printcolor

scanner = nmap.PortScanner()

def scanStatus(str, inputed):

    try:
        scanner.scan(str, '1', '-v -sT')
    except KeyboardInterrupt:  
        sys.exit('\n^C\n')
    except:
        e = sys.exc_info()
        printcolor('RED', f'\n{e}')
        sys.exit(1)
    else:
        if scanner[str].state() == 'up':
            printcolor('GREEN', f'Status: {str} is {scanner[str].state()}')
        else: 
            printcolor('RED', f'Status: {str} is {scanner[str].state()}')

def scan(str, inputed, prstart, prend, scantype):

    scanStatus(str, inputed)
    print('Scan will start. Press CTRL-C to cancel.') 

    try:
        print(f'Scanning {str}:{prstart}-{prend}') ###yellow
        scanner.scan(str, f'{prstart}-{prend}', f'-v {scantype}')
    except KeyboardInterrupt: 
        sys.exit('\n^C\n')
    except: 
        e = sys.exc_info()[1]
        printcolor('RED', f'\n{e}')
    else:
        if len(scanner[str].all_protocols()) == 0:
            print('\nNo port(s) found.')
        else:
            for protocol in scanner[str].all_protocols():
                if scanner[str][protocol].keys():
                    print(f'\nProtocol: {protocol.upper()}')
                    print('\n PORT     \t\tSTATE     \t\tSERVICE')
                    for port in scanner[str][protocol].keys():
                        print(f" {port}      \t\t{scanner[str][protocol][port]['state']}       \t\t{scanner[str][protocol][port]['name']}")
            
def scanWithPort(str, inputed, int, i, j, scantype):

    try:
        if j == 0:
            scanStatus(str, inputed)
            print(f'Scanning {str}') ###yellow
            print('Scan will start. Press CTRL-C to cancel.')
        scanner.scan(str, f'{int}', f'-v {scantype}')
    except KeyboardInterrupt: 
        sys.exit('^C\n')
    except:
        e = sys.exc_info()[1]
        print(f'{e}')
    else:
        for protocol in scanner[str].all_protocols():
            if scanner[str][protocol].keys():
                if j == 0:
                    print(f'Protocol: {protocol.upper()}')
                    print('\n PORT     \t\tSTATE     \t\tSERVICE')
                for port in scanner[str][protocol].keys():
                    print(f" {port}      \t\t{scanner[str][protocol][port]['state']}       \t\t{scanner[str][protocol][port]['name']}")
            

def scanLocalDevices():

    network = '192.168.1.0/24'

    try:
        print('Scanning for devices on local network') ###yellow
        scanner.scan(hosts = network, arguments = '-v -sn')
    except KeyboardInterrupt:
        sys.exit('\n^C\n')
    except: 
        e = sys.exc_info()[1]
        printcolor('RED', f'\n{e}')
    else:
        for host in scanner.all_hosts():
            if scanner[host]['status']['state'] == 'up':
                print(f'{host}')
           







'''
    ip = '192.168.1.0/24' # from 192.168.1.0 to 192.168.1.255

    animateProcess = multiprocessing.Process(target = animate, args = ((f'Scanning for devices on the local network',)))
    animateProcess.start()

    try:
        os.system(f'sudo nmap -sn {ip}')
        animateProcess.kill()
    except KeyboardInterrupt:
        # stop process
        animateProcess.kill()  
        sys.exit('^C\n')
    except:
        # stop process
        animateProcess.kill() 
        e = sys.exc_info()[1]
        print(f'\n{e}\n')
    else:
        # stop process
        animateProcess.kill()
'''