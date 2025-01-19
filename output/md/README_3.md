# Simple Web Application

## Overview

This project implements a simple web application with routing for two HTML pages: `index.html` and `message.html`. The application handles static resources, processes form submissions, and displays stored messages.

## Features

- **Routing**:

  - Two HTML pages: `index.html` and `message.html`.
  - Static resources: `style.css` and `logo.png`.
  - Error handling for 404 Not Found with `error.html`.

- **Form Handling**:

  - The form on `message.html` captures `username` and `message`.
  - Submitted data is converted to a dictionary and saved in `data.json` in the `storage` directory with a timestamp.

- **Message Display**:
  - A route `/read` displays all stored messages using a Jinja2 template.

## File Structure

```
/project-directory
│
├── storage/
│   └── data.json
│
├── templates/
│   ├── index.html
│   ├── message.html
│   ├── error.html
│   └── read.html
│
├── static/
│   ├── style.css
│   └── logo.png
│
├── app.py
└── Dockerfile (optional)
```

## Requirements

- Python 3.x
- Flask
- Jinja2

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:

   ```bash
   pip install Flask
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Access the application at `http://localhost:3000`.

## Results

- **Homepage**: ![Home Page](./screenshots/SCR_home.png)
- **Message Page**: ![Message Page](./screenshots/SCR_message_form.png)
- **Message Sent**: ![Message Sent](./screenshots/SCR_message_sent.png)
- **Message History**: ![Message History](./screenshots/SCR_history.png)
- **Page 404**: ![Page 404](./screenshots/SCR_page_404.png)
- **Status**: ![Status](./screenshots/SCR_status.png)
- **Docker**: ![Docker](./screenshots/SCR_docker.png)
