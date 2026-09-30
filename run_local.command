#!/bin/bash
set -e
cd "$(dirname "$0")"
PYTHON_BIN="$(command -v python3 || true)"
if [ -z "$PYTHON_BIN" ]; then
  echo "Python 3 is required. Install Python 3 and run this file again."
  read -r -p "Press Return to close..." _
  exit 1
fi
if [ ! -x .venv/bin/python ]; then
  "$PYTHON_BIN" -m venv .venv
fi
.venv/bin/python -m pip install -q --upgrade pip
.venv/bin/python -m pip install -q -r requirements.txt
.venv/bin/python -m streamlit run app.py --server.port 8501
