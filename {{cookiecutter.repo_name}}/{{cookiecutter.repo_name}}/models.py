"""
models.py
@author: {{cookiecutter.github_username}}

"""

from datetime import datetime

from django.db import models
from mongoengine import *
from users.models import Repository_User


class {{cookiecutter.repo_name}}AdapterConf(Document):
    user_id = ObjectIdField()  # Reference to user_id
    last_updated = DateTimeField(default=lambda: datetime.utcnow())

    def set_defaults(self, user):
        self.user_id = user.id
        self.save()


class JobInfo(Document):
    created_by = ObjectIdField()  # Reference to user_id
    task_id = StringField()
    output_file = StringField()
    job_active = BooleanField(default=True)
    job_state = StringField(default='PENDING')
    job_start = DateTimeField(default=lambda: datetime.utcnow())
