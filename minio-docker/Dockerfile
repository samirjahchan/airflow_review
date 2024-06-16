# Use MinIO base image
FROM minio/minio

# Set the user and password environment variables
ENV MINIO_ROOT_USER=minioadmin
ENV MINIO_ROOT_PASSWORD=Test@123

# Set the entrypoint to start MinIO as a server
ENTRYPOINT ["minio"]

# Default command to run the server and specify the data directory
CMD ["server", "/data", "--console-address", ":9001"]
