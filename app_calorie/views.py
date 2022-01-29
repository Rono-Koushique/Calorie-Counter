from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Consume, Food
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# custom class
class Consume_handler:
    def get_consumed_food(self, request):
        food_consumed = request.POST['food-consumed']
        return Food.objects.get(name=food_consumed)

    def get_consumer(self, request):
        return request.user
        
    def save_consume(self, request):
        food = self.get_consumed_food(request)
        consumer = self.get_consumer(request)
        consume = Consume(user = consumer, food_consumed = food)
        consume.save()

    def get_all_consumed_foods(self, request):
        current_user = request.user
        return Consume.objects.filter(user = current_user)
        

class Account_handler:
    def reset_account(self, request):
        user = request.user
        foods_consumed = Consume.objects.filter(user=user)
        for food in foods_consumed:
            food.delete()


# Create your views here.
@login_required
def index(request):
    context = {
        "title" : "Home",
        "username" : request.user.username,
        "foods" : Food.objects.all()
    }

    handler = Consume_handler()         # this objects simplifies the process of storing a consume
                                        # the object is decleared at the top
    if request.method == "POST":
        handler.save_consume(request)       # adding consumed food in to the Consume model of the user logged in
        messages.add_message(request, messages.INFO, 'Food Added')
    
    context["consumed_food"] = handler.get_all_consumed_foods(request)      # the user's every consumed food
    return render(request, 'app_calorie/index.html', context)


@login_required
def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == "POST":
        consumed_food.delete()
        messages.add_message(request, messages.INFO, 'Food Deleted')
        return redirect('../../')

    return render(request, 'app_calorie/delete.html')


@login_required
def account_reset(request):
    context = {
        "title":"Reset Account ?",
        "username":request.user.username
    }

    handler = Account_handler()
    if request.method == "POST":
        handler.reset_account(request)
        messages.add_message(request, messages.INFO, 'Account reset')
        return redirect('../')

    return render(request, 'app_calorie/account-reset.html', context)


@login_required
def logoff(request):
    logout(request)
    return redirect('/')


@login_required
def food_data(request):
    context = {
        "title" : "Food Data",
        "foods" : Food.objects.all(),
        "username" : request.user.username
    }
    return render(request, 'app_calorie/food-data.html', context)