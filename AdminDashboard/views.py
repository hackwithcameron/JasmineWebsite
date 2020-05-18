from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def admin_index(request):
    context = {}
    return render(request, 'AdminDashboard/index.html', context)
