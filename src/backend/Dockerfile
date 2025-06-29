# Use a Python 3.11 base image
# slim is a lighter version than the standard
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install the necessary system dependencies
# gcc: necessary to compile some Python dependencies
# postgresql-client: tools to interact with PostgreSQL
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
# --no-cache-dir: avoid saving packages in cache to reduce the image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port 8000 that will be used by our application
EXPOSE 8000

# Command that will be executed when the container starts
# uvicorn: ASGI server for FastAPI
# --host 0.0.0.0: allows connections from outside the container
# --port 8000: port where the application will run
# --reload: reloads automatically when there are changes in the code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 