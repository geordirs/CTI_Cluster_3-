# Multiplatform Ecommerce
This project is a complete e-commerce solution, including a web application and a mobile application, using modern technologies and following best development practices.

#### Main Technologies

- **Backend:** Python (FastAPI)
- **Web Frontend:** Svelte
- **Database:** PostgreSQL
- **Styles:** TailwindCSS
- **Version Control:** Git
- **Hosting:** Vercel (frontend) and railway.app (backend)

#### Project Structure

```
ecommerce/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── routes/
│   │   ├── stores/
│   │   └── App.svelte
│   ├── public/
│   └── package.json
├── docker-compose.yml
└── README.md
```

#### Development Environment Setup

Clone the repository:

```bash
git clone https://github.com/your-username/ecommerce-project.git
cd ecommerce-project
```

Set up the backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Set up the frontend:
```bash
cd ../frontend
npm install
```

Set up the mobile application:
```bash
cd ../mobile
npm install
```

Running the Project
Backend:
```bash
cd backend
uvicorn app.main:app --reload
```

Web Frontend:
```bash
cd frontend
npm run dev
```

Git Workflow
Create a new branch for each feature:
```bash
git checkout -b feature/new-feature
```

Make frequent and descriptive commits:
```bash
git add .
git commit -m "Add shopping cart functionality"
```

Push the branch and create a Pull Request on GitHub:
```bash
git push origin feature/new-feature
```

After review, merge with the main branch.

#### Deployment
- **Frontend:** Automatically deployed to GitHub Pages with each push to the main branch.
- **Backend:** Deployed on Heroku via CI/CD configured in `.github/workflows/deploy.yml`.

#### Ecommerce Features
- **Product catalog with search and filters**
- **Shopping cart**
- **Authentication system (registration, login, logout)**
- **Admin panel (CRUD of products)**
- **Payment process (integration with payment gateway)**
- **User profile and order history**

#### Innovative Idea: Sustainable Products Marketplace
Focus your e-commerce on sustainable and eco-friendly products. Include features like:

- **Carbon footprint calculation for each product**
- **Reward system for sustainable choices**
- **Community to share sustainable lifestyle tips**
- **Educational section on sustainability**
- **Option to offset carbon emissions with each purchase**

This idea is not only relevant today but also has growth potential and can attract conscious consumers.
