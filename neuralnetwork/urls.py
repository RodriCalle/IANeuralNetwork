from django.urls import path

from neuralnetwork import views as neuralnetwork_views

urlpatterns = [
    path('', neuralnetwork_views.NeuralNetwork.as_view()),
]