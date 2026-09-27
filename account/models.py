from django.db import models

# Create your models here.
class user(models.Model):
    role_choce=[
        ("jobseeker",'jobseeker'),
        ("company",'company')
    ]
    email=models.EmailField(max_length=30,unique=True)
    OTP=models.PositiveIntegerField(default=123)
    password=models.CharField(max_length=15)
    role=models.CharField(max_length=50,choices=role_choce)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class jobseeker(models.Model):
    user_fk=models.ForeignKey(user,on_delete=models.CASCADE)
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    number=models.PositiveIntegerField()
    skills=models.CharField(max_length=50)
    p_h=models.TextField(null=True,blank=True)
    location=models.CharField(max_length=40,null=True,blank=True)
    web=models.CharField(max_length=30,null=True,blank=True)
    profile_pic=models.FileField(upload_to="jobseeker/",default="default_pic.png")
    about_summary=models.TextField(null=True,blank=True)
    Institute=models.TextField(null=True,blank=True)
    degree=models.CharField(max_length=30,null=True,blank=True)
    s_year=models.PositiveIntegerField(null=True,blank=True)
    e_year=models.PositiveIntegerField(null=True,blank=True)
    percentage=models.FloatField(max_length=2,null=True,blank=True)
    

    
    def __str__(self):
        return self.f_name+" "+self.l_name

class departments(models.Model):
    d_name=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.d_name 

class company(models.Model):
    co_choice=[
        ("Software","Software"),
        ("Finance","Finance"),
        ("Healthcare","Healthcare"),
        ("Marketing","Marketing"),
        ("Education","Education"),
        ("other..","other..")
    ]
    size_choice=[
        ('1-10',"1-10"),
        ('11-50',"11-50"),
        ('51-200',"51-200"),
        ('201-500',"201-500"),
        ('500-1000',"500-1000"),
        ('1000+',"1000+")
    ]
    com_fk=models.ForeignKey(user,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,unique=True)
    company_tagline=models.CharField(max_length=20,null=True,blank=True)
    website=models.CharField(max_length=50)
    industry_type=models.CharField(max_length=20,choices=co_choice,null=True,blank=True)
    company_size=models.CharField(max_length=20,null=True,blank=True,choices=size_choice)
    founded_year=models.PositiveIntegerField(null=True,blank=True)
    hq_location=models.TextField(null=True,blank=True)
    about_summary=models.TextField(null=True,blank=True)

    logo=models.FileField(upload_to="company/",default="logo.png")
    cover_image=models.FileField(upload_to='company/',default="cover_image.png")
    def __str__(self):
        return self.name

class Chat(models.Model):
    jid_sender=models.ForeignKey(jobseeker,on_delete=models.CASCADE,related_name="jid_sender")
    jid_resever=models.ForeignKey(jobseeker,on_delete=models.CASCADE,related_name="jid_resever")
    # releted name pro models.py me ek hi ho sakta hai agar mujhe id milti hai or mujhe us id ne kitne chat 
    # send kiya hai vo dekhna hai to mai Chat.object.filter(jid_sender.id=id) rakhta hu to mujhe chat mil jayegi
    # par agar mujhe releted name se karna ho to  to pehle mujhe mustved=jobseeker.objects.get(id=id) se uska object nikalna 
    # hoga  fir me direct  mustved.jid_sender.all() sari chat nikal sakta hu ye automatic samajh jayega ki mujhe 
    # ye karna hai Chat.object.filter(jid_sender.id=id)
    massage=models.TextField(blank=True,null=True)
    fraind=models.CharField(max_length=20,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jid_sender} sended to {self.jid_resever}"

class Requests(models.Model):
    jid_r_sender=models.ForeignKey(jobseeker,on_delete=models.CASCADE,related_name="jid_r_sender")
    jid_r_resever=models.ForeignKey(jobseeker,on_delete=models.CASCADE,related_name="jid_r_resever")
    Request=models.CharField(max_length=20,null=True,blank=True)
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[ {self.jid_r_sender} ] -> sended request to -> [ {self.jid_r_resever} ]"