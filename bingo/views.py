import random
from datetime import date

import numpy as np
from django.shortcuts import redirect
from django.shortcuts import render

from .models import BingoCard


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

    userid = request.GET.get("userid", None).lower()  # default None if not present

    card = BingoCard.objects.filter(userid=userid, date=simple_date).first()

    if card:
        database = card.numbers
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

    context = {"userid": userid, "formatted_date": formatted_date, "random_numbers": array_2d}

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
                num = random.randint(1, 75)
                if num not in used_numbers:
                    used_numbers.add(num)
                    row.append(num)
                    break
        result.append(row)

    return result
