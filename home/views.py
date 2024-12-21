from django.shortcuts import render
from datetime import datetime
import requests

# Create your views here.
def home(request):
    try:
        response = requests.get('https://api.aladhan.com/v1/methods') # Get the prayer methods
        response_data = response.json()
        
        methods_list = []
        
        if response.status_code == 200 and response_data.get('data'): # If the request is successful
            methods = response_data['data']
            for key, value in methods.items():
                name = value.get('name', None)
            methods_list = [(index, method_info['name']) for index, method_info in methods.items() if 'name' in method_info]
        else:
            methods_list = [] # Empty list if there is an error
    except Exception as e:
        print(f"Error finding prayer methods: {e}")
        methods_list = [] # Empty list if there is an error
        
    
        
    if request.method == 'POST': # If form is submitted
        input_country = request.POST.get('country')
        input_city = request.POST.get('city')
        input_date = request.POST.get('date')
        input_method = request.POST.get('method')
        
        if input_method == "N/A":
            context ={
                'error_type' : 'Invalid input',
                'error_message' : 'Select a method',
            }
            return render(request, 'error.html', context)
        
        if not input_country or not input_city or not input_date:
            context = {
                'error_type' : 'Invalid input',
                'error_message' : 'Fill all the fields',
            }
            return render(request, 'error.html', context)
        
        path_parameter = input_date
        api_base_url = f"https://api.aladhan.com/v1/timingsByCity/{path_parameter}"
        query_parameters ={
            'country' : input_country,
            'city' : input_city,
            'method' : input_method,
        }
        
        api_response = requests.get(api_base_url, params = query_parameters)
        
        if api_response.status_code == 200:
            api_data = api_response.json()
            Suhoor = datetime.strptime(api_data['data']['timings']['Fajr'], "%H:%M").strftime("%I:%M %p").lower()
            Iftaar = datetime.strptime(api_data['data']['timings']['Maghrib'], "%H:%M").strftime("%I:%M %p").lower
            context = {
                'suhoor' : Suhoor,
                'iftar' : Iftaar
            }
            return render(request, 'displayTime.html', context)
        else:
            error_message = f"API Error: {api_response.status_code} - {api_response.text}"
            context = {
                'error_type': 'API Error',
                'error_message': error_message,
            }
            return render(request, 'error.html', context)
        
    context = {
        'methods': methods_list # Array of methods
    }
    
    return render(request, 'index.html', context)
