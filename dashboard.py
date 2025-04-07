import os
import json
from flask import Flask, render_template_string

app = Flask(__name__)

LOG_PATH = os.environ.get('LOG_PATH', 'fmcsa_scraper_log.json')

DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>FMCSA Scraper Dashboard</title>
    <style>
        body { font-family: Arial; padding: 30px; background-color: #f5f5f5; }
        .status-box { padding: 20px; border-radius: 10px; margin-top: 20px; }
        .green { background: #d4edda; color: #155724; }
        .red { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h1>FMCSA Scraper Status</h1>
    {% if status %}
        <div class="status-box green">
            <p><strong>Last Run:</strong> {{ last_run }}</p>
            <p><strong>Leads Pulled:</strong> {{ count }}</p>
        </div>
    {% else %}
        <div class="status-box red">
            <p><strong>Status:</strong> Not connected or failed</p>
            <p><strong>Error:</strong> {{ error }}</p>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def dashboard():
    try:
        if not os.path.exists(LOG_PATH):
            raise FileNotFoundError(f"Log file not found at {LOG_PATH}")
        with open(LOG_PATH, "r") as log_file:
            data = json.load(log_file)
            last_run = data.get("last_run", "Unknown")
            count = data.get("records", 0)
            return render_template_string(DASHBOARD_HTML, status=True, last_run=last_run, count=count)
    except Exception as e:
        return render_template_string(DASHBOARD_HTML, status=False, error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


