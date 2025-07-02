from django.shortcuts import render
import pickle
from .forms import AccidentForm

model = pickle.load(open('accident_model/accident_model.pkl', 'rb'))
scaler = pickle.load(open('accident_model/scaler.pkl', 'rb'))

def index(request):
    if request.method == 'POST':
        form = AccidentForm(request.POST)
        if form.is_valid():
            data = [
                form.cleaned_data['weather'],
                form.cleaned_data['road_surface'],
                form.cleaned_data['visibility'],
                form.cleaned_data['light_condition'],
            ]
            data_scaled = scaler.transform([data])
            prediction = model.predict(data_scaled)[0]
            return render(request, 'result.html', {'result': prediction})
    else:
        form = AccidentForm()
    return render(request, 'index.html', {'form': form})