gunicorn -w 4 -k uvicorn.workers.UvicornWorker Logistic_api.main:app
#gunicorn Logistic_api.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8443 --timeout 
pip install python-multipart

