FROM python:3.9

# Crear el usuario scraper


# Configuración de las variables de entorno
ENV APP_ENV='local' \
    APP_NAME='WebScrapr' \
    PORT=${PORT} \
    HOST='0.0.0.0' \
    LOG_LEVEL=INFO \
    APP_HOME='/usr/src/app' \
    MONGODB_URI=${MONGODB_URI} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Instalar dependencias del sistema necesarias para Playwright y otros paquetes
RUN apt-get update && \
    apt-get install -y \
    wget \
    curl \
    libx11-dev \
    libxcomposite-dev \
    libxdamage-dev \
    libpng-dev \
    libnss3-dev \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libxrandr2 \
    libgbm-dev \
    libasound2 \
    libgdk-pixbuf2.0-0 \
    libdbus-1-3 \
    libgtk-3-0 \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libnspr4 \
    libxss1 \
    libxtst6 \
    lsb-release \
    sudo && \
    apt-get clean

# Copiar el archivo de requerimientos e instalar dependencias de Python
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Instalar los navegadores necesarios para Playwright
RUN python -m playwright install --with-deps
RUN playwright install --with-deps

# Configuración de trabajo y copiado de la aplicación
WORKDIR $APP_HOME
COPY . $APP_HOME


# Exponer el puerto 3000
EXPOSE ${PORT}

# Ejecutar la aplicación
CMD ["python", "main.py"]
