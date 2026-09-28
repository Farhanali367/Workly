from django.shortcuts import render, redirect

from account.models import *

from django.contrib.auth.hashers import make_password, check_password

from django.http import HttpResponse, HttpResponseRedirect

from jobseeker.models import *

import random

from account.utils import MyCustomMail


# Create your views here.


def loginvalidate(myfun):

    def wrapper(request, *args, **kwargs):

        if "email" in request.session:

            uid = user.objects.get(
                email=request.session['email']
            )

            if uid.role == "jobseeker":

                jid = jobseeker.objects.get(
                    user_fk=uid
                )

                request.uid = uid
                request.jid = jid

                return myfun(request, *args, **kwargs)

            else:

                cid = company.objects.get(
                    com_fk=uid
                )

                request.uid = uid
                request.cid = cid

                return myfun(request, *args, **kwargs)

        else:

            return redirect("account:login")

    return wrapper


def home(request):

    if 'email' in request.session:

        return redirect("account:login")

    else:

        return render(
            request,
            "account/home.html"
        )


def gestcompny(request):

    if 'email' in request.session:

        return redirect("account:login")

    else:

        return render(
            request,
            "account/gest/companies.html"
        )


# ==========================================================
# LOGIN
# ==========================================================

def login(request):

    # If already logged in
    if "email" in request.session:

        uid = user.objects.get(
            email=request.session['email']
        )

        if uid.role == "jobseeker":

            # IMPORTANT:
            # Do NOT directly render dashboard here.
            # Redirect to dashboard so profile_completion
            # is calculated inside jobseeker.views.dashboard()
            return redirect("jobseeker:dashboard")

        else:

            return redirect("company:dashboard")


    # Login form submitted
    if request.POST:

        try:

            email = request.POST['email']
            password = request.POST['password']
            role = request.POST['role']

            uid = user.objects.get(
                email=email
            )

            if check_password(
                password,
                uid.password
            ):

                # Save email in session
                request.session['email'] = email

                # IMPORTANT:
                # Dashboard ko direct render nahi karna.
                # Dashboard view par redirect karna hai.
                if uid.role == "jobseeker":

                    return redirect(
                        "jobseeker:dashboard"
                    )

                else:

                    return redirect(
                        "company:dashboard"
                    )

            else:

                contax = {
                    "e_msg": "wrong password!!!!"
                }

                return render(
                    request,
                    "account/login.html",
                    contax
                )

        except user.DoesNotExist:

            contax = {
                "e_msg": "this email not exists!!!"
            }

            return render(
                request,
                "account/login.html",
                contax
            )

        except Exception:

            contax = {
                "e_msg": "Login failed. Please try again."
            }

            return render(
                request,
                "account/login.html",
                contax
            )


    return render(
        request,
        "account/login.html"
    )


# ==========================================================
# REGISTER
# ==========================================================

