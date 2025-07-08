# Personal Budget Tracker 💰

A clean, modern Django web application for tracking personal income and expenses with an intuitive dashboard and comprehensive transaction management.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-v4.0+-green.svg)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-v3.0+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- **Dashboard Overview**: Quick summary of total income, expenses, and net balance
- **Transaction Management**: Add, view, filter, and delete income/expense transactions
- **Category System**: Create and manage custom categories for better organization
- **Responsive Design**: Modern UI built with Tailwind CSS that works on all devices
- **Filtering & Search**: Filter transactions by type and category
- **Recent Activity**: View latest transactions at a glance
- **Admin Panel**: Full Django admin integration for advanced management

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/personal-budget-tracker.git
   cd personal-budget-tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv budget_env
   source budget_env/bin/activate  # On Windows: budget_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser** and navigate to `http://127.0.0.1:8000`


## 🛠️ Technology Stack

- **Backend**: Django 4.x
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Database**: SQLite (default), easily configurable for PostgreSQL/MySQL
- **Styling**: Tailwind CSS with Inter font family
- **Icons**: Custom styling with responsive design

## 📁 Project Structure

```
personal-budget-tracker/
├── budget/                 # Main budget app
│   ├── models.py          # Database models (Transaction, Category)
│   ├── views.py           # View logic and controllers
│   ├── forms.py           # Django forms for user input
│   ├── urls.py            # URL routing for budget app
│   ├── admin.py           # Django admin configuration
│   └── templates/budget/  # HTML templates
├── personalsite/          # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI configuration
├── manage.py              # Django management script
└── README.md              # This file
```

## 💾 Database Models

### Transaction Model
- `type`: Income ('IN') or Expense ('EX')
- `amount`: Decimal field for transaction amount
- `date`: Transaction date (defaults to current date)
- `category`: Foreign key to Category model
- `description`: Text description of the transaction

### Category Model
- `name`: Unique category name for organizing transactions

## 🎯 Usage

### Adding Transactions
1. Click "Add Transaction" in the navigation
2. Select transaction type (Income/Expense)
3. Enter amount, date, category, and description
4. Save to record the transaction

### Managing Categories
1. Navigate to "Categories" page
2. Add new categories using the form
3. Edit or delete existing categories as needed

### Filtering Transactions
1. Go to "Transactions" page
2. Use the filter form to narrow results by type or category
3. Click "Reset" to clear all filters

## ⚙️ Configuration

### Database Configuration
The app uses SQLite by default. To use PostgreSQL or MySQL, update the `DATABASES` setting in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Security Settings
**Important**: Before deploying to production:
1. Change the `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS` with your domain
4. Configure proper database settings

## 🚀 Deployment

### Basic Deployment Steps
1. Set environment variables for production
2. Configure static files collection
3. Set up a production database
4. Use a WSGI server like Gunicorn
5. Configure reverse proxy (Nginx recommended)

### Environment Variables
Consider using environment variables for sensitive settings:
- `SECRET_KEY`
- `DEBUG`
- Database credentials
- `ALLOWED_HOSTS`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/personal-budget-tracker/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the issue

## 🎯 Future Enhancements

- [ ] Monthly/yearly budget planning
- [ ] Data visualization with charts and graphs
- [ ] Export functionality (CSV, PDF)
- [ ] Mobile app version
- [ ] Multi-currency support
- [ ] Recurring transaction templates
- [ ] Email notifications and reports
- [ ] Data backup and restore features

---

⭐ If you found this project helpful, please consider giving it a star!
