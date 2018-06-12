from django.shortcuts import render,redirect

from .models import Comment
from django.http import HttpResponse #Allows us to create a response that gets returned after someone accesses it 
# Create your views here.
from .forms import CommentForm

from django.views.decorators.http import require_POST
def index(request):
	# retrun HttpResponse('Hello WOrld') #This gets returned in Browser 
	comments=Comment.objects.order_by('-date_added')
	context={'comments':comments}
	return render(request,'Notebook/index.html',context)

# @require_POST #Takes care that this view only takes POST request


def sign(request):
	if(request.method=='POST'):
		form=CommentForm(request.POST)
		if form.is_valid():
			newComment=Comment(name=request.POST['name'],comment=request.POST['comment'])
			newComment.save()
			return redirect('index')
	else:
		form=CommentForm #Instantiate A form
	context={'form':form}

	return render(request,'Notebook/sign.html',context)