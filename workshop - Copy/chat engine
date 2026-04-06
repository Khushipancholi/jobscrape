// Add a message bubble to the chat
function addMsg(role, html) {
  const c = document.getElementById('chatMsgs');
  const d = document.createElement('div');
  d.className = `msg ${role}`;
  const av = role === 'bot'
    ? `<div class="av bav">🛡️</div>`
    : `<div class="av uav">👤</div>`;
  d.innerHTML = `${av}<div class="bbl ${role}">${html}</div>`;
  c.appendChild(d);
  c.scrollTop = c.scrollHeight;
}

// Show animated typing dots
function showTyping() {
  const c = document.getElementById('chatMsgs');
  const d = document.createElement('div');
  d.className = 'msg bot'; d.id = 'typ';
  d.innerHTML = `
    <div class="av bav">🛡️</div>
    <div class="bbl bot">
      <div class="dots">
        <div class="dot"></div>
        <div class="dot"></div>
        <div class="dot"></div>
      </div>
    </div>`;
  c.appendChild(d);
  c.scrollTop = c.scrollHeight;
}
function hideTyping() { document.getElementById('typ')?.remove(); }

// Send message handler
function send() {
  const el  = document.getElementById('cin');
  const txt = el.value.trim();
  if (!txt) return;
  el.value = ''; rsz(el);
  addMsg('user', txt);
  showTyping();
  setTimeout(() => {
    hideTyping();
    const { text, jobs } = buildReply(txt);
    addMsg('bot', text + jobs.map(j => jobHTML(j)).join(''));
    // Highlight first matching job in sidebar
    if (jobs.length) {
      const idx = JOBS.indexOf(jobs[0]);
      if (idx !== -1) hlCard(idx);
    }
  }, 380); // 380ms fake "thinking" delay
}

// Click a chip → pre-fill and send
function ask(t) { document.getElementById('cin').value = t; send(); }

// Enter to send, Shift+Enter for newline
function handleKey(e) {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(); }
}

// Auto-resize textarea
function rsz(el) {
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 110) + 'px';
}