gunicorn -w 4 -k uvicorn.workers.UvicornWorker Logistic_api.main:app
pip install python-multipart
pip install -v scikit-learn==1.0.2
