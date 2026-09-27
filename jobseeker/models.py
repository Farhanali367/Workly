from django.db import models
from account.models import jobseeker
from django.utils import timezone
import math
from company.models import post_jobs
# Create your models here.
class resumes(models.Model):
    job_fk=models.ForeignKey(jobseeker,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=30,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    number=models.PositiveIntegerField(null=True,blank=True)
    location=models.TextField(null=True,blank=True)
    linkedin=models.CharField(max_length=50,null=True,blank=True)
    pot_web=models.CharField(max_length=50,null=True,blank=True)
    summary=models.TextField(null=True,blank=True)
    degree=models.CharField(max_length=40,null=True,blank=True)
    Institute=models.CharField(max_length=50,null=True,blank=True)
    p_year=models.PositiveIntegerField(null=True,blank=True)
    percentage=models.CharField(max_length=50,null=True,blank=True)
    job_tital=models.CharField(max_length=20,null=True,blank=True)
    w_company_name=models.CharField(max_length=50,null=True,blank=True)
    job_description=models.TextField(null=True,blank=True)
    skills=models.CharField(max_length=50,null=True,blank=True)
    Project_detail=models.TextField(null=True,blank=True)
    degree=models.CharField(max_length=50,null=True,blank=True)
    Language=models.CharField(max_length=50,null=True,blank=True)
    
    resume=models.FileField(upload_to="jobseeker/resume/",null=True,blank=True)

    def __str__(self):
        return self.job_fk.f_name
    
class Posts(models.Model):
    job_fk=models.ForeignKey(jobseeker,on_delete=models.CASCADE)
    tital=models.CharField(max_length=30,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    image=models.FileField(upload_to="jobseeker/posts/",blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_date

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

    def __str__(self):
        return self.job_fk.f_name

class Apply(models.Model):
    job_fk=models.ForeignKey(jobseeker,on_delete=models.CASCADE)
    jobs_fk=models.ForeignKey(post_jobs,on_delete=models.CASCADE)
    resume_fk=models.ForeignKey(resumes,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    Schedule_date=models.CharField(max_length=10,null=True,blank=True)
    Schedule_time=models.CharField(max_length=5,null=True,blank=True)
    Interviewer_Name=models.CharField(max_length=30,null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"user:- {self.job_fk.f_name} -> job:- {self.jobs_fk.job_title}"

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_date

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

class SavedJob(models.Model):
    ch=[
        ('Active',"Active"),
        ('Deactive',"Deactive")
    ]
    job_fk=models.ForeignKey(jobseeker,on_delete=models.CASCADE)
    job_post_fk = models.ForeignKey(post_jobs,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=ch,default='Deactive')

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_at

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