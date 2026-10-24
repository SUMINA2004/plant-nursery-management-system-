

from django.urls import path
from . import views

urlpatterns = [

    # WELCOME
    path('', views.welcome, name='welcome'),

    # SIGN UP AND LOGIN
    path('SIGUP/', views.SIGUP, name='SIGUP'),
    path('LOGIN/', views.LOGIN, name='LOGIN'),

    # USER AND ADMIN HOME
    path('userhome/', views.userhome, name='userhome'),
    path('adminhome/', views.adminhome, name='adminhome'),

    # ADMIN
    path('usersview/', views.usersview, name='usersview'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('viewproducts/', views.viewproducts, name='viewproducts'),
    path('editproduct/', views.editproduct, name='editproduct'),
    path('deleteproduct/', views.deleteproduct, name='deleteproduct'),
    path('delete_user/', views.delete_user, name='delete_user'),

    # LOGOUT
    path('logout/', views.logout, name='logout'),

    # USER PRODUCTS
    path('userviewproduct/', views.userviewproduct, name='userviewproduct'),
    path('productdetails/', views.productdetails, name='productdetails'),

    # CART
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('my-orders/', views.my_orders, name='my_orders'),

    # USER PROFILE
    path('profile/', views.profile, name='myprofile'),

    # PAYMENT SUCCESS
    path('payment-success/', views.payment_success, name='payment_success'),

    # ADMIN ORDER MANAGEMENT
    path('admin-orders/', views.admin_orders, name='admin_orders'),
    path(
        'update-order-status/<int:order_id>/',
        views.update_order_status,
        name='update_order_status'
    ),

    # FEEDBACK
    path('feedback/', views.feedback, name='feedback'),
    path('view-feedback/', views.view_feedback, name='view_feedback'),

    # EMAIL VERIFICATION
    path(
        'verify-email/<str:token>/',
        views.verify_email,
        name='verify_email'
    ),

    # TEST EMAIL
    path('test-email/', views.test_email, name='test_email'),

    # PLANT CARE TIPS - ADMIN
    path(
        'addplantcare/',
        views.addplantcare,
        name='addplantcare'
    ),

    path(
        'viewplantcare/',
        views.viewplantcare,
        name='viewplantcare'
    ),

    # PLANT CARE TIPS - USER
    path(
        'userplantcare/',
        views.userplantcare,
        name='userplantcare'
    ),

    # EDIT PLANT CARE TIPS
    path(
        'editplantcare/',
        views.editplantcare,
        name='editplantcare'
    ),

    # DELETE PLANT CARE TIPS
    path(
        'deleteplantcare/',
        views.deleteplantcare,
        name='deleteplantcare'
    ),
]
