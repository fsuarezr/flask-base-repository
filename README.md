<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" width="200" alt="Flask Logo" />
</p>

# Flask Base Template Project

## Getting Started 🚀
Hey developers! 👋

This template is your launchpad for building awesome Flask applications. It provides a clean foundation with core modules like database connections, logging, and routing already separated, ready for your customization.

### What's included?

- **Solid foundation**: A clean structure to easily manage routes, database connections, and logging.
- **Database options**: Pre-configured setups for MongoDB and PostgreSQL (easily extendable to other databases).
- **Logger support**: Centralized logging configuration with logs saved to a `logs` directory.
- **`.env` support**: Easily manage environment variables for secrets and configuration.

***
### Prerequisites 📋
   ```
   1) Make sure you have Python 3.8+ installed.
   2) Install Flask and other dependencies.
   3) Grab your favorite code editor or IDE.
   ```

***
### Installation 🔧

1. Clone the repository:
   ```bash
   https://github.com/fsuarezr/flask-base-repository.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Environment setup:
   * Create a `.env` file in the project root and refer to `.env.template` for guidance.
   * Install the database package based on your choice:
     * **MongoDB**: `pip install pymongo`
     * **PostgreSQL**: `pip install psycopg2`
   > For databases requiring SSL, upload your `*.crt` file to a folder within the project root and specify that path within the `DB_CERTIFICATE_PATH` variable in your `.env`. Ensure this file is added to your `.gitignore`.

**Optionally, for unused modules:** Remove references from the `src/database/connection_factory.py` file if you don't plan on using any of the pre-configured database modules.

***
### Running the project 🧑‍💻

1. To start the server in development mode, run:
   ```bash
   flask run --debug
   ```

2. To start the server in production mode, run:
   ```bash
   gunicorn --bind 0.0.0.0:5000 wsgi:app
   ```

***
## Features

- **Multiple database connections**: Implemented using the Repository Pattern, supporting MongoDB, PostgreSQL, and more. The connection logic is abstracted for easy switching between databases.
- **Centralized logging**: Logs are stored in the `logs/` folder at the root of the project.
- **Easy route management**: Use blueprints to organize your routes across multiple modules.
- **Future additions**: JWT authentication will be added for secure API access.

***
### Directory Structure

```
📁src
 └── 📁database
     └── connection_factory.py   # Database connection factory
     └── mongodb_connection.py   # MongoDB-specific connection
     └── postgres_connection.py  # PostgreSQL-specific connection
 └── 📁routes
     └── IndexRoutes.py          # Sample routes
 └── 📁utils
     └── Logger.py               # Logger configuration
 └── __init__.py                 # Flask app initialization
```

***
## Contributions
The community is invited to participate in the project development.

***
## Roadmap 📝
This project is continuously developing, with plans for the following improvements:

- **Integration with JWT** for user authentication.
- **Caching with Redis** for optimized performance.
- **Task queue management** with Celery and RabbitMQ.

***
## Author ✒️

- **Franz Suárez** - *Backend Developer* - [fsuarezr](https://github.com/fsuarezr)

🧑‍💻 Made with ❤️ by [fsuarezr](https://github.com/fsuarezr) 🤘 I hope you find it useful. 🤓🤘