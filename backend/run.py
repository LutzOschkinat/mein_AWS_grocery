import sys
import os

print("Python executable:", sys.executable)
print("sys.path:", sys.path)
print("Current working directory:", os.getcwd())

# Versuch, Flask hier zu importieren, um zu sehen, was passiert
try:
    import flask
    print("Flask imported successfully within the script")
except ImportError:
    print("Flask import failed within the script")

# Lassen die ursprüngliche Importzeile danach stehen
# from app import create_app
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
