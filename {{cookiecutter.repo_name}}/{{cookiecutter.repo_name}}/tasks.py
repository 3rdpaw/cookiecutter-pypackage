#!/usr/bin/env python2.7
"""
tasks.py
@author: mbutt

"""

import os
import sys
import traceback
from mongoengine import DoesNotExist
from lxml.etree import XMLSyntaxError
from mongoengine.connection import get_db

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'repository.settings')
from django.conf import settings

if not hasattr(settings, 'BASE_DIR'):
    raise Exception("Failed to import Django settings")

cfg = settings.ACTIVE_CONFIG

from celery import Celery

app = Celery('{{cookiecutter.repo_name}}', config_source='repository.celeryconfig', include=['{{cookiecutter.repo_name}}.tasks'])
# app.conf.update(
#     BROKER_URL="mongodb://localhost:27017/celery",
#     CELERY_RESULT_BACKEND="mongodb://localhost:27017/celery",
# )


@app.task
def run_demo(params):
    """
    Celery job to run the processing.
    :return:
    """
    pass