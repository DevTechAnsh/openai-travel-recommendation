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
   cd app

   ## For the frontend app
    cd ai-travelling-frontend
    npm i



2. Build the Docker image for the project inside the 'app' directory:


    ```
    docker build -t ai-piping-recommendations .

3. Run the Docker container:

    ```
    docker run -p 3000:3000 ai-piping-recommendations

 ## Application should now be accessible at -

    http://localhost:3000 (can check backend on Swagger)

- To run the tests using pytest, within the Docker container:
  ```
  docker exec -it <container-id-or-name> pytest test.py

- Start the frontend app separately for development:

    ```
    cd ai-travelling-frontend
    npm start



