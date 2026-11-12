(() => {
  const button = document.getElementById('copy-anfp-prompt');
  const input = document.getElementById('anfp-prompt');
  const status = document.getElementById('anfp-copy-status');
  if (!button || !input || !status) return;
  button.hidden = false;
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(input.value);
      status.textContent = 'Prompt copiat. Completează întrebarea, instituțiile și perioada înainte de utilizare.';
    } catch {
      input.focus();
      input.select();
      status.textContent = 'Textul este selectat. Folosește Copiere sau Ctrl+C / Cmd+C.';
    }
  });
})();
