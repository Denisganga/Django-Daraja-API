# Django STK Push Integration

## overview

This Django application demonstrates the integration of Safaricom's M-Pesa Daraja API to initiate an STK Push. STK (Sim Toolkit) Push is a feature provided by Safaricom that allows merchants to initiate M-Pesa transactions on behalf of customers.

# Requirements
Python (version 3.11.7)
Django (version 3.2.20)
Django-daraja(version 2.0)

Installation

### 1) Clone the repository:

```bash

git clone https://github.com/denisganga/django-daraja-API.git
cd django-daraja-API
```

### 2) Create a virtual environment:

```bash

python -m venv venv

```

### 3) Activate the virtual environment:

    On Linux/macOS:

```bash

source venv/bin/activate
```

On Windows:

```bash

    .\venv\Scripts\activate
```

### 4) Install dependencies:

```bash

pip install -r requirements.txt
```
### 5) Set up environment variables:

   setup your credentials from your developer account



### 6) Run migrations:

```bash

python manage.py migrate
```

### 7) Run the development server:

```bash

    python manage.py runserver
```

### 8) Usage

    Access the application at http://localhost:8000/index/.



Acknowledgments

    Safaricom due to Django Daraja library for M-Pesa integration.
