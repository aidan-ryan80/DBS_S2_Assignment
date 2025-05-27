FROM python:3.11-slim

WORKDIR /app

# Copying Python scripts

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY post_migration.py simulator.py /app/

CMD ["bash", "-c", "python post_migration.py && python simulator.py"]