import warnings

import requests
from bs4 import BeautifulSoup
import csv

from rdflib import Graph, URIRef, Namespace, Literal, BNode

foaf = Namespace("http://xmlns.com/foaf/0.1/")
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
v= Namespace("http://www.w3.org/2006/vcard/ns#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
g =Graph()

g.parse('KG.ttl',format='n3')
with open('StudentRecord.csv',"r") as student_file:
    student = csv.reader(student_file, delimiter=',')
    counter = 0
    for row in student:
        if counter == 0:
            counter+=1;
        else:
            student_id = row[0]
            student_firstname = str(row[1])
            student_lastname = str(row[2])
            student_email = str(row[3])
            student_enrolled_subject = row[4]
            student_enrolled_snumber = row[5]
            course_name = URIRef("http://focu.io/data#"+str(row[6]).replace(" ","%"))
            student_grade = row[7]
            student_enrolled_term = row[8]
            b_node = BNode()
            student_node = BNode()
            g.add((student_node,rdf.type,focu.Student))
            g.add((student_node,foaf.givenName,Literal(student_firstname)))
            g.add((student_node,foaf.familyName, Literal(student_lastname)))
            g.add((student_node,v.email,Literal(student_email)))
            g.add((student_node,focu.student_id,Literal(student_id)))
            g.add((b_node,foaf.name,course_name))
            g.add((b_node, focu.course_number_is, Literal(student_enrolled_snumber)))
            g.add((b_node, focu.course_subject, Literal(student_enrolled_subject)))
            g.add((b_node, focu.grades_achieved, Literal(student_grade)))
            g.add((b_node, focu.enrolled_term, Literal(student_enrolled_term)))
            g.add((student_node, focu.student_enrolled, b_node))

g.serialize('KG.ttl',format='turtle')
for items in g:
    print(items)
