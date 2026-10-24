from django.http import HttpResponse
from decimal import Decimal, InvalidOperation
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.urls import reverse
from django.conf import settings
from .models import TBL_PLANT_CARE

from .models import TBL_USER
from .models import (
    TBL_USER,
    TBL_PRODUCT,
    TBL_CART,
    TBL_ORDER,
    TBL_ORDER_ITEM,
    TBL_FEEDBACK
)

# ---------------- WELCOME ----------------
# ---------------- WELCOME ----------------

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TBL_USER



# ---------------- SIGN UP ----------------
# def SIGUP(request):

#     if request.method == 'POST':

#         name = request.POST.get('NAME', '').strip()
#         email = request.POST.get('EMAIL', '').strip()
#         password = request.POST.get('PASSWORD', '')
#         address = request.POST.get('ADDRESS', '').strip()

#         # Check required fields
#         if not name or not email or not password:
#             return render(request, 'sigup.html', {
#                 'error': 'Please fill in all required fields'
#             })

#         # Check existing email
#         if TBL_USER.objects.filter(email=email).exists():
#             return render(request, 'sigup.html', {
#                 'error': 'Email already exists'
#             })

#         # Create user
#         TBL_USER.objects.create(
#             name=name,
#             email=email,
#             password=password,
#             address=address,
#             user_role='user'
#         )

#         # Form success message
#         messages.success(
#             request,
#             'Registration successful! Please login.'
#         )

#         return redirect('LOGIN')

#     return render(request, 'sigup.html')

# ---------------- SIGN UP ----------------


# def SIGUP(request):
#     if request.method == 'POST':

#         name = request.POST.get('NAME', '').strip()
#         email = request.POST.get('EMAIL', '').strip()
#         password = request.POST.get('PASSWORD', '')
#         address = request.POST.get('ADDRESS', '').strip()

#         if not name or not email or not password:
#             return render(request, 'sigup.html', {
#                 'error': 'Please fill in all required fields'
#             })

#         if TBL_USER.objects.filter(email=email).exists():
#             return render(request, 'sigup.html', {
#                 'error': 'Email already exists'
#             })

#         # Create unverified user
#         user = TBL_USER.objects.create(
#             name=name,
#             email=email,
#             password=password,
#             address=address,
#             user_role='user',
#             email_verified=False
#         )

#         # Create verification token
#         signer = TimestampSigner()
#         token = signer.sign(str(user.id))

#         verify_url = request.build_absolute_uri(
#             reverse('verify_email', kwargs={'token': token})
#         )

#         # Send verification email
#         try:
#             send_mail(
#                 subject='Verify your GreenLeaf Nursery email',
#                 message=(
#                     f'Hello {name},\n\n'
#                     'Thank you for registering with GreenLeaf Nursery.\n'
#                     'Verify your email using this link:\n\n'
#                     f'{verify_url}\n\n'
#                     'This link expires in 24 hours.'
#                 ),
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 recipient_list=[email],
#                 fail_silently=False,
#             )

#         except Exception as e:
#             print('Email error:', e)
#             user.delete()

#             return render(request, 'sigup.html', {
#                 'error': (
#                     'Verification email could not be sent. '
#                     'Please check your Gmail settings.'
#                 )
#             })

#         messages.success(
#             request,
#             'Signup successful! Please check your email to verify your account.'
#         )

#         return redirect('LOGIN')

#     return render(request, 'sigup.html')


# ---------------- LOGIN ----------------
# def LOGIN(request):
#     if request.method == 'POST':
#         email = request.POST.get('EMAIL')
#         password = request.POST.get('PASSWORD')

#         # ADMIN LOGIN
#         if email == 'admin@gmail.com' and password == 'ADMIN':
#             admindata = TBL_USER.objects.filter(
#                 email=email,
#                 password=password
#             ).first()

