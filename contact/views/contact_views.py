from django.shortcuts import render
from contact.models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')[0:10]
    
    # print(contacts.query)  mostra a query(caminho) que o programa percorre e solicita no banco de dados
    
    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context,
    )

