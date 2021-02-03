from elasticsearch.helpers import bulk 
from elasticsearch import Elasticsearch 
from elasticsearch_dsl import Search, Q 
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text,Date
from . import models
from django.db import connection


connections.create_connection()

class BlogPostIndex(Document):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()

    class Index:
        name = 'blogpost-index'

class CollegeInfoIndex(Document):

    college_name = Text()

    class Index:
        name = 'college-index'


class CollegeCourseIndex(Document):

    college_id = Text()
    college_course_name = Text()

    class Index:
        name = 'course-index'
        
class DisplayDataIndex(Document):

    college_id = Text()
    college_course_name = Text()
    college_name = Text()
    city = Text()

    class Index:
        name = 'final-index'





def data_index():
    r=[]
    cursor=connection.cursor()
    cursor.execute('SELECT new_college_basic_info.id,new_college_basic_info.college_name,course_course.short_name,new_college_college_cities.city FROM new_college_basic_info JOIN new_college_course_new_course_info ON new_college_basic_info.id = new_college_course_new_course_info.id JOIN new_college_college_cities ON new_college_basic_info.city = new_college_college_cities.id JOIN course_course ON new_college_course_new_course_info.course_id = course_course.id;')
    results=cursor.fetchall()
    for i in results:
        obj = DisplayDataIndex(
        meta={'id': i[0]},
        college_id=i[0],
        college_name=i[1],
        college_course_name=i[2],
        city=i[3]
        )
        h=obj.to_dict(include_meta=True)
        r.append(h)
    return r



def bulk_indexing():
    DisplayDataIndex.init()
    es = Elasticsearch()
    dataValue=data_index()
    bulk(client=es, actions=(b for b in dataValue[:100]))



def esearch(college_course_name="",city="",term=1):      
    client = Elasticsearch()      
    q = Q("bool", should=[Q("match", college_course_name=college_course_name),Q("match", city=city)], minimum_should_match=term)
    s = Search(using=client, index="final-index").query(q)[0:20] 
    response = s.execute()
    # print('Total %d hits found.' % response.hits.total)     
    search = get_results(response)    
    return search  

def get_results(response): 
    results = []  
    for hit in response:
        result_tuple = (hit.college_id,hit.college_name)    
        results.append(result_tuple)  
    return results




