"""Reproducible, semantically tagged PDFs. Requires weasyprint>=69, PyMuPDF."""
from pathlib import Path
import html,json,re,shutil
from weasyprint import HTML
import fitz
P=Path(__file__).resolve().parent
ROOT=P.parents[1]
CSS='''
@page {size:A4;margin:19mm 18mm 18mm; @bottom-left {content:"Fotbal pentru Viitor";font:8pt "DejaVu Sans";color:#566369} @bottom-right {content:counter(page);font:8pt "DejaVu Sans";color:#566369}}
html {font:10.4pt/1.45 "DejaVu Sans";color:#20282c} body {margin:0} p {margin:0 0 8pt;orphans:3;widows:3} h1 {font-size:20pt;line-height:1.25;margin:15pt 0 12pt;break-after:avoid} h2 {font-size:12.4pt;line-height:1.35;margin:12pt 0 7pt;break-after:avoid} h3 {font-size:11pt;break-after:avoid} .cover {break-after:page} .cover h1 {font-size:32pt;margin-top:35pt} .toc {break-after:page} .toc a {display:block;font-size:9pt;line-height:1.35;margin:3pt 0;color:#20282c;text-decoration:none} .toc a::after {content:leader('.') target-counter(attr(href),page)}
table {width:100%;border-collapse:collapse;margin:8pt 0 12pt;font-size:8.3pt;line-height:1.42;table-layout:fixed} thead {display:table-header-group} tr {break-inside:avoid} th,td {padding:7pt 6pt;border:0.4pt solid #d9dfe1;vertical-align:top;overflow-wrap:anywhere} th {background:#223945;color:white;text-align:left} tbody tr:nth-child(even) {background:#f0f4f5} a {color:#27517b;overflow-wrap:anywhere} .source {font-size:8.5pt} ul {padding-left:15pt} li {margin-bottom:6pt} .major {break-before:page} .brief {font-size:9.4pt;line-height:1.34} .brief h1 {font-size:27pt;line-height:1.18;margin:0 0 12pt}.brief h2 {font-size:11.5pt;margin:8pt 0 6pt}.brief p {margin-bottom:6pt}.small {font-size:8.1pt;line-height:1.32}.newpage {break-before:page}
'''
def doc(body,title):
 return '<!doctype html><html lang="ro"><head><meta charset="utf-8"><title>'+html.escape(title)+'</title><meta name="author" content="George Dobritoiu"><style>'+CSS+'</style></head><body>'+body+'</body></html>'
def save(body,title,out):
 HTML(string=doc(body,title),base_url=str(P)).write_pdf(out,pdf_tags=True)
 d=fitz.open(out);print(json.dumps({'file':out.name,'pages':len(d),'bytes':out.stat().st_size}))
 return d

def render_full():
 lines=(P/'Fotbal-pentru-Viitor.md').read_text().splitlines();parts=['<section class="cover">'];toc=[];table=[];lst=[];first=True;chapter=0
 def flush():
  if table:
   parts.append('<table><thead><tr>'+''.join('<th scope="col">'+html.escape(x)+'</th>' for x in table[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+html.escape(x)+'</td>' for x in row)+'</tr>' for row in table[1:])+'</tbody></table>');table.clear()
  if lst:parts.append('<ul>'+''.join('<li>'+html.escape(x)+'</li>' for x in lst)+'</ul>');lst.clear()
 for line in lines:
  if line.startswith('|'):
   table.append([x.strip() for x in line.strip('|').split('|')]);continue
  if line.startswith('- '):lst.append(line[2:]);continue
  flush()
  if not line.strip():continue
  if line.startswith('# '):
   title=line[2:]
   if first:parts.append('<h1>'+html.escape(title)+'</h1>');first=False;continue
   if not chapter:parts.append('</section><!--TOC-->')
   chapter+=1;key='chapter-'+str(chapter);toc.append((key,title))
   parts.append('<h1 id="'+key+'"'+(' class="major"' if title.startswith(('1 ','9 ','21 ','Anexa A ','Anexa I ')) else '')+'>'+html.escape(title)+'</h1>')
  elif line.startswith('## '):parts.append('<h2>'+html.escape(line[3:])+'</h2>')
  elif line.startswith('https://'):parts.append('<p class="source"><a href="'+html.escape(line,quote=True)+'">'+html.escape(line)+'</a></p>')
  else:parts.append('<p>'+html.escape(line).replace('**','')+'</p>')
 flush();body=''.join(parts).replace('<!--TOC-->','<nav class="toc" aria-label="Cuprins"><h1>Cuprins</h1>'+''.join('<a href="#'+k+'">'+html.escape(t)+'</a>' for k,t in toc)+'</nav>')
 out=ROOT/'Fotbal-pentru-Viitor-2026-10-03-corectat.pdf';d=save(body,'Fotbal pentru Viitor | 2030–2040',out)
 page=next(item[2] for item in d.get_toc() if item[1].startswith('15 '))
 (P/'pdf-metadata.json').write_text(json.dumps({'pages':len(d),'diasporaPage':page},indent=2)+'\n')
 shutil.copyfile(out,ROOT/'Fotbal-pentru-Viitor.pdf')

def render_brief():
 parts=['<div class="brief">'];title_seen=False
 for item in json.loads((P/'brief.json').read_text()):
  if item.get('break'):parts.append('</div><div class="brief newpage">');continue
  style=item['style'];tag='h1' if style=='title' else 'h2' if style=='head' else 'p'
  parts.append('<'+tag+(' class="small"' if style=='small' else '')+'>'+item['html']+'</'+tag+'>')
 parts.append('</div>');out=ROOT/'Fotbal-pentru-Viitor-Rezumat-2026-10-03-corectat.pdf';d=save(''.join(parts),'Fotbal pentru Viitor | Rezumat executiv',out)
 assert len(d)==2, 'Brief must remain two pages'
 shutil.copyfile(out,ROOT/'Fotbal-pentru-Viitor-Rezumat-executiv.pdf')
if __name__=='__main__':render_full();render_brief()
