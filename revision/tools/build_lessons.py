# Builds practice/*.src.html into .html: inlines tools/lesson-style.html for {{STYLE}}, figures for {{IMG:file.png|alt}}, and links from tools/links.json.
# Cheatsheet sources use {{SHEETSTYLE}} and {{SHEETJS}} for the shared sheet style and Paper / Everything / Tap view script.
# Usage: python3 revision/tools/build_lessons.py revision/practice/week3-s1-graphs-lesson.src.html
# Careful: this overwrites the .html, so carry over any edits made in the Study Desk first.
import sys, re, base64, json, os
import pathlib; R=str(pathlib.Path(__file__).resolve().parent.parent); G=R+"/tools"
links=json.load(open(f"{G}/links.json")) if os.path.exists(f"{G}/links.json") else {}
style=open(f"{G}/lesson-style.html").read()
sheetstyle=open(f"{G}/sheet-style.html").read(); sheetjs=open(f"{G}/sheet-script.html").read()
def img(m):
    name=m.group(1); b=base64.b64encode(open(f"{R}/figures/{name}","rb").read()).decode()
    return f'<img class="fig" alt="{m.group(2)}" src="data:image/png;base64,{b}">'
for src in sys.argv[1:]:
    t=open(src).read().replace("{{SHEETSTYLE}}",sheetstyle).replace("{{SHEETJS}}",sheetjs).replace("{{STYLE}}",style)
    t=re.sub(r'\{\{IMG:([^|}]+)\|([^}]*)\}\}',img,t)
    for k,v in links.items(): t=t.replace("{{"+k+"}}",v)
    out=src.replace(".src.html",".html"); open(out,"w").write(t); print(out, len(t))
    left=re.findall(r'\{\{[A-Z]+\}\}',t)
    if left: print("  unresolved:",set(left))
