# Emloyee Manager application Python + Django + Tastypie Development with Docker
This is a base image for only Python development.

## Prerequisites

## Getting Started

### 1. DockerDocker
- You can install Docker follow this [guide](https://docs.docker.com/engine/installation/).

### 2. Build Python image

- Build your first Docpad image using Docker.

```
docker build -t employee:latest .
```

**NOTE**:

- You can change your image by replacing `employee` by any name you want.

- This command only need to run once in the beginning.

### 3. Run Python Development
```
docker run -it --rm -w /home/app -v $(pwd)/:/home/app employee:latest bash
```

**NOTE**:

- You can set permission for bash file and run it.

```
chmod 777 env.sh
./env.sh
```

### 4. Run test
```
cd src/test
./manage.py test
```

## Author
[Minh Tran](https://gitlab.asoft-python.com/minh-tran)

## Common Issues
