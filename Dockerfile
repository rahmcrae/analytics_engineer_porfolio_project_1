FROM python:3.9

WORKDIR /app

# Upgrade pip and install Poetry
RUN pip install --upgrade pip poetry

# Disable virtualenv creation by Poetry to install dependencies globally
RUN poetry config virtualenvs.create false

# Copy only files necessary for dependency installation
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-dev
COPY /src .

# Set year for census data
ENV YEAR=2022

CMD ["python3",  "app.py"]