# Census Data Ingestion Pipeline

### Objectives
- [x] Containerized application that pull metrics from US Census API & loads data into s3
- [x] User inputs desired year to retrieve latest Census data
- [x] Transform data for downstream analytics

## Project Setup & Run
### Project Requirements
- Poetry
- Docker

### Testing & Deployment with Make commands/Docker

have docker running to execute the following & run `aws sso login` prior
```
## for local testing
make local-test

# in seperate terminal
docker ps
docker exec -it <container_id> /bin/bash
python3 app.py

## to deploy to ECR & run the lambda app
make deploy
```