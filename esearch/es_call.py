from elasticsearch.helpers import bulk 
from elasticsearch import Elasticsearch 
from elasticsearch_dsl import Search, Q 
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text,Date
from . import models


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


# def bulk_indexing():

#     BlogPostIndex.init()
#     es = Elasticsearch()
#     bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))

# def bulk_indexing():
#     CollegeInfoIndex.init()
#     es = Elasticsearch()
#     bulk(client=es, actions=(b.indexing() for b in models.NewCollegeBasicInfo.objects.all().iterator()))

def bulk_indexing():
    CollegeInfoIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.NewCollegeCourseNewCourseInfo.objects.all()[:20].iterator()))



def esearch(college_course_name=""):      
    client = Elasticsearch()      
    q = Q("bool", should=[Q("match", college_course_name=college_course_name)], minimum_should_match=1)  
    s = Search(using=client, index="course-index").query(q)[0:20] 
    response = s.execute()
    # print('Total %d hits found.' % response.hits.total)     
    search = get_results(response)    
    return search  

def get_results(response): 
    results = []  
    for hit in response:
        result_tuple = (hit.college_id,hit.college_course_name)    
        results.append(result_tuple)  
    return results




