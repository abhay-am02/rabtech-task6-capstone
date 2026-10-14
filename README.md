# RabTech Task 6: Cloud Infrastructure Deployment & Monitoring

## Project Overview
A containerized Flask application deployed on AWS EC2 using Docker.
Prometheus monitors application metrics.

## Architecture
- AWS EC2 Ubuntu
- Flask application with Gunicorn
- Docker and Docker Compose
- Prometheus monitoring

## Endpoints
- Home: /
- Health check: /health
- Metrics: /metrics

## Environment Variables
APP_MESSAGE configures the application's home-page message.

## Deployment
Build the application:
sudo docker compose build app

Start the application:
sudo docker compose up -d app

Start Prometheus:
sudo docker compose up -d prometheus

Check containers:
sudo docker ps

## Monitoring
Prometheus scrapes the application metrics endpoint every 15 seconds.
The target was verified as UP.

## Grafana Dashboard

Grafana provides a dashboard to visualize application availability metrics
collected by Prometheus.

- Dashboard: RabTech Task 6 Monitoring
- Metric: `up`
- Expected value: `1` when the application is reachable
- Prometheus target status: UP

Grafana is accessed locally through VS Code SSH port forwarding on port 3000.

## Alerting
The alerts.yml file defines the ApplicationDown alert.

## Live Application
http://3.110.167.21/

Health check:
http://3.110.167.21/health
