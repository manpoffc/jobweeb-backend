# jobs/models.py

from django.db import models

class Job(models.Model):
    id = models.AutoField(primary_key=True)  # Add this line
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)

    class Meta:
        db_table = 'jobs'
