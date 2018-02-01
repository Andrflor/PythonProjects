# -*- coding: utf-8 -*-

from socket import *
from threading import *
import optparse

screenLock = Semaphore(value=1)

def init_args():
    parser = optparse.OptionParser("usage%prog "+" -H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-i', dest='tgtIP', type='string', help='specify target IP')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    tgtIP = options.tgtIP

    if (tgtHost == None) and (tgtIP == None):
        print('[-] You must specify a target host or IP.')
        exit(0)
    return tgtHost, tgtPorts, tgtIP

def format(string):
    string = str(string)
    string = string.replace("b'","")
    string = string.replace('\'',"")
    if(string[-2:]=="\\n"):
        string = string[:-2]
    string = string.replace("\\n","\n")
    string = string.replace("\\r","\r")
    return string

def connScan(tgtIP, tgtPort):

    screenLock.acquire()
    print('\nScanning port %s' % tgtPort)

    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtIP, tgtPort))
        print('[+] Port %d/tcp open' % tgtPort)
        try:
            print('[+] Welcome message: ' + format(connSkt.recv(1024)))
        except:
            pass
        try:
            connSkt.send(b'HiThere\r\n')
            print('[+] Response message: '+ format(connSkt.recv(1024)))
        except:
            pass
    except:
        print('[-] Port %d/tcp closed'% tgtPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(*args):
    print("")

    if (args[0]!=None):
        tgtHost = args[0]
        try:
            tgtIP = gethostbyname(tgtHost)
            print('[+] Scan Results from: '+ tgtHost)
        except:
            print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
            return

    if (args[2]!=None):
        tgtIP = args[2]

    tgtPorts = args[1]

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan Results for: ' + tgtName[0])
    except:
        pass
    print('[+] Scan Results IP: ' + tgtIP)

    setdefaulttimeout(1)

    for tgtPort in tgtPorts:

        t = Thread(target=connScan, args=(tgtIP, int(tgtPort)))
        t.start()

def main():
    host, ports, ip = init_args()
    if (ports == ['None']):
        ports = [str(i) for i in range(1,1025)]

    portScan(host,ports,ip)


if __name__=='__main__':
    main()
    print("")
