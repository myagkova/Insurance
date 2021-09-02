import numpy as np
import pandas as pd
import json
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


class Prediction(APIView):
    def post(self, request):
        data = request.data
        age = data['Age']
        driving_experience = data['Driving_experience']
        salary = data['Salary']
    
        model = ApiConfig.model
        predicted = model.predict([[age, driving_experience, salary]])
        predicted = np.round(predicted, 1)
        with open('ml/data/cluster_0.json') as json_file:
            cluster_1, cluster_2, cluster_3, cluster_4 = zip(*[line.rstrip().split(';') for line in json_file])
        if predicted == 0:
            return JsonResponse('\n'.join(cluster_1), safe=False)
        elif predicted == 1:
            return JsonResponse('\n'.join(cluster_2), safe=False)
        elif predicted == 2:
            return JsonResponse('\n'.join(cluster_3), safe=False)
        elif predicted == 3:
            return JsonResponse('\n'.join(cluster_4), safe=False)
