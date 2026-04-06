// Populate sidebar job cards
function renderSidebar(jobs) {
  document.getElementById('cnt').textContent = `${jobs.length} jobs`;
  document.getElementById('jobList').innerHTML = jobs.map((j, i) => `
    <div class="jcard" id="jc${i}" onclick="hlCard(${i})">
      <span class="src ${j.source === 'LinkedIn' ? 'li' : 'in'}">${j.source}</span>
      <div class="jt">${j.data.job_title}</div>
      <div class="jco">${j.data.company}</div>
      <div class="jl">📍 ${j.data.location}</div>
      <div class="jsk">${j.ai_summary.top_skills.map(s => `<span class="sk">${s}</span>`).join('')}</div>
    </div>
  `).join('');
}

// Highlight clicked card
function hlCard(i) {
  document.querySelectorAll('.jcard').forEach(c => c.classList.remove('hl'));
  document.getElementById(`jc${i}`)?.classList.add('hl');
}

// Filter sidebar from search box
function filterSidebar(v) {
  const q = v.toLowerCase();
  renderSidebar(q ? JOBS.filter(j =>
    j.data.job_title.toLowerCase().includes(q) ||
    j.data.company.toLowerCase().includes(q)   ||
    j.data.location.toLowerCase().includes(q)  ||
    j.ai_summary.top_skills.join(' ').toLowerCase().includes(q)
  ) : JOBS);
}

// Build a result card for inside the chat
function jobHTML(j) {
  return `
    <div class="rcard">
      <div class="rct">${j.data.job_title}</div>
      <div class="rcc">${j.data.company}</div>
      <div class="rcl">📍 ${j.data.location} &nbsp;|&nbsp; ${j.source}</div>
      <div class="rcsk">${j.ai_summary.top_skills.map(s => `<span class="sk">${s}</span>`).join('')}</div>
      <a class="rclink" href="${j.data.job_url}" target="_blank">View Job →</a>
    </div>
  `;
}