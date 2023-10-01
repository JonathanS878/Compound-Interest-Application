# DevOps Application-compound-interest

This repository contains the source code for the DevOps application, which is a part of a larger ecosystem composed of three repositories:

 **Application** (Current repository): [Application Repo](https://github.com/BinyaminR/Application-compound-interest)

 **GitOps**: [GitOps Repo](https://github.com/BinyaminR/Gitops-compound-interest)
 
 **Infrastructure**: [Infrastructure Repo](https://github.com/BinyaminR/Infrastructure-compound-interest)
 
## Application Overview

This application serves as a foundational template for a CI/CD (Continuous Integration/Continuous Deployment) pipeline, leveraging a multi-faceted technology stack. The CI/CD pipeline enables automated testing, building, and deployment of applications in a streamlined manner. The application is built on Python, using the Flask web framework for creating a simple REST API. It uses MongoDB as its data store, thereby enabling high-performance, easily scalable NoSQL storage.

### Key Features:

1. **Continuous Integration (CI)**: Implemented through GitHub Actions, the CI process involves automatic linting, unit testing, and building Docker images upon every Git push to the repository.

2. **Continuous Deployment (CD)**: Uses ArgoCD and Helm charts for the deployment phase, providing automated, GitOps-driven application updates directly into the GKE (Google Kubernetes Engine) clusters.

3. **Infrastructure as Code (IaC)**: Utilizes Terraform to provision and manage all required cloud infrastructure, making it highly replicable and version-controlled.

4. **Containerization**: The application and its components are containerized using Docker, making it environment agnostic and easy to scale.

5. **Orchestration**: Uses Kubernetes for container orchestration, allowing for high availability, load balancing, and horizontal scaling.

6. **Monitoring**: Incorporates Prometheus and Grafana for real-time monitoring and analytics of the application and the underlying infrastructure.

### CI Environment and Workflows

The CI environment is configured using GitHub Actions. There are various workflows defined in the `.github/workflows` directory of the repository. These workflows define the sequence of actions that will be automatically executed upon every push to the repository.

The typical workflow includes the following steps:

1. **Unit Testing**: Automated unit tests are run to ensure that the new changes do not break existing functionality.

2. **Building Docker Images**: Docker images for the application are built and pushed to a Docker registry.

Once the changes are pushed to a feature branch, they are automatically tested using the above-mentioned steps. If the tests pass, a Pull Request can be created to merge the changes into the main branch. The Pull Request is reviewed, and if everything is in order, the changes are merged into the main branch, thereby triggering the CD process.

## Technologies Used

- [Python](https://docs.python.org/3/): The programming language used for developing the application.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/): A micro web framework written in Python.
- [MongoDB](https://docs.mongodb.com/): A NoSQL database used for storing the application data.
- [Docker](https://docs.docker.com/): A platform used for developing, shipping, and running applications in containers.
- [Docker-Compose](https://docs.docker.com/compose/): A tool for defining and running multi-container Docker applications.
- [Kubernetes](https://kubernetes.io/docs/home/): An open-source container orchestration system for automating application deployment, scaling, and management.
- [Helm](https://helm.sh/docs/): A package manager for Kubernetes.
- [Terraform](https://www.terraform.io/docs/index.html): An infrastructure as code (IaC) tool for building, changing, and version-controlling infrastructure efficiently.
- [GitHub Actions](https://docs.github.com/en/actions): A CI/CD tool that automates workflows.
- [GCP/GKE](https://cloud.google.com/kubernetes-engine/docs): Google Kubernetes Engine (GKE) is a managed, production-ready environment for running containerized applications on Google Cloud.
- [ArgoCD](https://argoproj.github.io/argo-cd/): A declarative, GitOps continuous delivery tool for Kubernetes.
- [Prometheus](https://prometheus.io/docs/introduction/overview/): An open-source monitoring system with a dimensional data model, flexible query language, efficient time series database, and modern alerting approach.
- [Grafana](https://grafana.com/docs/grafana/latest/): An open-source analytics and monitoring solution.

## The application:

## Architecture
![Architecture](/images/Devops-project.jpg)<br>

## Deposit page
![Investment](/images/invest-1.png)<br>

## Investments page
![Investment](/images/invest-2.png)<br>
