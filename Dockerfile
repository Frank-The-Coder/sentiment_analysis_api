# Use a base image with Python 3.10
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the entire application code to the container
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8080

# Define the command to run the FastAPI app using uvicorn on port 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]


