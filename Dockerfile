# Build step #1: build the React front end
FROM node:20 AS build-step
WORKDIR /app
COPY ./react-frontend/ ./react-frontend/
WORKDIR /app/react-frontend
RUN npm install
RUN npm run build

# Build step #2: build the API with the client as static files
FROM python:3.10
WORKDIR /app
COPY --from=build-step /app/react-frontend/build ./react-frontend/build

COPY ./backend ./backend
WORKDIR /app/backend
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "-b", ":5000", "app:app"]
