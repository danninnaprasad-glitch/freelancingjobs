import json
from datetime import datetime, timedelta

with open('jobs.json', 'r') as f:
    jobs = json.load(f)

today = datetime.now().date()
active_jobs = []

for job in jobs:
    posted = datetime.strptime(job['posted_date'], '%Y-%m-%d').date()
    expiry = posted + timedelta(days=job['expiry_days'])
    
    if expiry >= today:
        active_jobs.append(job)

with open('jobs.json', 'w') as f:
    json.dump(active_jobs, f, indent=2)
