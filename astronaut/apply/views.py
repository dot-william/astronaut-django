from django.shortcuts import render

# Create your views here.

def apply(request):
    return render(request,"apply/index.html")

def submit(request):
    print("hello world", request)
    if request.method == 'POST':
        print("HELLO2")
        try:
            name = request.POST['name']
            height = float(request.POST['height'])
            if 160 < height < 190:
                return render(request, 'apply/result.html', {'message': f'Congratulations {name}! You have the correct height to be an astronaut.'})
            elif height < 160:
                return render(request, 'apply/result.html', {'message': f'Sorry, {name}. Your height is below the minimum height to be an astronaut.'})
            else:
                return render(request, 'apply/result.html', {'message': f'Sorry, {name}. Your height is above the maximum height to be an astronaut.'})
        except Exception:
            return render(request, 'apply/result.html', {'message': 'Sorry, something went wrong. Please try again.'})
        
    return render(request, 'apply/index.html')