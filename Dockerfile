FROM ubuntu:24.04


RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates time python3 python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*

COPY /src/requirements.txt ./src/requirements.txt
RUN python3 -m pip install -r src/requirements.txt --break-system-packages
COPY /src ./src

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8088", "src.service:app"]