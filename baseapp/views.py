from django.shortcuts import render

import calendar

# Create your views here.
def home(request):
	string="Hello World!"
	return render(request, "baseapp/index.html", {"string":string})