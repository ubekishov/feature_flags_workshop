# Stage 1: Build TypeScript
FROM node:14 AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install -g typescript
RUN npm install -D esbuild

COPY . .

RUN tsc
RUN npx esbuild flags.ts --bundle --target=es2020 --outfile=flags.js

# Stage 2: Python application
FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY --from=builder /app/app.js /app/static/js/
COPY --from=builder /app/flags.js /app/static/js/

CMD ["python", "app.py"]
