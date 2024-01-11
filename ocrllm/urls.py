from django.urls import path
from .views import GenerateHintOrExplanationView, retrieve_hints_explanations

urlpatterns = [
    # Define your registration and login URLs here...
    path('generate-hints-explanations/', GenerateHintOrExplanationView.as_view(), name='generate-hints-explanations'),
    path('retrieve-hints-explanations/', retrieve_hints_explanations, name='retrieve-hints-explanations'),
]