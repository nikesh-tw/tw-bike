#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
# breakpoint()
DEVELOPER='home/lenovo/bike_pro_api_swagger_integration/bike_pro/bike_pro/settings.dev'
def main():
    
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_pro.settings')

    #os.environ.setdefault('DJANGO_SETTINGS_MODULE',path)
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE','dev') #ModuleNotFoundError: No module named 'dev'
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE','/home/lenovo/bike_pro_api_swagger_integration/bike_pro/bike_pro/settings/dev') #ModuleNotFoundError: No module named '/home/lenovo/bike_pro_api_swagger_integration/bike_pro/bike_pro/settings/dev'
    #os.environ.get(Path)
    try:
        from django.core.management import execute_from_command_line
        # breakpoint()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    #breakpoint()
    execute_from_command_line(sys.argv) #here sys.argv is ['manage.py', 'runserver']


if __name__ == '__main__':
    main()
