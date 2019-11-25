from django.shortcuts import render

# Create your views here.
def ly_test(request):
	return render(request,'ly_app/test.html')
