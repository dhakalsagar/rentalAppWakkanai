from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponse
from .models import Post
# from .models import House, Appart

def home(request):
	all_apart =House.objects.all()
	apart =Appart.objects.all()
	return render(request, 'rentalapp/home.html', {'all_apart': all_apart})

def detail(request, house_id):
	house =get_object_or_404(House, pk= house_id)
	return render(request, 'rentalapp/detail.html', {'house': house})
	
def about(request):
	return render(request, 'rentalapp/about.html', {'title': 'About'})

def contact(request):
	return render(request, 'rentalapp/contact.html', {'title':'contact'})

def information(request):
	return render(request, 'rentalapp/information.html', {'title':'information'})

def createpost(request):
        if request.method == 'POST':
            if request.POST.get('owner'):
                post=Post()
                post.owner= request.POST.get('owner')
                # post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'rentalapp/home.html')  

        else:
                return render(request,'rentalapp/home.html')

