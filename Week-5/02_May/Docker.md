# Overview Of Docker

### (1) What is Docker and why is it used?
### (2) Docker vs Virtual Machines
### (3) Install Docker Locally
### (4) Images Vs Containers
### (5) Public and Private Registries
### (6) Run Containers
   - ### (6.1) Pull and Run Containers From Public Repo
   - ### (6.2) Port Binding, Detached Mode etc.
### (7) Create Own Image (Docker File)
   - ### (7.1) Syntax and Concepts Of Dockerfile
### (8) Main Docker Commands
   - ### (8.1) Pull,Run,Start,Stop,Logs,Build
### (9) Image Versioning

# =====================================

# (1) What is Docker and why is it used?

# Docker Architecture

![Docker Img](https://docs.docker.com/get-started/images/docker-architecture.webp)

## What is Docker ?
   - ### Docker is a containerization platform that allows developers to package applications and their dependencies into a standardized unit called a container.
   - ### Containers provide consistency across different environments, making it easier to develop, deploy, and scale applications.

## Why Docker?

   ### Portability: 
   - #### Containers can run on any platform that supports Docker, making it easy to move applications between environments.

   ### Isolation: 
   - #### Containers provide process isolation, ensuring that applications run consistently regardless of the underlying infrastructure.
   
   ### Efficiency:
   - #### Containers share the host operating system kernel, resulting in lightweight and efficient deployments.

   ### Scalability:
   - #### Docker containers can be quickly spun up or down, allowing for dynamic scaling of applications based on demand.


# (2) Docker Containers vs Virtual Machines

| Docker Containers       | Virtual Machines            |
|-------------------------|-----------------------------|
| Lightweight             | Heavyweight                 |
| Share host OS kernel    | Each VM has its own OS      |
| Faster startup time     | Slower startup time         |
| Less resource overhead  | Higher resource overhead    |
| Greater scalability     | Less scalability            |

# (3) Install Docker Locally

## Use this Link to Download : https://www.docker.com/products/docker-desktop/ 

# (4) Images Vs Containers
Images: Blueprints for containers. They contain everything needed to run an application, including code, runtime, libraries, and dependencies.
Containers: Running instances of images. They encapsulate an application and its environment, isolated from other containers and the host system.


# (5) Public and Private Registries
## Public Registries:
   - ### Repositories where Docker images are stored and can be accessed by anyone. Examples include Docker Hub and Google Container Registry.
## Private Registries:
   - ### Repositories for storing Docker images privately within an organization. They provide control over access and distribution of images.