#             if admindata:
#                 request.session['id'] = admindata.id
#                 request.session['email'] = admindata.email
#                 request.session['role'] = 'admin'
#                 return redirect('/adminhome/')

#         # USER LOGIN
#         userdata = TBL_USER.objects.filter(
#             email=email,
#             password=password,
#             user_role='user'
#         ).first()

#         if userdata:
#             request.session['id'] = userdata.id
#             request.session['email'] = userdata.email
#             request.session['role'] = 'user'
#             return redirect('/userhome/')

#         return render(request, 'login.html', {
#             'error': 'Invalid email or password'
#         })

#     return render(request, 'login.html')


# ---------------- LOGIN ----------------

# def LOGIN(request):

#     if request.method == 'POST':

#         email = request.POST.get('EMAIL', '').strip()
#         password = request.POST.get('PASSWORD', '')

#         # ADMIN LOGIN
#         if email == 'admin@gmail.com' and password == 'ADMIN':

#             admindata = TBL_USER.objects.filter(
#                 email=email,
#                 password=password
#             ).first()

#             if admindata:
#                 request.session['id'] = admindata.id
#                 request.session['email'] = admindata.email
#                 request.session['role'] = 'admin'

#                 messages.success(
#                     request,
#                     'Admin login successful! Welcome back.'
#                 )

#                 return redirect('/adminhome/')

#         # USER LOGIN
#         userdata = TBL_USER.objects.filter(
#             email=email,
#             password=password,
#             user_role='user'
#         ).first()

#         if userdata:

#             # Check email verification
#             if not userdata.email_verified:
#                 return render(request, 'login.html', {
#                     'error': (
#                         'Please verify your email before logging in. '
#                         'Check your Gmail inbox.'
#                     )
#                 })

#             request.session['id'] = userdata.id
#             request.session['email'] = userdata.email
#             request.session['role'] = 'user'

#             messages.success(
#                 request,
#                 'Login successful! Welcome to GreenLeaf Nursery.'
#             )

#             return redirect('/userhome/')

#         return render(request, 'login.html', {
#             'error': 'Invalid email or password'
#         })

#     return render(request, 'login.html')



# ---------------- USER HOME ----------------
def userhome(request):
    if request.session.get('role') != 'user':
        return redirect('/')

    return render(request, 'user/userhome.html')


# ---------------- ADMIN HOME ----------------
def adminhome(request):
    if request.session.get('role') != 'admin':
        return redirect('/')

    return render(request, 'admin/adminhome.html')


# ---------------- VIEW USERS ----------------
def usersview(request):
    if request.session.get('role') != 'admin':
        return redirect('/')

    userdata = TBL_USER.objects.filter(user_role='user')

    return render(request, 'admin/usersview.html', {
        'userdata': userdata
    })


# ---------------- ADD PRODUCT ----------------
def addproduct(request):
    if request.session.get('role') != 'admin':
        return redirect('/')

    if request.method == 'POST':
        product_name = request.POST.get('PRODUCT NAME')
        price = request.POST.get('PRICE')
        describtion = request.POST.get('DESCRIBTION')
        qty = request.POST.get('QTY')
        image = request.FILES.get('product_image')

        if not product_name or not price or not describtion or not qty:
            return render(request, 'admin/addproduct.html', {
                'error': 'Please fill in all required fields'
            })

        try:
            price_value = Decimal(price)
            qty = int(qty)

            if price_value < 0 or qty < 0:
                raise ValueError

        except (InvalidOperation, TypeError, ValueError):
            return render(request, 'admin/addproduct.html', {
                'error': 'Enter a valid price and quantity'
            })

        productdata = TBL_PRODUCT(
            product_name=product_name,
            price=str(price_value),
            describtion=describtion,
            quantity=str(qty)
        )

        if image:
            productdata.image = image

        productdata.save()
        return redirect('viewproducts')

    return render(request, 'admin/addproduct.html')


