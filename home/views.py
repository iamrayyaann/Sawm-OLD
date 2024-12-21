from django.shortcuts import render
import requests

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
        
    
        
    if request.method == 'POST':
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
        
    context = {
        'methods': methods_list # Array of methods
    }
    
    return render(request, 'index.html', context)
