from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['msg'] = "Well Come to Our task management web application with a REST API using Django"
        context['msg1'] = 'The application should allow multiple users to create, view, update, and delete tasks.       Utilize Django templates for rendering views, PostgreSQL for the database, and Django ORM for managing database relations. Additionally, use virtual environments, environment variables, and Git for proper development practices.'

        return context