import warnings

import requests
from bs4 import BeautifulSoup
import csv

from rdflib import Graph, URIRef, Namespace, Literal, BNode
from  urllib.parse import quote

foaf = Namespace("http://xmlns.com/foaf/0.1/")
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
v= Namespace("http://www.w3.org/2006/vcard/ns#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
g =Graph()

g.parse('NewBase.ttl',format='n3')
with open('StudentRecord.csv',"r") as student_file:
    student = csv.reader(student_file, delimiter=',')
    counter = 0
    for row in student:
        if counter == 0:
            counter+=1;
        else:
            student_id = row[0]
            student_firstname = str(row[1]).strip()
            student_lastname = str(row[2]).strip()
            student_email = str(row[3])
            program = str(row[4])
            student_enrolled_subject = row[5]
            student_enrolled_snumber = row[6]
            course_name = URIRef("http://focu.io/data#"+str(row[7]).replace(" ","%"))
            student_grade = row[8]
            student_enrolled_term = row[9]
            b_node = BNode()
            print("http://focu.io/data#"+quote(str(student_lastname+student_firstname)))
            student_node = URIRef("http://focu.io/data#"+quote(str(student_lastname+student_firstname)))
            print(student_node)
            g.add((student_node,rdf.type,focu.Student))
            g.add((student_node,foaf.givenName,Literal(student_firstname)))
            g.add((student_node,foaf.familyName, Literal(student_lastname)))
            g.add((student_node,v.email,Literal(student_email)))
            g.add((student_node,focu.student_id,Literal(student_id)))
            g.add((b_node,foaf.name,course_name))
            g.add((b_node, focu.Course_number, Literal(student_enrolled_snumber)))
            g.add((b_node, focu.Course_Subject, Literal(student_enrolled_subject)))
            g.add((b_node, focu.grades_achieved, Literal(student_grade)))
            g.add((b_node, focu.enrolled_term, Literal(student_enrolled_term)))
            g.add((student_node, focu.student_enrolled, b_node))

g.serialize('NewBase.ttl',format='turtle')
for items in g:
    print(items)
