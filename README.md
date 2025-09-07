# README.md

```markdown
# Micro-Demo — Simple Microservices with Docker Compose

This project demonstrates how to build **two microservices** (Account & Inventory), **containerize** them with Docker, and run them together behind a simple **NGINX gateway** using `docker-compose`.

---

## 📂 Project Structure
```

micro-demo/
├─ account/
│  ├─ app.py
│  └─ Dockerfile
├─ inventory/
│  ├─ app.py
│  └─ Dockerfile
├─ gateway/
│  └─ nginx.conf
└─ docker-compose.yml

````

---

## 🚀 Quick Start

### 1. Build the images
```bash
docker-compose build
````

### 2. Start the services

```bash
docker-compose up -d
```

### 3. Test endpoints

```bash
curl http://localhost:8080/                        # → gateway ok
curl http://localhost:8080/account/api/v1/users    # → list of users
curl http://localhost:8080/inventory/api/v1/products  # → list of products
```

---

## 🛠️ Useful Commands

* View running containers:

  ```bash
  docker ps
  ```

* Follow logs:

  ```bash
  docker-compose logs -f
  ```

* Stop services:

  ```bash
  docker-compose down
  ```

* Stop & remove everything (containers, images, networks):

  ```bash
  docker-compose down --rmi local
  ```

* Rebuild after code changes:

  ```bash
  docker-compose build
  docker-compose up -d
  ```

---

## 📖 How it Works

1. **Account Service** → Flask app exposes `/api/v1/users`.
2. **Inventory Service** → Flask app exposes `/api/v1/products`.
3. **NGINX Gateway** → Acts as an API Gateway:

   * `/account/*` → routes to account service
   * `/inventory/*` → routes to inventory service
4. **docker-compose** → Orchestrates all containers on a shared network.
5. Clients only talk to **gateway (port 8080)**, which forwards requests to services.

---

## ⚡ Troubleshooting

* **Port 8080 already in use** → change the port in `docker-compose.yml` (`"8081:80"`).
* **Gateway returns 502** → check if `account` and `inventory` containers are running (`docker ps`).
* **Code changes not reflected** → rebuild containers:

  ```bash
  docker-compose build
  docker-compose up -d
  ```

---

## 🧹 Cleanup

To remove everything:

```bash
docker-compose down --rmi local
```

---

