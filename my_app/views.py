from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from django.conf import settings
import base64
import hashlib
from datetime import datetime


def index(request):
    if request.method=='POST':
        phone_number=request.POST.get('phone_number')
        amount_str=request.POST.get('amount')

        try:
            amount=int(amount_str)

        except ValueError:
            return HttpResponse("Error.Please enter a valid amount")


        if phone_number and amount:
            cl = MpesaClient()
            business_short_code=settings.MPESA_SHORTCODE
            account_reference = 'Denis'
            transaction_desc = 'purchased a product'
            callback_url = 'https://api.darajambili.com/express-payment'
            timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
            data_to_hash = f"{business_short_code}{settings.MPESA_PASSKEY}".encode('utf-8') #combined according to doc
            hashed_data = hashlib.sha256(data_to_hash).hexdigest() #here we have been hashing the data
            password= base64.b64encode(bytes.fromhex(hashed_data)).decode('utf-8')
            partyb=""

            response = cl.stk_push(
                phone_number,
                amount,
                business_short_code,
                account_reference,
                transaction_desc,
                callback_url,
                timestamp,
                password)
            return HttpResponse(response)
        
    return render(request,'index.html')
