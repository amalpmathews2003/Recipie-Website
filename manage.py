#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import threading
import time
def add():
    time.sleep(30)
    from website_app import add_to_database2
    add_to_database2(pages=5,category=10)     
    print('addition completed')
    
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipie_website.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    t=threading.Thread(target=add)
    t.start()
    main()
