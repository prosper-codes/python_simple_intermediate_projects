from django.shortcuts import render
from django.views import  generic
from .models import Item, MEAL_TYPE

class MenuList(generic.ListView):
    model = Item
    template_name = "index.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["grouped_items"] = {}
        for key, value in MEAL_TYPE:
            context["grouped_items"][value] = Item.objects.filter(meal_type=key)

        return context