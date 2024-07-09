from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from scl_management.models import *


def login(request):
    return render(request,'login_index.html')

def admin_home(request):
    return render(request,'admin/admin_index.html')

def add_dept(request):
    return render(request,'admin/admin_dept_add.html')

def view_dept(request):
    ob=dept_table.objects.all()
    return render(request,'admin/admin_dept_view.html',{"data":ob})

def add_course(request):
    ob=dept_table.objects.all()
    return render(request,'admin/admin_add_course.html',{"dep":ob})

def view_course(request):
    ob=course_table.objects.all()
    return render(request,'admin/admin_view_course.html',{"data":ob})

def add_subject(request):
    ob1=dept_table.objects.all()
    ob2=course_table.objects.all()
    return render(request,'admin/admin_add_subject.html',{"dep":ob1,"crs":ob2})

def view_subject(request):
    ob=course_table.objects.all()
    return render(request,'admin/admin_view_subject.html',{"cor":ob})

def add_staff(request):
    ob=dept_table.objects.all()
    return render(request,'admin/admin_add_staff.html',{"dept":ob})

def view_staff(request):
    ob=staff_table.objects.all()
    return render(request,'admin/admin_view_staff.html',{"staff":ob})

def assign_subject(request,id):
    request.session["staffid"]=id
    return  redirect(assign_subject1)

def assign_subject1(request):
    ob=staff_table.objects.get(id= request.session["staffid"])
    depid=ob.DEPT.id
    ob2=course_table.objects.filter(DEPT=depid)
    return render(request,'admin/admin_assign_subject.html',{"crs":ob2})








# ----------------------------------------------------------------------------------------------------------------------
def login_code(request):
    username=request.POST["textfield"]
    password=request.POST["textfield2"]
    try:
        ob = login_table.objects.get(username=username, password=password)
        if ob.type=="admin":
            return HttpResponse("<script>alert('success');window.location='/admin_home'</script>")
        elif ob.type=="staff":
            request.session["lid"]=ob.id
            return HttpResponse("<script>alert('success');window.location='/staff_home'</script>")
        elif ob.type=="stud":
            request.session["lid"]=ob.id
            ob2 = stud_table.objects.get(LOGIN=request.session["lid"])
            request.session["crsid"]=ob2.COURSE_id
            return HttpResponse("<script>alert('success');window.location='/stud_home'</script>")
        else:
            return HttpResponse("<script>alert('Somthing went wrong');window.location='/login_code'</script>")

    except:
        return HttpResponse("<script>alert('invalid');window.location='/'</script>")


def add_dept_code(request):
    dept=request.POST["textfield"]
    ob=dept_table()
    ob.dept_name=dept
    ob.save()
    return HttpResponse("<script>alert('department added');window.location='/add_dept'</script>")


# ------------------------------------------------------------------------------------------------------------------------
def add_course_code(request):
    dept=request.POST["select"]
    course=request.POST["textfield"]
    ob=course_table()
    ob.DEPT_id=dept
    # ob.DEPT=dept_table.objects.get(id=dept)
    ob.course_name=course
    ob.save()
    return HttpResponse("<script>alert('Course added');window.location='/add_course'</script>")

# ------------------------------------------------------------------------------------------------------------------------

def add_subject_code(request):
    crs=request.POST["select2"]
    sub=request.POST["textfield"]
    sem=request.POST["textfield2"]
    ob=sub_table()
    ob.COURSE_id=crs
    ob.sub_name=sub
    ob.sem=sem
    ob.save()
    return HttpResponse("<script>alert('Subject added');window.location='/add_subject'</script>")

def courses_dp(request,id):
    ob=course_table.objects.filter(DEPT_id=id)
    c=[]
    for i in ob:
        r={"id":i.id, "course_name":i.course_name}
        c.append(r)
    return JsonResponse(c, safe=False)


# ------------------------------------------------------------------------------------------------------------------------

def show_sub_code(request):
    id=request.POST["select2"]
    ob=sub_table.objects.filter(COURSE_id=id)
    ob2=course_table.objects.all()
    return render(request,"admin/admin_view_subject.html",{"data2":ob,"cor":ob2})

