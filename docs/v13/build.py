from pathlib import Path
import json,re,html
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, CondPageBreak, LongTable, TableStyle, KeepTogether
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
P=Path('/workspace/scratch/9e81b6b71a6d/v13-extins')
OUT=Path('/workspace/scratch/9e81b6b71a6d/output/Proiect_Romania_Fotbal_pentru_Viitor_V13.pdf')
fonts='/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV',fonts+'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB',fonts+'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DVB',italic='DV',boldItalic='DVB')
styles={}
styles['body']=ParagraphStyle('body',fontName='DV',fontSize=10.4,leading=15.1,spaceAfter=8,textColor=colors.HexColor('#20282c'),allowWidows=0,allowOrphans=0)
styles['h1']=ParagraphStyle('h1',parent=styles['body'],fontName='DVB',fontSize=20,leading=25,spaceAfter=16,keepWithNext=True,textColor=colors.black)
styles['h2']=ParagraphStyle('h2',parent=styles['body'],fontName='DVB',fontSize=12.4,leading=17,spaceBefore=12,spaceAfter=7,keepWithNext=True,textColor=colors.black)
styles['title']=ParagraphStyle('title',parent=styles['h1'],fontSize=32,leading=39,spaceAfter=26)
styles['small']=ParagraphStyle('small',parent=styles['body'],fontSize=8.5,leading=12)
styles['cell']=ParagraphStyle('cell',parent=styles['body'],fontSize=8.3,leading=11.8,spaceAfter=0)
styles['th']=ParagraphStyle('th',parent=styles['cell'],fontName='DVB',textColor=colors.white)
styles['bullet']=ParagraphStyle('bullet',parent=styles['body'],leftIndent=12,firstLineIndent=-10,bulletIndent=0)
styles['link']=ParagraphStyle('link',parent=styles['small'],textColor=colors.HexColor('#27517b'),wordWrap='CJK',spaceAfter=10)
W,H=A4; inner=W-104
class Doc(SimpleDocTemplate):
 def afterFlowable(self,f):
  if isinstance(f,Paragraph) and f.style.name=='h1':
   txt=f.getPlainText();key='sec'+str(self.seq.nextf('heading'))
   self.canv.bookmarkPage(key);self.canv.addOutlineEntry(txt,key,0)
   self.notify('TOCEntry',(0,txt,self.page,key))
def footer(c,d):
 c.saveState();c.setFillColor(colors.HexColor('#566369'));c.setFont('DV',8)
 c.drawString(52,27,'Proiect România  |  Fotbal pentru Viitor  |  V13 extins')
 c.drawRightString(W-52,27,str(d.page))
 if d.page>1:
  c.setStrokeColor(colors.HexColor('#d9dfe1'));c.line(52,H-36,W-52,H-36)
  c.setFont('DV',7.4);c.drawString(52,H-29,'DOCUMENT DE LUCRU  •  ORIZONT 2030–2040')
 c.restoreState()
s=P.joinpath('proiect.md').read_text()
for k,v in json.loads(P.joinpath('tables.json').read_text()).items():s=s.replace('{{'+k+'}}',v)
assert '{{' not in s
P.joinpath('V13_extins_sursa.md').write_text(s)
lines=s.splitlines(); story=[]; first=True;table=[]
def p(t,style='body'):
 return Paragraph(html.escape(t).replace('**',''),styles[style])
def flushtable():
 global table
 if not table:return
 data=[[p(x,'th' if i==0 else 'cell') for x in row] for i,row in enumerate(table)]
 n=len(table[0]); widths={2:[.64,.36],3:[.27,.36,.37],4:[.28,.23,.26,.23],5:[.12,.18,.2,.25,.25]}.get(n,[1/n]*n)
 # favour numeric columns only in financial tables
 if n==3 and ('Total EUR' in table[0] or 'cost unitar' in ' '.join(table[0])):widths=[.48,.32,.20]
 if n==3 and 'Dovadă' in ' '.join(table[0]):widths=[.23,.40,.37]
 if n==5 and 'Adulți' in ' '.join(table[0]):widths=[.12,.15,.16,.32,.25]
 t=LongTable(data,colWidths=[inner*x for x in widths],repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#223945')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f0f4f5')]),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#d9d9d9')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
 story.extend([t,Spacer(1,12)]);table=[]
for line in lines:
 if line.startswith('|'):
  table.append([x.strip() for x in line.strip('|').split('|')]);continue
 flushtable()
 if not line.strip():continue
 if line.startswith('# '):
  title=line[2:]
  if first:
   story.extend([Spacer(1,52),p('PROIECT ROMÂNIA','small'),Spacer(1,20),p(title,'title')]);first=False
  else:
   if title.startswith('1 '):
    story.append(PageBreak());story.append(p('Cuprins','h2'))
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc',fontName='DV',fontSize=9.5,leading=14,spaceBefore=5,leftIndent=0,firstLineIndent=0)]
    story.append(toc)
   story.extend([PageBreak() if title.startswith(('1 ', '9 ', '21 ', '23 ', '25 ', 'Anexa A ', 'Anexa J ')) else CondPageBreak(240),Spacer(1,12),p(title,'h1')])
 elif line.startswith('## '):story.append(p(line[3:],'h2'))
 elif line.startswith('- '):story.append(p('• '+line[2:],'bullet'))
 elif line.startswith('https://'):
  story.append(Paragraph('<link href="'+html.escape(line,quote=True)+'">'+html.escape(line)+'</link>',styles['link']))
 else:story.append(p(line))
flushtable()
doc=Doc(str(OUT),pagesize=A4,rightMargin=52,leftMargin=52,topMargin=53,bottomMargin=48,title='Fotbal pentru Viitor | Proiect România | V13 extins | 2030–2040',author='George Dobritoiu',pageCompression=1)
doc.multiBuild(story,onFirstPage=footer,onLaterPages=footer)
import fitz
pdf=fitz.open(OUT)
print(json.dumps({'pages':len(pdf),'words':len(s.split()),'bytes':OUT.stat().st_size,'path':str(OUT)},ensure_ascii=False))
# contact sheets for all pages, readable enough to detect layout problems; larger pages separately
from PIL import Image,ImageDraw
for start in range(0,len(pdf),12):
 thumb=Image.new('RGB',(1200,4*438),'#cbd1d5');draw=ImageDraw.Draw(thumb)
 for j,page in enumerate(pdf[start:start+12]):
  pix=page.get_pixmap(matrix=fitz.Matrix(.48,.48),alpha=False)
  im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
  x=(j%3)*400+(400-im.width)//2;y=(j//3)*438+20
  thumb.paste(im,(x,y));draw.text((x,y-16),str(start+j+1),fill='black')
 thumb.save(P/f'contact-{start//12+1}.jpg')
# layout metrics
problems=[]
for i,page in enumerate(pdf):
 for b in page.get_text('blocks'):
  if b[0]<45 or b[2]>W-45:problems.append((i+1,'horizontal',b[:4]))
print('layout_outliers',problems[:20])
print('short_pages',[(i+1,len(p.get_text())) for i,p in enumerate(pdf) if len(p.get_text())<500])
