# Modules
from django.conf.urls import url
from django_yaml_redirects import load_redirects
from django_template_finder_view import TemplateFinder

# Local
from webapp.views import custom_404, custom_500, MarkdownView

# Match any redirects first
urlpatterns = load_redirects()

default_markdown_template = 'includes/base_markdown.html'

# Try to find templates
urlpatterns += [
    url(
        r'^(?P<path>core(/.*)?)$',
        MarkdownView.as_view(),
        {
            'template_name': default_markdown_template
        }
    ),
    url(r'^(?P<template>.*)/?$', TemplateFinder.as_view()),
]

# Error handlers
handler404 = custom_404
handler500 = custom_500
