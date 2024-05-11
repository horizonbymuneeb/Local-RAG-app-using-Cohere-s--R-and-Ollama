import subprocess
import time

def is_qdrant_container_running():
    """Check if any container running the Qdrant image is up."""
    try:
        # List all containers using qdrant image and check if they are running
        result = subprocess.run(['docker', 'ps', '--filter', 'ancestor=qdrant/qdrant', '--format', '{{.Names}}'],
                                capture_output=True, text=True)
        running_containers = result.stdout.strip().split('\n')
        if running_containers and running_containers[0]:  # Check if the list is not empty
            print(f"Running Qdrant container(s): {running_containers}")
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error checking containers: {e}")
        return False

def wait_for_qdrant_container(timeout=180, interval=5):
    """Wait for any Qdrant Docker container to be running."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        if is_qdrant_container_running():
            print("Qdrant vector DB server is up and running.")
            return True
        print("Waiting for Qdrant vector DB server to start...")
        time.sleep(interval)
    print("Timeout reached. No Qdrant container is running.")
    return False

