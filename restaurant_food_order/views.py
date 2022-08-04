from django.shortcuts import render
from .models import MainDish, SideDish, Dessert, Order
from .form import MakeOrderForm, MakeReportForm


def quary_value_to_number(quary_value):
    for value in quary_value:
        return value[0]


def make_order(request):
    if request.method == 'POST':
        form = MakeOrderForm(request.POST)

        if form.is_valid():
            main_dish = request.POST['main_type']
            main_dish_qty = request.POST['main_qty']
            side_dish = request.POST['side_type']
            side_dish_qty = request.POST['side_qty']
            desert = request.POST['desert_type']
            desert_qty = request.POST['desert_qty']

            q_val_main_dish_unit_price = MainDish.objects.filter(dish_name=main_dish).values_list('price')
            q_val_side_dish_unit_price = SideDish.objects.filter(dish_name=side_dish).values_list('price')
            q_val_desert_dish_unit_price = Dessert.objects.filter(desert_name=desert).values_list('price')

            main_dish_unit_price = quary_value_to_number(q_val_main_dish_unit_price)
            side_dish_unit_price = quary_value_to_number(q_val_side_dish_unit_price)
            desert_dish_unit_price = quary_value_to_number(q_val_desert_dish_unit_price)

            Order.objects.create(
                main_dish=main_dish,
                main_dish_qty=main_dish_qty,
                side_dish=side_dish,
                side_dish_qty=side_dish_qty,
                desert=desert,
                desert_qty=desert_qty,
                amount=(main_dish_unit_price * int(main_dish_qty)) + (side_dish_unit_price * int(side_dish_qty)) + (desert_dish_unit_price * int(desert_qty)),
                is_pay=False
            )

            clean_data = form.clean()

    else:
        form = MakeOrderForm()

    return render(request, 'order.html', {'form': form})


def order_list(request):
    all_order = Order.objects.all().values()
    if request.method == 'POST':
        order_id = request.POST['order_id']
        is_pay = request.POST['pay']
        order = Order.objects.get(id=order_id)
        order.is_pay = is_pay
        order.save()

    return render(request, 'order_list.html', {'all_order': all_order})


def repord_display(request):
    if request.method == 'POST':
        form = MakeReportForm(request.POST)

        if form.is_valid():
            date = request.POST['date']
            daily_order = Order.objects.all().filter(order_time=date, is_pay=True).values()

            daily_revenue = 0.
            for row in daily_order:
                daily_revenue += float(row['amount'])

        return render(request, 'report.html', {'daily_revenue': daily_revenue, 'form': form, 'date': date})

    else:
        form = MakeReportForm()

    return render(request, 'report.html', {'form': form})







