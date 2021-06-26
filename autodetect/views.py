# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import ConvertFactory, DetectFactory, SUPPORTED_LANG

from .forms import InputForm

data_received = ""
data_format = ""

def predict(request):
    dflag = 0

    if ((request.method == 'POST') and ("detect" in request.POST)):
        parsed_form = InputForm(request.POST)

        if parsed_form.is_valid():

            # Receive Text and Conversion Fomrat from UI.
            global data_received, data_format
            data_received = parsed_form.cleaned_data['input_text']

            # Detection object that is called to predict text format.
            detect_object = DetectFactory(data_received)
            data_format = detect_object.detect_text()

            if data_format == "error":
                result_format = "Error detecting string. Please enter valid string for conversion."
                return render(request, 'autodetect/home.html', {'text_form' : parsed_form,
                                'result_format' : result_format, 'dflag' : dflag})

            result_format = data_format.upper()
            CHOICES = dict(SUPPORTED_LANG)
            del CHOICES[data_format]
            drop_response = sorted(CHOICES.items())
            dflag = 1

            return render(request, 'autodetect/home.html', {'text_form' : parsed_form,
                            'result_format' : result_format, 'dflag' : dflag,
                              'drop_down' : drop_response })

    else:
        parsed_form = InputForm()

    return render(request, 'autodetect/home.html',
        {'text_form' : parsed_form, 'dflag' : dflag })

def convertAjax(request):
    if request.method == 'GET':
        conversion_format = request.GET.get('to_format')

        convert_object = ConvertFactory(data_format, conversion_format, data_received)
        data_converted = convert_object.do_conversion()
        
        if data_converted == "error":
            return HttpResponse("Conversion to the specified format is Incompatible")
        else:
            return HttpResponse(data_converted)