def register(request):

    if request.POST:

        role = request.POST['role']


        # ==================================================
        # JOBSEEKER REGISTER
        # ==================================================

        if role == "jobseeker":

            email = request.POST['email']

            f_name = request.POST['f_name']

            l_name = request.POST['l_name']

            number = request.POST['number']

            skills = request.POST['skills']

            password = request.POST['password']

            cnfpassword = request.POST["cnfpassword"]


            if "terms" in request.POST:

                if password == cnfpassword:

                    try:

                        uid = user.objects.create(
                            email=email,
                            password=make_password(
                                cnfpassword
                            ),
                            role=role
                        )

                    except:

                        context = {
                            "e_msg": "email alredy exists !!!",
                        }

                        return render(
                            request,
                            "account/registeration.html",
                            context
                        )


                    jid = jobseeker.objects.create(

                        user_fk=uid,

                        f_name=f_name,

                        l_name=l_name,

                        number=number,

                        skills=skills

                    )


                    # Resume object create
                    rid = resumes.objects.create(
                        job_fk=jid
                    )


                    user_role = {
                        "imboss": "jobseeker"
                    }


                    return render(
                        request,
                        "account/login.html",
                        user_role
                    )


                else:

                    context = {
                        "e_msg": "Wrong pasword!!!",
                    }

                    return render(
                        request,
                        "account/registeration.html",
                        context
                    )


            else:

                context = {
                    "e_msg": "terms requerd!!!",
                }

                return render(
                    request,
                    "account/registeration.html",
                    context
                )


        # ==================================================
        # COMPANY REGISTER
        # ==================================================

        elif role == "company":

            email = request.POST['email']

            name = request.POST['name']

            web = request.POST['web']

            indestry = request.POST['indestry']

            password = request.POST['password']

            cnfpassword = request.POST["cnfpassword"]


            if "terms" in request.POST:

                if password == cnfpassword:

                    try:

                        uid = user.objects.create(

                            email=email,

                            password=make_password(
                                password
                            ),

                            role=role

                        )

                    except:

                        context = {
                            "e_msg": "email alredy exists !!!",
                        }

                        return render(
                            request,
                            "account/registeration.html",
                            context
                        )


                    try:

                        cid = company.objects.create(

                            com_fk=uid,

                            name=name,

                            website=web,

                            industry_type=indestry

                        )


                        user_role = {
                            "imboss": "company"
                        }


                        return render(
                            request,
                            "account/login.html",
                            user_role
                        )


                    except:

                        context = {
                            "e_msg": "company name is alredy exists !!!",
                        }

                        return render(
                            request,
                            "account/registeration.html",
                            context
                        )


                else:

                    context = {
                        "e_msg": "Wrong pasword!!!",
                    }

                    return render(
                        request,
                        "account/registeration.html",
                        context
                    )


            else:

                context = {
                    "e_msg": "terms requerd!!!",
                }

                return render(
                    request,
                    "account/registeration.html",
                    context
                )


    else:

        return render(
            request,
            "account/registeration.html"
        )


# ==========================================================
# LOGOUT
# ==========================================================

def logout(request):

    if "email" in request.session:

        del request.session['email']

        return HttpResponseRedirect('/')

    else:

        return HttpResponseRedirect('/')


# ==========================================================
# FORGOT PASSWORD
# ==========================================================

def forgot_password(request):

    if 'email' in request.session:

        return redirect("account:login")

    else:

        if request.POST:

            email = request.POST['email']

            uid = user.objects.get(
                email=email
            )

            if uid.role == "jobseeker":

                jid = jobseeker.objects.get(
                    user_fk=uid
                )

                otp = random.randint(
                    1000,
                    9999
                )

                uid.OTP = otp

                uid.save()

                con = {
                    'name': jid.f_name,
                    'otp': otp
                }


            MyCustomMail(
                "Forgote Password",
                "Email_template",
                email,
                con
            )

            return render(
                request,
                "account/otp.html",
                {'e': email}
            )


        return render(
            request,
            "account/forgot_password.html"
        )


# ==========================================================
# OTP
# ==========================================================

def otp(request):

    if request.POST:

        email = request.POST['email']

        otp = request.POST['otp']

        uid = user.objects.get(
            email=email
        )

        if str(uid.OTP) == otp:

            return render(
                request,
                "account/reset_password.html",
                {'e': email}
            )

        else:

            return render(
                request,
                "account/otp.html",
                {
                    'e_msg': "Wrong OTP !!!!",
                    'e': email
                }
            )


    return redirect(
        "account:login"
    )


# ==========================================================
# RESET PASSWORD
# ==========================================================

def reset_password(request):

    if request.POST:

        email = request.POST['email']

        new_pass = request.POST['new_pass']

        con_pass = request.POST['con_pass']

        uid = user.objects.get(
            email=email
        )


        if new_pass == con_pass:

            uid.password = make_password(
                new_pass
            )

            uid.save()

            return redirect(
                "account:login"
            )

        else:

            return render(
                request,
                "account/reset_password.html",
                {
                    'e_msg': "Password Not Matching !!!!",
                    'e': email
                }
            )


    return redirect(
        "account:login"
    )


# ==========================================================
# USER CHAT
# ==========================================================

def user_chat(request, pk):

    return redirect()