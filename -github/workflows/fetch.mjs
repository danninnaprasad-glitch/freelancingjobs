// fetch.mjs
import axios from 'axios';
import { writeFile } from 'fs/promises';

const res = await axios.get('https://remoteok.com/api', {
  headers: {'User-Agent': 'JobBot'}
});

const jobs = res.data
  .filter(j => j.position && j.company && j.url)
  .map(j => ({
    title: j.position,
    company: j.company,
    location: j.location || 'Remote',
    url: j.url,
    posted: j.created_at
  }))
  .filter(j => {
    const days = (Date.now() - new Date(j.posted)) / 864e5;
    return days <= 30; // auto-expire after 30 days
  });

await writeFile('jobs.json', JSON.stringify(jobs, null, 2));
