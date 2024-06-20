# Census Data Ingestion Pipeline

## Objectives
- [x] Containerized application that pull metrics from US Census API & loads data into s3
- [x] User inputs desired year to retrieve latest Census data
- [x] Transform data for downstream analytics

## Setup & Application Run
### Requirements
- AWS Account
- Poetry
- Docker

### Run App with Make commands/Docker
have docker running to execute the following & run `aws sso login` prior
```
## to run locally
make local-run
```