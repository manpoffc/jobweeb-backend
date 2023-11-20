from django.urls import path
from .views import job_list, job_detail, job_create, job_update, job_delete

urlpatterns = [
    path('jobs/', job_list, name='job_list'),
    path('jobs/<int:pk>/', job_detail, name='job_detail'),
    path('jobs/create/', job_create, name='job_create'),
    path('jobs/<int:pk>/update/', job_update, name='job_update'),
    path('jobs/<int:pk>/delete/', job_delete, name='job_delete'),
]
