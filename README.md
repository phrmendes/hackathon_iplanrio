# Hackiplan

Project for the IplanRio 2024 hackathon.

## Overview

Hackiplan is a project developed for the IplanRio hackathon. The main goal of this project is to facilitate the creation, search, and monitoring of public tenders in the city of Rio de Janeiro.

## Features

- **Backend**: Developed using Python and the Django framework.
- **Frontend**: Utilizes HTMX for dynamic content and PicoCSS for styling.

## Installation

To install and set up the project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/phrmendes/hackiplan.git
cd hackiplan
```

2. Sync the dependencies with `uv`:

```bash
uv sync
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Run the development server:

```bash
python manage.py runserver
```

## Usage

To use the application, navigate to [http://localhost:8000](http://localhost:8000) in your web browser. You can create, search, and monitor public tenders from the web interface.
