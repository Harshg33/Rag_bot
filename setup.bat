@echo off
echo Setting up Wyrd Wiki Bot...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo.
echo Setup Complete! Pulling models...
ollama pull mistral
ollama pull nomic-embed-text
echo.
echo All ready. Now run 'python ingest.py' then 'python app.py'
pause