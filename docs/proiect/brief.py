from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from pathlib import Path
import fitz
for n,f in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/dejavu/'+f))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DVB')
body=ParagraphStyle('body',fontName='DV',fontSize=9.7,leading=13.4,spaceAfter=7,textColor=colors.HexColor('#20282c'))
head=ParagraphStyle('head',parent=body,fontName='DVB',fontSize=12,leading=16,spaceBefore=8,spaceAfter=7)
title=ParagraphStyle('title',parent=head,fontSize=28,leading=33,spaceAfter=16)
small=ParagraphStyle('small',parent=body,fontSize=8.5,leading=12)
s=[]
def p(t,style=body):s.append(Paragraph(t,style))
p('Fotbal pentru Viitor',title)
p('REZUMAT EXECUTIV • ORIZONT 2030–2040',head)
p('Propunere: George Dobritoiu<br/>Document de lucru | octombrie 2026',small)
p('Investim în copii, în oamenii care îi pregătesc și în comunitățile în care pot continua să joace. Propunem dezvoltarea unei rețele comunitare conectate cu structurile sportive existente, cu acces, siguranță și rezultate măsurabile.')
p('Schimbarea propusă',head)
p('Propunem redirecționarea sprijinului public destinat primei echipe din Superliga către baza piramidei: copii, antrenori, arbitri, fotbal feminin și infrastructură comunitară. Autoritățile decid realocarea după analiza contractelor și a cadrului juridic. Finanțările intră în planul de numerar numai după contractare.')
p('Un pilot concret, înainte de extindere',head)
p('<b>400 de copii • circa 25 de echipe • un municipiu și 4–6 comune.</b><br/>Aproximativ 60 de adulți locali verificați și instruiți, trei mentori tehnici cu timp parțial, coordonare operațională și un responsabil pentru protecția copilului. Pregătim și 12 candidați formatori; activitățile inițiale sunt conduse de profesioniști deja calificați.')
p('<b>21 de luni:</b> șase luni de pregătire, 12 luni de activitate și trei luni de evaluare. Urmărirea ulterioară a cohortelor are nevoie de un buget distinct de continuitate.')
p('<b>Buget estimativ: 365.505 EUR</b>, din care 317.830 EUR costuri de bază și 47.675 EUR rezervă. Sume de planificare la prețuri 2026, de înlocuit prin oferte și acorduri înainte de contractare.')
p('Ce câștigă partenerii',head)
p('<b>FRF:</b> o bază mai largă de participare, oameni pregătiți și date comparabile pentru dezvoltare și selecție.<br/><b>AJF-uri:</b> sprijin pentru formare, coordonare și retenția arbitrilor, cu instrumente comune și responsabilități clare.<br/><b>Comunități și finanțatori:</b> acces regulat pentru copii, evidența costurilor și rezultate verificabile.')
p('Decizia solicitată acum',head)
p('Alegerea organizației gazdă și aprobarea etapei de pregătire, cu responsabil și buget. Diagnosticul local, parteneriatele, ofertele și procedurile de protecție fundamentează decizia ulterioară de lansare.')
s.append(PageBreak())
p('Cum construim și când extindem',title)
p('Formăm capacitatea, apoi creștem',head)
p('Evaluăm capacitatea și performanța existente pe ultimii 3–5 ani. Un nucleu de specialiști pregătește formatori regionali, care instruiesc și sprijină practicienii locali. Două transferuri metodologice, programe comune și evaluare independentă. Antrenoratul, arbitrajul, protecția copilului, administrarea și voluntariatul au trasee distincte. Recunoașterea în traseele oficiale se negociază cu organismele competente.')
p('Diaspora: o componentă operațională distinctă',head)
p('Programul sprijină funcția de scouting existentă a FRF, fără să creeze un sistem paralel; selecția și convocarea rămân decizia exclusivă a staff-ului tehnic FRF. Identificăm de la U13 și observăm structurat U14–U19, fete și băieți. U21/A rămân în afara rețelei. Dosarele sunt prioritizate transparent după eligibilitate, fereastra sportivă și dovezi; distanța servește organizării logistice.')
p('Ipoteza de cost este de <b>32.430 EUR pentru un hub de țară</b> și <b>1.610 EUR pentru deplasarea unui copil și a unui însoțitor</b>, cu rezerve incluse. Exemplul cu patru hub-uri și 20 de deplasări însumează <b>161.920 EUR</b>. Organizarea sportivă la destinație se bugetează separat dacă nu este deja acoperită. Componenta are buget separat de pilotul comunitar.')
p('Resurse și finanțare',head)
p('Combinăm finanțări publice eligibile, sponsorizări, contribuții în natură și granturi competitive. Rutele UEFA/FIFA se discută instituțional prin FRF; programele europene depind de apel, eligibilitate și parteneriat. Veniturile se înregistrează după contractare.')
p('Documentul complet conține trei scenarii anuale pentru 2030–2040. Modelul separă costul variabil de 420 EUR pe loc de costurile hub-urilor, coordonării centrale, extinderii și rezervei. Scenariile exprimă necesarul de resurse. Capacitatea oamenilor și bazelor limitează ritmul creșterii.')
p('Condiții pentru continuare',head)
p('Urmărim participarea regulată și retenția copiilor, calitatea activității în teren, absolvenții activi la 6 și 12 luni, costul pe participant activ, continuitatea arbitrilor și respectarea procedurilor de protecție. Pragurile de succes se aprobă înaintea pilotului. Publicăm rezultate agregate și explicăm abaterile; protejăm datele minorilor.')
p('Ce nu promitem',head)
p('Nu promitem calificări internaționale, un număr de jucători profesioniști sau finanțări încă necontractate. Promitem un cadru de lucru propus, verificabil: responsabilități, costuri, evaluare și decizii documentate. Extinderea se aprobă numai când resursele, calitatea și siguranța o permit.')
p('Consultarea și descărcarea documentului sunt gratuite, pentru informare și evaluare. Drepturile de utilizare a materialelor protejate din documentație pentru implementare se acordă contra cost, prin contract de licență. George Dobritoiu poate fi remunerat pentru licențierea documentației. Autorul și firmele asociate lui nu participă la contractele de implementare a strategiei, inclusiv dezvoltarea platformei, formare, consultanță de implementare sau administrarea programului. Interesul financiar din licențiere este declarat transparent. Taxa de licență nu este stabilită și nu este inclusă în estimările financiare publicate. Dacă este necesară pentru utilizarea convenită, se bugetează separat și se include în necesarul total de finanțare înainte de contractare.',small)
p('Detalii, ipoteze, bugete și surse: documentul integral „Fotbal pentru Viitor”, octombrie 2026, capitolele 1–31 și anexele A–I.',small)
def footer(c,d):
 c.setFont('DV',8);c.setFillColor(colors.HexColor('#566369'));c.drawString(48,27,'Fotbal pentru Viitor');c.drawRightString(A4[0]-48,27,str(d.page))
out=Path(__file__).resolve().parents[2]/'Fotbal-pentru-Viitor-Rezumat-2026-10-03-corectat.pdf'
SimpleDocTemplate(str(out),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=39,bottomMargin=43,title='Fotbal pentru Viitor | Rezumat executiv',author='George Dobritoiu').build(s,onFirstPage=footer,onLaterPages=footer)
doc=fitz.open(out);assert len(doc)==2,len(doc)
print('Executive brief: 2 pages')
