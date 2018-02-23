from django.shortcuts import render
from .models import ProblemKeep
from django.contrib.auth.decorators import login_required

# Create your views here.

# Tryを登録する
def showtry(request) :
    return render(request, '')

@login_required
def index(request):
    pk_list = ProblemKeep.objects.order_by('title')
    context = {'pk_list': pk_list, 'page_title': '課題リスト'}
    return render(request, 'kaizen/index.html', context)
    