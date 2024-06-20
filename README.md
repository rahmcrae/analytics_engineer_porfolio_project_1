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
![census-ingestion](https://github.com/rahmcrae/analytics_engineer_porfolio_project_1/assets/63305557/18908cdf-3e45-4443-a09a-9a720e013cf7)
