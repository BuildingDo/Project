from django.shortcuts import render
from django.db.models import Count
from .models import Disease, Symptom
from .forms import SymptomForm

def search_symptoms(request):
    MAX_MATCHING_DISEASES = 3  # You can adjust this threshold as needed

    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            selected_symptoms = form.cleaned_data['symptoms']
            matching_diseases = Disease.objects.annotate(num_symptoms=Count('symptoms')).filter(symptoms__in=selected_symptoms).distinct()

            if not matching_diseases.exists():
                error_message = "No diagnosis found. Please seek the advice of a doctor."
                return render(request, 'core/search_results.html', {'form': form, 'error_message': error_message})

            matching_diseases = matching_diseases.filter(num_symptoms__gte=len(selected_symptoms))
            if matching_diseases.count() > MAX_MATCHING_DISEASES:
                error_message = "Multiple possible diagnoses found. Please seek the advice of a doctor."
                return render(request, 'core/search_results.html', {'form': form, 'error_message': error_message})

            return render(request, 'core/search_results.html', {'form': form, 'diseases': matching_diseases})
    else:
        form = SymptomForm()
    return render(request, 'core/search.html', {'form': form})
