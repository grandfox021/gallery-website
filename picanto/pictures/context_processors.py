from .models import Customer


def customers(request) :

    return {'customer' : Customer.objects.all()}