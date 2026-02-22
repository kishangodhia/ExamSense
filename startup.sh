#!/bin/bash

apt-get update
apt-get install -y tesseract-ocr poppler-utils

export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata
export PATH="/usr/bin:$PATH"

streamlit run app.py --server.port $PORT --server.address 0.0.0.0