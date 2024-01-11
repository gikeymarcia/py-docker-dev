# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Section to import host uid and gid into container
# This is done so files created by 'appuser' are owned by person building/running
# the container

# Accept UID and GID as build arguments
ARG USER_ID
ARG GROUP_ID

# Create a group and user with the specified USER_ID and GROUP_ID
RUN groupadd --gid $GROUP_ID appgroup && \
    useradd --create-home --no-log-init --shell /bin/bash --uid $USER_ID --gid $GROUP_ID appuser

# Set the working directory in the container
WORKDIR /usr/src/app

# Change ownership of the working directory to the appuser
# This should come after the user and group have been created
RUN chown appuser:appgroup /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
# Ensure that the copied files have the appropriate ownership
COPY --chown=appuser:appgroup requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Switch to the appuser to run subsequent commands
USER appuser

# Run app.py when the container launches
CMD ["python", "app.py"]
