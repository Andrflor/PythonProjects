import socket
import sys

def ret_banner(ip,port):

    """
        C'est marrant de faire des gauffres yummy
    """

    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return "marche pas PD"

if __name__=="__main__":
    if len(sys.argv)==2:
        print("Banner = %s" % ret_banner(sys.argv[1],21))
    pass
