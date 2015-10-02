#!/usr/bin/env bash

#
# Soltra Snort Adapter
# Copyright 2015 Soltra Solutions, LLC
#
# See LICENSE.txt for more information.
# STIX to Snort Rule Generator Adapter for Soltra Edge.
# Please see the LICENSE.txt file for licensing details.
#
# This product includes software developed at Soltra Solutions, LLC
# (http://www.soltra.com/).
#

#
# author: {{cookiecutter.full_name}}
# date: {{cookiecutter.release_date}}
#
# Build a simple archive file needed for installing as an Edge adapter.
#

tar -zcvf {{cookiecutter.repo_name}}.tgz {{cookiecutter.repo_name}}