#!/bin/bash
# Double-click to open the Study Desk with editing enabled.
cd "$(dirname "$0")"
if curl -s -o /dev/null http://localhost:8611/study.html; then
  open "http://localhost:8611/study.html"
else
  python3 serve.py
fi
