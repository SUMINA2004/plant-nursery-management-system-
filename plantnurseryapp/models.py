

from django.db import models


# ---------------- USER ----------------
class TBL_USER(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    user_role = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='')

    # Profile image
    image = models.ImageField(
        upload_to='profile/',
        null=True,
        blank=True
    )

    # Email verification
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# ---------------- PRODUCT ----------------
class TBL_PRODUCT(models.Model):
    product_name = models.CharField(max_length=50, default='')
    price = models.CharField(max_length=50, default='')
    quantity = models.CharField(max_length=50, default='')
    describtion = models.CharField(max_length=50, default='')

    # Product image
    image = models.ImageField(
        upload_to='products/',
        default='',
        blank=True
    )

    def __str__(self):
        return self.product_name


# ---------------- CART ----------------
class TBL_CART(models.Model):
    user = models.ForeignKey(
        TBL_USER,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        TBL_PRODUCT,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name


# ---------------- ORDER ----------------
class TBL_ORDER(models.Model):
    user = models.ForeignKey(
        TBL_USER,
        on_delete=models.CASCADE
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=30,
        default='Placed'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


# ---------------- ORDER ITEM ----------------
class TBL_ORDER_ITEM(models.Model):
    order = models.ForeignKey(
        TBL_ORDER,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        TBL_PRODUCT,
        on_delete=models.SET_NULL,
        null=True
    )

    product_name = models.CharField(max_length=100)

    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.product_name


# ---------------- FEEDBACK ----------------
class TBL_FEEDBACK(models.Model):
    user = models.ForeignKey(
        TBL_USER,
        on_delete=models.CASCADE
    )

    message = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name

from django.db import models


class TBL_PLANT_CARE(models.Model):
    plant_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='plant_care/')
    watering = models.TextField()
    sunlight = models.TextField()
    soil = models.TextField()
    fertilizer = models.TextField()
    growing_tips = models.TextField()

    def __str__(self):
        return self.plant_name
