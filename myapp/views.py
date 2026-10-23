from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Myclass(APIView):
    def get(self,request):
        return Response(
            {"Message":"Good Afternoon..!"}
        )
class AdditionView(APIView):
    def post(self,request):
        x=request.data.get('num1')
        y=request.data.get('num2')
        result = x + y
        return Response(
            {"sum":result}
        )
    
class SubtractionView(APIView):
    def post(self,request):
        x=request.data.get('num1')
        y=request.data.get('num2')
        result = x - y
        return Response(
            {"subtraction":result}
        )
    
class MultiplicationView(APIView):
    def post(self,request):
        x=request.data.get('num1')
        y=request.data.get('num2')
        result = x * y
        return Response(
            {"multiplication":result}
        )
    
class LargestView(APIView):
    
    def post(self, request):

        x = request.data.get('num1')

        y = request.data.get('num2')

        z = request.data.get('num3')

        if x > y and x > z:
            result = x

        elif y > z:
            result = y

        else:
            result = z

        return Response(
            {"largest": result}
        )
    

class CelsiusToFahrenheitView(APIView):
    
    def post(self, request):

        c = request.data.get('celsius')

        result = (c * 9/5) + 32

        return Response(
            {"fahrenheit": result}
        )
    
class ReverseTextView(APIView):
    
    def post(self, request):

        text = request.data.get('text')

        result = text[::-1]

        return Response(
            {"reversed_text": result}
        )
    
class VowelCountView(APIView):
    
    def post(self, request):

        text = request.data.get('text')
        vowels="aeiou"

        count = 0

        for ch in text:
            if ch in vowels:
                count = count + 1

        return Response(
            {"vowel_count": count}
        )