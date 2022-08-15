# Sudoku

This is a single-player sudoku game service. You can start the game, make moves, erase moves and reset the game. Once a win is detected, you get the returned data showing this. This service has the following endpoints: Schema for the endpoints are as below;

- `GET api/heath_check` - This endpoint is provided for pinging the service to check if it is up or not.
  response:

  ```json
  {
    "status": "healthy"
  }
  ```

- `POST api/games/reset` - This can be used to start the game or reset the game back to the default state. No other actions can be taken on the game without resetting it first. It returns the game board (which is a 9 x 9 matrix - 2D array of numbers) and the win status of the game.

  request:
  `/api/games/reset`

  response:

  ```json
  {
    "board": [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,8,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ],
    "game_win": false
  }
  ```

- `POST api/games/cell/move` - This is used to make a move on the board.

  request:

  ```json
  {
    "value": 2,
    "row": 0,
    "column": 2,
  }
  ```

  response:

  ```json
  {
    "board": [
        [5,3,2,0,7,0,0,0,0],
        [6,0,0,1,8,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ],
    "game_win": false
  }
  ```

- `POST api/games/cell/erase` - This is used to erase an editable cell on the board.

  request:

  ```json
  {
    "row": 0,
    "column": 2,
  }
  ```

  response:

  ```json
  {
    "board": [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,8,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ],
    "game_win": false
  }
  ```

## Tools Used

### Docker

For easy distribution and ease of starting up, I have dockerized the app.

### Flask

I used flask, flask-restx, and other related flask libraries to build the app.

## Running the app

Clone the repository using either `https` or `ssh`

### Using Docker (recommended)

- Install and launch Docker. Ensure it's running.
- Ensure no other service is running on port `8000`.
- On a terminal, `cd` into the root directory.
- Run the command below. This should build and run the app.

  ```sh
      docker compose up
  ```

- After the containers have been successfully built and running, we can access the endpoints at `http://localhost:8000/api/health_check` and api documentation at `http://localhost:8000/api`.

### Running tests with Docker

Stop the app process and run the command below in the root directory.

```sh
      docker compose -f docker-compose-test.yml up
```

### Without Docker

- On a terminal, `cd` into the root directory.
- Install `python3.x` and run the command below to create a virtual environment for the project.

  ```sh
      python -m venv sudoku_env
  ```

- Activate the environment by running the command from the project directory:

  ```sh
      source sudoku_env/bin/activate
  ```

- Install all dependencies with the command:

  ```sh
      pip install -r requirements.txt
  ```

- Ensure no other service is running on port `5000`.
- Run the command below to start the app;

  ```sh
      FLASK_ENV=development flask run
  ```

- You can now access the endpoints at `http://localhost:8000/api/health_check` and api documentation at `http://localhost:8000/api`.

### Running tests without Docker

Run the command below in the root directory while the virtual environment is still activated.

```sh
      python -m unittest discover
```

## App Structure

This app is structured in a MVC format such that there can be separation of responsibilities between the different layers of the app. The folder structure is displayed below. Each resource has a model, controller and corresponding view.

```files
root directory
.
+-- models
|   +-- model_a.py
|   +-- model_b.py
+-- restapi
|   +-- endpoints
|   |   +-- resource_a.py
|   |   +-- resource_b.py
|   +-- api_setup.py
+-- other files
```
