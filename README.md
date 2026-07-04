# 🚀 Flask Progressive Delivery Demo

> Enterprise-grade GitOps Progressive Delivery using **Argo CD**, **Argo Rollouts**, **GitHub Actions**, **Helm**, **Prometheus**, **Grafana**, and **Amazon EKS**.

![Python](https://img.shields.io/badge/Python-Flask-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-EKS-326CE5?logo=kubernetes)
![ArgoCD](https://img.shields.io/badge/GitOps-ArgoCD-EF7B4D)
![Rollouts](https://img.shields.io/badge/Progressive-Delivery-success)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C)
![Grafana](https://img.shields.io/badge/Visualization-Grafana-F46800)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

This repository demonstrates an enterprise-grade GitOps Progressive Delivery workflow on Amazon EKS.

The application is packaged with Helm, deployed using Argo CD, released progressively with Argo Rollouts, monitored using Prometheus, visualized with Grafana, and built automatically through GitHub Actions.

New versions are deployed as Canary Releases. During rollout, Prometheus continuously evaluates application metrics. If the configured threshold is violated, Argo Rollouts automatically aborts the deployment and restores the previous stable version.

---

# 🏗️ Architecture

<p align="center">
<img src="docs/Architecture.png" width="100%">
</p>

---

# 🎯 Features

- Flask REST API
- Dockerized Application
- Helm-based Kubernetes Deployment
- GitHub Actions CI/CD
- Amazon ECR Image Publishing
- GitOps with Argo CD
- Canary Deployments
- Automated Metric Analysis
- Automatic Rollback
- Prometheus Monitoring
- Grafana Dashboards
- Kubernetes ServiceMonitor

---

# 📂 Repository Structure

```text
flask-rollouts-demo/
├── .github/
├── app/
├── argocd/
├── docs/
├── helm/
├── Dockerfile
├── requirements.txt
├── run.py
├── VERSION
├── README.md
└── LICENSE
```

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python (Flask) |
| Containerization | Docker |
| Kubernetes | Amazon EKS |
| Helm | Helm |
| GitOps | Argo CD |
| Progressive Delivery | Argo Rollouts |
| Monitoring | Prometheus |
| Dashboards | Grafana |
| CI/CD | GitHub Actions |
| Registry | Amazon ECR |

---

# 📸 Screenshots

## Architecture

<img src="docs/Architecture.png" width="100%">

## Amazon EKS

<img src="docs/EKS.png" width="100%">

## GitHub Actions

<img src="docs/Githubactions.png" width="100%">

## Argo CD

<img src="docs/Argo CD.png" width="100%">

## Argo Rollouts

<img src="docs/Argo-rollout.png" width="100%">

## Rollout Analysis

<img src="docs/argo-rollout-1.png" width="100%">

---

# 👨‍💻 Author

**Murali Krishna**

Cloud & DevOps Engineer

AWS • Terraform • Kubernetes • Docker • GitHub Actions • Argo CD • Argo Rollouts • Prometheus • Grafana

---

# 📄 License

MIT License
