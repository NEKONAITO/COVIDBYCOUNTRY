from django.shortcuts import redirect, render
import requests



# Create your views here.
def home(request):

    if request.method == "POST":
        country = request.POST["COVIDSEARCH"]
        url = "https://corona-rest-api.herokuapp.com/Api/" + country
        response = requests.get(url)
        data = response.json()["Success"]
        # data = dict
        
        keys = list(data.keys())
        values = list(data.values())
        
        context = {"keys":keys, "values":values}
    else:
        context = {}

    return render(request, 'App/home.html', context)
