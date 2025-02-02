from calendar import error

from django.shortcuts import render

from online.models import customer, transaction, loan, CustomerLoan


# Create your views here.

def home(req):
    return render(req,'home.html')


def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')


def register(req):
    if req.method=='POST':
        a=int(req.POST.get('cid'))
        b=req.POST.get('cname')
        c = req.POST.get('gender')
        d = int(req.POST.get('phno'))
        e = float(req.POST.get('amt'))
        f = req.POST.get('uname')
        g = req.POST.get('pwd')
        h=req.POST.get('cpwd')
        special_characters = '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
        if g != h:
            return render(req, 'register.html', {'msg': 'Password and Confirm Password should be the same.'})
        if not any(char.isupper() for char in g):
            return render(req, 'register.html', {'msg': 'Password must contain at least one uppercase letter.'})
        if not any(char.isdigit() for char in g):
            return render(req, 'register.html', {'msg': 'Password must contain at least one number.'})
        if not any(char in special_characters for char in g):
            return render(req, 'register.html', {'msg': 'Password must contain at least one special character.'})
        if len(g) < 8 or len(g) > 12:
            return render(req, 'register.html', {'msg': 'Password must be between 8 and 12 characters long.'})
        d1 = customer(customer_id=a, customer_name=b, gender=c, phone_no=d, amount=e, username=f, password=g)
        d1.save()
        return render(req, 'register.html', {'msg': 'Successfully Registered. Proceed to Login'})
    else:
        return render(req,'register.html')


def login(req):
    if req.method=='POST':
        try:
            a =req.POST.get('uname')
            b= req.POST.get('pwd')
            c=customer.objects.get(username=a)
            if c.password == b:
                return render(req, 'welcome.html')
            else:
                error = 'Invalid Credentials'
                return render(req, 'login.html', {'error': error})
        except:
            error = 'Invalid Credentials'
            return render(req, 'login.html', {'error': error})
    else:
        return render(req,'login.html')


def welcome(req):
    return render(req,'welcome.html')


def withdraw(req):
    if req.method=='POST':
        a=int(req.POST.get('cid'))
        b=req.POST.get('date')
        c=req.POST.get('ttype')
        d=float(req.POST.get('amt'))
        g=customer.objects.get(customer_id=a)
        h=g.amount
        if d < h:
            e=transaction(customer_id=a,transaction_date=b,transaction_type=c,amount=d)
            e.save()
            f=customer.objects.get(customer_id=a)
            g=f.amount-d
            f.amount=g
            f.save()
            return render(req,'withdraw.html',{'msg':'Transaction Successfully Done'})
        else:
            return render(req,'withdraw.html',{'msg':'InSufficient Balance'})
    else:
        return render(req,'withdraw.html')


def deposit(req):
    if req.method=='POST':
        a = int(req.POST.get('cid'))
        try:
            g = customer.objects.get(customer_id=a)
            h=g.customer_id
            if a == h:
                b = req.POST.get('date')
                c = req.POST.get('ttype')
                d = float(req.POST.get('amt'))
                e = transaction(customer_id=a, transaction_date=b, transaction_type=c, amount=d)
                e.save()
                g.amount = g.amount+d
                g.save()
                return render(req, 'deposit.html', {'msg': 'Transaction Successfully Done'})
        except:
            return render(req,'deposit.html',{'error':'Account Not Found'})

    else:
        return render(req,'deposit.html')


def loans(req):
    if req.method =='POST':
        a=int(req.POST.get('lid'))
        b=req.POST.get('lname')
        c=float(req.POST.get('roi'))
        try:
            if loan.objects.filter(loan_id=a).exists():
                return render(req, 'loan.html', {'msg': ' Please check your Loan id. Already exists and try again.'})
            else:
                res = loan(loan_id=a, loan_name=b, roi=c)
                res.save()
                return render(req, 'loan.html', {'msg': 'Added Successfully'})
        except:
            return render(req, 'loan.html', {'msg': 'Invalid input. Please check Loan Id and try again.'})
    else:
        return render(req,'loan.html')


def loaninfo(req):
    if req.method =='POST':
        a=req.POST.get('cid')
        b=req.POST.get('lid')
        c=float(req.POST.get('amt'))
        d=req.POST.get('time')
        msg = "Customer Loan Information Added Successfully!"
        e = CustomerLoan(customer_id_id=a, loan_id_id=b, amount=c, time_period=d)
        e.save()
        return render(req, 'loansinfo.html', {'msg': msg})
    else:
        res1 = customer.objects.all().values_list('customer_id', flat= True)
        res2 = loan.objects.all().values_list('loan_id', flat=True)
        return render(req,'loansinfo.html',{'customer_ids': res1,'loan_ids': res2})


def custloan(req):
    if req.method =='POST':
        a = req.POST.get('cid')
        b = CustomerLoan.objects.filter(customer_id=a)
        res1 = customer.objects.all().values_list('customer_id', flat=True)
        if b:
            return render(req, 'custloan.html', {'loans': b,'customer_ids':res1})
        else:
            return render(req, 'custloan.html', {'error': 'No Loans found for this Customer','customer_ids':res1})
    else:
        res1 = customer.objects.all().values_list('customer_id', flat=True)
        return render(req,'custloan.html',{'customer_ids': res1})


def mini(req):
    if req.method == 'POST':
        a = int(req.POST.get('cid'))
        b = transaction.objects.filter(customer_id=a)
        if b:
            return render(req, 'mini.html', {'payments': b})
        else:
            return render(req, 'mini.html', {'error': 'No transactions found for this Customer ID'})
    else:
        return render(req, 'mini.html')
