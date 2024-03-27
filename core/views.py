from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from django.db.models import Sum
from uuid import UUID
from django.utils import timezone
from django.db.models import F


from .models import Customer, Balances, Withdrawal, Deposit


def index(request):
    context = {}
    user_id = "30016556"
    try:
        customer = Customer.objects.get(id_number=user_id)

        balance = Balances.objects.get(customer_id=customer.customer)

        context = {
            "name": f"{customer.f_name} {customer.s_name} {customer.l_name}",
            "id": customer.customer,
            "balance": balance.balance,
        }
        print(context)
    except Exception as e:
        print(f"Error: {e}")
    return render(request, "index.html", context=context)


@api_view(["GET"])
def getbalances(request):
    user_id = 1
    results = {}
    try:
        customer = Customer.objects.get(id_number=user_id)

        balance = Balances.objects.get(customer_id=customer.customer)
        results["balance"] = balance.balance

        return Response(results)
    except Exception as e:
        print(f"Error: {e}")
        return Response([], status="403")


@api_view(["POST"])
def postdeposit(request):
    user_id = 1
    amount = request.data.get("amount")
    userInstance = Customer.objects.get(customer=user_id)

    if amount is None:
        return Response(
            {"error": "Amount not provided"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        amount = int(amount)
    except ValueError:
        return Response({"error": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)

    if amount > 40000:
        return Response(
            {"error": "Exceeds maximum deposit per transaction"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    today_deposits = Deposit.objects.filter(created_at=date.today()).aggregate(
        total_amount=Sum("amount")
    )["total_amount"]
    if today_deposits and today_deposits + amount > 150000:
        return Response(
            {"error": "Exceeds maximum deposit for the day"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    today_transactions = Deposit.objects.filter(created_at=date.today()).count()
    if today_transactions >= 4:
        return Response(
            {"error": "Exceeds maximum deposit frequency for the day"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    deposit = Deposit(amount=amount, customer=userInstance)
    deposit.save()
    getbalance = Balances.objects.get(customer=userInstance)

    newbal = getbalance.balance + amount
    getbalance.balance = newbal
    getbalance.save()
    total_amount = Balances.objects.filter(id=userInstance.customer).aggregate(
        total_amount=Sum("amount")
    )["total_amount"]

    return Response(
        {"success": "Deposit successful", "balance": total_amount},
        status=status.HTTP_201_CREATED,
    )


@api_view(["POST"])
def postwithdraw(request):
    user_id = 1
    userInstance = Customer.objects.get(customer=user_id)

    withdrawal_amount = float(request.data.get("amount"))

    if withdrawal_amount <= 0:
        return Response({"error": "Invalid withdrawal amount"})

    balance = Balances.objects.get(customer=user_id)

    if balance.balance < withdrawal_amount:
        return Response({"error": "Insufficient balance"})

    if withdrawal_amount > 20000:
        return Response({"error": "Exceeded maximum withdrawal per transaction"})

    today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + timezone.timedelta(days=1)
    total_withdrawals_today = (
        Withdrawal.objects.filter(
            customer=userInstance, created_at__gte=today_start, created_at__lt=today_end
        ).aggregate(total_amount=Sum("amount"))["total_amount"]
        or 0
    )

    if total_withdrawals_today + withdrawal_amount > 50000:
        return Response({"error": "Exceeded maximum withdrawal amount for the day"})

    withdrawal_count_today = Withdrawal.objects.filter(
        customer=userInstance, created_at__gte=today_start, created_at__lt=today_end
    ).count()

    if withdrawal_count_today >= 3:
        return Response({"error": "Exceeded maximum withdrawal frequency for the day"})

    balance.balance = F("balance") - withdrawal_amount
    balance.save()
    
    newbal = balance.balance

    withdrawal_transaction = Withdrawal.objects.create(
        customer=userInstance, amount=withdrawal_amount, created_at=timezone.now()
    )

    return Response({"success": "Withdrawal successful", 'balance': newbal},  status=status.HTTP_201_CREATE)
