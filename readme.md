# Panduan Instalasi Virtual Environment dan Flask

## 1. Instalasi Python Virtual Environment

```bash
# Install python3-venv jika belum ada
sudo apt-get update
sudo apt-get install python3-venv
```

## 2. Membuat Virtual Environment

```bash
# Buat folder project (opsional)
mkdir python-api
cd python-api

# Buat virtual environment
python3 -m venv venv
```

## 3. Aktivasi Virtual Environment

```bash
# Aktifkan virtual environment
source venv/bin/activate

# Pastikan menggunakan Python dari venv
which python
```

## 4. Instalasi Flask

```bash
# Upgrade pip
pip install --upgrade pip

# Install Flask
pip install flask
```

## 5. Verifikasi Instalasi

```bash
# Cek versi Flask
python -c "import flask; print(flask.__version__)"
```

## 6. Membuat File Test

```bash
# Buat file test.py
nano test.py
```

Isi `test.py` dengan kode berikut:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask is running!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
```

## 7. Menjalankan Aplikasi

```bash
python test.py
```

## Perintah Tambahan

```bash
# Keluar dari virtual environment
deactivate

# Melihat daftar package terinstall
pip list
```
