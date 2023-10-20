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

### Backend (Django) - Need Python version less than 3.9

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
   Note: Use `python3` instead of `python` if your default Python version is Python 2.x.

4. Activate the virtual environment:
   - On Windows: `env\Scripts\activate`
   - On macOS and Linux: `source env/bin/activate`

5. Install the required packages:
   - On macOS and Linux:
   ```bash
   pip install -r requirements.txt
   ```
   - On Windows:
   ```
   python -m pip install -r requirements.txt
   ```
   Note: Use `pip3` instead of `pip` if you are using Python 3 and have both Python 2 and Python 3 installed.

6. Navigate to the directory where manage.py is located:
   ```bash
   cd crm
   ```

7. Run migrations:
   ```bash
   python manage.py migrate
   ```
   Note: Use `python3` instead of `python` if your default Python version is Python 2.x.

8. Start the Django server:
   ```bash
   python manage.py runserver
   ```
   Note: Use `python3` instead of `python` if your default Python version is Python 2.x.

## Usage

1. Open and running two terminal at the same time, one for back-end server and one for front-end.
2. For back-end terminal `python manage.py runserver`, for front-end terminal `npm start`.
3. Open your browser and navigate to `http://localhost:3000` to access the frontend.
4. The backend API can be accessed at `http://localhost:8000`.

## Test Plan

| ID | Role | Action | Goal | Pass Criteria | Fail Criteria |
|----|------|--------|------|---------------|---------------|
| 1  | New user | Sign up | Sign up by filling first name, last name, email and password, and have an account | The page will go to the login page. | There will be a Sign Up Warning pop-up window containing the message That email format is invalid. Try another. |
| 2  | User who forgot password | Reset my password through email | Log in again | Successfully get the verification code from email, and be able to reset the password. The new password will be hashed first and then stored into the database. | Couldn’t get the verification code from email. |
| 3  | User | Log in to the CRM by email and password | Enter the CRM system | The page jumps to profile page. | A message in red font will pop up on the page, Please ensure your Email or Password is correct and retry again!. |
| 4  | User | Update my profile | Change my personal information including first name, last name, date of birth, address, phone number and   profile picture | The updated information is displayed correctly on the profile page. | The updated information is not displayed on the profile page. |
| 5  | User | Reset my password in profile page | Reset my password by inputting my old password in profile page after logging in | The old password matches the input and responds: "Password matches!". The new password will be hashed first and then stored into the database. | The old password does not match the input and responds: "Password does not match.".  OR The new password is the same as the old one and responds: "Password is the same.". |
| 6  | User | Log out on profile page | Log out the CRM system | Successfully log out and return to the log in page. | There will be error with 400_BAD_REQUEST. |
| 7  | User | Filter/search by tag on contact page | provide efficient organization and retrieval of contacts based on specific categories or attributes | Return correct contacts after filtering/searching by tag | Wrong contacts returned after filtering/searching by tag |
| 8  | User | Pop up window for notes on dashboard page | Write some quick notes | After entering some notes, click the save button and the notes are saved successfully. | After entering some notes and clicking the save button, the notes were not saved. |
| 9  | User | Add/delete/edit events on calendar page | Enable efficient scheduling and tracking of events | After creating an event, it is successfully displayed on the calendar. Moreover, it is able to edit and delete these events or meetings. | After creating an event, it does not appear on the calendar. Or, there is no response after editing and deleting these events or meeting. |
| 10 | User | Add/Delete/Edit cards of todo list, in progress list and completed list on Trello Board | Facilitate task management, allowing users to prioritize and track progress | Add/remove/edit cards of to-do lists, in-progress lists, and completed lists all react correctly. | Add/remove/edit cards of to-do lists, in-progress lists, and completed lists  react incorrectly. |
| 11 | User | Create/read/update/delete tags of contacts on contact page | help in better organization and categorization of contacts based on custom labels | Tags react normally after creating/reading/updating/deleting contact tags | Tags not reacting correctly after creating/reading/updating/deleting contact tags |
| 12 | User | Create/read/update/delete contacts on contact page | Maintaining an updated database of clients, partners, and other contacts. | React normally after after create/read/update/delete contacts | Not reacting correctly after create/read/update/delete contacts |
| 13 | User | Select contacts by several categories on contact page | Enable users to view contacts based on different criteria, facilitating quicker access and better organization. | The contacts displayed correspond to the selected category | The displayed contact does not correspond to the selected category |
| 14 | User | Get a list of contacts whose birthday is today | Allow users to send personalized greetings or offers, enhancing customer relations. | Contacts whose birthday today is displayed on the dashboard page | Contacts whose birthday today is not displayed on the dashboard page |

### Test Cases

