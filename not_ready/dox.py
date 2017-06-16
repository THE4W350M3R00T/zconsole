import os, sys
import requests
import bs4 as bs
import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}

class dox:
        
    def __init__(self, namefile, site):
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
    
    def pipl(self, name):
        url = "https://pipl.com/search/?q=" + str(name.replace(' ', '+')) + "&l=&sloc=&in=6"
        return url

    def fullname2(self, fullname):
        url = 'http://webmii.com/people?n="' + str(fullname.replace(' ', '+')) + '"'
        urlist = []
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = bs.BeautifulSoup(response.text, 'html.parser')
        print("Youtube channels found: ")
        for p in soup.find_all('a'):
            p = p.get('href')
            if p:
                if "youtube.com/" in p:
                    print(p)
        for p in soup.find_all('a'):
            p = p.get('href')
            if p:
                if "twitter.com/" in p:
                    urlist.append(p)
        urlist = list(set(urlist))
        print("Twitter accounts found: ")
        for ul in urlist:
            print(ul)
        print("Related people found: ")
        for p in soup.find_all('td'):
            print(p.text)
        print("Tags: ")
        for p in soup.find_all(id="tags"):
            p = p.text
            p = p.replace('\n', '')
            print(p)
    
    def username(self, username):
        url = "http://socialmention.com/search?t=all&q=" + str(username.replace(' ', '+')) + "&btnG=Search"
        response = requests.get(url, headers=headers)
        soup = bs.BeautifulSoup(response.text, 'html.parser')
        urllist = []
        for url in soup.find_all("h3", "a"):
            print(url)
        print(urllist)

    def username2(self, username):
        url = "https://usersearch.org/results_advanced.php?URL_username=" + str(username.replace(' ', '+'))
        response = requests.get(url, headers=headers)
        soup = bs.BeautifulSoup(response.text, 'html.parser')
        urllist = []
        for url in soup.find_all('a'):
            url = url.get('href')
            urllist.append(url)
        for ul in urllist:
            if "help" in ul:
                urllist.remove(ul)
            if "/discussions/forum/1/" in ul:
                urllist.remove(ul)
            if "Can_I_delete_my_account" in ul:
                urllist.remove(ul)
            if "faq" in ul:
                urllist.remove(ul)
            if "blog/index.ph" in ul:
                urllist.remove(ul)
            if "privacy." in ul:
                urllist.remove(ul)
            if "index.ph" in ul:
                urllist.remove(ul)
            if 'http://www.everify.com/?s=rw&addPixel=yes&source=' in ul:
                urllist.remove(ul)
        for final in urllist:
            print(final)

    def randomemail(self, email):
        print("Spokeo:\nhttp://www.spokeo.com/email-search/search?g=email_pt_lullar_text_0131&e=" + str(email))
        print("Instagram:\nhttps://instagram.com/" + str(email.replace("@gmail.com", '')))
        print("Facebook:\nhttp://www.facebook.com/search/?q=" + str(email))
        print("Youtube:\nhttp://www.youtube.com/results?search_query=" + str(email))
        print("Tumblr:\nhttp://www.tumblr.com/blog/" + str(email.replace("@gmail.com", '')))
        print("Google Plus:\nhttps://plus.google.com/s/" + str(email.replace("@gmail.com", '')) + "/people")

    def USAfullname1(self, fullname):
        url = "https://www.intelius.com/people-search/" + str(fullname.replace(' ', '-'))
        page = requests.get(url, headers=headers)
        soup = bs.BeautifulSoup(page.text, 'html.parser')
        agelist = []
        for p in soup.find_all('span'):
            p = p.text
            p = p.replace("\n", ' ').strip()
            agelist.append(p)
        newlist = []
        for p in agelist:
            if "$" in p:
                p1 = p.replace(str(p), '')
            if "Advance Roofing" in p:
                p = p1.replace(str(p), '')
            newlist.append(p)
        del newlist[0:19]
        print("---------------------------------")
        print("Results for: {}".format(fullname))
        print("Sorted by: name, age, has lived in, has worked at, has studied at and related to.")
        for n in newlist:
            print(n.replace('    ', ''))
        
    def whois(self, site):
        command = os.popen("whois " + str(site))
        result = command.read()
        print(result)
