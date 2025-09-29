# microsvc/views.py
import numpy as np
from sklearn.linear_model import LinearRegression
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

# --------------------------------------------------------------------------
# 1. API Endpoint (Phase 3 Core Feature)
# --------------------------------------------------------------------------

class PredictionAPI(APIView):
    """
    A simple API to demonstrate an ML prediction service.
    
    It simulates a prediction based on a single input feature (e.g., 'size').
    """
    def post(self, request, format=None):
        try:
            # 1. Input Validation
            # Expects a JSON body like: {"input_feature": 5.0}
            input_feature = request.data.get('input_feature')
            if input_feature is None:
                return Response({"error": "Missing 'input_feature' in request body."}, 
                                status=status.HTTP_400_BAD_REQUEST)
            
            # Ensure input is a valid number
            try:
                X_pred = np.array([[float(input_feature)]])
            except ValueError:
                return Response({"error": "Input feature must be a valid number."}, 
                                status=status.HTTP_400_BAD_REQUEST)

            # 2. Simulate Model Training (In a real app, the model is loaded from a file!)
            # Simulate a simple relationship: y = 2*x + 10
            X = np.array([[1], [2], [3], [4], [5]])
            y = np.array([12, 14, 16, 18, 20])
            
            model = LinearRegression()
            model.fit(X, y)
            
            # 3. Get Prediction
            prediction = model.predict(X_pred)[0]
            
            # 4. Return Structured Response
            return Response({
                "status": "success",
                "input": input_feature,
                "prediction": round(prediction, 2),
                "model_summary": "Simulated Linear Regression (y = 2x + 10)"
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            # Catch all unexpected errors and return a 500 error
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# --------------------------------------------------------------------------
# 2. Frontend Demo Page View (For interaction)
# --------------------------------------------------------------------------

def api_demo(request):
    """Renders the HTML page for users to interact with the API."""
    # We pass the API URL to the template for JavaScript to use
    context = {
        'api_endpoint': '/api/predict/'
    }
    return render(request, "microsvc/api_demo.html", context)