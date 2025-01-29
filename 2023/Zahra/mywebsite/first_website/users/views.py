from django.shortcuts import render


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('----------------')
        print(username, password)
        print('----------------')
    
    print("after post")
    return render(request, "login.html")