import os, sys
import requests
import bs4 as bs
import urllib.request

class dox:
        
    def __init__(self, namefile, fullname, site):
        self.site = site
        self.fullname = fullname
        self.namefile = namefile
        self.filename = open(self.namefile, 'w')

    def info(self):
        infolist = ["Usernames: ", "E-mail: ", "Full name: ", "Age: ", "City: ", "Zip/Postal: ", "State/Province: ", "Country: ", "IP address: ", "ISP: ", "Home address: ", "Phone numbers: ", "Social Networks: ", "Other: "]
        for x in range(len(infolist)):
            enter = input(infolist[x])
            if enter == "exit":
                sys.exit(1)
            else:
                self.filename.write(infolist[x] + enter + "\r\n")
        print("Saved results in {}\nDirectory: {}".format(self.namefile, os.getcwd()))

    def ipsearch(self, ip):
        url1 = urllib.request.Request("https://ipaddress.ip-adress.com/" + str(ip), headers=headers)
        
        page = urllib.request.urlopen(url1)
        pageread = page.read()
        soup = bs.BeautifulSoup(pageread, 'html.parser')
        s1 = soup.find_all('th')
        s2 = soup.find_all('td')
        for i in range(len(s1)):
            print(str(s1[i].text) + ": " + str(s2[i].text))
        print("-----------------------------------")
        url = urllib.request.Request("https://www.ip2location.com/demo/" + str(ip), headers=headers)
        
        page2 = urllib.request.urlopen(url)
        page2read = page2.read()
        soup2 = bs.BeautifulSoup(page2read, 'html.parser')
        for pas in soup2.find_all('td'):
            p = pas.text
            p = p.split("Shortcut")[0]
            p = p.split("http://www.ip2location.com/31.13.64.35")[0]
            p = p.split("Twitterbot")[0]
            p = p.split("@ip2location 31.13.64.35")[0]
            p = p.split("Slackbot")[0]
            p = p.split("/ip2location 31.13.64.35")[0]
            p = p.strip("\n")
            p = p.strip('\t\t\t\t\t\t')
            p = p.strip('\t\t\t\t\t\t\xa0\xa0\r')
            p = p.strip('\r')
            p = p.strip()
            print(p)
        return "-------------------------------".strip()
    
     def fullname2(self, fullname):
        url = 'http://webmii.com/people?n="' + str(fullname.replace(' ', '+')) + '"'
        urlist = []
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = bs.BeautifulSoup(response.text, 'html.parser')
        for p in soup.find_all('a'):
            p = p.get('href')
            urlist.append(p)
           # if "twitter.com" in p:
           # 	print(p)
        urlist = list(set(urlist))
        for ul in urlist:
            if "twitter.com" in ul:
                print(ul)
              
    def whois(self, site):
        command = os.popen("whois " + str(site))
        result = command.read()
        print(result)
