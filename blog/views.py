from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post

def index(request):
	'''
	return render(request,'blog/index.html',context={
			'title':'This is my blog.',
			'welcome':'You are welcome.',
		})
	'''
	post_list=Post.objects.all().order_by('-created_time')
	return render(request,'blog/index.html',context={'post_list':post_list})