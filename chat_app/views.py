from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
from .models import message  # Assuming you have a ChatMessage model

def get_chat_messages(request):
    messages = message.objects.all()
    messages_data = [{'user': msg.user, 'text': msg.text} for msg in messages]
    return JsonResponse({'messages': messages_data})


def send_tanishq(request):
    msg = request.POST.get('message')
    if(msg != ''):
        new_message = message(user='tanishq',text=msg)
        new_message.save()
    return HttpResponse('Message sent successfully')

def send_mudra(request):
    msg = request.POST.get('message')
    new_message = message(user='mudra',text=msg)
    new_message.save()
    return HttpResponse('Message sent successfully')


def home(request):
    return render(request,'home.html')
def tanishq(request):
    msg = message.objects.all()  
    return render(request,'tanishq.html',{'msg':msg})
    
def mudra(request):
    return render(request,'mudra.html')