# ---------------- VIEW PRODUCTS (ADMIN) ----------------
def viewproducts(request):
    if request.session.get('role') != 'admin':
        return redirect('/')

    userdata = TBL_PRODUCT.objects.all()

    return render(request, 'admin/viewproduct.html', {
        'userdata': userdata
    })


# ---------------- EDIT PRODUCT ----------------
# def editproduct(request):
#     if request.session.get('role') != 'admin':
#         return redirect('/')

#     product_id = (
#         request.GET.get('id')
#         if request.method == 'GET'
#         else request.POST.get('id')
#     )

#     product = get_object_or_404(TBL_PRODUCT, id=product_id)

#     if request.method == 'POST':
#         product_name = request.POST.get('product_name', '').strip()
#         price = request.POST.get('price', '').strip()
#         describtion = request.POST.get('describtion', '').strip()
#         qty = request.POST.get('qty', '').strip()

#         try:
#             qty_value = int(qty)
#             price_value = Decimal(price)

#             if (
#                 not product_name
#                 or not describtion
#                 or qty_value < 0
#                 or price_value < 0
#             ):
#                 raise ValueError

#         except (InvalidOperation, TypeError, ValueError):
#             return render(request, 'admin/editproduct.html', {
#                 'product': product,
#                 'error': 'Enter valid product details, price and quantity'
#             })

#         product.product_name = product_name
#         product.price = price_value
#         product.describtion = describtion
#         product.quantity = qty_value

#         if request.FILES.get('image'):
#             product.image = request.FILES['image']

#         print("Product Name:", product.product_name)
#         print("Price:", product.price)
#         print("Description:", product.describtion)
#         print("Quantity:", product.quantity)

#         product.save()

#         print("Product saved successfully!")

#         return redirect('viewproducts')

#     return render(request, 'admin/editproduct.html', {
#         'product': product
#     })

def editproduct(request):
    if request.session.get('role') != 'admin':
        return redirect('/')

    print("EDIT METHOD:", request.method)

    product_id = request.GET.get('id') or request.POST.get('id')

    if not product_id:
        return HttpResponse("Product ID missing")

    product = get_object_or_404(TBL_PRODUCT, id=product_id)

    if request.method == 'POST':
        print("POST REQUEST RECEIVED")
        print(request.POST)

        product_name = request.POST.get('product_name', '').strip()
        describtion = request.POST.get('describtion', '').strip()

        try:
            price_value = Decimal(request.POST.get('price', ''))
            qty_value = int(request.POST.get('qty', ''))

            if (
                not product_name
                or not describtion
                or price_value < 0
                or qty_value < 0
            ):
                raise ValueError

        except (InvalidOperation, TypeError, ValueError):
            return render(request, 'admin/editproduct.html', {
                'product': product,
                'error': 'Please enter valid product details, price and quantity'
            })

        product.product_name = product_name
        product.price = price_value
        product.describtion = describtion
        product.quantity = qty_value

        if request.FILES.get('image'):
            product.image = request.FILES['image']

        product.save()

        print("PRODUCT SAVED:", product.id)

        return redirect('viewproducts')

    return render(request, 'admin/editproduct.html', {
        'product': product
    })

# ---------------- DELETE PRODUCT ----------------
@require_POST
def deleteproduct(request):
    if request.session.get('role') != 'admin':
        return redirect('/')

    product_id = request.POST.get('id')
    product = get_object_or_404(TBL_PRODUCT, id=product_id)
    product.delete()

    return redirect('viewproducts')


# ---------------- DELETE USER ----------------
@require_POST
def delete_user(request):
    if request.session.get('role') != 'admin':
        return redirect('/')

    user_id = request.POST.get('id')

    TBL_USER.objects.filter(
        id=user_id,
        user_role='user'
    ).delete()

    return redirect('/usersview/')


# ---------------- LOGOUT ----------------
def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')