# ------------------------------------------------------------------------------------------------------------------------

def add_staff_code(request):
    name=request.POST["textfield"]
    gender=request.POST["radiobutton"]
    dept=request.POST["select"]
    phone=request.POST["textfield2"]
    email=request.POST["textfield3"]
    pic=request.FILES["file"]
    address=request.POST["textarea"]
    uname=request.POST["textfield4"]
    password=request.POST["textfield5"]

    fs=FileSystemStorage()
    sa=fs.save(pic.name,pic)

    ob=login_table()
    ob.username=uname
    ob.password=password
    ob.type="staff"
    ob.save()

    ob2=staff_table()
    ob2.stf_name=name
    ob2.gender=gender
    ob2.DEPT_id=dept
    ob2.phone=phone
    ob2.email=email
    ob2.address=address
    ob2.img=sa
    ob2.LOGIN=ob
    ob2.save()
    return HttpResponse("<script>alert('New Staff added');window.location='/add_staff'</script>")

# ------------------------------------------------------------------------------------------------------------------------

def show_assign_sub(request,id):
    ob=sub_table.objects.filter(COURSE_id=id)
    s=[]
    for i in ob:
        r={"name": i.sub_name, "id":i.id}
        s.append(r)
    return JsonResponse(s, safe=False)

def assign_code(request):
    sub=request.POST["select3"]
    ob=assign_table()
    ob.SUB_id=sub
    ob.STAFF_id=request.session['staffid']
    ob.save()
    return HttpResponse("<script>alert('subject assigned');window.location='/view_staff'</script>")

# ------------------------------------------------------------------------------------------------------------------------


def delete_sub(request,id):
    ob=sub_table.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_subject'</script>")

def delete_dept(request,id):
    ob=dept_table.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_dept'</script>")

def delete_coures(request,id):
    ob=course_table.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_course'</script>")

def delete_staff(request,id):
    ob=staff_table.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_staff'</script>")
# ------------------------------------------------------------------------------------------------------------------------

def admin_edit_staff(request,id):
    ob=staff_table.objects.get(id=id)
    request.session["sid"] = ob.id
    return redirect(admin_edit_staff1)

def admin_edit_staff1(request):
    ob=staff_table.objects.get(id=request.session["sid"])
    ob2=dept_table.objects.all()
    return render(request, 'admin/admin_edit_staff.html', {"data": ob,"data2":ob2})

def admin_edit_staff_code(request):
    name=request.POST["textfield"]
    gender=request.POST["radiobutton"]
    dept=request.POST["select"]
    phone=request.POST["textfield2"]
    email=request.POST["textfield3"]
    address=request.POST["textarea"]


    if 'file' in request.FILES:
        pic = request.FILES["file"]
        fs = FileSystemStorage()
        sa = fs.save(pic.name, pic)

        ob=staff_table.objects.get(id=request.session["sid"])
        ob.stf_name=name
        ob.gender=gender
        ob.DEPT_id=dept
        ob.phone=phone
        ob.email=email
        ob.address=address
        ob.img=sa
        ob.save()
    else:
        ob = staff_table.objects.get(id=request.session["sid"])
        ob.stf_name = name
        ob.gender = gender
        ob.DEPT_id = dept
        ob.phone = phone
        ob.email = email
        ob.address = address
        ob.save()

    return HttpResponse("<script>alert('Updated');window.location='/view_staff'</script>")
# ---------------------------------------------------------------

def admin_edit_subject(request,id):
    ob=sub_table.objects.get(id=id)
    request.session["subbid"]=ob.id
    return redirect(admin_edit_subject1)

def admin_edit_subject1(request):
    ob=sub_table.objects.get(id=request.session["subbid"])
    ob2=course_table.objects.all()
    ob3=dept_table.objects.all()
    return render(request,'admin/admin_edit_subject.html',{"data1":ob,"data2":ob2,"data3":ob3})

