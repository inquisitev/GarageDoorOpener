#!/bin/bash
exec gunicorn --config gunicorn_config.py  gunicorn:app --reload