# ---------------- USER VIEW PRODUCTS ----------------
def userviewproduct(request):
    if request.session.get('role') != 'user':
        return redirect('/')

    data = TBL_PRODUCT.objects.all()

    return render(request, 'user/userviewproduct.html', {
        'data': data
    })


# ---------------- PRODUCT DETAILS ----------------
def productdetails(request):
    if request.session.get('role') != 'user':
        return redirect('/')

    product_id = request.GET.get('id')
    data = get_object_or_404(TBL_PRODUCT, id=product_id)

    return render(request, 'user/userproductdetails.html', {
        'data': data
    })


# ---------------- ADD TO CART ----------------
def add_to_cart(request):
    if request.session.get('role') != 'user':
        return redirect('/')

    product_id = request.GET.get('id')

    try:
        quantity = int(request.GET.get('number', 1))
        if quantity < 1:
            raise ValueError
    except (TypeError, ValueError):
        return redirect('/userviewproduct/')

    product = get_object_or_404(TBL_PRODUCT, id=product_id)
    user = get_object_or_404(
        TBL_USER, id=request.session['id']
    )

    try:
        price = Decimal(str(product.price))
        stock = int(product.quantity)

        if price < 0 or stock < 0:
            raise ValueError

    except (InvalidOperation, TypeError, ValueError):
        return redirect('/userviewproduct/')

    cart_item = TBL_CART.objects.filter(
        user=user,
        product=product
    ).first()

    old_quantity = cart_item.quantity if cart_item else 0
    new_quantity = old_quantity + quantity

    if new_quantity > stock:
        return render(request, 'user/userviewproduct.html', {
            'data': TBL_PRODUCT.objects.all(),
            'error': f'Only {stock} items available.'
        })

    if cart_item:
        cart_item.quantity = new_quantity
        cart_item.price = price
        cart_item.total_price = price * new_quantity
        cart_item.save()
    else:
        TBL_CART.objects.create(
            user=user,
            product=product,
            quantity=quantity,
            price=price,
            total_price=price * quantity
        )

    return redirect('/cart/')


# ---------------- CART PAGE ----------------
def cart_view(request):
    if request.session.get('role') != 'user':
        return redirect('/')

    user = get_object_or_404(
        TBL_USER, id=request.session['id']
    )

    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        action = request.POST.get('action')

        item = get_object_or_404(
            TBL_CART,
            id=cart_id,
            user=user
        )

        if action == 'remove':
            item.delete()

        elif action == 'update':
            try:
                quantity = int(request.POST.get('quantity', 1))
                stock = int(item.product.quantity)

                if quantity < 1 or quantity > stock:
                    return render(request, 'user/cart.html', {
                        'items': TBL_CART.objects.filter(user=user),
                        'grand_total': sum(
                            (
                                x.total_price
                                for x in TBL_CART.objects.filter(user=user)
                            ),
                            Decimal('0.00')
                        ),
                        'error': f'Quantity must be between 1 and {stock}.'
                    })

                item.quantity = quantity
                item.price = Decimal(str(item.product.price))
                item.total_price = item.price * quantity
                item.save()

            except (InvalidOperation, TypeError, ValueError):
                return redirect('/cart/')

        return redirect('/cart/')

    items = TBL_CART.objects.filter(user=user)

    grand_total = sum(
        (item.total_price for item in items),
        Decimal('0.00')
    )

    return render(request, 'user/cart.html', {
        'items': items,
        'grand_total': grand_total
    })



# ---------------- CHECKOUT ----------------

from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import (
    TBL_USER,
    TBL_CART,
    TBL_ORDER,
    TBL_ORDER_ITEM,
)


