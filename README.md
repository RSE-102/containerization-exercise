# Quantum Circuit Execution Service

The circuit execution service enables the execution of quantum circuits on different quantum devices via an REST API.

## Running the Service

1. Build the Docker container: ``docker build -t execution-service .``
2. Run the Docker container: ``docker run -p 5075:5075 execution-service``

Then the service can be accessed via: [http://127.0.0.1:5075](http://127.0.0.1:5075).

## API Documentation

The execution service provides a Swagger UI, specifying the request schemas and showcasing exemplary requests for all API endpoints.
 * Swagger UI: [http://127.0.0.1:5075/app/swagger-ui](http://127.0.0.1:5075/app/swagger-ui).