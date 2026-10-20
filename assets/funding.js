/* Reclassify on every visit, while open, and on return to the tab. Dates include
   Romania's UTC offset, so a visitor's timezone cannot change the deadline. */
(function () {
  function isExpired(expiry, now) {
    const end = Date.parse(expiry);
    return !Number.isFinite(end) || now >= end;
  }
  if (typeof module !== 'undefined') module.exports = { isExpired };
  if (typeof document === 'undefined') return;
  function refresh() {
    const now = Date.now();
    const active = document.getElementById('funding-active');
    const archive = document.getElementById('funding-archive');
    document.querySelectorAll('[data-funding-expiry]').forEach(function (card) {
      const closed = isExpired(card.dataset.fundingExpiry, now);
      card.dataset.fundingStatus = closed ? 'expired' : 'active';
      const label = card.querySelector('[data-funding-label]');
      if (card.matches('article.project-card')) {
        if (label) label.textContent = closed ? 'Înscrieri închise' : 'Apel activ';
        const target = closed ? archive : active;
        if (target && card.parentNode !== target) target.appendChild(card);
      } else if (closed && label) {
        label.textContent = 'Înscrieri închise — articol arhivat.';
      }
    });
    ['active', 'archive'].forEach(function (kind) {
      const list = document.getElementById('funding-' + kind);
      const empty = document.getElementById('funding-' + kind + '-empty');
      if (list && empty) empty.hidden = !!list.querySelector('article');
    });
  }
  refresh();
  setInterval(refresh, 1000);
  document.addEventListener('visibilitychange', refresh);
})();
