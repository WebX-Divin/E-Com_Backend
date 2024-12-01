# Backend Setup and Migration Guide

This document provides instructions to set up and run the backend service, including database migrations using Alembic and Docker.

## Prerequisites

Make sure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup Instructions

Follow the steps below to set up the backend project:

### 1. Initialize Alembic

If Alembic has not been initialized in your project, you can do so by running:

```bash
alembic init alembic
```

This will create the necessary Alembic configuration files in your project directory.

### 2. Build Docker Images

To build the Docker images for your application, execute:

```bash
docker-compose build
```

This will build all the services defined in your `docker-compose.yml` file.

### 3. Start the Services

To start the application services, run:

```bash
docker-compose up
```

This will start all the services (e.g., app, database) in the foreground. You can add the `-d` flag to run the services in detached mode:

```bash
docker-compose up -d
```

### 4. Generate a Database Migration

To create a new database migration, use the following command:

```bash
docker-compose run app alembic revision --autogenerate -m "Migration name"
```

Replace `"Migration name"` with a descriptive name for your migration.

### 5. Apply the Migration

Apply the migration to the database with:

```bash
docker-compose run app alembic upgrade head
```

This will upgrade your database schema to the latest version.

## Notes

- Ensure that your Alembic configuration (`alembic.ini`) and `env.py` file are correctly set up to connect to your database.
- If you encounter any issues, check the logs by running `docker-compose logs`.

## Common Commands

Here are some additional helpful commands:

- Stop all services:  

  ```bash
  docker-compose down
  ```

- Rebuild services after changes:  

  ```bash
  docker-compose up --build
  ```

- View logs for a specific service:  

  ```bash
  docker-compose logs <service_name>
  ```

- Access the running app container:  

  ```bash
  docker-compose exec app /bin/bash
  ```
