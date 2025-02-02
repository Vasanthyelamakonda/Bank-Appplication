from django.db import models

# Create your models here.

class customer(models.Model):
    customer_id=models.IntegerField(primary_key=True)
    customer_name=models.CharField(max_length=25)
    gender=models.CharField(max_length=2)
    phone_no=models.IntegerField()
    amount=models.FloatField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=12)


class transaction(models.Model):
    slno=models.IntegerField(primary_key=True)
    customer_id=models.IntegerField()
    transaction_date=models.DateField()
    transaction_type=models.CharField(max_length=2)
    amount=models.FloatField()

class loan(models.Model):
    loan_id=models.IntegerField(primary_key=True)
    loan_name=models.CharField(max_length=30)
    roi=models.FloatField()


class CustomerLoan(models.Model):
    ref_id=models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    loan_id = models.ForeignKey(loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time_period = models.PositiveIntegerField()
