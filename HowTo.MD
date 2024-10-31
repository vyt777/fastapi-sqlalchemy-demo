## Useful commands

### Setting up the environment commands
pip install fastapi uvicorn sqlalchemy psycopg2
python3 -m venv venv
source venv/bin/activate
sudo lsof -i :5432

### Docker with PostgreSQL commands
docker run --name fastapi-postgres -e POSTGRES_USER=fastapi_user -e POSTGRES_PASSWORD=your_password -e POSTGRES_DB=fastapi_db -p 5432:5432 -d postgres
docker exec -it fastapi-postgres psql -U fastapi_user -d fastapi_db
docker containers
docker ps

### PostgreSQL commands
psql -U fastapi_user -d fastapi_db
\d
\l
\q

### Launching commands
uvicorn main:app --reload
