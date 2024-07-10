from django.db import models

# Create your models here.
class RawData(models.Model):
    Store_ID = models.IntegerField()
    Date = models.DateField()
    Product_ID = models.CharField(max_length=100)
    Quantity_Sold = models.IntegerField()
    Total_Sales = models.IntegerField()
    
    


class ProcessedData(models.Model):
    Date = models.DateField()
    Store_ID = models.IntegerField()
    Total_Sales = models.IntegerField()
    Top_Selling_Product = models.CharField(max_length=50)