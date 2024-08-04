# Multiplatform Ecommerce

This project is a unified ecommerce solution that works as a web, mobile, and desktop application.

## Project Structure

ecommerce-multiplatform/
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── main.py
│ │ ├── models.py
│ │ └── routes/
│ ├── tests/
│ └── requirements.txt
├── frontend/
│ ├── src/
│ │ ├── routes/
│ │ ├── lib/
│ │ └── app.html
│ ├── static/
│ └── svelte.config.js
├── database/
│ └── schema.sql
├── .gitignore
└── README.md



## Technologies Used

- **Backend:** Python with FastAPI
- **Database:** SQLite (development) / PostgreSQL (production)
- **Frontend:** Svelte with SvelteKit
- **Styling:** Tailwind CSS
- **Deployment:** GitHub Pages (web), Capacitor (mobile and desktop)

## Development Environment Setup

1. Install Python 3.8+
2. Install Node.js 14+

### Install backend dependencies:

```sh
cd backend
pip install -r requirements.txt
```

#Install frontend dependencies:

```sh
cd frontend
npm install
```

Running the Project
Start the backend:

```sh
cd backend
uvicorn app.main:app --reload
```

Start the frontend:

```sh
cd frontend
npm run dev
```

Start the frontend:

```sh
cd frontend
npm run dev
```
Open your browser at http://localhost:5000


