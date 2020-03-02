from rdflib import Namespace
from rdflib import Literal
from rdflib import BNode
import requests
import csv
def kg_builder(g):
    topics=open("TopicsExtracted2.csv",'r')
    random_data=open("Random_Stu_data.csv",'r')
    Course_data=open("Automated_KB_Construct.csv",'r')

    foaf = Namespace("http://xmlns.com/foaf/0.1/")
    focu = Namespace("http://focu.io/schema#")
    focudata = Namespace("http://focu.io/data#")
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

    for rows in Course_data:
        row_data=rows.split(',')
        course_name=row_data[0]
        course_name_join='_'.join(row_data[0].split(' '))
        course_dept=row_data[1]
        course_number=row_data[2]
        course_description=' '.join(row_data[3:])
        g.add(BNode("http://focu.io/data#"+course_name_join, rdf.type, focu.Course)
        g.add(BNode("http://focu.io/data#"+course_name_join, focu.course_name, Literal(course_name))
        g.add(BNode("http://focu.io/data#"+course_name_join, focu.course_subject, Literal(course_dept))
        g.add(BNode("http://focu.io/data#"+course_name_join, focu.course_number, Literal(course_number))
        g.add(BNode("http://focu.io/data#"+course_name_join, focu.course_description, Literal(course_description))
        g.serialize(format='turtle')