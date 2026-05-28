# 🧑‍💼 Sistema de Gestión de Leads

Aplicación full-stack que genera y muestra una lista de 10 personas con datos ficticios, consumiendo la [RandomUser API](https://randomuser.me/documentation).

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────┐
│     randomuser.me/api               │
│     Fuente de datos externos        │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│  Backend — Python + FastAPI         │
│  http://localhost:3000              │
│  http://localhost:3000/docs         │
└─────────────────┬───────────────────┘
                  │  REST API / JSON
                  ▼
┌─────────────────────────────────────┐
│  Frontend — Angular                 │
│  http://localhost:4200              │
└─────────────────────────────────────┘
```

---

## 📁 Estructura del proyecto

```
sistema_de_gesti-n_de_leads/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── person.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   └── persons.py
│   │   └── services/
│   │       ├── __init__.py
│   │       └── randomuser_service.py
│   ├── venv/
│   ├── requirements.txt
│   └── .env
└── frontend/
    ├── src/
    │   ├── app/
    │   │   ├── components/
    │   │   │   └── persons-list/
    │   │   ├── models/
    │   │   ├── services/
    │   │   └── app.config.ts
    │   └── environments/
    │       ├── environment.ts
    │       └── environment.prod.ts
    └── angular.json
```

---

## ⚙️ Requisitos previos

| Herramienta | Versión mínima |
|---|---|
| Python | 3.10+ |
| Node.js | 18+ |
| Angular CLI | 17+ |

---

## 🚀 Instalación y ejecución local

### 1 — Clonar el repositorio

```bash
git clone https://github.com/sihomaramipc20223-tech/sistema_de_gesti-n_de_leads.git
cd sistema_de_gesti-n_de_leads
```

---

### 2 — Backend (FastAPI)

```bash
# Entrar a la carpeta
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
source venv/Scripts/activate     # Windows Git Bash
venv\Scripts\activate            # Windows CMD
source venv/bin/activate         # Mac / Linux

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
uvicorn app.main:app --reload --port 3000
```

| URL | Descripción |
|---|---|
| `http://localhost:3000` | API principal |
| `http://localhost:3000/docs` | Swagger UI interactivo |
| `http://localhost:3000/redoc` | Documentación ReDoc |

---

### 3 — Frontend (Angular)

Abre una **segunda terminal**:

```bash
# Entrar a la carpeta
cd frontend

# Instalar dependencias
npm install

# Ejecutar la aplicación
ng serve
```

✅ Aplicación en: `http://localhost:4200`

---

## 🔌 Endpoints disponibles

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/` | Health check del servidor |
| `GET` | `/health` | Estado del servicio |
| `GET` | `/api/persons/` | Lista de 10 personas |
| `GET` | `/api/persons/{cantidad}` | N personas (máx. 50) |
| `GET` | `/docs` | Swagger UI |
| `GET` | `/redoc` | ReDoc |

---

## 📦 Dependencias

### Backend — `requirements.txt`

```
fastapi==0.115.5
uvicorn==0.32.1
httpx==0.27.2
python-dotenv==1.0.1
pydantic==2.10.3
```

### Frontend — `package.json`

```
Angular 19
TypeScript
SCSS
```

---

## 📋 Variables de entorno

Crea el archivo `backend/.env`:

```env
PORT=3000
```

---

## 🌐 Fuente de datos

Los datos son generados por **[RandomUser API](https://randomuser.me/documentation)**:

```
https://randomuser.me/api/?results=10&inc=name,gender,location,email,dob,picture
```

Cada persona incluye nombre, género, ubicación, correo, fecha de nacimiento y fotografía.

---

## ▶️ Ejecución rápida

```bash
# Terminal 1 — Backend
cd backend && source venv/Scripts/activate && uvicorn app.main:app --reload --port 3000

# Terminal 2 — Frontend
cd frontend && ng serve
```

Abre `http://localhost:4200` en tu navegador 🎉

---

*Desarrollado como parte del Bootcamp NTT Data — 2026*
