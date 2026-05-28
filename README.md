# sistema_de_gesti-n_de_leads
markdown# 🧑‍💼 Sistema de Gestión de Leads

Aplicación full-stack que genera y muestra una lista de 10 personas con datos ficticios, consumiendo la [RandomUser API](https://randomuser.me/documentation).

---

## 🏗️ Arquitectura
RandomUser API (https://randomuser.me)
↓
Backend — Python + FastAPI  →  http://localhost:3000
↓
Frontend — Angular          →  http://localhost:4200

---

## 📁 Estructura del proyecto
sistema_de_gesti-n_de_leads/
├── backend/
│   ├── app/
│   │   ├── init.py
│   │   ├── main.py
│   │   ├── models/
│   │   │   ├── init.py
│   │   │   └── person.py
│   │   ├── routers/
│   │   │   ├── init.py
│   │   │   └── persons.py
│   │   └── services/
│   │       ├── init.py
│   │       └── randomuser_service.py
│   ├── venv/
│   ├── requirements.txt
│   └── .env
└── frontend/
├── src/
│   ├── app/
│   │   ├── components/persons-list/
│   │   ├── models/
│   │   ├── services/
│   │   └── app.config.ts
│   └── environments/
│       ├── environment.ts
│       └── environment.prod.ts
└── angular.json

---

## ⚙️ Requisitos previos

- Python 3.10+
- Node.js 18+
- Angular CLI 17+

---

## 🚀 Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/sihomaramipc20223-tech/sistema_de_gesti-n_de_leads.git
cd sistema_de_gesti-n_de_leads
```

---

### 2. Backend — FastAPI

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

✅ API disponible en: `http://localhost:3000`
📄 Documentación Swagger: `http://localhost:3000/docs`
📄 Documentación ReDoc: `http://localhost:3000/redoc`

---

### 3. Frontend — Angular

Abre una segunda terminal:

```bash
# Entrar a la carpeta
cd frontend

# Instalar dependencias
npm install

# Ejecutar la aplicación
ng serve
```

✅ Aplicación disponible en: `http://localhost:4200`

---

## 🔌 Endpoints del backend

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/` | Health check |
| `GET` | `/api/persons/` | Lista de 10 personas |
| `GET` | `/api/persons/{cantidad}` | Lista de N personas (1–50) |
| `GET` | `/docs` | Swagger UI interactivo |
| `GET` | `/redoc` | Documentación ReDoc |

---

## 📦 Dependencias

### Backend (`requirements.txt`)
fastapi==0.115.5
uvicorn==0.32.1
httpx==0.27.2
python-dotenv==1.0.1
pydantic==2.10.3

### Frontend (`package.json`)
- Angular 19
- TypeScript
- SCSS

---

## 🌐 Fuente de datos

Los datos de personas son generados por **[RandomUser API](https://randomuser.me/documentation)**:
https://randomuser.me/api/?results=10&inc=name,gender,location,email,dob,picture

Cada persona incluye: nombre, género, ubicación, correo, fecha de nacimiento y fotografía.

---

## 📋 Variables de entorno

Crea un archivo `.env` dentro de `/backend`:

```env
PORT=3000
```

---

## ▶️ Ejecución rápida (resumen)

```bash
# Terminal 1 — Backend
cd backend && source venv/Scripts/activate && uvicorn app.main:app --reload --port 3000

# Terminal 2 — Frontend
cd frontend && ng serve
```

Abre `http://localhost:4200` en el navegador. 🎉
