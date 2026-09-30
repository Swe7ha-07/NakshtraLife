@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -q --upgrade pip
.venv\Scripts\python.exe -m pip install -q -r requirements.txt
set NAKSHATRALIFE_LOCAL_PERSIST=1
.venv\Scripts\python.exe -m streamlit run app.py --server.port 8501
