const english=document.documentElement.lang==='en';
const toast=document.getElementById('toast');let timer;
function notice(text){toast.textContent=text;toast.classList.add('visible');clearTimeout(timer);timer=setTimeout(()=>toast.classList.remove('visible'),4500)}
function revealHash(){const el=document.getElementById(location.hash.slice(1));if(el?.classList.contains('measure')){const d=el.querySelector('details');if(d)d.open=true}}
window.addEventListener('hashchange',revealHash);revealHash();
function syncLanguageHash(){document.querySelectorAll('.language-switch a, .languages a').forEach(a=>{a.hash=location.hash})} syncLanguageHash(); window.addEventListener('hashchange',syncLanguageHash);
document.querySelectorAll('.share').forEach(button=>button.addEventListener('click',async()=>{const url=new URL(location.href);url.hash=button.dataset.id||'';const data={title:button.dataset.title||'Proiect România',text:button.dataset.text||(english?'Practical proposals for Romania. An initiative by George Dobritoiu.':'Propuneri concrete pentru România. O inițiativă de George Dobritoiu.'),url:url.href};try{if(navigator.share){await navigator.share(data)}else if(navigator.clipboard){await navigator.clipboard.writeText(url.href);notice(english?'Link copied. You can now share it.':'Linkul a fost copiat. Îl poți distribui.')}else{window.prompt(english?'Copy the link to share:':'Copiază linkul pentru distribuire:',url.href)}}catch(e){if(e.name!=='AbortError')notice(english?'Unable to share. Copy the address from your browser.':'Nu am putut distribui linkul. Copiază adresa din bara de navigare.')}}));
document.querySelectorAll('.join-form').forEach(form=>form.addEventListener('submit',event=>{event.preventDefault();if(!form.reportValidity())return;const data=new FormData(form);const name=String(data.get('name')).trim();const area=String(data.get('area')).trim();const message=String(data.get('message')).trim();if(!name||!area||!message){notice(english?'Please complete all fields.':'Completează toate câmpurile.');return}const text=english?`Hello George! I would like to contribute to Proiect România.\nName: ${name}\nArea: ${area}\nMy contribution: ${message}`:`Salut, George! Aș vrea să contribui la Proiect România.\nNume: ${name}\nDomeniu: ${area}\nContribuția mea: ${message}`;window.open('https://wa.me/40722565555?text='+encodeURIComponent(text),'_blank','noopener,noreferrer')}));

document.documentElement.classList.add('js');
const toggle=document.querySelector('.menu-toggle'), menu=document.querySelector('.site-nav');
toggle?.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));menu.classList.toggle('is-open',open)});

const projectMenu=document.querySelector('.nav-projects');
document.addEventListener('click',event=>{if(projectMenu?.open&&!projectMenu.contains(event.target))projectMenu.open=false});
document.addEventListener('keydown',event=>{if(event.key!=='Escape')return;if(projectMenu?.open){projectMenu.open=false;projectMenu.querySelector('summary').focus()}else if(toggle?.getAttribute('aria-expanded')==='true'){toggle.setAttribute('aria-expanded','false');menu.classList.remove('is-open');toggle.focus()}});
menu?.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{if(projectMenu)projectMenu.open=false;if(toggle){toggle.setAttribute('aria-expanded','false');menu.classList.remove('is-open')}}));

function addPageSharing() {
  const canonical = document.querySelector('link[rel="canonical"]');
  const url = new URL(canonical?.href || location.href);
  const isArticle = /^\/(?:proiecte|initiative-cetatenesti|en\/projects|audit|oportunitati-de-finantare)\/[^/]+\/?$/.test(url.pathname);
  const heading = document.querySelector('main h1') || document.querySelector('h1');
  if (!isArticle || !heading) return;

  url.search = '';
  url.hash = '';
  const title = document.querySelector('meta[property="og:title"]')?.content || heading.textContent.trim();
  const controls = document.createElement('div');
  controls.className = 'page-sharing';

  function addButton(label) {
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = label;
    controls.append(button);
    return button;
  }

  const shareButton = addButton(english ? 'Share' : 'Distribuie');
  const copyButton = addButton(english ? 'Copy link' : 'Copiază linkul');
  const status = document.createElement('span');
  status.setAttribute('role', 'status');

  const manualLink = document.createElement('input');
  manualLink.type = 'url';
  manualLink.readOnly = true;
  manualLink.hidden = true;
  manualLink.value = url.href;
  manualLink.setAttribute('aria-label', english ? 'Link to copy' : 'Link de copiat');
  controls.append(status, manualLink);
  heading.after(controls);

  async function copyLink() {
    try {
      await navigator.clipboard.writeText(url.href);
      manualLink.hidden = true;
      status.textContent = english ? 'Link copied.' : 'Link copiat.';
    } catch {
      status.textContent = english ? 'Select and copy this link.' : 'Selectează și copiază linkul.';
      manualLink.hidden = false;
      manualLink.focus();
      manualLink.select();
    }
  }

  copyButton.addEventListener('click', copyLink);
  shareButton.addEventListener('click', async () => {
    status.textContent = '';
    if (typeof navigator.share !== 'function') {
      await copyLink();
      return;
    }
    try {
      await navigator.share({ title, url: url.href });
    } catch (error) {
      if (error.name !== 'AbortError') await copyLink();
    }
  });
}

addPageSharing();
