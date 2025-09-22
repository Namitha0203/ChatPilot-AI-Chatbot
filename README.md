**Prerequisites**

Python 3.10+
PostgreSQL or SQLite
Git
Virtualenv (recommended)

**Setup Steps**
bash
# Clone the repo
git clone https://github.com/Namitha0203/ChatPilot-AI-Chatbot.git
cd ChatPilot-AI-Chatbot

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set environment variable
export DJANGO_SETTINGS_MODULE=chatpilot.settings

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start the server
python manage.py runserver
