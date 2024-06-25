I had a simple repetitive task to accomplish and wanted to play with chatgpt. Everything in this repo and most of theis README was generated by it. Intended to be used with something like Uptime Kuma for notifications on low disk space.

# Disk Space Monitor Setup

This project provides a Flask application that sets up a disk space monitoring script on a remote server. The application takes user inputs through a web form and sets up a cron job on the remote server to monitor disk space usage.

## Features

- Web interface for inputting server details and URL to curl.
- Automatic creation of a disk space monitoring script on the remote server.
- Automatic setup of a cron job to run the script every 3 hours.
- Uses Material Design for a clean and modern interface.

## Prerequisites

- Python 3.x
- Flask
- sshpass

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/pete1450/DiskSpaceMonitorSetup.git
    cd disk-space-monitor-setup
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install Flask sshpass
    ```
4. Update app.py by replacing /dev/sdb1 with your disk mount and update the host at the bottom to your servers ip.

## Usage


1. Run the Flask application:

    ```bash
    python app.py
    ```
    
2. Open your web browser and go to `http://{serverip}:5000/`.

3. Fill out the form with the following details:
    - IP Address of the remote server.
    - Username to log in to the remote server.
    - Password for the username.
    - URL to curl when disk usage is below 90%.

4. Click the "Submit" button.

The application will then set up the disk space monitoring script and cron job on the specified remote server.

## Files

- `app.py`: Main Flask application file.
- `templates/index.html`: HTML template for the web form.
- `README.md`: This README file.

## Security Note

For security reasons, avoid hardcoding sensitive information such as passwords in the source code. Consider using environment variables or other secure methods to handle sensitive data.
