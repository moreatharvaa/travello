#logic building comes here

from django.shortcuts import render
from .models import destination

# Create your views here.
def home(request):

    # dest1 = destination()
    # dest1.name = "Bombay"
    # dest1.desc="The City which nevers sleeps"
    # dest1.price = 1200
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = True

    # dest2 = destination()
    # dest2.name = "Hyderabad"
    # dest2.desc="First Biryani, then Sherwani"
    # dest2.price = 1500
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = False


    # dest3 = destination()
    # dest3.name = "Pune"
    # dest3.desc=" Cultural Capital of the Maratha peoples"
    # dest3.price = 2000
    # dest3.img = 'destination_3.jpg'
    # dest3.offer = False


    # dest4 = destination()
    # dest4.name = "Kerala"
    # dest4.desc=" God's own country"
    # dest4.price = 3500
    # dest4.img = 'destination_4.jpg'
    # dest4.offer = False


    # dest5 = destination()
    # dest5.name = "Bangalore"
    # dest5.desc=" Bengaluru - Be U"
    # dest5.price = 4500
    # dest5.img = 'destination_5.jpg'
    # dest5.offer = True


    # dest6 = destination()
    # dest6.name = "Kashmir"
    # dest6.desc=" Kashmir, where heaven touches the earth"
    # dest6.price = 6000
    # dest6.img = 'destination_6.jpg'
    # dest6.offer = False

    # dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    dests = destination.objects.all()


    return render(request, 'index.html', {'dests': dests})