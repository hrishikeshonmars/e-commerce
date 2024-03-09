from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField(max_length=500)
    phonenumber = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name
    

from django.db import models

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.TextField()  # Use TextField for larger text fields
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Use DecimalField for storing monetary values
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=90)  # Use EmailField for email addresses
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True, null=True)  # Allow blank and null values for optional fields
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    oid = models.CharField(max_length=150, blank=True)  # Make oid field non-null by removing null=True
    amountpaid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Use DecimalField for storing monetary values, allow null values
    paymentstatus = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)  # Use ForeignKey to establish a relationship between OrderUpdate and Orders
    update_desc = models.TextField()  # Use TextField for larger text fields
    delivered = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)  # Use DateTimeField for timestamp

    def __str__(self):
        return self.update_desc[:50] + "..."  # Truncate the update_desc field for better readability
