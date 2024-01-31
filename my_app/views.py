from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaResponse

@csrf_exempt
def express_payment_callback(request):
    if request.method == 'POST':
        # Parse the callback data
        mpesa_response = MpesaResponse(request.body.decode('utf-8'))

        # Check if the payment was successful
        if mpesa_response.is_successful():
            # Payment was successful, you can update your database or trigger other processes
            print("Payment successful. Transaction ID:", mpesa_response.transaction_id)
        else:
            # Payment failed or was canceled
            print("Payment failed or canceled. Response:", mpesa_response.response_text)

        # Respond to Safaricom with a success message
        return HttpResponse("Callback received successfully")

from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

def index(request):
    cl = MpesaClient()
    phone_number = '0115735292'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)
