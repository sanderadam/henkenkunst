from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import SchilderijForm
from .models import Schilderij
from django.conf import settings

def index(request):
	
	schilderijen = Schilderij.objects.all().filter(zichtbaar=True)	

	#generate indicators for carousel
	indicators = '<li data-target="#myCarousel" data-slide-to="0" class="active"></li>\n'
	for i in range (1,schilderijen.count()):
		indicators += '<li data-target="#myCarousel" data-slide-to="' + str(i) +'"></li>\n'


	active = [False] * 6
	active[0] = True 


	context = {
	'schilderijen':schilderijen,
	'indicators':indicators,
	'active': active,
	}

	return render(request, 'photomgr/index.html', context)

   
def contact(request):
	active = [False] * 6
	active[2] = True 

	context = {
	'active': active,
	}

	return render(request, 'photomgr/contact.html', context)



def add_schilderij(request):


	active = [False] * 6
	active[3] = True 

	if request.method == 'POST':
		form = SchilderijForm(request.POST,request.FILES)
		#print(form)

		if form.is_valid():
			schilderij = form.save(commit=False)
			schilderij.image = request.FILES['image']
			schilderij.save()
			
			return redirect('view_schilderij',pk=schilderij.pk)
		else:
			#do stuff for unvalid form
			pass
	else:
		#only if method is not POST
		form = SchilderijForm()

	context = {
	'form':form,
	'active': active,
	}

	return render(request, 'photomgr/add_schilderij.html', context)


def edit_schilderij(request,pk):

	if request.method == 'POST':
		schilderij_instance = get_object_or_404(Schilderij, pk=pk)
		form = SchilderijForm(request.POST,request.FILES, instance = schilderij_instance)
		#print(form)

		if form.is_valid():
			schilderij = form.save(commit=False)
			if request.FILES:
				schilderij.image = request.FILES['image']
			schilderij.save()
			
			return redirect('view_all')
		else:
			#do stuff for unvalid form
			print(form.errors)
			return HttpResponse("Invalid form" + form.errors)

	else:
		#only if method is not POST
		schilderij = get_object_or_404(Schilderij, pk=pk)
		form = SchilderijForm(instance=schilderij)

		context = {
		'form':form,
		'mediaurl':settings.MEDIA_URL,
		'pk':pk
		}

		return render(request, 'photomgr/edit_schilderij.html', context)



def view_schilderij(request,pk):
	schilderij = get_object_or_404(Schilderij, pk=pk)

	context = {
	'schilderij':schilderij,
	}

	return render(request, 'photomgr/view_schilderij.html', context)

def view_all(request):
	schilderijen = Schilderij.objects.all()
	active = [False] * 6
	active[4] = True 
	
	context = {
	'schilderijen':schilderijen,
	'active':active,
	}

	return render(request, 'photomgr/view_all.html', context)

def overview(request):
	schilderijen = Schilderij.objects.all().filter(zichtbaar=True)
	active = [False] * 6
	active[1] = True 
	
	context = {
	'schilderijen':schilderijen,
	'active':active,
	}

	return render(request, 'photomgr/overview.html', context)
