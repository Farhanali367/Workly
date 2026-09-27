from django.shortcuts import render,redirect

from account.models import *

from django.contrib.auth.hashers import make_password,check_password

from django.http import HttpResponse,HttpResponseRedirect

from jobseeker.models import * 
import random
from account.utils import MyCustomMail
# Create your views here.

def loginvalidate(myfun):

    def wrapper(request,*args,**kwargs):

        if "email" in request.session:

            uid=user.objects.get(email = request.session['email'])

        # try:

            if uid.role=="jobseeker":

                jid=jobseeker.objects.get(user_fk = uid)

                request.uid=uid

                request.jid=jid

                return myfun(request,*args,**kwargs)

            else:

                cid=company.objects.get(com_fk=uid)    

                request.uid=uid

                request.cid=cid

                return myfun(request,*args,**kwargs)

        # except:

                return redirect("account:login")

        else:

            return redirect("account:login")

    return wrapper

def home(request):
    if 'email' in request.session:
        return redirect("account:login")
    else:
        return render(request,"account/home.html")

def gestcompny(request):
    if 'email' in request.session:
        return redirect("account:login")
    else:
        return render(request,"account/gest/companies.html")

def login(request):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])

        if uid.role=="jobseeker":

            jid=jobseeker.objects.get(user_fk = uid)

            request.uid=uid

            request.jid=jid

            con={

                'jid':jid,

                'uid':uid,

                'name':"dashboard" #ye action ke liye hai

            }

            return render(request,"jobseeker/dashboard.html",con)

        else:

            cid=company.objects.get(com_fk=uid)

            request.uid=uid

            request.cid=cid

            con={

            'cid':cid,

            'uid':uid,

            'name':"dashboard" #ye action ke liye hai

                }

            return render(request,"company/dashboard.html",con)

    if request.POST:

        try:

            email=request.POST['email']

            password=request.POST['password']

            role=request.POST['role']


            uid=user.objects.get(email=email) # ye sare email me se hmara vala ek email nikal ke dega agar hoga to

            # print("---------->uid :",uid.password)

            if uid:

                if check_password(password,uid.password):# agar dono pasword shihoga to age jayega

                    request.session['email'] = email

                    if uid.role=="jobseeker":

                        jid=jobseeker.objects.get(user_fk=uid)

                        con={

                            'jid':jid,

                            'uid':uid,

                            'name':'dashboard'

                        }

                        return render(request,"jobseeker/dashboard.html",con)

                    else:

                        request.session['email']=email

                        cid=company.objects.get(com_fk=uid)

                        con={

                            'cid':cid,

                            'uid':uid,

                            'name':'dashboard'

                        }

                        return render(request,"company/dashboard.html",con)

                else:
                    contax={
                        "e_msg":"wrong password!!!!"
                        }
                    return render(request,"account/login.html",contax)   
        except:     
            contax={
                "e_msg": "this email not exists!!!"
            }

            return render(request,"account/login.html",contax)

    return render(request,"account/login.html")

def register(request):

    if request.POST:

        role=request.POST['role']


        # print("--------->",role)

        if role=="jobseeker":

            email=request.POST['email']

            f_name=request.POST['f_name']

            l_name=request.POST['l_name']

            number=request.POST['number']

            skills=request.POST['skills']

            password=request.POST['password']

            cnfpassword=request.POST["cnfpassword"]

            if "terms" in request.POST:

                if password==cnfpassword:

                    try:

                        uid=user.objects.create(email=email,

                                                password=make_password(cnfpassword),

                                                role=role)

                    except:

                        context={

                        "e_msg":"email alredy exists !!!",

                        }

                        return render(request,"account/registeration.html",context)

                    jid=jobseeker.objects.create(

                        user_fk=uid,

                        f_name=f_name,

                        l_name=l_name,

                        number=number,

                        skills=skills

                    )

                    #ye mere resume ke liye hai isse me is user ko dhundo ga sare resume mense

                    rid=resumes.objects.create(

                        job_fk=jid

                    )

                    user_role={

                        "imboss":"jobseeker"

                    }

                    return render(request,"account/login.html",user_role)

                else:

                    context={

                        "e_msg":"Wrong pasword!!!",

                    }

                    return render(request,"account/registeration.html",context)

            else:

                context={

                    "e_msg":"terms requerd!!!",

                }

                return render(request,"account/registeration.html",context)

        elif role=="company":

            email=request.POST['email']

            name=request.POST['name']

            web=request.POST['web']

            indestry=request.POST['indestry']

            password=request.POST['password']

            cnfpassword=request.POST["cnfpassword"]

            if "terms" in request.POST:

                if password==cnfpassword:

                    try:

                        uid=user.objects.create(

                            email=email,

                            password=make_password(password),
                            role=role

                        )

                    except:

                        context={

                        "e_msg":"email alredy exists !!!",

                        }

                        return render(request,"account/registeration.html",context)

                    try:

                        cid=company.objects.create(

                            com_fk=uid,

                            name=name,

                            website=web,

                            industry_type=indestry

                        )

                        user_role={

                            "imboss":"company"

                        }

                        return render(request,"account/login.html",user_role)

                    except:

                        context={

                        "e_msg":"company name is alredy exists !!!",

                        }

                        return render(request,"account/registeration.html",context)

                else:

                    context={

                        "e_msg":"Wrong pasword!!!",

                    }

                    return render(request,"account/registeration.html",context)

            else:

                context={

                    "e_msg":"terms requerd!!!",

                }

                return render(request,"account/registeration.html",context)

    else:   

        return render(request,"account/registeration.html")

def logout(request):

    if "email" in request.session:

        del request.session['email']

        return HttpResponseRedirect('/')# ye login page pe jayega login me aga humne kuch nhi lkha hai iske liye / liya hai
    # day 6
    else :

        return HttpResponseRedirect('/')

def forgot_password(request):
    if 'email' in request.session:
        return redirect("account:login")
    else:
        if request.POST:
            email=request.POST['email']
            uid=user.objects.get(email=email)
            if uid.role=="jobseeker":
                jid=jobseeker.objects.get(user_fk=uid)
                otp=random.randint(1000,9999)
                uid.OTP=otp
                uid.save()
                con={
                    'name':jid.f_name,
                    'otp':otp
                }
            MyCustomMail("Forgote Password","Email_template",email,con)
            return render(request,"account/otp.html",{'e':email})

        return render(request,"account/forgot_password.html")

def otp(request):
    if request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        uid=user.objects.get(email=email)      
        if str(uid.OTP)==otp: 
            return render(request,"account/reset_password.html",{'e':email})
        else:
            return render(request,"account/otp.html",{'e_msg':"Wrong OTP !!!!",'e':email})
    return redirect("account:login")

def reset_password(request):
    if request.POST:
        email=request.POST['email']
        new_pass=request.POST['new_pass']
        con_pass=request.POST['con_pass']
        uid=user.objects.get(email=email)
        if new_pass==con_pass:
            uid.password=make_password(new_pass)
            uid.save()
            return redirect("account:login")
        else:
            return render(request,"account/reset_password.html",{'e_msg':"Password Not Matching !!!!",'e':email})

    return redirect("account:login")

def user_chat(request,pk):
    return redirect()