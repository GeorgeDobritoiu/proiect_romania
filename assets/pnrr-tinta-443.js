const dateFormatter = new Intl.DateTimeFormat('ro-RO', {
  dateStyle: 'long',
  timeZone: 'UTC',
});

function formatDate(value) {
  return dateFormatter.format(new Date(value));
}

async function showRequestTracker() {
  const message = document.getElementById('status-message');
  try {
    const response = await fetch('/data/pnrr-tinta-443.json');
    if (!response.ok) throw new Error('Request tracker unavailable');
    const { requests, updates } = await response.json();
    const orderedUpdates = [...updates].sort((a, b) => b.date.localeCompare(a.date));
    const rows = document.createDocumentFragment();
    for (const request of requests) {
      const row = document.createElement('tr');
      const name = document.createElement('th');
      name.scope = 'row';
      name.textContent = request.institution;
      row.append(name);
      const values = [
        formatDate(request.sent),
        request.registrationNumber ?? 'În așteptare',
        request.deadline ? formatDate(request.deadline) : 'De stabilit',
        request.status,
      ];
      for (const value of values) row.insertCell().textContent = value;
      const documentCell = row.insertCell();
      if (request.responseUrl) {
        const link = document.createElement('a');
        link.href = request.responseUrl;
        link.textContent = 'Deschide răspunsul (PDF)';
        documentCell.append(link);
      } else {
        documentCell.textContent = '—';
      }
      rows.append(row);
    }
    const journal = document.createDocumentFragment();
    for (const update of orderedUpdates) {
      const item = document.createElement('li');
      const date = document.createElement('time');
      date.dateTime = update.date;
      date.textContent = formatDate(update.date);
      item.append(date, ' · ', update.text);
      journal.append(item);
    }
    const updated = document.getElementById('updated');
    if (orderedUpdates.length) {
      updated.dateTime = orderedUpdates[0].date;
      updated.textContent = formatDate(updated.dateTime);
    }
    document.getElementById('requests').replaceChildren(rows);
    document.getElementById('updates').replaceChildren(journal);
    message.hidden = true;
  } catch {
    message.textContent = 'Statusul cererilor nu s-a putut încărca. Reîncarcă pagina pentru a încerca din nou.';
  }
}

showRequestTracker();