def checkout(request):

    # Check user login
    if request.session.get('role') != 'user':
        return redirect('LOGIN')

    user = get_object_or_404(
        TBL_USER,
        id=request.session.get('id')
    )

    # Get cart items
    cart_items = TBL_CART.objects.filter(user=user)

    if not cart_items.exists():
        return redirect('cart')

    # Calculate total
    total = sum(
        (item.total_price for item in cart_items),
        Decimal('0.00')
    )

    if request.method == 'POST':

        payment_method = request.POST.get('payment_method')

        # Validate payment method
        if payment_method not in ['UPI', 'Card', 'Net Banking']:
            return render(request, 'user/payment.html', {
                'cart_items': cart_items,
                'total': total,
                'error': 'Please select a payment method.'
            })

        # DEMO PAYMENT ONLY
        with transaction.atomic():

            # Save order in database
            order = TBL_ORDER.objects.create(
                user=user,
                total_amount=total,
                status='Placed'
            )

            # Save order items
            for item in cart_items:
                TBL_ORDER_ITEM.objects.create(
                    order=order,
                    product=item.product,
                    product_name=item.product.product_name,
                    quantity=item.quantity,
                    price=item.price,
                    total_price=item.total_price
                )

            # Clear cart after saving order
            cart_items.delete()

        # Save order details in session
        request.session['last_order_id'] = order.id
        request.session['last_payment_method'] = payment_method

        return redirect('payment_success')

    return render(request, 'user/payment.html', {
        'cart_items': cart_items,
        'total': total
    })


# ---------------- PAYMENT SUCCESS ----------------

def payment_success(request):

    if request.session.get('role') != 'user':
        return redirect('LOGIN')

    order_id = request.session.get('last_order_id')

    if not order_id:
        return redirect('my_orders')

    order = get_object_or_404(
        TBL_ORDER,
        id=order_id,
        user_id=request.session.get('id')
    )

    return render(request, 'user/payment_success.html', {
        'order': order,
        'payment_method': request.session.get(
            'last_payment_method', ''
        )
    })

# ---------------- MY ORDERS ----------------
def my_orders(request):
    if request.session.get('role') != 'user':
        return redirect('/')

    user = get_object_or_404(
        TBL_USER, id=request.session['id']
    )

    orders = (
        TBL_ORDER.objects
        .filter(user=user)
        .prefetch_related('items')
        .order_by('-created_at')
    )

    return render(request, 'user/my_orders.html', {
        'orders': orders
    })



# ---------------- MY PROFILE ----------------
def profile(request):
    if request.session.get('role') != 'user':
        return redirect('/login/')

    user = get_object_or_404(
        TBL_USER,
        id=request.session['id']
    )

    if request.method == 'POST':
        image = request.FILES.get('image')

        if image:
            user.image = image
            user.save()

    return render(
        request,
        'user/myprofile.html',
        {'user': user}
    )

def my_orders(request):
    if request.session.get('role') != 'user':
        return redirect('LOGIN')

    user = get_object_or_404(
        TBL_USER,
        id=request.session.get('id')
    )

    orders = TBL_ORDER.objects.filter(
        user=user
    ).prefetch_related('items').order_by('-created_at')

    return render(
        request,
        'user/my_orders.html',
        {'orders': orders}
    )

# ---------------- ADMIN VIEW ORDERS ----------------

def admin_orders(request):

    if request.session.get('role') != 'admin':
        return redirect('LOGIN')

    orders = TBL_ORDER.objects.select_related(
        'user'
    ).prefetch_related(
        'items'
    ).order_by('-created_at')

    return render(
        request,
        'admin/admin_orders.html',
        {'orders': orders}
    )


# ---------------- UPDATE ORDER STATUS ----------------

def update_order_status(request, order_id):

    if request.session.get('role') != 'admin':
        return redirect('LOGIN')

    if request.method == 'POST':

        order = get_object_or_404(
            TBL_ORDER,
            id=order_id
        )

        new_status = request.POST.get('status')

        allowed_statuses = [
            'Placed',
            'Processing',
            'Shipped',
            'Delivered',
            'Cancelled'
        ]

        if new_status in allowed_statuses:
            order.status = new_status
            order.save()

    return redirect('admin_orders')

