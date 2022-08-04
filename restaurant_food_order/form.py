from django import forms
from .models import MainDish, SideDish, Dessert
from django.core import validators


def make_type_list(types_from_db):
    main_types_list = []
    for type in types_from_db:
        type_string = str(type)
        main_types_list.append([type_string, type_string])

    return main_types_list


class MakeOrderForm(forms.Form):
    main_types = MainDish.objects.only('dish_name').distinct()
    side_types = SideDish.objects.only('dish_name').distinct()
    dessert_types = Dessert.objects.only('desert_name').distinct()
    main_type = forms.ChoiceField(choices=make_type_list(main_types), required=True)
    main_qty = forms.IntegerField(min_value=1, required=True, widget=forms.NumberInput)
    side_type = forms.ChoiceField(choices=make_type_list(side_types), required=True)
    side_qty = forms.IntegerField(min_value=1, required=True)
    desert_type = forms.ChoiceField(choices=make_type_list(dessert_types), required=False)
    desert_qty = forms.IntegerField(min_value=0, required=False)


class MakeReportForm(forms.Form):
    date = forms.DateField(required=True)
