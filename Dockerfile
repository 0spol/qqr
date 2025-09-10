FROM python:3.11-slim

# Set non-interactive frontend for apt-get to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install SSH server and git
RUN apt-get update && \
    apt-get install -y \
    openssh-server \
    git \
    && rm -rf /var/lib/apt/lists/*

# Define build arguments for user and port
ARG USERNAME=dockeruser
ARG SSH_PORT=2222

# Create user and set password
RUN useradd -m -s /bin/bash ${USERNAME} && \
    echo "${USERNAME}:dockerpass" | chpasswd

# Configure SSH server
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i "s/#Port 22/Port ${SSH_PORT}/" /etc/ssh/sshd_config && \
    echo "LogLevel VERBOSE" >> /etc/ssh/sshd_config

# Install Python libraries
RUN pip install --no-cache-dir textual rich

# Set working directory and copy Python script if it exists
WORKDIR /app
COPY test.py* .

# Ensure SSH directory exists and has correct permissions
RUN mkdir -p /var/run/sshd && \
    chmod 755 /var/run/sshd

# Expose the SSH port
EXPOSE ${SSH_PORT}

# Start SSH server
CMD ["/usr/sbin/sshd", "-D", "-e"]

