# Personal CRM - MyCircle

A simple and intuitive Personal CRM built using Django and React.js. Manage your contacts and calendar, keep track of interactions, and never miss a follow-up.

## Features

- **Contact Management**: Add, edit, and delete contacts with ease.
- **Interaction Tracking**: Log interactions with your contacts, be it meetings, calls, or emails.
- **Calendar**: Set remindar for follow-ups or important dates on your own calendar。
- **Trello Board**: Manage notes for important things according to their priorities (low, medium, high).
- **Responsive UI**: A modern and responsive interface built with React.js.

## Prerequisites

- Python (3.8 or newer)
- Node.js (14.0 or newer)
- npm or yarn

## Setup & Installation

### Backend (Django)

1. Navigate to the backend directory:
   ```bash
   cd CRM-BACKEND
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:
   - On Windows: `env\Scripts\activate`
   - On macOS and Linux: `source env/bin/activate`

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the Django server:
   ```bash
   python manage.py runserver
   ```

### Frontend (React.js)

1. Navigate to the frontend directory:
   ```bash
   cd CRM-Web
   ```

2. Install the required packages:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

## Usage

1. Open your browser and navigate to `http://localhost:3000` to access the frontend.
2. The backend API can be accessed at `http://localhost:8000`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

