#!/bin/bash

exec gunicorn --bind=0.0.0.0:8082 --workers=1 wsgi:app