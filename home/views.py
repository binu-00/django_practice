from django.shortcuts import render

def home_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        print("Name:", username)
        print("Email:", email)

    return render(request, 'home/index.html')

