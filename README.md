# 📊 Business Management System (BMS)

A comprehensive web-based Business Management System built with Django to manage customers, products, and orders efficiently. This system provides a clean, user-friendly interface for small to medium-sized businesses to track their operations. 

## 🔐 Admin login credentials

- **Username:** `Admin001`
- **Password:** `password@123`

## ✨ Features

### 🔐 Authentication System
- Secure user login and logout
- Session-based authentication
- Protected routes requiring authentication

### 👥 Customer Management
- Add, view, edit, and delete customer records
- Store customer information (name, phone, email)
- Unique phone and email validation
- Track customer creation dates

### 📦 Product Management
- Maintain product catalog
- Track product pricing and stock levels
- Add, update, and remove products
- Real-time stock monitoring

### 🛒 Order Management
- Create and manage customer orders
- Add multiple products to a single order
- Automatic total calculation
- Order history tracking
- View order details with itemized breakdown

### 📈 Dashboard
- Overview of business operations
- Quick access to all modules
- User-friendly navigation

## 🛠️ Technology Stack

- **Framework**: Django 5.0.1
- **Database**: PostgreSQL (Production)
- **Frontend**: Bootstrap 5.0 +
- **Deployment**: Vercel
- **Static Files**: WhiteNoise
- **Server**: Gunicorn

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.12 or higher
- pip (Python package manager)
- Git
- PostgreSQL

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd mini-business-system
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Database Setup
```bash
# Run migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
```

### 6. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.


## 🌐 Deployment

### Vercel Deployment

1. **Install Vercel CLI** (optional):
```bash
npm i -g vercel
```

2. **Configure Environment Variables** in Vercel Dashboard:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: False
   - `DATABASE_URL`: Your PostgreSQL connection string
   - `ALLOWED_HOSTS`: Your Vercel domain

## 🔒 Security Features

- CSRF protection enabled
- Secure password validation
- Session-based authentication
- SSL redirect in production
- Secure cookies in production
- XSS filtering
- Content type sniffing protection

## 🎨 User Interface

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Bootstrap 5**: Modern, clean interface
- **Centered Login**: Professional authentication page
- **Navigation Bar**: Easy access to all modules
- **Alert Messages**: User feedback for actions

## 📝 Usage Guide

### Adding a Customer
1. Navigate to Customers section
2. Click "Add Customer"
3. Fill in name, phone, and email
4. Submit the form

### Creating an Order
1. Go to Orders section
2. Click "Create Order"
3. Select a customer
4. Add products with quantities
5. System automatically calculates total
6. Submit to create order

### Managing Products
1. Access Products section
2. Add new products with name, price, and stock
3. Edit existing products
4. Monitor stock levels

## 👨‍💻 Author

**Nawin**

