import requests
import json
import time
from datetime import datetime
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def scrape_freelancer():
    jobs = []
    try:
        # Sample job data - you can replace with real scraping later
        sample_titles = [
            "Web Developer Needed - React & Node",
            "Mobile App Developer - Flutter",
            "WordPress Website Designer", 
            "Python Django Backend Developer",
            "Full Stack JavaScript Developer",
            "UI/UX Designer for E-commerce",
            "Shopify Expert Needed",
            "PHP Laravel Developer",
            "Android iOS Mobile Developer",
            "Data Scraping Specialist"
        ]
        
        for i, title in enumerate(sample_titles):
            jobs.append({
                'id': f"job_{int(time.time())}_{i}",
                'title': title,
                'company': f'Client #{i+1}',
                'description': f'Looking for experienced {title} for remote project',
                'budget': ['$500-$1000', '$30-50/hr', 'Fixed $800', '$1000-1500'][i % 4],
                'posted_date': datetime.now().strftime('%Y-%m-%d'),
                'expiry_days': 30,
                'url': '#',
                'source': 'freelancer'
            })
    except Exception as e:
        logging.error(f"Scraping failed: {e}")
    
    return jobs

def scrape_all_jobs():
    all_jobs = []
    all_jobs.extend(scrape_freelancer())
    
    with open('jobs.json', 'w', encoding='utf-8') as f:
        json.dump(all_jobs, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Created {len(all_jobs)} sample jobs")
    return all_jobs

if __name__ == "__main__":
    scrape_all_jobs()
