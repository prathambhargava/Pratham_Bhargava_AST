# views.py
from django.shortcuts import render
from .models import JobListing

def job_search(request):
    keyword = request.GET.get('keyword', '')
    jobs = JobListing.objects.filter(title__icontains=keyword)
    return render(request, 'Index.html', {'jobs': jobs, 'keyword': keyword})
