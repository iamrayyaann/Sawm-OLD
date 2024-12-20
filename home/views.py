from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
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

    return render(request, 'index.html')
