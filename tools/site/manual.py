"""Build the public HTML fragment and PDF from one maintained HTML source.
Requires reportlab, beautifulsoup4, and DejaVu Sans fonts on the build machine.
"""
from pathlib import Path
from html import escape
import re
from bs4 import BeautifulSoup, NavigableString
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, LongTable, TableStyle, KeepTogether, CondPageBreak
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

P=Path(__file__).resolve().parents[2]
source=P/'docs/manual-partid-responsabil.html'
soup=BeautifulSoup(source.read_text(),'html.parser')
FONT=Path('/usr/share/fonts/truetype/dejavu')
for name,file in [('DV','DejaVuSans.ttf'),('DV-Bold','DejaVuSans-Bold.ttf'),('DV-Oblique','DejaVuSans.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DV-Bold',italic='DV-Oblique',boldItalic='DV-Bold')
green=colors.HexColor('#173E38'); gold=colors.HexColor('#B09050'); ink=colors.HexColor('#20352F')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyRO',fontName='DV',fontSize=9.3,leading=14,spaceAfter=9,textColor=ink,allowWidows=0,allowOrphans=0))
styles.add(ParagraphStyle(name='H2RO',fontName='DV-Bold',fontSize=21,leading=26,textColor=green,spaceAfter=18,keepWithNext=True))
styles.add(ParagraphStyle(name='H3RO',fontName='DV-Bold',fontSize=12,leading=17,textColor=green,spaceBefore=12,spaceAfter=8,keepWithNext=True))
styles.add(ParagraphStyle(name='CellRO',parent=styles['BodyRO'],fontSize=8.1,leading=11.7,spaceAfter=0))
styles.add(ParagraphStyle(name='HeadRO',parent=styles['CellRO'],fontName='DV-Bold',textColor=colors.white))
styles.add(ParagraphStyle(name='SmallRO',parent=styles['BodyRO'],fontSize=8,leading=11))
styles.add(ParagraphStyle(name='CoverRO',fontName='DV-Bold',fontSize=34,leading=40,textColor=green,spaceAfter=24))
styles.add(ParagraphStyle(name='LeadRO',parent=styles['BodyRO'],fontSize=14,leading=21,spaceAfter=20))
styles.add(ParagraphStyle(name='TocRO',fontName='DV',fontSize=10,leading=16,textColor=green,spaceBefore=3,leftIndent=0,firstLineIndent=0))

def rich(n):
 if isinstance(n,NavigableString):
  return escape(str(n)).replace('−','-').replace('→',' &gt; ').replace('↗','').replace('↓','')
 if n.name in ['strong','b']: return '<b>'+''.join(rich(c) for c in n.children)+'</b>'
 if n.name in ['em','i']: return '<i>'+''.join(rich(c) for c in n.children)+'</i>'
 if n.name=='a':
  url=n.get('href','')
  if url.startswith('/'):url='https://proiectromania.ro'+url
  return '<link href="'+escape(url,quote=True)+'" color="#176657">'+''.join(rich(c) for c in n.children)+'</link>'
 return ''.join(rich(c) for c in n.children)

class ManualDoc(SimpleDocTemplate):
 def afterFlowable(self,f):
  if isinstance(f,Paragraph) and getattr(f,'chapter_id',None):
   key=f.chapter_id; self.canv.bookmarkPage(key);self.canv.addOutlineEntry(f.getPlainText(),key,0)
   self.notify('TOCEntry',(0,f.getPlainText(),self.page,key))

def pageframe(c,doc):
 c.saveState();w,h=doc.pagesize
 if doc.page>1:
  c.setFont('DV',8);c.setFillColor(green);c.drawString(48,h-32,'PROIECT ROMÂNIA / MANUAL DE ORGANIZARE')
  c.setStrokeColor(colors.HexColor('#D7E1DB'));c.line(48,h-42,w-48,h-42)
 c.setFont('DV',7.3);c.setFillColor(colors.HexColor('#586A63'))
 c.drawString(48,28,'v1.0 · 10.10.2026 · Cerințe legale + propuneri de guvernanță')
 c.drawRightString(w-48,28,str(doc.page));c.restoreState()

out=P/'downloads/manual-partid-responsabil.pdf'
doc=ManualDoc(str(out),pagesize=(595.28,841.89),leftMargin=48,rightMargin=48,topMargin=65,bottomMargin=49,title='Partidul ca organizație responsabilă - Manual de lucru',author='Proiect România · George Dobritoiu',subject='Înființare și administrare democratică a unui partid politic în România')
story=[Spacer(1,65),Paragraph('PROIECT ROMÂNIA',styles['H3RO']),Spacer(1,30),Paragraph('Partidul ca<br/>organizație<br/>responsabilă',styles['CoverRO']),Paragraph('Cum înființezi și organizezi un partid politic în România',styles['LeadRO']),Spacer(1,18),Paragraph('Manual de lucru pentru un grup fondator',styles['H3RO']),Paragraph('18 capitole · 14 indicatori · 8 modele de completat',styles['BodyRO']),Spacer(1,40),Paragraph('Concept: George Dobritoiu<br/>Versiunea 1.0 · 10 octombrie 2026',styles['BodyRO']),Paragraph('Un cadru administrativ bazat pe reguli democratice, responsabilități clare, finanțe verificabile și protejarea datelor.',styles['BodyRO']),PageBreak(),Paragraph('Cum folosești manualul',styles['H2RO'])]
for p in soup.find_all(['aside','p'],recursive=False)[:2]:story.append(Paragraph(rich(p),styles['BodyRO']))
story.append(Paragraph('Parcurgeți capitolele 1-4 cu grupul fondator și juristul; capitolele 5-13 cu echipa administrativă; testați propunerile din capitolele 15-17 într-un pilot. Sursele și data ediției sunt în capitolul 18. Linkurile din PDF sunt active.',styles['BodyRO']))
story.extend([PageBreak(),Paragraph('Cuprins',styles['H2RO'])])
toc=TableOfContents();toc.levelStyles=[styles['TocRO']];story.append(toc)
for section in soup.find_all('section',recursive=False):
 story.extend([PageBreak()] if section['id']=='principii' else [CondPageBreak(200),Spacer(1,20)])
 for el in section.children:
  if isinstance(el,NavigableString):continue
  if el.name=='h2':
   q=Paragraph(rich(el),styles['H2RO']);q.chapter_id=section['id'];story.append(q)
  elif el.name=='h3':story.append(Paragraph(rich(el),styles['H3RO']))
  elif el.name=='p':
   content=rich(el)
   if section['id']=='modele' and '___' in content: content=content.replace(' · ','<br/>')
   story.append(Paragraph(content,styles['BodyRO']))
  elif el.name in ['ul','ol']:
   for i,li in enumerate(el.find_all('li',recursive=False),1):
    bullet=str(i)+'.' if el.name=='ol' else '•'
    story.append(Paragraph(rich(li),ParagraphStyle(name='List',parent=styles['BodyRO'],leftIndent=13,firstLineIndent=0,bulletIndent=0),bulletText=bullet))
  elif el.name=='table':
   rows=[]
   for tr in el.find_all('tr'):
    rows.append([Paragraph(rich(td),styles['HeadRO'] if td.name=='th' else styles['CellRO']) for td in tr.find_all(['td','th'],recursive=False)])
   cols=len(rows[0]);width=doc.width
   widths=[width*.30,width*.70] if cols==2 else [width*.34,width*.40,width*.26]
   if section['id']=='kpi':widths=[width*.44,width*.32,width*.24]
   t=LongTable(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
   t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),green),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#F0F5F1'),colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('LINEBELOW',(0,0),(-1,-1),.3,colors.HexColor('#CCD8D0'))]))
   story.extend([t,Spacer(1,12)])
doc.multiBuild(story,onFirstPage=pageframe,onLaterPages=pageframe)
print(out)
