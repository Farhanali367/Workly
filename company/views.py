from django.shortcuts import render, redirect
from account.views import loginvalidate
from account.models import *
from company.models import *
from jobseeker.models import *
# ── Dashboard & Profile ──────────────────────────────────────────
@loginvalidate
def dashboard(request):
    return render(request, 'company/dashboard.html', {
        'uid': request.uid, 'cid': request.cid, 'name': 'dashboard'})

@loginvalidate
def profile(request):
    return render(request, 'company/profile.html', {
        'uid': request.uid, 'cid': request.cid, 'name': 'profile'})

@loginvalidate
def edit_profile(request):
    d_all=departments.objects.all()
    if request.POST:
        cid=request.cid
        uid=request.uid
        cid.name=request.POST['name']
        cid.company_tagline=request.POST['company_tagline']
        cid.website=request.POST['website']
        cid.industry_type=request.POST['industry_type']
        cid.company_size=request.POST['company_size']
        cid.founded_year=request.POST['founded_year']
        cid.hq_location=request.POST['hq_location']
        cid.about_summary=request.POST['about_summary']
        cid.save()
        if request.FILES:
            if "logo" in request.FILES:    
                cid.logo=request.FILES['logo']
            else:
                cid.cover_image=request.FILES['cover_image']
            cid.save()
        return redirect('company:profile')
    else:
        return render(request, 'company/edit-profile.html', {
            'uid': request.uid, 'cid': request.cid, 'name': 'profile'})
            # d_all me dipartrment hai
            # jab hum edit_profile ka ke ander ayenge to vo pehle to yhi aye ga q ki abhi usko reques.post nhi mili hai na to yha ane ke 
            # bad ye ham ko edit_profile ka page dikhaye ga fir jub hum form bhar ke submit karenge to request.POST aye gi

@loginvalidate
def jobs(request):
    con={
        'uid':request.uid,
        'cid':request.cid,
        'name':'jobs'
    }
    return render(request,'company/jobs.html',con)

@loginvalidate
def create_jobs(request):
    d_all=departments.objects.all()
    if request.POST:
        job_title=request.POST['job_title']
        employment_type=request.POST['employment_type']
        location=request.POST['location']
        min_salary=request.POST['min_salary']
        max_salary=request.POST['max_salary']
        experience=request.POST['experience']
        key_skils=request.POST['key_skils']
        job_discription=request.POST['job_discription']
        dip_name=request.POST['dip_name']
        did=departments.objects.get(d_name=dip_name)

        jobid=post_jobs.objects.create(
            company_fk=request.cid,
            job_title=job_title,
            department_fk=did,
            employment_type=employment_type,
            location=location,
            min_salary=min_salary,
            max_salary=max_salary,
            experience=experience,
            key_skils=key_skils,
            job_discription=job_discription
        )
        con={
            'uid':request.uid,
            'cid':request.cid,
            'name':'jobs',
            'd_all':d_all
        }
        return render(request,'company/create-job.html',con)
    else:
        con={
            'uid':request.uid,
            'cid':request.cid,
            'name':'jobs',
            'd_all':d_all
        }
        return render(request,'company/create-job.html',con)

@loginvalidate
def applications(request):
    all_applicant=Apply.objects.filter(jobs_fk__company_fk=request.cid)
    uid=request.uid
    cid=request.cid
    con={
        'applications':all_applicant,
        'cid':cid,
        'uid':uid,
        'name':'applications'
    }
    return render(request,'company/applications.html',con)

@loginvalidate
def applicant(request):
    if request.POST:
        pk=int(request.POST['pk'])
        status=request.POST['status']
        applicant=Apply.objects.get(id=pk)
        applicant.status=status
        applicant.save()
        uid=request.uid
        cid=request.cid
        con={
            'applicant':applicant,
            'cid':cid,
            'uid':uid,
            'name':'applications'
        }
        return render(request,'company/application-details.html',con)
    return redirect("company:dashboard")


@loginvalidate
def sta_tus(request):
    if request.POST:
        pk=int(request.POST['pk'])
        applicant=Apply.objects.get(id=pk)
        if "Shortlisted" in request.POST:
            applicant.status=request.POST['Shortlisted']
            applicant.save()
            return redirect("company:applications")
        elif "Interview" in request.POST:
            applicant.Schedule_date=request.POST['date']
            applicant.Schedule_time=request.POST['time']
            applicant.Interviewer_Name=request.POST["e_name"]
            applicant.status=request.POST['Interview']
            applicant.save()
            return redirect("company:applications")
        elif "Rejected" in request.POST:
            applicant.status=request.POST['Rejected']
            applicant.save()
            return redirect("company:applications")
    return redirect("company:dashboard")