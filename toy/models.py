# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=50)
    cust_address = models.CharField(max_length=50, blank=True, null=True)
    cust_city = models.CharField(max_length=50, blank=True, null=True)
    cust_state = models.CharField(max_length=5, blank=True, null=True)
    cust_zip = models.CharField(max_length=10, blank=True, null=True)
    cust_country = models.CharField(max_length=50, blank=True, null=True)
    cust_contact = models.CharField(max_length=50, blank=True, null=True)
    cust_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Orderitems(models.Model):
    order_num = models.OneToOneField('Orders', models.DO_NOTHING, db_column='order_num', primary_key=True)
    order_item = models.IntegerField()
    prod = models.ForeignKey('Products', models.DO_NOTHING)
    quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'orderitems'
        unique_together = (('order_num', 'order_item'),)


class Orders(models.Model):
    order_num = models.AutoField(primary_key=True)
    order_date = models.DateTimeField()
    cust = models.ForeignKey(Customers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders'


class Productnotes(models.Model):
    note_id = models.AutoField(primary_key=True)
    prod_id = models.CharField(max_length=10)
    note_date = models.DateTimeField()
    note_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productnotes'


class Products(models.Model):
    prod_id = models.CharField(primary_key=True, max_length=10)
    vend = models.ForeignKey('Vendors', models.DO_NOTHING)
    prod_name = models.CharField(max_length=255)
    prod_price = models.DecimalField(max_digits=8, decimal_places=2)
    prod_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Vendors(models.Model):
    vend_id = models.AutoField(primary_key=True)
    vend_name = models.CharField(max_length=50)
    vend_address = models.CharField(max_length=50, blank=True, null=True)
    vend_city = models.CharField(max_length=50, blank=True, null=True)
    vend_state = models.CharField(max_length=5, blank=True, null=True)
    vend_zip = models.CharField(max_length=10, blank=True, null=True)
    vend_country = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendors'
