const f = document.getElementById('form');
const q = document.getElementById('query');
const google = 'https://www.google.com/search?q=';

function onglet() {
  const url = google + '+' + q.value;
  const win = window.open(url);
  win.focus();
}

f.addEventListener('submit', onglet);