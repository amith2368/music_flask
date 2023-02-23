# Music-Flask Application Installation Guide
This guide will take you through the steps required to install a Flask application on your local machine.

## Prerequisites
Before installing the Flask application, you need to ensure that the following software is installed on your machine:

- Python 3.x (recommended version 3.6 or above)
- pip (Python package manager)
You can check if Python and pip are installed by running the following commands in your terminal:

```bash
python --version
pip --version
```

If these commands are not recognized, you will need to install Python and pip on your machine before proceeding. You can download Python from the official website here. Pip should be included with your Python installation.


## Installation
Once you have confirmed that Python and pip are installed on your machine, follow the steps below to install the Flask application:

Clone the application repository to your local machine using the following command in your terminal:

```bash
git clone https://github.com/amith2368/music_flask.git
```

Navigate to the application directory using the following command:

```bash
cd <application-directory>
```

Create a virtual environment for the application using the following command:

```bash
python3 -m venv venv
```

Activate the virtual environment using the following command:

```bash
source venv/bin/activate
```

Install the required packages for the application using the following command:
```bash
pip install -r requirements.txt
```

Set the Flask application environment variable using the following command:

```bash
export FLASK_APP=app.py
```

Start the application using the following command:

```bash
flask run
```

Open your web browser and go to the following URL to access the application:

```bash
http://localhost:5000/
```

Congratulations! You have successfully installed the Flask application on your local machine. If you encounter any issues during the installation process, please open an issue for further clarification.