# Darma Test

This is a demo app for the Family Activity Planning Web App to enable Darma to explore its potential to enhance the lives of busy families and let them attend their children’s sports activities.

# Setting up the project

This project has 3 parts:

  * Infrastructure created with Docker and Docker Compose.
  * Backend created with FastAPI, Redis, and PostgreSQL.
  * Frontend created with React using Vite.

## Infrastructure

To run the infrastructure, you need to have `docker` and `docker compose` installed. Then, you can run the following commands:

```bash
cd docker
cp .env.example .env
sh install.sh
```

To stop the infrastructure, you can run the following commands:

```bash
cd docker
sh uninstall.sh
```

## Backend

To run the backend, you need to have `python` v3.x and `pip` installed. Then, you can run the following commands:

* Navigate to the `backend` directory and copy the `.env.example` file to `.env`:
```bash
cd backend
cp .env.example .env
```

* Create a virtual environment:
```bash
python3 -m venv venv
```

* Activate the virtual environment and install the dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

* Run the migrations:
```bash
alembic upgrade head
```

* Run the backend server:
```bash
uvicorn src.main:app --reload
```

* Run the backend service to listen to the Redis key expiration events:
```bash
cd src
python scheduler.py
```

* Close the virtual environment:
```bash
deactivate
```

### API Documentation

You can access the API documentation by visiting `http://localhost:8000/docs` in your browser, to see the available endpoints given by FastAPI.

Also, you can open Postman and import the [Darma.postman_collection.json](./Darma%20test.postman_collection.json) file to see the available endpoints and test them. There are some examples of requests and responses in the collection.

## Frontend

To run the frontend, you need to have `node` and `npm` installed. Then, you can run the following commands:

* Navigate to the `frontend` directory:
```bash
cd frontend
```

* Install the dependencies:
```bash
npm install
```

* Run the frontend:
```bash
npm run dev
```

***note***: the frontend is far from complete and functional (sorry!).

# Admin tools

There are 2 tools in the `docker compose` infrastructure to help you manage the data in the database and the Redis.

## PGAdmin

You can access the PGAdmin tool by visiting `http://localhost:5050` in your browser. The default username is `admin@admin.com` and the default password is `admin`.

To add the database, select `add new server` and fill in the following fields:

  * Name: `darma database`
  * Host name/address: `postgres` (docker service name)
  * Port: `5432`
  * Username: `postgres`
  * Password: `postgres`

## Redis Commander

You can access the Redis Commander tool by visiting `http://localhost:8081` in your browser. When you open Redis Commander, you should see the local database.
