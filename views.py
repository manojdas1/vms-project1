from django.shortcuts import render, HttpResponseRedirect
from .forms import VaccineRegistration
from .models import User
# Create your views here.

# This function will add and show them
def add_show(request):
    if request.method == 'POST':
        fm = VaccineRegistration(request.POST)
        if fm.is_valid():
            ad = fm.cleaned_data['Aadhaar_Number']
            nm = fm.cleaned_data['Name']
            ag = fm.cleaned_data['Age']
            gn = fm.cleaned_data['Gender']
            mb = fm.cleaned_data['Mobile_Number']
            ds = fm.cleaned_data['Dose']
            vn = fm.cleaned_data['Vaccine_Name']
            reg = User(Aadhaar_Number=ad, Name=nm, Age=ag, Gender=gn, Mobile_Number=mb, Dose=ds, Vaccine_Name=vn)
            reg.save()
            fm = VaccineRegistration()


    else:
        fm = VaccineRegistration()
    stud = User.objects.all()
    return render(request, 'myapp/addandshow.html', {'form':fm, 'stu':stud })

# This function will update/edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = VaccineRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = VaccineRegistration(instance=pi)
    return render(request, 'myapp/update.html', {'form':fm})

# This function will delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')