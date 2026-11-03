# Builds a practice question page from practice/<name>-questions.src.json.
# Writes practice/<name>-questions.html and practice/<name>-answer-key.json.
# Usage: python3 revision/tools/build_questions.py revision/practice/week5-questions.src.json
import sys, json, base64, pathlib
R = pathlib.Path(__file__).resolve().parent.parent; G = R / "tools"
style = (G / "q-style.html").read_text(); script = (G / "q-script.html").read_text()
for src in sys.argv[1:]:
    spec = json.loads(pathlib.Path(src).read_text())
    for t in spec["sections"]:
        if t.get("fig"):
            b = base64.b64encode((R / "figures" / t["fig"]).read_bytes()).decode()
            t["fig"] = "data:image/png;base64," + b
        else: t["fig"] = None
        t.setdefault("figcap", "")
        for q in t["qs"]: q.setdefault("code", None)
    n = sum(len(t["qs"]) for t in spec["sections"])
    html = f'''<title>{spec["title"]}</title>
<meta name="claude:viewport-fit-sides" content="cover">
{style}<div class="wrap">
<header>
  <div class="eyebrow">{spec["eyebrow"]}</div>
  <h1>{spec["h1"]}</h1>
  <div class="meta"><span class="pill">{len(spec["sections"])} sections, {n} questions</span><span class="pill">exam-style, 4 options</span><span class="pill" id="total">0 / {n} checked</span></div>
  <p class="how"><b>Best way to use this:</b> keep the {spec["sheet"]} open, and answer in the chat thinking out loud, for example "1.3: B, because I looked at {spec["eg_ref"]}". You'll get a correction that points to the sheet. To self-check here instead, pick an option and press Check.</p>
</header>
<div id="topics" style="display:flex;flex-direction:column;gap:22px"></div>
<footer>{spec["footer"]}</footer>
</div>
''' + script.replace("{{DATA}}", json.dumps(spec["sections"], ensure_ascii=False))
    out = src.replace("-questions.src.json", "-questions.html"); pathlib.Path(out).write_text(html)
    key = {q["id"]: "ABCD"[q["ans"]] for t in spec["sections"] for q in t["qs"]}
    pathlib.Path(src.replace("-questions.src.json", "-answer-key.json")).write_text(json.dumps(key, indent=1))
    print(out, n, "questions", "".join(key.values()))
