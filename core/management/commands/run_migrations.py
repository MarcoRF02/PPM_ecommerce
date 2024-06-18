import os
import subprocess

def handler(request, response):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
    result = subprocess.run(['python', 'manage.py', 'migrate'], capture_output=True, text=True)
    return response.json({
        'stdout': result.stdout,
        'stderr': result.stderr
    })