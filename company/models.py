from django.db import models
from django.utils import timezone
import math
from account.models import *
# Create your models here.
class post_jobs(models.Model):
    e_type=[
        ('Full-Time','Full-Time'),
        ('Part-Time','Part-Time'),
        ('Contract','Contract'),
        ('Internship','Internship'),
        
    ]
    exp_level=[
        ('Fresher','Fresher'),
        ('Junior (1-3 yrs)','Junior (1-3 yrs)'),
        ('Mid-level (3-5 yrs)','Mid-level (3-5 yrs)'),
        ('Senior (5+ yrs)','Senior (5+ yrs)'),
        ('Lead / Architect (8+ yrs)','Lead / Architect (8+ yrs)')
    ]
    company_fk=models.ForeignKey(company,on_delete=models.CASCADE)
    job_title=models.CharField(max_length=30)
    department_fk=models.ForeignKey(departments,on_delete=models.CASCADE)
    employment_type=models.CharField(max_length=20,choices=e_type)
    location=models.TextField()
    min_salary=models.PositiveIntegerField()
    max_salary=models.PositiveIntegerField()
    experience=models.CharField(max_length=30,choices=exp_level)
    key_skils=models.TextField()
    job_discription=models.TextField()
    post_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_fk.name
    def whenpublished(self):
        
        now = timezone.now()
        
        diff= now - self.post_time

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"