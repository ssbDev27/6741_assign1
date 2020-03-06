import warnings

import requests
from bs4 import BeautifulSoup
import csv

from rdflib import Graph, URIRef, Namespace, Literal, BNode

foaf = Namespace("http://xmlns.com/foaf/0.1/")
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
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
            student_name = URIRef("http://focu.io/data#"+str(row[1]).replace(" ","%"))
            student_enrolled_subject = row[2]
            student_enrolled_snumber = row[3]
            course_name = URIRef("http://focu.io/data#"+str(row[4]).replace(" ","%"))
            student_grade = row[5]
            student_enrolled_term = row[6]
            b_node = BNode("data")
            print("student_enrolled_term")
            g.add((student_name,rdf.type, focu.student))
            g.add((student_name, focu.student_name, Literal(student_name)))
            g.add((student_name, focu.student_id, Literal(student_id)))
            g.add((b_node,focu.course_name_is,course_name))
            g.add((b_node, focu.course_number_is, Literal(student_enrolled_snumber)))
            g.add((b_node, focu.course_subject, Literal(student_enrolled_subject)))
            g.add((b_node, focu.grades_achieved, Literal(student_grade)))
            g.add((b_node, focu.enrolled_term, Literal(student_enrolled_term)))
            g.add((student_name, focu.student_enrolled, b_node))

g.serialize('KG.ttl',format='turtle')
for items in g:
    print(items)
