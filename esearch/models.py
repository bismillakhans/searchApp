
from django.db import models
from .es_call import BlogPostIndex,CollegeInfoIndex,CollegeCourseIndex
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Blogpost to be indexed into ElasticSearch
class BlogPost(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
   posted_date = models.DateField(default=timezone.now)
   title = models.CharField(max_length=200)
   text = models.TextField(max_length=1000)

   def indexing(self):

        obj = BlogPostIndex(
        meta={'id': self.id},
        author=self.author.username,
        posted_date=self.posted_date,
        title=self.title,
        text=self.text)
        obj.save()
        return obj.to_dict(include_meta=True)

  
class CourseCourse(models.Model):
    short_name = models.CharField(max_length=200, blank=True, null=True)
    full_form = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    avg_fees = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    degree = models.CharField(max_length=200, blank=True, null=True)
    mode = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.CharField(max_length=200, blank=True, null=True)
    updated_on = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    slug_name = models.CharField(max_length=200)
    course_image = models.CharField(max_length=100)
    career_scope = models.TextField()
    eligibility = models.TextField()
    duration_in_month = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'course_course'


class CourseStream(models.Model):
    course_id = models.CharField(max_length=10, blank=True, null=True)
    stream = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    full_form = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.CharField(max_length=200, blank=True, null=True)
    s_duration = models.CharField(max_length=200, blank=True, null=True)
    s_stream = models.CharField(max_length=200, blank=True, null=True)
    s_type = models.CharField(max_length=200, blank=True, null=True)
    short_form = models.CharField(max_length=200, blank=True, null=True)
    type_id = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_stream'


class NewCollegeBasicInfo(models.Model):
    college_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    country_id = models.CharField(max_length=200, blank=True, null=True)
    state_id = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    university_id = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    accredited_by = models.CharField(max_length=200, blank=True, null=True)
    approved_by = models.CharField(max_length=200, blank=True, null=True)
    campuz_size = models.CharField(max_length=200, blank=True, null=True)
    established_on = models.CharField(max_length=200, blank=True, null=True)
    genders_accepted = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    logo = models.CharField(max_length=1000, blank=True, null=True)
    ownership = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    course_types = models.CharField(max_length=200, blank=True, null=True)
    degrees = models.CharField(max_length=200, blank=True, null=True)
    colg_type = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.CharField(max_length=200, blank=True, null=True)
    created_time = models.CharField(max_length=200, blank=True, null=True)
    affiliation = models.CharField(max_length=200, blank=True, null=True)
    banner = models.TextField(blank=True, null=True)
    facilities = models.CharField(max_length=200, blank=True, null=True)
    modification_time = models.CharField(max_length=200, blank=True, null=True)
    placement = models.CharField(max_length=200, blank=True, null=True)
    placement_average = models.CharField(max_length=200, blank=True, null=True)
    placement_high = models.CharField(max_length=200, blank=True, null=True)
    short_desc = models.TextField(blank=True, null=True)
    scholarship_providing_college = models.CharField(max_length=10)
    college_website = models.CharField(max_length=200)
    banner_alt_text = models.CharField(max_length=200)
    logo_alt_text = models.CharField(max_length=200)
    college_name_slug = models.CharField(max_length=200)
    top_courses = models.CharField(max_length=200)
    placement_description = models.TextField()
    keywords = models.CharField(max_length=200)
    verified_by_college_partner = models.CharField(max_length=45)
    college_partner_id = models.CharField(max_length=200)
    commission = models.CharField(max_length=200)
    approved_by_admin = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'new_college_basic_info'

    def indexing(self):
        obj = CollegeInfoIndex(
            meta={'id': self.id},
            college_name=self.college_name,
           
        )
        obj.save()
        return obj.to_dict(include_meta=True)


class NewCollegeCollegeCities(models.Model):
    country_id = models.CharField(max_length=200, blank=True, null=True)
    state_id = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_college_college_cities'


class NewCollegeCourseNewCourseInfo(models.Model):
    college_id = models.CharField(max_length=200, blank=True, null=True)
    course_id = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    course_type_id = models.CharField(max_length=200, blank=True, null=True)
    avg_fees = models.CharField(max_length=200, blank=True, null=True)
    degree = models.CharField(max_length=200, blank=True, null=True)
    course_mode = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.CharField(max_length=200, blank=True, null=True)
    updated_on = models.CharField(max_length=200, blank=True, null=True)
    college_course_name = models.CharField(max_length=200, blank=True, null=True)
    college_stream_name = models.CharField(max_length=200, blank=True, null=True)
    specialization_id = models.CharField(max_length=200, blank=True, null=True)
    scholarship_amount = models.CharField(max_length=200)
    alloted_seat = models.CharField(max_length=200)
    booking_fee = models.CharField(max_length=200)
    combination_or_add_on = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    donation = models.CharField(max_length=200)
    fee_type = models.CharField(max_length=200)
    fees = models.CharField(max_length=200)
    package = models.CharField(max_length=200)
    reg_or_admission_fees = models.CharField(max_length=200)
    scholarship_college_category = models.CharField(max_length=200)
    seat_details = models.CharField(max_length=200)
    course_categories = models.CharField(max_length=200)
    description = models.TextField()
    course_fee_type = models.CharField(max_length=200)
    sem_or_year_fee = models.CharField(max_length=200)
    top_courses = models.CharField(max_length=200)
    eligibility = models.TextField()
    seats = models.CharField(max_length=300)
    on_demand_seats = models.CharField(max_length=300)
    add_on_courses_id = models.CharField(max_length=200)
    note = models.CharField(max_length=300)
    college_partner_id = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'new_college_course_new_course_info'

    def indexing(self):
        obj = CollegeCourseIndex(
            meta={'id': self.id},
            college_id=self.college_id,
            college_course_name=self.college_course_name,
           
        )
        obj.save()
        return obj.to_dict(include_meta=True)


class NewCollegeStates(models.Model):
    country_id = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_college_states'