| ID | Functional | Test Name | Test Steps | Excepted |
|----|------------|----------|------------|----------|
| 1  | Create account | Create success | Enter first name, last name, valid and not registered email, valid password, Click Create an account | Successfully create |
|    | Create account | Create account with a invalid or registered email | Enter first name, last name, invalid or registered email, valid password, Click Create an account | A Sign Up Warning pop-up window appears showing That email format is invalid. Try another. |
|    | Create account | Create account with a invalid password | Enter first name, last name, valid and not registered email, invalid password, Click Create an account | The password bar turns red. The message "Password is made up of more than six digits of numbers, letters, symbols" is displayed. |
| 2  | Forgot password | Reset password through email | Click Forgot password, Enter email address, Click Get Code, Enter received code, Enter new valid password, Re-enter new valid password, Click Reset | Successfully reset password |
|    | Forgot password | Reset password with wrong code | Click Forgot password, Enter email address, Click Get Code, Enter wrong code, Enter new invalid password, Re-enter new invalid password, Click Reset | Reset password failure. The pop-up window displays "The verification code you entered is incorrect. Please try again." |
| 3  | Sign-in | Sign-in success | Enter a valid Email, Enter a valid Password, Click Login | Successfully Logged in |
|    | Sign-in | Sign in with an incorrect password | Enter a valid Email, Enter a invalid Password, Click Login | User are redirected to the login page with a message Please ensure your Email or Password is correct and retry again! |
| 4  | Profile updating | Update success | Click Edit, Change the personal information including name, date of birth, address, phone number and profile picture, Click Save | Successfully update |
| 5  | Reset password on profile page | Reset password success | Enter current password and it matches, Input new password and it is not same with the old password, Re-write the password again, Click Confirm | Successfully reset password |
|    | Reset password on profile page | new password same with old password | Enter current password and it matches, Enter new password and it is same with the old password, Re-write the password again, Click Confirm | Reset password failure |
|    | Reset password in profile page | Input current password but it doesn't matches | Enter current password but it doesn‘t matches, Enter new password, Re-write the password again, Click Confirm | Reset password failure |
| 6  | Logout on profile page | Logout success | Click Logout | Successfully Logout |
| 7  | Filter/search by tag on contact page | Filter/search by tag | Click FILTERS/Search, Enter tag | Successfully Filter/search |
| 8  | Pop up window for writing notes on dashboard page | Note saved successfully | Click pop up window, Enter notes, Click save | Save successfully |
| 9  | Add events on calendar page | Add events successfully | Click Create Event, Enter or Select information you want, Click Save | Add successfully |
|    | Edit events on calendar page | Edit events successfully | Click existed event, Click Edit Event, Enter or Select information you want, Click Save Changes | Edit successfully |
|    | Delete events on calendar page | Delete events successfully | Click existed event, Click Delete Event | Delete successfully |
| 10 | Add cards of todo list, in progress list and completed list on Trello Board | Add cards of todo list, in progress list and completed list successfully | Click Add a card, Enter information, Click Save Changes | Add successfully |
|    | Edit cards of todo list, in progress list and completed list on Trello Board | Edit cards of todo list, in progress list and completed list successfully | Click existed card, Change information, Click Save Changes | Edit successfully |
|    | Delete cards of todo list, in progress list and completed list on Trello Board | Delete cards of todo list, in progress list and completed list successfully | Click the trash can in the upper right corner of the existing card | Delete successfully |
| 11 | Create tags of contacts | Create tag successfully | Click +Add Tag, Enter information, Press Enter key, Click Save Changes | Create successfully |
|    | Read tags of contacts | Read tag successfully | Click Tag(or +Add Tag) of contact | Read successfully |
|    | Update tags of contacts | Update tag successfully | Click Tag(or +Add Tag), Enter information, Press Enter key, Click Save Changes | Update successfully |
|    | Delete tags of contacts | Delete tag successfully | Click Tag, Click X of the tag, Click Save Changes | Delete successfully |
| 12 | Create contacts on contact page | Create contact by email successfully | Click Add a Contact, Click Add by Email, Enter valid email, Click ADD | Create successfully |
|    | Create contacts on contact page | Create contact by manually successfully | Click Add a Contact, Click Add by Manually, Enter information, Click Save | Create successfully |
|    | Read contacts on contact page | Read contact successfully | Click existed contact’s name | Read successfully |
|    | Update contacts on contact page | Update contact successfully | Click existed contact’s name, Click Edit, Change information, Click Save, Click Cancel to exit | Update successfully |
|    | Delete contacts on contact page | Delete contact successfully | Click on the frontmost box of the contact you want to delete, Click DELETE, Click DELETE | Delete successfully |
| 13 | Select contacts by several categories on contact page | Select contacts by several categories successfully | Click COLUMNS, Click categories | Select contacts by several categories successfully |
| 14 | Get a list of contacts whose birthday is today | Successful display of contacts who have birthdays today | Click Dashboard | Successful display of contacts who have birthdays today |


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

