FROM rasa/rasa:3.6.15-full

# Copy all project files
COPY . /app

# Switch to root to set permissions
USER root
RUN chmod -R 777 /app /opt/venv

# Train the model
RUN rasa train --quiet

# Switch back to non-root user
USER 1001

# Command to run Rasa
CMD ["run", "--enable-api", "--cors", "*", "--debug"]