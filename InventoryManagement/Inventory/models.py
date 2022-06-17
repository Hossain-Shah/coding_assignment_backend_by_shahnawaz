from django.db import models


class Supplier(models.Model):
    id = models.BigAutoField(primary_key=True, 
                             editable=False,
                             unique=True
                            )
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        app_label = "Inventory"


class Inventory(models.Model):
    id = models.BigAutoField(primary_key=True, 
                             editable=False,
                             unique=True
                            )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        app_label = "Inventory"



