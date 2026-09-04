#!/bin/sh
# Logt tijdstip + workspace/git-staat naar tools/timing-log.md
cd /home/user/natuurgids
F=tools/timing-log.md
[ -f "$F" ] || echo "# Timing- en workspace-log\n\n| UTC | lokaal (CEST) | fase | HEAD | dirty | .git/HEAD mtime | tools/ files |\n|---|---|---|---|---|---|---|" > "$F"
printf '| %s | %s | %s | %s | %s | %s | %s |\n' \
  "$(date -u +'%H:%M:%S')" \
  "$(TZ=Europe/Amsterdam date +'%H:%M:%S')" \
  "$1" \
  "$(git log --oneline -1 2>/dev/null | cut -c1-7)" \
  "$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')" \
  "$(stat -c '%y' .git/HEAD 2>/dev/null | cut -c12-19)" \
  "$(ls tools/*.py 2>/dev/null | wc -l | tr -d ' ')" >> "$F"
