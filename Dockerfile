FROM quay.io/katonic/katonic-base-images:py38-base-conda4.9.2

COPY Katonic_app.py .
COPY img_src img_src
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD streamlit run Katonic_app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error
