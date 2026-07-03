# 🚀 Flask Progressive Delivery Platform on Amazon EKS

> Enterprise-grade GitOps Progressive Delivery demonstration using Argo Rollouts, Argo CD, Helm, Prometheus, Grafana, GitHub Actions, and Amazon EKS.

![Platform](https://img.shields.io/badge/Platform-AWS-orange)
![Kubernetes](https://img.shields.io/badge/Kubernetes-EKS-blue)
![GitOps](https://img.shields.io/badge/GitOps-ArgoCD-red)
![Progressive Delivery](https://img.shields.io/badge/Progressive%20Delivery-Argo%20Rollouts-success)
![Helm](https://img.shields.io/badge/Helm-v3-blueviolet)
![Terraform](https://img.shields.io/badge/Terraform-IaC-623CE4)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-orange)
![Grafana](https://img.shields.io/badge/Visualization-Grafana-F46800)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF)

---

# 📖 Overview

This repository demonstrates an **enterprise-grade GitOps Progressive Delivery platform** deployed on **Amazon EKS**.

The project showcases how modern DevOps teams safely release new application versions using **Argo Rollouts Canary Deployments** with **automated rollback** based on **Prometheus metrics**.

Instead of deploying directly to production, new application versions are released gradually while continuously monitoring application health. If the error rate exceeds the configured threshold, Argo Rollouts automatically aborts the rollout and restores the previous stable version.

The infrastructure required to run this application—including Amazon EKS, networking, IAM, GitHub OIDC, monitoring, ingress, and platform add-ons—is managed in a **separate Platform repository** using Terraform.

---

# 🎯 Project Objectives

- Demonstrate Enterprise GitOps workflows
- Implement Progressive Delivery using Argo Rollouts
- Automate Canary Deployments
- Perform Metric-Based Automated Rollback
- Integrate Prometheus Monitoring
- Visualize Metrics with Grafana
- Build CI/CD using GitHub Actions
- Store container images in Amazon ECR
- Deploy applications using Helm and Argo CD
- Follow Kubernetes production best practices

---

# 🏗 Repository Architecture

This project intentionally separates **Platform Engineering** and **Application Delivery** responsibilities.

## Platform Repository

Responsible for provisioning and managing the Kubernetes platform.

Features include:

- Terraform Infrastructure
- Amazon VPC
- Amazon EKS
- IAM Roles
- GitHub OIDC
- NGINX Ingress Controller
- Prometheus Stack
- Grafana
- Metrics Server
- Argo CD
- Argo Rollouts

---

## Application Repository (This Repository)

Responsible for application delivery.

Features include:

- Flask Application
- Docker
- Helm Chart
- GitHub Actions CI
- GitHub Actions CD
- Amazon ECR Image Publishing
- GitOps Deployment
- Canary Rollouts
- Automated Rollback
- Prometheus Metrics
- Grafana Dashboards

---

# ⭐ Key Features

- Enterprise Flask Application
- Dockerized Deployment
- Amazon ECR Integration
- Helm-Based Kubernetes Deployment
- GitOps with Argo CD
- Progressive Delivery with Argo Rollouts
- Canary Deployment Strategy
- Automated Rollback
- Prometheus Monitoring
- Grafana Dashboards
- ServiceMonitor Integration
- GitHub Actions CI/CD
- Security Scanning using Trivy
- Non-Root Docker Container
- Production-Ready Helm Templates

---