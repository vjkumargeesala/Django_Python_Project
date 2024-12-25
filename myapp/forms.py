from django.forms import ModelForm
from myapp.models import Spoll,rate,answer,POLL,covid,covid_details
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class mycovid_details(ModelForm):
	class Meta:
		model=covid_details
		fields=['name','gender','age','city','address','phno','email']

class mycovid(ModelForm):
	class Meta:
		model=covid
		fields=['diffculty_Breathing','chest_pain','loss_of_Speech','loss_of_Taste','fever','cold','dry_cough','triedness','sore_throat','headache']

class Myform(ModelForm):
	class Meta:
		model=Spoll
		fields=['name','opt']

class mypoll(ModelForm):
	class Meta:
		model=POLL
		fields='__all__'
		
class myrate(ModelForm):
	class Meta:
		model=rate
		fields='__all__'

class myanswer(ModelForm):
	class Meta:
		model=answer
		fields="__all__"		

class Myforms(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','password1','password2','email']		