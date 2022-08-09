FROM python:3
LABEL maintainer="olasodeadeyemi@gmail.com"
LABEL description="Sudoku service that allows playing Sudoku game"

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

# Start processes
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]