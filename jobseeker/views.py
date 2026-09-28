from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from account.views import loginvalidate
from account.models import *
from company.models import *
from jobseeker.models import *
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.paginator import Paginator
from django.http import JsonResponse
import re
# Create your views here.

@loginvalidate
def dashboard(request):
    jid = request.jid
    uid = request.uid

    profile_fields = [
        'f_name',
        'l_name',
        'number',
        'skills',
        'p_h',
        'location',
        'web',
        'about_summary',
        'Institute',
        'degree',
        's_year',
        'e_year',
        'percentage',
        'profile_pic',
    ]

    completed_fields = 0

    for field in profile_fields:
        value = getattr(jid, field, None)

        if value is not None and str(value).strip() != "":
            completed_fields += 1

    profile_completion = round(
        (completed_fields / len(profile_fields)) * 100
    )

    remaining_fields = len(profile_fields) - completed_fields

    if profile_completion == 100:
        profile_message = "Your profile is complete! You're ready to stand out."
    elif remaining_fields == 1:
        profile_message = "You are 1 step away from completing your profile."
    else:
        profile_message = f"You are {remaining_fields} steps away from completing your profile."

    con = {
        'jid': jid,
        'uid': uid,
        'name': "dashboard",
        'profile_completion': profile_completion,
        'profile_message': profile_message,
    }

    return render(request, "jobseeker/dashboard.html", con)

@loginvalidate
def profile(request):
    con={
        'jid':request.jid,
        'uid':request.uid,
        'name':"profile"
    }
    return render(request,"jobseeker/profile.html",con)

