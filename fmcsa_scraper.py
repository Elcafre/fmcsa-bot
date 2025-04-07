import json
import time

log_data = {
    "status": "Running",
    "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"),
    "last_run": time.strftime("%Y-%m-%d %H:%M:%S"),
    "total_leads": 37,
    "notes": "Test data for dashboard status"
}

with open("fmcsa_scraper_log.json", "w") as f:
    json.dump(log_data, f, indent=2)

print("Scraper ran and created fmcsa_scraper_log.json")
