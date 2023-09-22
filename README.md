# AI-PIPING (Recommendation App)

## objective
Create a simple FastAPI application that serves an endpoint to recommend three things to do in a given country during a specific season by consulting the OpenAI API.



## Prerequisites

Before you begin, make sure you have the following installed:
- [Node.js](https://nodejs.org/) (for the React frontend)
- [Python](https://www.python.org/) (for the FastAPI backend)
- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/downloads) (optional for cloning the project)

## Getting Started

1. Clone the project:

   ```bash
   git clone <repository-url>

2. Create a .env file in the project backend directory and add your Open API KEY like this:

    ```
    OPENAI_API_KEY=your_open_api_key_here


3. Run the backend and frontend server with this command

    ```
    docker compose up --build

 ## Application should now be accessible at -

    http://localhost:8000

- To run the tests using pytest, within the Docker container:
  ```
  docker exec -it <container-id-or-name> pytest test.py




