from django.db import models

class product(models.Model):
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    price = models.IntegerField(default="100")
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class checkout(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    First_name = models.CharField(max_length=90)
    Last_name = models.CharField(max_length=90)
    phone = models.CharField(max_length=15, default="")
    email = models.CharField(max_length=110, default="")
    Address = models.CharField(max_length=1000)
    Country = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=15)


class status(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000, default="")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
