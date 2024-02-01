from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient


def index(request):
    if request.method=='POST':
        phone_number=request.POST.get('phone_number')
        amount=request.POST.get('amount')

        if phone_number and amount:
            cl = MpesaClient()
            account_reference = 'Denis'
            transaction_desc = 'purchased a product'
            callback_url = 'https://api.darajambili.com/express-payment'
            response = cl.stk_push(phone_number,amount,account_reference,transaction_desc,callback_url)
            return HttpResponse(response)
        
    return render(request,'index.html')
