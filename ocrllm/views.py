from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .models import HintExplanation
from .serializers import HintExplanationSerializer

# Your registration and login views go here...

class GenerateHintOrExplanationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Create an object of the logged-in user using request parameters
        logged_in_user = request.user

        # Access request parameters
        image = request.data.get('image')
        user = request.data.get('user')
        user_input = request.data.get('user_input')

        # Call function here
        hint_or_explanation_text = ""
        # Save generated hints, explanations, and image in the database
        HintExplanation.objects.create(
            hint_or_explanation_text=hint_or_explanation_text,
            image=image,
            user=request.user,
            user_input=user_input
        )

        # Return a response
        return Response({"message": "Hint or Explanation generated successfully"})

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def retrieve_hints_explanations(request):
    hints_explanations = HintExplanation.objects.all()
    serializer = HintExplanationSerializer(hints_explanations, many=True)
    return Response(serializer.data)