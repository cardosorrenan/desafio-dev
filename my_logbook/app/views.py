from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import transaction as transaction_db
from itertools import islice
from django.shortcuts import get_object_or_404


from .utils import FileCNAB
from .forms import UploadCNABForm
from .models import FileOrigin, Transaction, TransactionType, Store

# Create your views here.
def index(request):
    return render(request, 'base.html')


def upload_cnab(request):
    form = UploadCNABForm()
    return render(request, 'form.html', { 'form': form })


def manage_cnab(request):
    if request.method == 'POST':
        form = UploadCNABForm(request.POST, request.FILES)
        if form.is_valid():
            cnab_file = FileCNAB(request.FILES['cnab_file'])
            cnab_file.load_data()
            try:
                with transaction_db.atomic():
                    # Persisting FileOrigin
                    file, _ = FileOrigin.objects.get_or_create(**cnab_file.file_origin_fields())
                    
                    # Persisting Stores
                    stores = [Store(name=s['name'], owner=s['owner']) for s in cnab_file.stores]
                    batch_stores = list(islice(stores, len(stores)))
                    Store.objects.bulk_create(batch_stores, len(stores))

                    # Persisting Transactions
                    transactions = [Transaction(file_origin=file,
                                                type=TransactionType.objects.filter(type_num=t['type']).first(), 
                                                store=Store.objects.filter(name=t['store']).first(), 
                                                value=t['value'],
                                                cpf=t['cpf'],
                                                card=t['card'],
                                                datetime=t['datetime']) 
                                                for t in cnab_file.transactions]
                    batch_transactions = list(islice(transactions, len(transactions)))
                    Transaction.objects.bulk_create(batch_transactions, len(transactions))
            except Exception as e:
                print(e)

    return HttpResponseRedirect('/upload_cnab')


