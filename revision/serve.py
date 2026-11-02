#!/usr/bin/env python3
"""Study Desk local server.

Serves the revision/ folder at http://localhost:8611/study.html and lets the
Study Desk save edits to lesson / cheatsheet / question pages (HTTP PUT).
Before each save, the previous file is copied to revision/.edit-backups/.
Only listens on 127.0.0.1, and only writes .html files inside revision/.
"""
import http.server, os, shutil, sys, time, webbrowser
from functools import partial

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("STUDY_DESK_PORT", "8611"))


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_PUT(self):
        rel = self.path.split("?", 1)[0].lstrip("/")
        target = os.path.realpath(os.path.join(ROOT, rel))
        if not target.startswith(ROOT + os.sep) or not target.endswith(".html") \
                or os.path.basename(target) == "study.html" or not os.path.isfile(target):
            self.send_error(403, "Can only save existing .html pages inside revision/")
            return
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        backup_dir = os.path.join(ROOT, ".edit-backups", os.path.dirname(rel))
        os.makedirs(backup_dir, exist_ok=True)
        stamp = time.strftime("%Y%m%d-%H%M%S")
        shutil.copy2(target, os.path.join(backup_dir, f"{os.path.basename(rel)[:-5]}.{stamp}.html"))
        with open(target, "wb") as f:
            f.write(body)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"saved")

    def log_message(self, fmt, *args):
        if self.command == "PUT":
            sys.stderr.write("saved %s\n" % self.path)


if __name__ == "__main__":
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), partial(Handler, directory=ROOT))
    url = f"http://localhost:{PORT}/study.html"
    print("Study Desk running at", url, "(Ctrl+C to stop)")
    if "--no-open" not in sys.argv:
        webbrowser.open(url)
    srv.serve_forever()
