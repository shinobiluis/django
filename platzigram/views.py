from django.http import HttpResponse
#importamos  el modulo para saber la hora
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('la hora del servidor es {now}'.format(now=str(now)))

def sort_integers(request):
    # print(request)
    # import pdb; pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message':'todo bien'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

def say_hi(request, name, age):
    if age < 12:
        message = 'Perdon {}, tu edadad es menor'.format(name)
    else:
        message = 'Hola, {}, bienvenido.'.format(name)
    return HttpResponse(message)