@loginvalidate
def edit_profile(request):
    if request.POST:
        jid=request.jid
        uid=request.uid

        jid.f_name=request.POST['f_name']
        jid.l_name=request.POST['l_name']
        jid.number=request.POST['number'] or None
        jid.skills=request.POST['skills']
        jid.p_h=request.POST['p_h']
        jid.location=request.POST['location']
        jid.web=request.POST['web']
        jid.about_summary=request.POST['about_summary']
        jid.Institute=request.POST['Institute']
        jid.degree=request.POST['degree']
        jid.s_year=request.POST['s_year'] or None
        jid.e_year=request.POST['e_year'] or None
        jid.percentage=request.POST['percentage'] or None
        if "profile_pic" in request.FILES:
            jid.profile_pic=request.FILES['profile_pic']
        jid.save()
        return redirect("jobseeker:profile")
    else:    
        con={
            'jid':request.jid,
            'uid':request.uid,
            'name':'edit_profile' # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
        return render(request,"jobseeker/edit-profile.html",con)

# @loginvalidate
# def job_search(request):
    # jobs=post_jobs.objects.all()
    # con={
    #         'jid':request.jid,
    #         'uid':request.uid,
    #         'name':'job_search', # ye condition ke liye hai user jaha click karega action vhi dikhega
    #         'jobs':jobs
    #     }
    # return render(request,"jobseeker/job-search.html",con)

@loginvalidate
def resume_build(request):
    jid=request.jid
    uid=request.uid
    my_resume=resumes.objects.get(job_fk=jid)
    if request.POST:
        my_resume.full_name=request.POST['full_name']
        my_resume.email=request.POST['email']
        my_resume.number=request.POST['number']
        my_resume.location=request.POST['location']
        my_resume.linkedin=request.POST['linkedin']
        my_resume.pot_web=request.POST['pot_web']
        my_resume.summary=request.POST['summary']
        my_resume.degree=request.POST['degree']
        my_resume.Institute=request.POST['Institute']
        my_resume.p_year=request.POST['p_year']
        my_resume.percentage=request.POST['percentage']
        my_resume.job_tital=request.POST['job_tital']
        my_resume.w_company_name=request.POST['w_company_name']
        my_resume.job_description=request.POST['job_description']
        my_resume.skills=request.POST['skills']
        my_resume.Project_detail=request.POST['Project_detail']
        my_resume.degree=request.POST['degree']
        my_resume.Language=request.POST['Language']
        my_resume.save()
        if 'resume' in request.FILES:
            my_resume.resume=request.FILES['resume']
            my_resume.save()
        con={   
                'rid':my_resume,
                'jid':jid,
                'uid':uid,
                'name':'resume_build', # ye condition ke liye hai user jaha click karega action vhi dikhega
            }
        return render(request,'jobseeker/resume_done.html',con)
    else:
        con={
            'rid':my_resume,
            'jid':jid,
            'uid':uid,
            'name':'resume_build', # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
        return render(request,'jobseeker/resume-build.html',con)

job_tipes=[i[1].title() for i in post_jobs.e_type]

@loginvalidate
def search(request):
    uid=request.uid
    jid=request.jid
    all_saved_jobs=SavedJob.objects.filter(job_fk=jid)# idhar se mujhe jitni bhi jobs is user ne save kiya hoga 
    # unsab ka object mil jayega 
    saved_job_ids = [i.job_post_fk.id for i in all_saved_jobs ]
    # un object me se me sare jobpost ki id list me le lunga id ki jgah me pura object bhi lesakta hu par fir jab
    # hum html page me compare karenge to ye pura object compare karega id me bas id compare karega 

    # saved_job_ids = SavedJob.objects.filter(job_fk=jid).values_list('job_post_fk_id',flat=True) ye sort way hai
    
    all_jobs=post_jobs.objects.all()

    selected_job_type=request.GET.getlist('job_tipe')    
    # print(lst)
    
    if ('skills' in request.GET and request.GET['skills']!="") and \
       ('location' in request.GET and request.GET['location']!=""):
        skills=request.GET.get('skills')
        location=request.GET.get('location')
        # print("both")
        jobs=post_jobs.objects.filter(
            Q(job_title__icontains=skills,location__icontains=location) |
            Q(key_skils__icontains=skills,location__icontains=location) |
            Q(department_fk__d_name__icontains=skills,location__icontains=location)
        )

        con={
            'saved_job_ids':saved_job_ids,
            'selected_job_type':selected_job_type,
            'job_types':job_tipes,
            'jid':jid,
            'uid':uid,
            'name':'job_search',
            'jobs':jobs # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
        return render(request,'jobseeker/job-search.html',con)

    elif 'skills' in request.GET and request.GET['skills']!="":
        skills=request.GET.get('skills')
        # print("skills")
        jobs=post_jobs.objects.filter(
            Q(job_title__icontains=skills) |
            Q(key_skils__icontains=skills) |
            Q(department_fk__d_name__icontains=skills)
        )

        con={
            'saved_job_ids':saved_job_ids,
            'selected_job_type':selected_job_type,
            'job_types':job_tipes,
            'jid':jid,
            'uid':uid,
            'name':'job_search',
            'jobs':jobs # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
        return render(request,'jobseeker/job-search.html',con)
    elif 'location' in request.GET:
        # print("location")
        location=request.GET.get('location')
        jobs=post_jobs.objects.filter(
            Q(location__icontains=location)
        )

        con={
            'saved_job_ids':saved_job_ids,
            'selected_job_type':selected_job_type,
            'job_types':job_tipes,
            'jid':jid,
            'uid':uid,
            'name':'job_search',
            'jobs':jobs # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
        return render(request,'jobseeker/job-search.html',con)
    else:
        # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
        jobs=post_jobs.objects.all()

        con={
                'saved_job_ids':saved_job_ids,
                'selected_job_type':selected_job_type,
                'job_types':job_tipes,
                'jid':jid,
                'uid':uid,
                'jobs':jobs,
                'name':'job_search', # ye condition ke liye hai user jaha click karega action vhi dikhega
            }
            
        return render(request,'jobseeker/job-search.html',con)

@loginvalidate
def job_detail(request):
    jid=request.jid
    uid=request.uid
    if request.POST:
        pk=int(request.POST['pk'])
        my_job_detail=post_jobs.objects.get(id=pk)
        skills=re.split(r"[_,|-]+",my_job_detail.key_skils)
        con={
            'skills':skills,
            'my_job_detail':my_job_detail,
            'jid':jid,
            'uid':uid,
            'name':'job_search', # ye condition ke liye hai user jaha click karega action vhi dikhega
            }
        return render(request,'jobseeker/job-details.html',con)

    return redirect("jobseeker:search")

@loginvalidate
def saved_job(request):
    if request.POST:
        pk=request.POST['pk']
        print(pk)
        sid = post_jobs.objects.get(id = int(pk))
        already_saved = SavedJob.objects.get(
                job_fk=request.jid,
                job_post_fk=sid
            )

        already_saved.delete()

    all_job=SavedJob.objects.filter(job_fk=request.jid)
    
    con={   'all_job':all_job,
            'jid':request.jid,
            'uid':request.uid,
            'name':'saved_job', # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
    return render(request,'jobseeker/saved-jobs.html',con)

@loginvalidate
def Save_job(request, pk):

    if request.method == "POST":

        sid = post_jobs.objects.get(id=pk)

        try:

            already_saved = SavedJob.objects.get(
                job_fk=request.jid,
                job_post_fk=sid
            )

            already_saved.delete()

            return JsonResponse({
                "status": "removed"
            })

        except SavedJob.DoesNotExist:

            SavedJob.objects.create(
                job_fk=request.jid,
                job_post_fk=sid,
                status="Active"
            )

            return JsonResponse({
                "status": "saved"
            })

    return redirect("jobseeker:search")

@loginvalidate
def applye_jobs(request):
    if request.POST:
        pk=int(request.POST['pk'])
        page=request.POST['page']
        try:
            alrady_applayed=Apply.objects.get(jobs_fk = pk,job_fk=request.jid)
            # print("-------------------->cheking")
            if page=="job_search":
                return redirect("jobseeker:search")
            elif page=="saved":
                return redirect("jobseeker:saved_job")
        except:
            # print("-------------------->okoo")
            sid=post_jobs.objects.get(id = pk)
            rid=resumes.objects.get(job_fk = request.jid)
            status="Applied"
            # print("--------------------------->",sid)
            uid=request.uid
            jid=request.jid
            entry=Apply.objects.create(
                job_fk=jid,
                jobs_fk=sid,
                resume_fk=rid,
                status=status
            )
            if page=="job_search":
                return redirect("jobseeker:search")
            elif page=="saved":
                return redirect("jobseeker:saved_job")
    return redirect("jobseeker:dashboard")

@loginvalidate
def applayed_jobs(request):
    jid=request.jid
    uid=request.uid
    jobs=Apply.objects.filter(job_fk=request.jid)
    con={
        'jobs':jobs,
        'jid':jid,
        'uid':uid,
        'name':"apply"
    }
    return render(request,'jobseeker/Applayed.html',con) 

@loginvalidate
def delete_application(request,pk):
    applayed=Apply.objects.get(id=pk)
    applayed.delete()
    return redirect("jobseeker:applayed_jobs")


@loginvalidate
def all_feed(request):
    pid=Posts.objects.all()
    con={
        'pid':pid,
        'jid':request.jid,
        'uid':request.uid,
        'name':'all_feed', # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
    return render(request,'jobseeker/all_feed.html',con)

@loginvalidate
def add_post(request):
    if request.POST:
        tital=request.POST['tital']
        description=request.POST['description']
        if 'image' in request.FILES:
            image=request.FILES['image']
        else:
            image=None
        pid=Posts.objects.create(
            job_fk=request.jid,
            tital=tital,
            description=description,
            image=image
        )
        con={
        'jid':request.jid,
        'uid':request.uid,
        'name':'all_feed', # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
        return render(request,'jobseeker/add_post.html',con)
    con={
        'jid':request.jid,
        'uid':request.uid,
        'name':'all_feed', # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
    return render(request,'jobseeker/add_post.html',con)

@loginvalidate
def my_post(request):
    jid=request.jid
    pid=Posts.objects.filter(job_fk = jid)
    con={
        'pid':pid,
        'jid':jid,
        'uid':request.uid,
        'name':'my_post', # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
    return render(request,'jobseeker/my_post.html',con)

@loginvalidate
def delete_post(request,pk):
    jid=request.jid
    del_post=Posts.objects.get(id = pk)
    del_post.delete()
    
    return redirect("jobseeker:my_post")

@loginvalidate
def edit_post(request,pk):

    pid=Posts.objects.get(id = pk)
    # print(pid.tital)
    if request.POST:
        try:
            pid.tital=request.POST['tital']
            pid.description=request.POST['description']
            if 'image' in request.FILES:
                pid.image=request.FILES['image']
            else:
                pid.image=None
            pid.save()
            return redirect("jobseeker:my_post")
            
        except:
            return redirect("jobseeker:edit_post")
    con={
        'pid':pid,
        'jid':request.jid,
        'uid':request.uid,
        'name':'my_post', # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
    return render(request,"jobseeker/edit_post.html",con)

@loginvalidate
def conection(request):
    if request.POST:
        pk=int(request.POST['pk'])
        sender_id=request.jid
        resever_id=jobseeker.objects.get(id = pk)
        # print(resever_id.f_name)
        con={
        'jid':request.jid,
        'uid':request.uid,
        'name':'messages', # ye condition ke liye hai user jaha click karega action vhi dikhega
        'resever_id':resever_id
        }
        return render(request,"jobseeker/messages.html",con)
        
    job_request=Requests.objects.filter(jid_r_resever=request.jid,Request="Fraind_Request")
    remove_from_all_jobseeker=Requests.objects.filter(jid_r_resever=request.jid,Request="Accept")
    # print(remove_from_all_jobseeker)
    all_ids=set([i.jid_r_sender.id for i in remove_from_all_jobseeker])
    all_ids.add(request.jid.id)
    # print(all_ids)
    all_jobseeker=jobseeker.objects.exclude(id__in=all_ids)
    con={
        "all_jobseeker":all_jobseeker,
        "job_request":job_request,
        'jid':request.jid,
        'uid':request.uid,
        'name':'conection', # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
    return render(request,"jobseeker/connections.html",con)

@loginvalidate
def messages(request):
    if request.POST:
        pk=int(request.POST['pk'])
        sender_id=request.jid
        resever_id=jobseeker.objects.get(id = pk)
        print(sender_id,resever_id)
        con={
        'jid':request.jid,
        'uid':request.uid,
        'name':'messages', # ye condition ke liye hai user jaha click karega action vhi dikhega
        'resever_id':resever_id
        }
        return render(request,"jobseeker/messages.html",con)
    
    friends=Requests.objects.filter(jid_r_resever=request.jid,Request="Accept")
    con={
        'friends':friends,
        'jid':request.jid,
        'uid':request.uid,
        'name':'messages', # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
    return render(request,"jobseeker/messages.html",con)

@loginvalidate
def job_request(request,pk):
    try:
        check=Requests.objects.get(jid_r_sender=request.jid,jid_r_resever=pk)
        return redirect("jobseeker:conection")
    except:
        resever=jobseeker.objects.get(id=pk)
        entry=Requests.objects.create(
            jid_r_sender=request.jid,
            jid_r_resever=resever,
            Request="Fraind_Request"
        )
        return redirect("jobseeker:conection")

@loginvalidate
def job_accept(request,pk):
    try:
        if request.POST:
            entry=Requests.objects.get(jid_r_sender=pk,jid_r_resever=request.jid)
            entry.Request=request.POST['status']
            entry.save()
            return redirect("jobseeker:conection")
        return redirect("jobseeker:conection")
    except:
        return redirect("jobseeker:conection")

@loginvalidate
def setting(request):
    con={
        'jid':request.jid,
        'uid':request.uid,
        'name':'setting', # ye condition ke liye hai user jaha click karega action vhi dikhega
        }
    return render(request,"jobseeker/settings.html",con)


@loginvalidate
def download_resume(request):
    jid = request.jid
    my_resume = resumes.objects.get(job_fk=jid)

    template = get_template('jobseeker/resume_pdf.html')

    html = template.render({
        'rid': my_resume
    })

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="resume.pdf"'
    )

    pisa.CreatePDF(
        html,
        dest=response
    )

    return response

