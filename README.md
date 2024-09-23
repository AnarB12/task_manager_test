# **Task Manager Web App**

This is a simple task management web app created using **Flask**. It's a practice project since I have just started working on these kinds of web projects and want to learn more. My goal is to understand the basics of building web apps, handling user logins, and managing data like tasks.

## **Features**

- **User Registration and Login**: Users can create an account and log in.
- **Task Management**: Users can add, edit, delete, and view tasks.
- **Mark Tasks as Completed**: You can check off tasks as "completed."
- **Search**: There's a search feature to look for tasks based on titles or descriptions.
- **Simple UI**: The interface is built with Bootstrap for a clean look.

## **Technologies Used**

- **Python**: For the server-side code.
- **Flask**: A simple web framework for building web apps.
- **SQLite**: For storing tasks and user data locally.
- **Bootstrap**: For making the web pages look better with responsive design.

## **Installation**

### **1. Prerequisites**

Make sure you have **Conda** installed and set up on your machine.

### **2. Set Up the Project**

1. **Clone the repository**:

    ```bash
    git clone https://github.com/AnarB12/task-manager.git
    cd task-manager
    ```

2. **Create and activate a Conda environment**:

    ```bash
    conda create -n task_manager_env python=3.10
    conda activate task_manager_env
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the application**:

    ```bash
    python run.py
    ```

6. **Access the app**:  
    Go to `http://localhost:5000` in your web browser.

## **Project Structure**

```bash
task_manager_test/
├── app/
│   ├── __init__.py
│   ├── auth_routes.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   └── templates/
├── migrations/
├── .env
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

## **What I’ve Learned**

This project helped me practice:

- Creating user accounts and logging in/out with Flask.
- Managing tasks (create, edit, delete) in a database.
- Building simple web pages and layouts with Bootstrap.
- Using forms to submit data and process it in Python.
  
## **Weaknesses / What's Missing**

Since this is just a practice project, there are a few things that were **not included**:

- **Security**: This app does not include advanced security like password recovery or multi-factor authentication. I’m focusing on the basics.
- **Error Handling**: Some parts of the app might not have full error messages or user-friendly notifications.
- **No Advanced Features**: Things like push notifications, file uploads, or more complex task management (like recurring tasks) are not included.
- **Only Local Data**: The data is stored on the local machine using SQLite, so if you delete the app files, the tasks will be lost. There is no online or cloud storage.
