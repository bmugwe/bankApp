from django.db import models
import uuid
# import reverse from


ID_TYPE = (
    ('ID', 'National ID'),
    ('Passport', 'Passport Number'),
    ('Military ID', 'Military ID'),
    ('Alien ID', 'ALIEN ID')
)

# Create your models here.
class Customer(models.Model):
    customer = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=100)
    s_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    id_type = models.CharField(max_length=100, choices=ID_TYPE, null=False)
    id_number = models.CharField(max_length=100, unique=True)
    created_at =models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    

    class Meta:
        db_table = "customer"

    def __str__(self):
        return f"{self.f_name} - {self.f_name} {self.l_name}"

    def get_absolute_url(self):
        # return reverse("_detail", kwargs={"pk": self.pk})
        pass
    
class Balances(models.Model):
    id = models.AutoField(primary_key=True)
    customer  = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, unique=True)
    balance = models.IntegerField(default=0, null=False) 
    created_at =models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    
    class Meta:
        db_table = 'balances'
    
    
class Withdrawal(models.Model):
    id = models.AutoField(primary_key=True)
    customer  = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=0, null=False) 
    created_at =models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    
    class Meta:
        db_table = 'withdrawals'


class Deposit(models.Model):
    id = models.AutoField(primary_key=True)
    customer  = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=0, null=False) 
    created_at =models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)
    
    class Meta:
        db_table = 'deposits'