from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Job
from .forms import JobForm

@csrf_exempt
def job_list(request):
    if request.method == 'GET':
        jobs = Job.objects.all()
        data = [{'job_title': job.job_title, 'company': job.company} for job in jobs]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save()
            return JsonResponse({'job_title': job.job_title, 'company': job.company})
        return JsonResponse({'error': 'Invalid data'})

@csrf_exempt
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    data = {'job_title': job.job_title, 'company': job.company}
    return JsonResponse(data)

@csrf_exempt
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save()
            return JsonResponse({'job_title': job.job_title, 'company': job.company})
        return JsonResponse({'error': 'Invalid data'})

@csrf_exempt
def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'PUT':
        form = JobForm(request.PUT, instance=job)
        if form.is_valid():
            job = form.save()
            return JsonResponse({'job_title': job.job_title, 'company': job.company})
        return JsonResponse({'error': 'Invalid data'})

@csrf_exempt
def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    job.delete()
    return HttpResponse(status=204)
