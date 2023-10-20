from django.shortcuts import render
from hr.models import JobPost, CandidateApplication, SelectCandidateJob

# Create your views here.
def hrHome_views(request):
    return render(request, 'hr/hrdashboard.html')

def post_job_views(request):
    msg = None
    if request.method == 'POST':
        job_title = request.POST.get('job-title')
        address = request.POST.get('address')
        company_name = request.POST.get('company-name')
        salary_low = request.POST.get('salary-low')
        salary_high = request.POST.get('salary-high')
        last_date = request.POST.get('last-date')
        print(job_title+" "+address+" "+company_name)
        msg = "Job added successfully"
        job_post = JobPost(user=request.user, title=job_title, address=address, companyName=company_name, salaryLow=salary_low, lastDateToApply=last_date)
        job_post.save()
    return render(request,'hr/postjob.html', {'msg':msg})

def candidate_view(request, pk):
    print(pk)
    return render(request, 'hr/candidate.html')