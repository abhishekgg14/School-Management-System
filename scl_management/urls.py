from django.urls import path

from scl_management import views

urlpatterns = [
    path('', views.login,name="login"),

    path('admin_home',views.admin_home),
    path('add_dept', views.add_dept),
    path('view_dept', views.view_dept),
    path('add_course', views.add_course),
    path('view_course', views.view_course),
    path('add_subject', views.add_subject),
    path('view_subject', views.view_subject),
    path('add_staff', views.add_staff),
    path('view_staff', views.view_staff),
    path('assign_subject/<id>', views.assign_subject),
    path('assign_subject1', views.assign_subject1),

    path('login_code', views.login_code),
    path('add_dept_code',views.add_dept_code),
    path('add_course_code',views.add_course_code),
    path('add_subject_code',views.add_subject_code),
    path('courses_dp/<id>',views.courses_dp),
    path('show_sub_code',views.show_sub_code),
    path('add_staff_code',views.add_staff_code),
    path('show_assign_sub/<id>',views.show_assign_sub),
    path('assign_code',views.assign_code),

    path('delete_sub/<id>',views.delete_sub),
    path('delete_dept/<id>',views.delete_dept),
    path('delete_coures/<id>',views.delete_coures),
    path('delete_staff/<id>', views.delete_staff),

    path('admin_edit_staff/<id>',views.admin_edit_staff),
    path('admin_edit_staff1',views.admin_edit_staff1),
    path('admin_edit_staff_code',views.admin_edit_staff_code),
    path('admin_edit_subject/<id>',views.admin_edit_subject),
    path('admin_edit_subject1',views.admin_edit_subject1),
    path('admin_edit_sub_code',views.admin_edit_sub_code),
    path('admin_edit_course/<id>',views.admin_edit_course),
    path('admin_edit_course1',views.admin_edit_course1),
    path('admin_edit_course_code',views.admin_edit_course_code),
    path('admin_edit_dept/<id>',views.admin_edit_dept),
    path('admin_edit_dept1',views.admin_edit_dept1),
    path('admin_edit_dept_code',views.admin_edit_dept_code),
    # ---------------------------------------------------------------------------

    path('staff_home',views.staff_home),
    path('staff_profile', views.staff_profile),
    path('staff_view_sub', views.staff_view_sub),
    path('staff_add_note', views.staff_add_note),
    path('staff_view_note', views.staff_view_note),
    path('staff_add_stud', views.staff_add_stud),
    path('staff_view_stud', views.staff_view_stud),

    path('add_notes_code',views.add_notes_code),
    path('add_stud_code',views.add_stud_code),
    path('show_stud_code',views.show_stud_code),

    path('delete_note/<id>', views.delete_note),
    path('delete_stud/<id>', views.delete_stud),

    path('staff_edit_stud/<id>',views.staff_edit_stud),
    path('staff_edit_stud1',views.staff_edit_stud1),
    path('staff_edit_stud_code',views.staff_edit_stud_code),
    # ---------------------------------------------------------------------------

    path('stud_home',views.stud_home),
    path('stud_profile',views.stud_profile),
    path('stud_view_notes',views.stud_view_notes),

    path('show_notes_code',views.show_notes_code),
]