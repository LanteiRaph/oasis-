import email
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from django import forms
from .models import Profile

import json


class Home(TemplateView):
    def get(self, request):

        #Render the page as is.
        return render(request, 'register.html', context={})

    def post(self, request):
        #Extarct the posted data.
        payload = request.POST
        #Compile the name property for the user
        name = payload.get('first_name') + ' ' + payload.get('last_name')
        #Create a new user with the new data.
        partcipant = Profile(name=name, phone=payload.get('phone'))
        #Set the is_student depending on the value of user type
        is_student = payload.get('is_student')
        #Check for value
        if is_student == 'yes':
            partcipant.is_student = True
            partcipant.course_name = payload.get('course_name')
            partcipant.student_id = payload.get('student_id')
        #Save the participant
        partcipant.save()
        #Render the success page.
        return render(request, 'success.html', context={})