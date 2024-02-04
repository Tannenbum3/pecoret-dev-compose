#!/bin/bash

if [ ! -f "/app/conf/production.py" ]; then
    touch /app/conf/__init__.py
    cp docker/local_settings.template.py /app/conf/production.py
fi