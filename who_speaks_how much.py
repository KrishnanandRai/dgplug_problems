from bs4 import BeautifulSoup
import urllib.request
import requests

def extract_all_url(url):
    with urllib.request.urlopen(url) as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')
        links = soup.find_all('a')
        for tag in links:
            link = tag.get('href')
            if link.startswith('Logs'):
                loglink = "https://dgplug.org/irclogs/2017/" + link
                print(loglink)
                try:
                    r = requests.get(loglink)
                    with open('logcontent.txt', 'a') as file:
                        file.write(r.text)
                except:
                    pass

extract_all_url("https://dgplug.org/irclogs/2017/")
data = open('logcontent.txt').read()
log = data.split("\n")[1:-2]
record = {}
for line in log:
    user = line.split()[1].strip("<>")
    if user not in record:
        record[user]=1
    else:
        record[user] += 1

for user , no_of_lines in record.items():
    print(user + " : " + str(no_of_lines))
    


