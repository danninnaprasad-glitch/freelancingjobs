import requests
import json
from datetime import datetime

def scrape_jobs():
    jobs = []
    
    # Example: RemoteOK API
    try:
        response = requests.get('https://remoteok.io/api')
        if response.status_code == 200:
            remote_jobs = response.json()
            for job in remote_jobs[1:6]:  # First 5 jobs
                jobs.append({
                    'id': len(jobs) + 1,
                    'title': job.get('position', 'N/A'),
                    'company': job.get('company', 'N/A'),
                    'posted_date': datetime.now().strftime('%Y-%m-%d'),
                    'expiry_days': 30,
                    'url': job.get('url', '#')
                })
    except:
        pass
    
    # Add more job sources here
    if len(jobs) == 0:
        # Fallback sample jobs
        jobs = [
            {
                'id': 1,
                'title': 'Web Developer',
                'company': 'Tech Company',
                'posted_date': datetime.now().strftime('%Y-%m-%d'),
                'expiry_days': 30,
                'url': 'https://example.com/job1'
            }
        ]
    
    # Save to jobs.json
    with open('jobs.json', 'w') as f:
        json.dump(jobs, f, indent=2)
    
    print(f"Scraped {len(jobs)} jobs")

if __name__ == "__main__":
    scrape_jobs()
