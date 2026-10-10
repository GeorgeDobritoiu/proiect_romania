"""Original editorial SVG pictograms; not third-party organisational logos."""
from pathlib import Path
from html import escape
P=Path(__file__).resolve().parents[2]
OUT=P/'assets/img/project-symbols';OUT.mkdir(parents=True,exist_ok=True)
icons={
'votat':('Ștampilă VOTAT', '#133e70', '''<g transform="rotate(-12 80 80)"><circle cx="80" cy="80" r="66" fill="none" stroke-width="5"/><circle cx="80" cy="80" r="57" fill="none" stroke-width="1.5"/><path d="m63 50 11 10 22-24" fill="none" stroke-width="6"/><path d="M23 66h114v36H23z" fill="#fff" stroke-width="3"/><text x="80" y="91" text-anchor="middle" font-family="Arial,sans-serif" font-size="29" font-weight="900" fill="#133e70" stroke="none">VOTAT</text><path d="M64 119h32" stroke-width="3"/></g>'''),
'refoloseste':('Reutilizare și economie circulară','#24705b','''<path d="M40 51a48 48 0 0 1 77-8l10 12M128 35v21h-22M120 109a48 48 0 0 1-77 8l-10-12M32 125v-21h22"/><path d="m58 66 22-12 22 12v30l-22 12-22-12zM58 66l22 12 22-12M80 78v30"/>'''),
'statii-verzi':('Stație verde de transport','#36715d','''<path d="M26 126V57h82v69M21 56l32-22h62M45 99h42M51 99v21M81 99v21"/><path d="M112 90V49M112 69c-22-3-28-19-25-33 23 2 28 16 25 33ZM113 57c1-20 15-29 29-28 0 19-10 31-29 28Z"/><path d="M21 130h120"/>'''),
'biciclete':('Bicicletă în siguranță','#2b6582','''<circle cx="42" cy="110" r="23"/><circle cx="117" cy="110" r="23"/><path d="m42 110 24-42 23 42H42l15-27h48l12 27M62 67h19M101 66l-8-17h-12"/><rect x="107" y="29" width="27" height="25" rx="5"/><path d="M113 29v-8a8 8 0 0 1 16 0v8"/>'''),
'gradini':('Îngrijirea grădinilor','#397445','''<path d="M80 111V61M80 82c-26 0-37-19-34-38 26 0 36 14 34 38ZM81 65c0-25 17-39 38-37 0 23-13 38-38 37Z"/><path d="M23 114l30-16 22 9c10 4 5 16-5 13l-15-5M21 126l36 13 55-22c13-6 5-18-4-14l-23 9"/>'''),
'spatiuviu':('Grădină și vecinătate','#497341','''<path d="M22 126V60h34v66M31 74h6M43 74h5M31 90h6M43 90h5M104 126V45h34v81M113 59h5M125 59h5M113 75h5M125 75h5"/><path d="M79 125V87M79 101c-16 0-23-10-21-23 16 0 22 9 21 23ZM80 89c0-17 12-26 26-25-1 16-10 26-26 25ZM18 132h125"/>'''),
'banii-partidelor':('Transparența finanțării','#956820','''<path d="M29 51 80 27l51 24M32 56h96M38 119h85M30 130h96M45 65v43M68 65v43M92 65v25M115 65v20"/><circle cx="111" cy="111" r="23" fill="#fff"/><path d="m127 127 15 15M103 111h16M111 103v16"/>'''),
'vot-corect':('Verificarea votului','#406191','''<path d="M31 89h98v46H31zM56 101h48M49 80l-9-43 61-13 13 56"/><path d="m60 55 13 10 18-27M23 89l15-14M137 89l-15-14"/>'''),
'bugete-locale':('Bugete locale transparente','#985839','''<path d="M32 25h64l25 25v84H32zM96 25v27h25M49 115V89h13v26M76 115V72h13v43M103 115V91"/><path d="m48 67 18-12 15 6 10-13"/>'''),
}
for name,(title,color,body) in icons.items():
 if name=='votat':bg='#eef3fa'
 else:bg='#f2f5f1'
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><rect x="2" y="2" width="156" height="156" rx="26" fill="{bg}"/><g fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>'''
 (OUT/(name+'.svg')).write_text(svg)
print('Created',len(icons),'editorial vector symbols')
