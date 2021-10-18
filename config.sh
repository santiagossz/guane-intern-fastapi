source env/bin/activate

export APP_NAME=GUANE TEST
export APP_VERSION=0.1
export PSQL_HOST=localhost:5050
export PSQL_USER=postgres
export PSQ_PSSW=gb-test
export PSQL_DB=GB 

uvicorn app.main:app --reload --port 5005 

