# Creating views
from django.shortcuts import render, redirect
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required

@login_required
def submit_request(request):
    if request.method == 'POST':
        service_type = request.POST.get('service_type')
        details = request.POST.get('details')
        attachment = request.FILES.get('attachment')
        ServiceRequest.objects.create(
            user=request.user,
            service_type=service_type,
            details=details,
            attachment=attachment
        )
        return redirect('track_requests')
    return render(request, 'submit_request.html')

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'track_requests.html', {'requests': requests})