# ---------------- USER FEEDBACK ----------------

# ---------------- USER FEEDBACK ----------------

def feedback(request):
    if request.session.get('role') != 'user':
        return redirect('LOGIN')

    user = get_object_or_404(
        TBL_USER,
        id=request.session.get('id')
    )

    if request.method == 'POST':
        message = request.POST.get('message', '').strip()
        rating = request.POST.get('rating', '5')

        if message and rating.isdigit() and 1 <= int(rating) <= 5:
            TBL_FEEDBACK.objects.create(
                user=user,
                message=message,
                rating=int(rating)
            )
            return redirect('userhome')

    return render(request, 'user/feedback.html')


# ---------------- ADMIN VIEW FEEDBACK ----------------

def view_feedback(request):
    if request.session.get('role') != 'admin':
        return redirect('LOGIN')

    feedbacks = TBL_FEEDBACK.objects.select_related(
        'user'
    ).order_by('-created_at')

    return render(
        request,
        'admin/view_feedback.html',
        {'feedbacks': feedbacks}
    )
#  welcome(request):
#     feedbacks = TBL_FEEDBACK.objects.select_related(
#         'user'
#     ).order_by('-created_at')

#     return render(request, 'welcome.html', {
#         'feedbacks': feedbacks
#     })
def test_email(request):
    send_mail(
        subject='GreenLeaf Nursery Email Test',
        message='Your Django email setup is working!',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
    return HttpResponse('Email sent successfully!')
def verify_email(request, token):
    signer = TimestampSigner()

    try:
        user_id = signer.unsign(token, max_age=86400)
    except SignatureExpired:
        return HttpResponse('Verification link expired.')
    except BadSignature:
        return HttpResponse('Invalid verification link.')

    user = get_object_or_404(TBL_USER, id=user_id)

    user.email_verified = True
    user.save(update_fields=['email_verified'])

    return HttpResponse(
        'Email verified successfully! You can now login.'
    )


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TBL_USER


# ---------------- SIGNUP ----------------

# def SIGUP(request):
#     if request.method == 'POST':

#         name = request.POST.get('NAME', '').strip()
#         email = request.POST.get('EMAIL', '').strip()
#         password = request.POST.get('PASSWORD', '')
#         address = request.POST.get('ADDRESS', '').strip()

#         # Check required fields
#         if not name or not email or not password:
#             return render(request, 'sigup.html', {
#                 'error': 'Please fill in all required fields'
#             })

#         # Check duplicate email
#         if TBL_USER.objects.filter(email=email).exists():
#             return render(request, 'sigup.html', {
#                 'error': 'Email already exists'
#             })

#         # Create user account
#         TBL_USER.objects.create(
#             name=name,
#             email=email,
#             password=password,
#             address=address,
#             user_role='user',
#             email_verified=True
#         )

#         messages.success(
#             request,
#             'Signup successful! Please login.'
#         )

#         return redirect('LOGIN')

#     return render(request, 'sigup.html')


# ---------------- LOGIN ----------------

def LOGIN(request):
    if request.method == 'POST':

        email = request.POST.get('EMAIL', '').strip()
        password = request.POST.get('PASSWORD', '')

        # ADMIN LOGIN
        if email == 'admin@gmail.com' and password == 'ADMIN':

            admindata = TBL_USER.objects.filter(
                email=email,
                password=password
            ).first()

            if admindata:
                request.session['id'] = admindata.id
                request.session['email'] = admindata.email
                request.session['role'] = 'admin'

                messages.success(
                    request,
                    'Admin login successful!'
                )

                return redirect('/adminhome/')

        # USER LOGIN
        userdata = TBL_USER.objects.filter(
            email=email,
            password=password,
            user_role='user'
        ).first()

        if userdata:

            request.session['id'] = userdata.id
            request.session['email'] = userdata.email
            request.session['role'] = 'user'

            messages.success(
                request,
                'Login successful!'
            )

            return redirect('/userhome/')

        return render(request, 'login.html', {
            'error': 'Invalid email or password'
        })

    return render(request, 'login.html')

def SIGUP(request):
    if request.method == 'POST':

        name = request.POST.get('NAME', '').strip()
        email = request.POST.get('EMAIL', '').strip()
        password = request.POST.get('PASSWORD', '')
        address = request.POST.get('ADDRESS', '').strip()

        if not name or not email or not password:
            return render(request, 'sigup.html', {
                'error': 'Please fill all required fields'
            })

        if TBL_USER.objects.filter(email=email).exists():
            return render(request, 'sigup.html', {
                'error': 'Email already exists'
            })

        try:
            user = TBL_USER.objects.create(
                name=name,
                email=email,
                password=password,
                address=address,
                user_role='user',
                email_verified=True
            )

            messages.success(
                request,
                'Signup successful! Please login.'
            )

            return redirect('LOGIN')

        except Exception as e:
            print('Signup error:', e)

            return render(request, 'sigup.html', {
                'error': 'Signup failed. Please check the server error.'
            })

    return render(request, 'sigup.html')



# ADMIN: Add plant care tips
def addplantcare(request):
    if request.session.get('role') != 'admin':
        return redirect('/')

    if request.method == 'POST':
        TBL_PLANT_CARE.objects.create(
            plant_name=request.POST.get('plant_name'),
            image=request.FILES.get('image'),
            watering=request.POST.get('watering'),
            sunlight=request.POST.get('sunlight'),
            soil=request.POST.get('soil'),
            fertilizer=request.POST.get('fertilizer'),
            growing_tips=request.POST.get('growing_tips')
        )

        return redirect('/viewplantcare/')

    return render(request, 'admin/addplantcare.html')


# ADMIN: View all plant care tips
def viewplantcare(request):
    if request.session.get('role') != 'admin':
        return redirect('/')

    data = TBL_PLANT_CARE.objects.all().order_by('-id')

    return render(
        request,
        'admin/viewplantcare.html',
        {'data': data}
    )


# USER: View plant care tips
def userplantcare(request):
    if request.session.get('role') != 'user':
        return redirect('/')

    data = TBL_PLANT_CARE.objects.all().order_by('-id')

    return render(
        request,
        'user/userplantcare.html',
        {'data': data}
    )


# ADMIN: Edit plant care tips
def editplantcare(request):
    if request.session.get('role') != 'admin':
        return redirect('/')

    plant_id = request.GET.get('id')

    plant = get_object_or_404(
        TBL_PLANT_CARE,
        id=plant_id
    )

    if request.method == 'POST':
        plant.plant_name = request.POST.get('plant_name')
        plant.watering = request.POST.get('watering')
        plant.sunlight = request.POST.get('sunlight')
        plant.soil = request.POST.get('soil')
        plant.fertilizer = request.POST.get('fertilizer')
        plant.growing_tips = request.POST.get('growing_tips')

        if request.FILES.get('image'):
            plant.image = request.FILES.get('image')

        plant.save()

        return redirect('/viewplantcare/')

    return render(
        request,
        'admin/editplantcare.html',
        {'plant': plant}
    )


# ADMIN: Delete plant care tips
def deleteplantcare(request):
    if request.session.get('role') != 'admin':
        return redirect('/')

    if request.method == 'POST':
        plant_id = request.POST.get('id')

        plant = get_object_or_404(
            TBL_PLANT_CARE,
            id=plant_id
        )

        plant.delete()

    return redirect('/viewplantcare/')

# ---------------- WELCOME ----------------
def welcome(request):
    reviews = TBL_FEEDBACK.objects.select_related(
        'user'
    ).order_by('-created_at')

    print("TOTAL REVIEWS:", reviews.count())

    return render(request, 'welcome.html', {
        'reviews': reviews
    })
