from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class ShopView(View):
    def get(self, request):
        context = {'data': [{'name': 'Bell Pepper',
                             'discount': 30,
                             'price_before': 120.00,
                             'price_after': 80.00,
                             'id': 1,
                             'url': 'store/images/product-1.jpg'},
                            {'name': 'Strawberry',
                             'discount': None,
                             'price_before': 120.00,
                             'id': 2,
                             'url': 'store/images/product-2.jpg'},
                            {'name': 'Green Beans',
                             'discount': None,
                             'price_before': 120.00,
                             'id': 3,
                             'url': 'store/images/product-3.jpg'},
                            {'name': 'Purple Cabbage',
                             'discount': None,
                             'price_before': 120.00,
                             'id': 4,
                             'url': 'store/images/product-4.jpg'},
                            {'name': 'Tomatoe',
                             'discount': 30,
                             'price_before': 120.00,
                             'price_after': 80.00,
                             'id': 5,
                             'url': 'store/images/product-5.jpg'},
                            {'name': 'Brocolli',
                             'discount': None,
                             'price_before': 120.00,
                             'id': 6,
                             'url': 'store/images/product-6.jpg'},
                            {'name': 'Carrots',
                             'discount': None,
                             'price_before': 120.00,
                             'id': 7,
                             'url': 'store/images/product-7.jpg'},
                            {'name': 'Fruit Juice',
                             'discount': None,
                             'price_before': 120.00,
                             'id': 8,
                             'url': 'store/images/product-8.jpg'},
                            {'name': 'Onion',
                             'discount': 30,
                             'price_before': 120.00,
                             'price_after': 80.00,
                             'id': 9,
                             'url': 'store/images/product-9.jpg'},
                            {'name': 'Apple',
                             'discount': None,
                             'price_before': 120.00,
                             'id': 10,
                             'url': 'store/images/product-10.jpg'},
                            {'name': 'Garlic',
                             'discount': None,
                             'price_before': 120.00,
                             'id': 11,
                             'url': 'store/images/product-11.jpg'},
                            {'name': 'Chilli',
                             'discount': None,
                             'price_before': 120.00,
                             'id': 12,
                             'url': 'store/images/product-12.jpg'},
                            ]
                   }
        return render(request, 'store/shop.html', context)


class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')


class ProductSingleView(View):
    def get(self, request, id):
        data = {1: {'name': 'Bell Pepper',
                    'description': 'Bell Pepper',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-1.jpg'},
                2: {'name': 'Strawberry',
                    'description': 'Strawberry',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-2.jpg'},
                3: {'name': 'Green Beans',
                    'description': 'Green Beans',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-3.jpg'},
                4: {'name': 'Purple Cabbage',
                    'description': 'Purple Cabbage',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-4.jpg'},
                5: {'name': 'Tomatoe',
                    'description': 'Tomatoe',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-5.jpg'},
                6: {'name': 'Brocolli',
                    'description': 'Brocolli',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-6.jpg'},
                7: {'name': 'Carrots',
                    'description': 'Carrots',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-7.jpg'},
                8: {'name': 'Fruit Juice',
                    'description': 'Fruit Juice',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-8.jpg'},
                9: {'name': 'Onion',
                    'description': 'Onion',
                    'price': 120.00,
                    'rating': 5.0,
                    'url': 'store/images/product-9.jpg'},
                10: {'name': 'Apple',
                     'description': 'Apple',
                     'price': 120.00,
                     'rating': 5.0,
                     'url': 'store/images/product-10.jpg'},
                11: {'name': 'Garlic',
                     'description': 'Garlic',
                     'price': 120.00,

                     'rating': 5.0,
                     'url': 'store/images/product-11.jpg'},
                12: {'name': 'Chilli',
                     'description': 'Chilli',
                     'price': 120.00,
                     'rating': 5.0,
                     'url': 'store/images/product-12.jpg'}
                }
        return render(request, "store/product-single.html", context=data[id])