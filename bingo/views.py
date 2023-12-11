import random
from datetime import date

import numpy as np
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone

from .models import BingoCard, System


def back(request):
    return redirect('/')


# Create your views here.
def index(request):
    today = date.today()
    formatted_date = today.strftime("%d/%m/%Y")

    context = {"formatted_date": formatted_date}
    return render(request, "bingo/index.html", context)


def join(request):
    today = date.today()
    formatted_date = today.strftime("%d/%m/%Y")
    simple_date = today.strftime("%d%m%Y")

    userid = request.GET.get("userid", None).lower().strip()  # default None if not present

    card = BingoCard.objects.filter(userid=userid, date=simple_date).first()

    if card:
        my_list = card.numbers.split(',')
        array_2d = np.array(my_list).reshape(5, 5)
    else:
        array_2d = generate_unique_numbers()

        numbers = ""
        for row in array_2d:
            for col in row:
                numbers = numbers + str(col) + ", "
        numbers = numbers[:-2]

        card = BingoCard(userid=userid, date=simple_date, numbers=numbers)
        card.save()

    system = System.objects.all().first()

    count_players = BingoCard.objects.filter(date=simple_date).count()

    context = {"userid": userid, "formatted_date": formatted_date, "random_numbers": array_2d,
               "lock_submit": system.lock_submit, "count_players": count_players}

    return render(request, "bingo/paper.html", context)


def regen(request, userid):
    today = date.today()
    formatted_date = today.strftime("%d/%m/%Y")
    simple_date = today.strftime("%d%m%Y")

    count_players = BingoCard.objects.filter(date=simple_date).count()

    card = BingoCard.objects.filter(userid=userid, date=simple_date).first()

    system = System.objects.all().first()

    if system.lock_submit != 1:
        array_2d = generate_unique_numbers()
        numbers = ""
        for row in array_2d:
            for col in row:
                numbers = numbers + str(col) + ", "

        card.numbers = numbers[:-2]
        card.create_datetime = timezone.now()
        card.save()
    else:
        my_list = card.numbers.split(',')
        array_2d = np.array(my_list).reshape(5, 5)

    context = {"userid": userid, "formatted_date": formatted_date, "random_numbers": array_2d,
               "lock_submit": system.lock_submit, "count_players": count_players}

    return render(request, "bingo/paper.html", context)


def generate_unique_numbers():
    # Define an empty two-dimensional list
    result = []

    # Define a set to keep track of generated numbers
    used_numbers = set()

    for i in range(5):
        row = []
        for j in range(5):
            if i == 2 and j == 2:
                row.append("$$")
                continue
            # Generate a unique random number from 1 to 75
            while True:
                if j == 0:
                    num = random.randint(1, 15)
                elif j == 1:
                    num = random.randint(15, 30)
                elif j == 2:
                    num = random.randint(30, 49)
                elif j == 3:
                    num = random.randint(40, 59)
                else:
                    num = random.randint(60, 75)
                if num not in used_numbers:
                    used_numbers.add(num)
                    row.append(num)
                    break
        result.append(row)

    return result
