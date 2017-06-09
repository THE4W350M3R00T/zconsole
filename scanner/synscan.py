from scapy.all import sr1,send,TCP,IP,ICMP
class module:
    def __init__(self):
        self.description = 'A syn portscanner'
        self.name = 'syn scanner'
        self.help = 'RHOST Host to scan\nMINPORT the lowest port to scan\nMAXPORT the maximum port to scan'
        self.RHOST = '127.0.0.1'
        self.MINPORT = 1
        self.MAXPORT = 1024
    def checkup(self):
        print('[*] Pinging host')
        pkt = IP(dst=self.RHOST)/ICMP()
        answer = sr1(pkt,timeout=5,verbose=0)
        if answer != None:
            print('[*] Host is up')
            return True
        else:
            print('[-] Host seems down')
            return False
    def checkport(self,port):
        pkt = IP(dst=self.RHOST)/TCP(dport=port,flags='S')
        answer = sr1(pkt,timeout=5,verbose=0)
        if answer['TCP'].flags != 18:
            return False
        else:
            send(IP(dst=self.RHOST)/TCP(dport=port,flags='R'),verbose=0)
            return True
    def main(self):
        if not self.checkup():
            print('[-] Exiting')
        else:
            self.MINPORT = int(self.MINPORT)
            self.MAXPORT = int(self.MAXPORT)+1
            for port in range(self.MINPORT,self.MAXPORT):
                if self.checkport(port):
                    print('[*] Port '+str(port)+' is open')
            print('[*] Finished')
