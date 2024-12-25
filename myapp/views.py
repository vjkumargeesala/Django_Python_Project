from django.shortcuts import render,redirect
from myapp.models import POLL,Spoll,rate,answer,covid,covid_details
from myapp.forms import Myform,Myforms,myrate,myanswer,mypoll,mycovid,mycovid_details
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from project import settings



# Create your views here.
def hello(req,name):
	return HttpResponse("Hello "+name+" Handsome")
def help(req):
	return render(req,"myapp/help.html")
def view(req,name):
	if(name=="Yes" or name=="yes"):
		data=Spoll.objects.filter(opt="Yes")
	else:
		data=Spoll.objects.filter(opt="No")
	return render(req,'myapp/answer.html',{'data':data,'i':'t'})		

def ansorrate(req,name):	
	if( name == "Answer"):
		data=answer.objects.all()
		return render(req,'myapp/answer.html',{'data':data,'i':'ans'})	
	elif( name == "Rating"):
		data=rate.objects.all()
		return render(req,'myapp/answer.html',{'data':data,'i':'rat'})	

def register(request):
	if request.method=="POST":
		data=Myforms(request.POST)
		if data.is_valid():
			data.save()
			return redirect('login')
	form=Myforms()
	return render(request,'myapp/register.html',{'form':form})
@login_required
def poll_q(req):
	if req.method=="POST":
		data=mypoll(req.POST)
		data.save()
		sp=Spoll.objects.all().delete()
		ra=rate.objects.all().delete()
		aa=answer.objects.all().delete()        
		return redirect('/admin_page')
	form=mypoll()	
	return render(req,'myapp/poll_q.html',{'form':form})	

def covid_check(req):
	# if req.method == "POST":
	# 	data=mycovid(req.POST)
	# 	data.save()
	# 	subject="Regarding to your Covid details"
	# 	body=" "
	# 	sender=settings.EMAIL_HOST_USER
	# 	email=User.objects.last()
	# 	reciver=email.email
	# 	send_mail(subject,body,sender,[reciver])
	# 	return redirect('/help')
	if req.method == "POST":
		info=mycovid(req.POST)
		info.save()

		data=covid.objects.last()
		a=data.id
		email=covid_details.objects.last()
		p=0
		if(data.diffculty_Breathing=="Yes" or data.chest_pain=="Yes" or data.loss_of_Speech=="Yes" or data.loss_of_Taste=="Yes"):
			p="critical"
		elif(data.fever== "Yes" or data.cold=="Yes" or data.dry_cough=="Yes"):
			p="high"
		elif(data.triedness=="Yes" or data.sore_throat=="Yes" or data.headache=="Yes"):
			p="starting"
		else:
			p="none"
		subject="Regarding to your Covid Symptoms Response"
		body=""" \n Thanks for Response. \n\nThese Symptoms reports will be verified by authorised Doctors. \nand will get back to you through mail/phone regarding neccessary medications you need to take. \nMeanwhile Quarantine yourself in your Home and try not get contact with your family members to stop spreading and also try to imporve your immunity using Zeincvit and vitamin C.\n\nThank You.\n\n STAY HOME STAY SAFE"""
		receiver=email.email
		sender=settings.EMAIL_HOST_USER
		return render(req,'myapp/help.html',{'k':p})
		send_mail(subject,body,sender,[receiver])

	form=mycovid()
	return render(req,'myapp/covid.html',{'form':form})

def covid_intro(req):
	return render(req,"myapp/covidintro.html")

def covid_func(req):
	if req.method == "POST":
		data=mycovid_details(req.POST)
		data.save()
		return redirect('covid_check')
	form=mycovid_details()
	return render(req,'myapp/coviddetails.html',{'form':form})


def submit(req):
	if req.method=="POST":
		data=Myform(req.POST)
		data.save()
		return HttpResponse("<br><br><br><br><br><br><br><br><br><br><h1><center>Done</center></h1>")
	form=Myform()
	data=POLL.objects.last()
	# data={'data':data.question}
	return render(req,'myapp/submit.html',{'form':form,'data':data.question,'k':data.category})

def rating(req):
	if req.method=="POST":
		data=myrate(req.POST)
		data.save()
		return HttpResponse("<br><br><br><br><br><br><br><br><br><br><h1><center>Done</center></h1>")
	form=myrate()
	data=POLL.objects.last()
	return render(req,'myapp/submit.html',{'form':form,'data':data.question,'k':data.category})

def ans(req):
	if req.method=="POST":
		data=myanswer(req.POST)
		if data.is_valid():
			data.save()
		return HttpResponse("<br><br><br><br><br><br><br><br><br><br><h1><center>Done</center></h1>")
	form=myanswer()
	data=POLL.objects.last()
	# data={'data':data.question}
	return render(req,'myapp/submit.html',{'form':form,'data':data.question,'k':data.category})	

def home(request):
	return render(request,'myapp/home.html')	

def about(req):
	return render(req,"myapp/about.html")	

@login_required
def admin_page(req):
	data=Spoll.objects.all()
	y=0
	n=0
	for i in data:
		if i.opt=="Yes":
			y=y+1
		else:
			n=n+1
	data={'Yes':y,"No":n,"i":"yes","j":"no"}
	j=POLL.objects.last()
	try:
		return render(req,"myapp/result.html",{'data':data,'j':j.category})	
	except:
		return render(req,"myapp/result.html")