def admin_edit_sub_code(request):
    cou=request.POST["select2"]
    sub=request.POST["textfield"]
    sem=request.POST["textfield2"]

    ob=sub_table.objects.get(id=request.session["subbid"])
    ob.COURSE_id=cou
    ob.sub_name=sub
    ob.sem=sem
    ob.save()
    return HttpResponse("<script>alert('Updated');window.location='/view_subject'</script>")
# ----------------------------------------------------------------

def admin_edit_course(request,id):
    ob=course_table.objects.get(id=id)
    request.session["courrid"]=ob.id
    return redirect(admin_edit_course1)

def admin_edit_course1(request):
    ob=course_table.objects.get(id=request.session["courrid"])
    ob2=dept_table.objects.all()
    return render(request,'admin/admin_edit_course.html',{"data":ob,"data2":ob2})

def admin_edit_course_code(request):
    dept=request.POST["select"]
    name=request.POST["textfield"]

    ob=course_table.objects.get(id=request.session["courrid"])
    ob.DEPT_id=dept
    ob.course_name=name
    ob.save()
    return HttpResponse("<script>alert('Updated');window.location='/view_course'</script>")
# ----------------------------------------------------------------

def admin_edit_dept(request,id):
    ob=dept_table.objects.get(id=id)
    request.session["depid"]=ob.id
    return redirect(admin_edit_dept1)

def admin_edit_dept1(request):
    ob=dept_table.objects.get(id=request.session["depid"])
    return render(request,'admin/admin_edit_dept.html',{"data":ob})

def admin_edit_dept_code(request):
    name=request.POST["textfield"]

    ob=dept_table.objects.get(id=request.session["depid"])
    ob.dept_name=name
    ob.save()
    return HttpResponse("<script>alert('Updated');window.location='/view_dept'</script>")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def staff_home(request):
    return render(request,'staff/staff_index.html')

def staff_profile(request):
    ob=staff_table.objects.get(LOGIN=request.session['lid'])
    return render(request,'staff/staff_profile.html',{"data":ob})

def staff_view_sub(request):
    # ob=staff_table.objects.get(LOGIN=request.session['lid'])
    # sfid=ob.id
    ob2=assign_table.objects.filter(STAFF__LOGIN=request.session["lid"])
    return render(request,'staff/staff_view_subjects.html',{"data":ob2})

def staff_add_note(request):
    # ob=staff_table.objects.get(LOGIN=request.session['lid'])
    # sfid=ob.id
    ob2=assign_table.objects.filter(STAFF__LOGIN=request.session["lid"])
    return render(request,'staff/staff_upload_notes.html',{"data":ob2})

def staff_view_note(request):
    # ob=staff_table.objects.get(LOGIN=request.session['lid'])
    # sfid=ob.id
    ob2=notes_table.objects.filter(STAFF__LOGIN=request.session["lid"])
    return render(request,'staff/staff_view_notes.html',{"data":ob2})

def staff_add_stud(request):
    ob = staff_table.objects.get(LOGIN=request.session['lid'])
    dept=ob.DEPT_id
    ob2=course_table.objects.filter(DEPT_id=dept)
    return render(request,'staff/staff_add_stud.html',{"data":ob2})

def staff_view_stud(request):
    ob = staff_table.objects.get(LOGIN=request.session['lid'])
    dept = ob.DEPT_id
    ob2 = course_table.objects.filter(DEPT_id=dept)
    return render(request,'staff/staff_view_stud.html',{"data":ob2})


# ------------------------------------------------------------------------------------------------------------------------


def add_notes_code(request):
    sub=request.POST["select"]
    title=request.POST["textfield"]
    file=request.FILES["file"]

    ob2=staff_table.objects.get(LOGIN=request.session['lid'])

    ob=notes_table()
    ob.STAFF=ob2
    ob.SUB_id=sub
    ob.title=title
    ob.file=file
    ob.save()
    return HttpResponse("<script>alert('Note uploaded');window.location='/staff_home'</script>")

# ------------------------------------------------------------------------------------------------------------------------

