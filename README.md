# NTSecurity
Api for file scanner with static analysis and sandbox

## Tests
Install pytest.
```bash
pip3 install pytest
```
If you want to run tests go to NiyauBackend directory and run this command.
```bash
pytest
```
## Run with docker-compose (Recommended)
```bash
docker-compose up
```

## Build
You need to build docker image from Dockerfile.
Run this command in project home directory.
```bash
docker build -t api_server .
```
## Run in reload mode for develop
To run server from image complete this command.
```bash
docker run -p80:80 -d --mount type=bind,source="$(pwd)"/app,target=/app --name server api_server
```
You can change source code and your changes are applied automatically.
## Stop container
```bash
docker stop server
```


