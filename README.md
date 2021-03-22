# Checkout assessment code

## About

This is a project for a simple checkout assessment code.

### Pure python
To run the project using Python:

Go to the folder **consumer_store/**

Run main.py
```bash
$ python main.py
```

### Docker

To run the project using Docker:

Go to the folder **consumer_store/**

Build Docker image:
```bash
$ docker build -t assement -f app/main/configuration/Dockerfile .
```

Run Docker container:
```bash
$ docker run -it --name assement --rm assement
```