from django.shortcuts import render
from forms import AplicantsForm

def  index(request):
    if request.methord == "POST":
        form =AplicantsForm()
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        occupation = form.cleaned_data["occupation"]



    return render(request, "index.html")
