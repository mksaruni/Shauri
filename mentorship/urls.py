from django.urls import path


from . import views


urlpatterns=[


            path('', views.index, name='index'),
            path('layout/', views.layout, name='layout'),
            path('mentees/', views.mentees, name='mentees'),
            path('details/', views.details, name='details'),
            path('regpagementee/', views.regpagementee, name='regpagementee'),
            path('regpagementor/', views.regpagementor, name='regpagementor'),
]