from django.shortcuts import render
from django.views import View
from neuralnetwork.VegetablesNeuralNetwork.predict import predict
from neuralnetwork.VegetablesNeuralNetwork.train import train

from neuralnetwork.forms import UploadForm

import os.path

# Create your views here.

class NeuralNetwork(View):

    def get(self, request):
        form = UploadForm()
        if not os.path.exists('model/'):
            train()
        return render(request, 'neuralnetwork/index.html', { 'form': form, 'resultadoObtenido' : False })

    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_path = 'static/imagenes/' + request.FILES['file'].name
            img_path_show = '/imagenes/' + request.FILES['file'].name
            return render(request, 'neuralnetwork/index.html', { 'form': form, 'resultadoObtenido' : True, 
                'resultado' : predict(img_path), 
                'img_path' : img_path_show })
        else:
            return render(request, 'neuralnetwork/index.html', { 'form': form, 'resultadoObtenido' : False})