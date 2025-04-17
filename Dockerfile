# Base image with TensorFlow 2.9.1
FROM tensorflow/tensorflow:2.9.1

# Set working directory
WORKDIR /usr/src/app

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
