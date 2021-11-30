from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.add_course),
    path('courses/del_page/<int:_id>', views.del_page),
    path('courses/destroy/<int:_id>', views.destroy)
]