def add_stud_code(request):
    name=request.POST["textfield"]
    gender=request.POST["radiobutton"]
    dob=request.POST["birth"]
    place=request.POST["textfield2"]
    course=request.POST["select"]
    sem=request.POST["textfield3"]
    pic=request.FILES["file"]
    uname=request.POST["textfield4"]
    password=request.POST["textfield5"]
    phone=request.POST["textfield6"]
    email=request.POST["textfield7"]

    fs=FileSystemStorage()
    sa=fs.save(pic.name,pic)

    ob=login_table()
    ob.username=uname
    ob.password=password
    ob.type="stud"
    ob.save()

    ob2=stud_table()
    ob2.img=sa
    ob2.gender=gender
    ob2.sem=sem
    ob2.std_name=name
    ob2.dob=dob
    ob2.place=place
    ob2.LOGIN=ob
    ob2.phone=phone
    ob2.email=email
    ob2.COURSE_id=course
    ob2.save()

    return HttpResponse("<script>alert('New student added');window.location='/staff_home'</script>")

# ------------------------------------------------------------------------------------------------------------------------

def show_stud_code(request):
    id=request.POST["select"]
    ob=stud_table.objects.filter(COURSE_id=id)

    ob2 = staff_table.objects.get(LOGIN=request.session['lid'])
    dept = ob2.DEPT_id
    ob3= course_table.objects.filter(DEPT_id=dept)

    return render(request,"staff/staff_view_stud.html",{"data2":ob,"data":ob3})
# ------------------------------------------------------------------------------------------------------------------------

def delete_note(request,id):
    ob=notes_table.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/staff_view_note'</script>")

def delete_stud(request,id):
    ob=stud_table.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/staff_view_stud'</script>")
# ------------------------------------------------------------------------------------------------------------------------

def staff_edit_stud(request,id):
    ob=stud_table.objects.get(id=id)
    request.session["stdid"]=ob.id
    return redirect(staff_edit_stud1)

def staff_edit_stud1(request):
    ob=stud_table.objects.get(id=request.session["stdid"])
    ob2=staff_table.objects.get(LOGIN_id=request.session['lid'])
    ob3=course_table.objects.filter(DEPT_id=ob2.DEPT_id)
    return render(request,"staff/staff_edit_stud.html",{"data":ob,"data2":ob3})

def staff_edit_stud_code(request):
    name=request.POST["textfield"]
    gender=request.POST["radiobutton"]
    dob=request.POST["birth"]
    place=request.POST["textfield2"]
    course=request.POST["select"]
    sem=request.POST["textfield3"]
    phone=request.POST["textfield6"]
    email=request.POST["textfield7"]

    if 'file' in request.FILES:
        pic = request.FILES["file"]
        fs = FileSystemStorage()
        sa = fs.save(pic.name, pic)

        ob=stud_table.objects.get(id=request.session["stdid"])
        ob.img=sa
        ob.sem=sem
        ob.email=email
        ob.phone=phone
        ob.gender=gender
        ob.place=place
        ob.dob=dob
        ob.COURSE_id=course
        ob.std_name=name
        ob.save()
    else:
        ob=stud_table.objects.get(id=request.session["stdid"])
        ob.sem=sem
        ob.email=email
        ob.phone=phone
        ob.gender=gender
        ob.place=place
        ob.dob=dob
        ob.COURSE_id=course
        ob.std_name=name
        ob.save()
    return HttpResponse("<script>alert('UPDATED');window.location='/staff_view_stud'</script>")



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def stud_home(request):
    return render(request,'student/stud_index.html')

def stud_profile(request):
    ob=stud_table.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'student/stud_profile.html',{"data":ob})

def stud_view_notes(request):
    ob=sub_table.objects.filter(COURSE_id=request.session['crsid'])
    return render(request,'student/stud_view_notes.html',{"data":ob})

# ------------------------------------------------------------------------------------------------------------------------

def show_notes_code(request):
    sub=request.POST["select"]
    ob=notes_table.objects.filter(SUB_id=sub)
    ob2=sub_table.objects.filter(COURSE_id=request.session['crsid'])
    return render(request, "student/stud_view_notes.html", {"data1": ob,"data":ob2})

















