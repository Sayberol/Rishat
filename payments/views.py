import stripe
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from .models import Item

stripe.api_key = settings.STRIPE_API_KEY

def buy_item(id):
    try:
        item = Item.objects.get(id=id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(item.price*100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )
        return JsonResponse({'sessionId': session.id})
    except Item.DoesNotExist:
        return HttpResponse(status=404)


def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
        return render(request, 'item_detail.html', {'item': item, 'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY})
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Не найдено'}, status=404)
