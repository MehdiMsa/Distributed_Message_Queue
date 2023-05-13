# Distributed Message Queue with Kafka, HAProxy, Prometheus, and Grafana

This project is a practical implementation of a distributed message queue using Apache Kafka, with load balancing provided by HAProxy, and monitoring and visualization set up with Prometheus and Grafana. 

## Tools Used

* [Apache Kafka](https://kafka.apache.org/documentation/) - Distributed Streaming Platform
* [HAProxy](http://www.haproxy.org/#docs) - Reliable, High Performance TCP/HTTP Load Balancer
* [Prometheus](https://prometheus.io/docs/introduction/overview/) - Monitoring system and Time Series Database
* [Grafana](https://grafana.com/docs/grafana/latest/) - Analytics and interactive visualization web application

## Setting Up the Environment

The following steps guide you through setting up the environment:

1. Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).
2. Clone this repository: `git clone <repository-url>`.
3. Navigate to the project directory: `cd <repository-dir>`.
4. Run `docker-compose up -d` to start up the Docker containers.

## Executing the Project

Follow these steps to execute the project:

1. Verify that all services (Kafka, Zookeeper, HAProxy, Prometheus, and Grafana) are running using `docker ps`.
2. Run the producer Python scripts: `python producer.py <id>`.
3. Run the consumer Python scripts: `python consumer.py <id>`.
4. Access the Grafana dashboard at `http://localhost:3000` to visualize the metrics.

## Contributors

- Mehdi M'sallem
- Ines Ktiti
- Ala Boussarsar
- Sarra Ben Rjeb
- Emir Aissa
