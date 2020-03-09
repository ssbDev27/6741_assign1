import warnings

import requests
from bs4 import BeautifulSoup
import csv
from collections import Counter
warnings.filterwarnings("ignore")

# faultencoding('ut
# f8')

#r = requests.get("http://www.concordia.ca/academics/graduate/calendar/current/sgs/indi-ma-msc.html")
#r = requests.get("http://www.concordia.ca/academics/graduate/calendar/current/sgs/indi-phd.html")
#r= requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/adip-dip.html")
#r= requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/apli-ma.html")
#r= requests.get("http://www.concordia.ca/academiacs/graduate/calendar/current/fasc/biol-msc.html#phd-msc-courses")
#r= requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/biol-phd.html#phd-msc-courses")
#r= requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/chem-msc.html#courses")
#r= requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/chem-phd.html#courses")
#r= requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/chem-phd.html#courses")
#r= requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/econ-ma.html#courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/engl-ma.html#courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/geog-menv.html#courses-menv")
#r=requests.get("http://www.concordia.ca/academics/graduate/exercise-science-msc.html")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/hist-ma.html#courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/ahsc-ma.html#ma-courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/reli-judaic-ma.html#MAJudCourses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/mast-ma-msc.html#ma-msc-courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/coms-ma.html#courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/phil.html#courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/physics-msc.html")
####r=requests.get("http://www.concordia.ca/artsci/polisci/programs/graduate/ma-political-science/courses.html")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/psyc-ma.html#courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/socianth-ma.html#ma-social-cultural-courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/theo.html#courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fasc/ftra-ma.html#cours")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fofa/arte-ma.html")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fofa/arth-ma.html")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fofa/cats-art.html#cats-courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fofa/fmst-ma.html#MA-courses")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/sgs/indi-ma-msc.html")
#r=requests.get("http://www.concordia.ca/academics/graduate/calendar/current/fofa/star.html#courses")
r=requests.get("http://www.concordia.ca/jmsb/mba/program/curriculum/courses.html#MBA-640")




soup=BeautifulSoup(r.content)
soup_main=soup.find_all("span",{"class":"large-text"})
#''.join(third_p.find('br').next_siblings)
#Topics_file = open('TopicsExtracted.csv', 'w', encoding="utf-8")

# with open('Automated_KB_Construct.csv', mode='w') as scrapper_file:
#   scrapper_writer = csv.writer(scrapper_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#   scrapper_writer.writerow(["Course Name","Course subject","Course number","Course description"])
#   #scrapper_writer.close()
counter=0
for lis in soup_main:
  counter+=1
  if counter>0:
    print(lis)
    subject=str(lis.find("b")).replace("<b>","").replace("</b>","").replace("(*)","").replace("(***)","")
    name=""
    try:
      name = subject.replace(subject.split()[0], "").replace(subject.split()[1], "").lstrip()
    except:
      continue
    subject_act=subject.split()[0]
    number=subject.split()[1]
    test_str=str(lis)
    test_str2=test_str[test_str.find("\n")+1:]
    description=test_str2.replace("<span class=large-text>","").replace("(***)","").replace('"',"").replace("</span>","").replace('<span class="large-text">',"").replace("<i>","").replace("</i>","").replace("</i>","").replace("<br/>","").replace("<b>","").replace("</b>","").lstrip()
    if name.find("\n")==-1 and number.isnumeric() and description.find("href")==-1 and description.find("<span class=large-text>")==-1 and description.find("credits)")==-1 and Counter(description)['\n']<8:
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