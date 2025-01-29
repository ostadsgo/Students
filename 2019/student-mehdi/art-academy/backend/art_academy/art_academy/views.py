from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

from json import JSONEncoder

from users.models import Payment


@login_required(login_url='/login')
def info(request):
    user = request.user
    payments = Payment.objects.filter(user = user.id).order_by('-date')
    return render(request, 'info.html', {'payments': payments})


@csrf_exempt
@require_POST
def auth(request):
	print(request.POST)
	response_data = {}
	superuser = User.objects.filter(is_superuser=True).first()
	if 'username' in request.POST and 'password' in request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username == superuser.username and superuser.check_password(password):
			response_data['result'] = 'ok'
			response_data['status_code'] = 200
			response_data['message'] = 'Credential is correct'
			return JsonResponse(response_data, encoder=JSONEncoder)
		else:
			response_data['result'] = 'error'
			response_data['status_code'] = 403
			response_data['message'] = 'Invalid Credentials'
			return JsonResponse(response_data, encoder=JSONEncoder)
	else:
		response_data['result'] = 'error'
		response_data['status_code'] = 500
		response_data['message'] = 'Incorrect parameters'
		return JsonResponse(response_data, encoder=JSONEncoder)
		


