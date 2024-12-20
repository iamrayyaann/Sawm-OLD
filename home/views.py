from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    if request.method == 'POST':
        selected_country = request.POST.get('country')
        selected_city = request.POST.get('city')
        selected_date = request.POST.get('date')
        selected_method = request.POST.get('method')
        
        if selected_method == "not selected":
            context ={
                'error_type' : 'Invalid input',
                'error_message' : 'Select a valid method from the dropdown',
                
            }
            return render(request, 'error.html', context)
        
        if not selected_country or not selected_city or not selected_date:
            context ={
                'error_type' : 'Invalid input',
                'error_message' : 'Fill All of the Form Fields',
            }
            return render(request, 'error.html', context)
        
    prayer_calculation_methods = [
    "Jafari / Shia Ithna-Ashari",
    "University of Islamic Sciences, Karachi",
    "Islamic Society of North America",
    "Muslim World League",
    "Umm Al-Qura University, Makkah",
    "Egyptian General Authority of Survey",
    None,  # Index 6 is missing
    "Institute of Geophysics, University of Tehran",
    "Gulf Region",
    "Kuwait",
    "Qatar",
    None,  # Index 11 is missing
    "Majlis Ugama Islam Singapura, Singapore",
    "Union Organization islamic de France",
    "Diyanet İşleri Başkanlığı, Turkey",
    "Spiritual Administration of Muslims of Russia",
    None,
    "Dubai (experimental)",
    "Jabatan Kemajuan Islam Malaysia (JAKIM)",
    "Tunisia",
    "Algeria",
    "KEMENAG - Kementerian Agama Republik Indonesia",
    "Morocco",
    "Comunidade Islamica de Lisboa",
    "Ministry of Awqaf, Islamic Affairs and Holy Places, Jordan"
    ]
    
    context = {
        'methods' : [(index, method) for index, method in enumerate(prayer_calculation_methods) if method] #creating array of tuples that will contain index and method name, also skipping "None" values
    }
    
    return render(request, 'index.html', context)
