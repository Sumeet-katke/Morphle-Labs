from django.http import HttpResponse
import os
import subprocess
from datetime import datetime
import pytz

def htop_view(request):
    full_name = "Sumeetkumar Katke"  # Replace with your full name
    username = os.getenv('USER') or os.getenv('USERNAME') or "codespace"

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get top command output (first 20 lines)
    top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout
    top_lines = "\n".join(top_output.splitlines()[:20])

    # Format output as HTML
    response = f"""
    <pre>
    Name: {full_name}
    user: {username}
    Server Time (IST): {server_time}

    TOP output:
    {top_lines}
    </pre>
    """
    
    return HttpResponse(response, content_type="text/html")