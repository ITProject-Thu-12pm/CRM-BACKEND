# Personal CRM - MyCircle

Welcome to MyCircle, a user-friendly Personal CRM built with Django and React.js. With MyCircle, you can manage your contacts, track interactions, and never miss a follow-up.

## Features

- **Contact Management**: Seamlessly add, edit, and delete contacts.
- **Interaction Tracking**: Keep a log of all your interactions - meetings, calls, emails, and more.
- **Calendar Integration**: Set remindar for follow-ups or important dates on your own calendar。
- **Task Management**: Use the Trello-like board to manage notes and prioritize tasks.
- **Responsive UI**: Enjoy a modern and responsive interface built with React.js.

## Prerequisites

Ensure you have the following installed on your local machine:

- Python (3.8 or newer)
- Node.js (14.0 or newer)
- npm

## Setup & Installation

### Frontend (Javascript)

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ITProject-Thu-12pm/CRM-Web.git
   ```

2. Navigate to the frontend directory:
   ```bash
   cd CRM-Web
   ```

3. Install the required packages:
   ```bash
   npm install
   ```

4. Start the React development server:
   ```bash
   npm start
   ```
   Open http://localhost:3000 to view it in your browser.

### Backend (Django)

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ITProject-Thu-12pm/CRM-BACKEND.git
   ```

2. Navigate to the backend directory:
   ```bash
   cd CRM-BACKEND
   ```

3. Create a virtual environment:
   ```bash
   python -m venv env
   ```
   Note: Use python3 instead of python if your default Python version is Python 2.x.

4. Activate the virtual environment:
   - On Windows: `env\Scripts\activate`
   - On macOS and Linux: `source env/bin/activate`

5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

6. Navigate to the directory where manage.py is located:
   ```bash
   cd crm
   ```

7. Connect to the Testing MongoDB Atlas Database:

   Before migrating and running the server, you need to connect to our MongoDB Atlas testing database:

   - Download and install MongoDB Compass if you haven't already.

   - Open MongoDB Compass and connect using the following connection string:
   ```bash
   mongodb+srv://it_project:crm@cluster0.noh4ktd.mongodb.net/
   ```
   - Once connected, you can view and interact with the test database collections.

8. Run migrations:
   ```bash
   python manage.py migrate
   ```
   Note: Use python3 instead of python if your default Python version is Python 2.x.

9. Start the Django server:
   ```bash
   python manage.py runserver
   ```
   Note: Use python3 instead of python if your default Python version is Python 2.x.

## Usage

1. Open your browser and navigate to `http://localhost:3000` to access the frontend.
2. The backend API can be accessed at `http://localhost:8000`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

