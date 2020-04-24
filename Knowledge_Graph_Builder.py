
from rdflib import Namespace, URIRef
from rdflib import Literal
from rdflib import BNode
from rdflib import Graph
import requests
import csv

# topics=open("TopicsExtracted2.csv",'r')
# random_data=open("Random_Stu_data.csv",'r')
Course_data = open("Automated_KB_Construct.csv", 'r')
ttl_file = open("KG.ttl","a")
foaf = Namespace("http://xmlns.com/foaf/0.1/")
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
counter = 0

g = Graph()
g.parse("NewBase.ttl", format='n3')

files = ['grad_data.csv','under_grad_data.csv']
for i in range(len(files)):
    escaped_winpath = ("%r" % files[i]).replace("'",'')
    with open(escaped_winpath,encoding ='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        counter =0
        for row in csv_reader:
            print(row)
            counter +=1
            if counter > 2 and counter < 5:
                course_name = URIRef("http://focu.io/data#"+str(row[0]).replace(" ","%"))
                # print(course_name)
                course_dept = row[1]
                course_number = row[2]
                try:
                    course_description = row[3]
                except:
                    course_description =""
                g.add((course_name, rdf.type, focu.Course))
                g.add((course_name,foaf.name,Literal(str(row[0]))))
                g.add((course_name, focu.Course_Subject, Literal(course_dept)))
                g.add((course_name, focu.Course_number, Literal(course_number)))
                g.add((course_name, focu.Description, Literal(course_description)))
                if i == 0:
                    g.add((course_name,focu.Program,Literal("Graduate")))
                else:
                    g.add((course_name, focu.Program, Literal("Undergraduate")))
    g.serialize('NewBase.ttl',format='turtle')

for items in g:
    print(items)


def kg_builder(g):
    topics = open("TopicsExtracted2.csv",'r')
    random_data = open("Random_Stu_data.csv",'r')
    Course_data = open("Automated_KB_Construct.csv",'r')
