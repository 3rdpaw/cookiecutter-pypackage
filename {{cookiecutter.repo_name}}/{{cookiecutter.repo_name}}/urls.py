"""
urls.py
@author: {{cookiecutter.github_username}}

"""

# Copyright 2013-2015 Soltra
# All Rights Reserved
# See LICENSE.txt for more information.

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^settings/$', 'adapters.{{cookiecutter.repo_name}}.views.settings', name='{{cookiecutter.repo_name}}_settings'),
                       url(r'^process/$', 'adapters.{{cookiecutter.repo_name}}.views.process', name='{{cookiecutter.repo_name}}_process'),
                       )

# Just create one link from menu
# todo: implement nested menu to allow direct navigation
navitems = [
    ('{{cookiecutter.navitem}}', '{{cookiecutter.repo_name}}_process'),
]
