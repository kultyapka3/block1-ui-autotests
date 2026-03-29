FROM python:3.11-slim

WORKDIR /app

# Системные зависимости
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Allure CLI
RUN wget -qO- https://github.com/allure-framework/allure2/releases/download/2.25.0/allure-2.25.0.tgz | \
    tar xz -C /opt/ && \
    ln -s /opt/allure-2.25.0/bin/allure /usr/local/bin/allure

# Кеш pip
ENV PIP_CACHE_DIR=/root/.cache/pip
RUN mkdir -p $PIP_CACHE_DIR

# Зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Исходный код
COPY . .

# Переменные окружения для Selenoid
ENV SELENIUM_HOST=http://selenoid:4444/wd/hub
ENV CI=true
ENV WDM_LOCAL=/app/.wdm_cache

# Создаём папки для отчётов
RUN mkdir -p allure_results/selenoid allure_report .wdm_cache

# Команда по умолчанию
CMD ["pytest", "tests/test_basic_auth.py tests/test_input_alert.py tests/test_login_parameterized.py",
    "--run-mode=grid", "--grid-url=${SELENIUM_HOST}", "--alluredir=./allure_results/selenoid", "-v"]
