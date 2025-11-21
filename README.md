# t2e-translator

## Bu repo, Türkçe ↔ İngilizce metin çevirisi yapan bir Python FastAPI uygulamasıdır. Basit bir HTTP API ile metin alır ve istenen dile çevirisini döner.

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
source venv/bin/activate
cd app
uvicorn main:app --host 0.0.0.0 --port 8000
```
