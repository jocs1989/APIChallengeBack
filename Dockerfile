FROM python:3.11


RUN useradd -m -d /home/scraper scraper


ENV APP_ENV='local' \
  APP_NAME='WebScrapr' \
  PORT=3000 \
  HOST='0.0.0.0'  \
  LOG_LEVEL=DEBUG  \
  LOG_LEVEL=INFO \
  APP_HOME='/usr/src/app' \
  MONGODB_URI=''  \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# System deps:
COPY requirements.txt . 
RUN pip install -r requirements.txt

# Copy only requirements to cache them in docker layer
WORKDIR $APP_HOME
# Creating folders, and files for a project:
COPY . $APP_HOME


# Cambiar propietario de los archivos al usuario no root
RUN chown -R scraper:scraper $APP_HOME

# Cambiar al usuario no root
USER scraper

# Run the web service on container startup.

CMD ["python", "main.py"]