import json
from datetime import datetime, timedelta

def cleanup_expired_jobs():
    try:
        with open('jobs.json', 'r', encoding='utf-8') as f:
            jobs = json.load(f)
        
        today = datetime.now().date()
        active_jobs = []
        
        for job in jobs:
            posted_date = datetime.strptime(job['posted_date'], '%Y-%m-%d').date()
            expiry_date = posted_date + timedelta(days=job['expiry_days'])
            
            if expiry_date >= today:
                active_jobs.append(job)
        
        with open('jobs.json', 'w', encoding='utf-8') as f:
            json.dump(active_jobs, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Removed {len(jobs) - len(active_jobs)} expired jobs")
        print(f"📊 Active jobs: {len(active_jobs)}")
        
    except Exception as e:
        print(f"❌ Cleanup error: {e}")

if __name__ == "__main__":
    cleanup_expired_jobs()
