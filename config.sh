source env/bin/activate


export PSQL_HOST=localhost:5050
export PSQL_USER=postgres
export PSQ_PSSW=gb-test
export PSQL_DB=GB 

uvicorn backend.app.main:app --reload --port 5005 

