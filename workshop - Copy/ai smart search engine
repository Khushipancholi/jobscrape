function smartSearch(q) {
  q = q.toLowerCase();
  return JOBS.filter(j =>
    j.data.job_title.toLowerCase().includes(q)  ||
    j.data.company.toLowerCase().includes(q)    ||
    j.data.location.toLowerCase().includes(q)   ||
    j.source.toLowerCase().includes(q)          ||
    j.ai_summary.top_skills.join(' ').toLowerCase().includes(q)
  );
}

// ── Intent detection & reply builder ──
function buildReply(input) {
  const q = input.toLowerCase().trim();

  // Greeting
  if (/^(hi|hello|hey|hii|yo|sup|howdy)\b/.test(q))
    return {
      text: `Hey! 👋 I'm <strong>CyberJob Scout</strong> — your offline cyber security job assistant.<br><br>
             I have <strong>${JOBS.length} scraped internship listings</strong> from LinkedIn & Indeed across India.<br><br>
             Try asking: <em>"Jobs in Bengaluru"</em>, <em>"SOC roles"</em>, or <em>"What skills should I learn?"</em>`,
      jobs: []
    };

  // Show all jobs
  if (/all jobs|show all|list all|every job/.test(q))
    return { text: `Here are all <strong>${JOBS.length} scraped listings</strong>:`, jobs: JOBS };

  // Count
  if (/how many|count|total/.test(q)) {
    const li = JOBS.filter(j => j.source === 'LinkedIn').length;
    return {
      text: `<strong>${JOBS.length} jobs</strong> total — <strong>${li}</strong> from LinkedIn, <strong>${JOBS.length - li}</strong> from Indeed.`,
      jobs: []
    };
  }

  // Companies hiring
  if (/compan|who.*(hiring|recruit)|which.*compan/.test(q)) {
    const cos = [...new Set(JOBS.map(j => j.data.company))];
    return {
      text: `<strong>${cos.length} companies</strong> currently hiring:<br><br>${cos.map((c, i) => `${i+1}. ${c}`).join('<br>')}`,
      jobs: []
    };
  }

  // Skills roadmap
  if (/skill|learn|prepare|roadmap|study/.test(q)) {
    const freq = {};
    JOBS.flatMap(j => j.ai_summary.top_skills).forEach(s => freq[s] = (freq[s] || 0) + 1);
    const top = Object.entries(freq).sort((a, b) => b[1] - a[1]).slice(0, 8);
    return {
      text: `<strong>Most in-demand skills across all listings:</strong><br><br>
             ${top.map(([s, n]) => `• <strong>${s}</strong> — ${n} job${n > 1 ? 's' : ''}`).join('<br>')}<br><br>
             Focus on these to stand out! 🎯`,
      jobs: []
    };
  }

  // Source filters
  if (/\blinkedin\b/.test(q)) {
    const r = JOBS.filter(j => j.source === 'LinkedIn');
    return { text: `<strong>${r.length} LinkedIn</strong> listings:`, jobs: r };
  }
  if (/\bindeed\b/.test(q)) {
    const r = JOBS.filter(j => j.source === 'Indeed');
    return { text: `<strong>${r.length} Indeed</strong> listings:`, jobs: r };
  }

  // City filters
  const cityMap = {
    bengaluru:'bengaluru', bangalore:'bengaluru', mumbai:'mumbai',
    hyderabad:'hyderabad', pune:'pune', chennai:'chennai',
    noida:'noida', delhi:'delhi', kolkata:'kolkata'
  };
  for (const [alias, city] of Object.entries(cityMap)) {
    if (q.includes(alias)) {
      const r = JOBS.filter(j =>
        j.data.location.toLowerCase().includes(city) ||
        (city === 'bengaluru' && j.data.location.toLowerCase().includes('bangalore'))
      );
      const label = city.charAt(0).toUpperCase() + city.slice(1);
      return r.length
        ? { text: `<strong>${r.length} job${r.length > 1 ? 's' : ''}</strong> in <strong>${label}</strong>:`, jobs: r }
        : { text: `No listings found in <strong>${label}</strong>. Try Bengaluru, Mumbai, or Noida.`, jobs: [] };
    }
  }

  // General keyword fallback
  const r = smartSearch(q);
  if (r.length)
    return { text: `<strong>${r.length} match${r.length > 1 ? 'es' : ''}</strong> for "<em>${input}</em>":`, jobs: r };

  return {
    text: `Hmm, nothing found for "<em>${input}</em>".<br><br>
           Try a <strong>skill</strong> (Python, SOC, Wireshark), a <strong>city</strong> (Bengaluru, Delhi, Mumbai),
           or a <strong>company</strong> (TCS, Infosys, DRDO).`,
    jobs: []
  };
}