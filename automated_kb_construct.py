import warnings

import requests
from bs4 import BeautifulSoup
import csv
warnings.filterwarnings("ignore")

# faultencoding('ut
# f8')

r = requests.get("http://www.concordia.ca/academics/graduate/calendar/current/encs/computer-science-courses.html")

soup=BeautifulSoup(r.content)
soup_main=soup.find_all("span",{"class":"large-text"})
#''.join(third_p.find('br').next_siblings)
Topics_file = open('TopicsExtracted2.csv', 'w', encoding="utf-8")

with open('Automated_KB_Construct.csv', mode='w') as scrapper_file:
  scrapper_writer = csv.writer(scrapper_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  scrapper_writer.writerow(["Course Name","Course subject","Course number","Course description"])
  #scrapper_writer.close()
counter=0
for lis in soup_main:
  counter+=1
  if counter>34:
    subject=str(lis.find("b")).replace("<b>","").replace("</b>","").replace("(*)","")
    name=subject.replace(subject.split()[0],"").replace(subject.split()[1],"").lstrip()
    subject_act=subject.split()[0]
    number=subject.split()[1]
    test_str=str(lis)
    test_str2=test_str[test_str.find("\n")+1:]
    description=test_str2.replace("</span>","").replace('<span class="large-text">',"").replace("<i>","").replace("</i>","").replace("</i>","").replace("<br/>","").replace("<b>","").replace("</b>","").lstrip()
    with open('Automated_KB_Construct.csv', mode='a',encoding="utf-8") as scrapper_file:
      scrapper_writer = csv.writer(scrapper_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
      if subject_act=="SOEN" and number=="8901":
        scrapper_writer.writerow([name,subject_act,number])
      else:
        scrapper_writer.writerow([name,subject_act,number,description])

    SearchString = name + description
    parameters = {"text": SearchString}
    response = requests.get('https://api.dbpedia-spotlight.org/en/annotate', params=parameters)
    soup2 = BeautifulSoup(response.text, 'html.parser')
    lt = soup2.findAll('a')
    print(response)

    # wr = csv.writer(Topics_file, quoting=csv.QUOTE_MINIMAL)

    with open('TopicsExtracted2.csv', mode='a',encoding="utf-8") as Topics_file:
      Topics_writer = csv.writer(Topics_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
      for l in lt:
        print(l.get_text(), l.get('href'))
        Topics_writer.writerow([name, l.get_text(), l.get('href')])


