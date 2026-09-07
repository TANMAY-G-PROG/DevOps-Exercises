import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    ports={'5000/tcp': 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

print(f"Container started: {container.short_id}")

# Test 1: Read /etc/passwd
exit_code, output = container.exec_run(
    "cat /etc/passwd",
    stderr=True
)

print("\n--- Test 1: Read /etc/passwd ---")
print(f"Exit Code: {exit_code}")
print(f"Output: {output.decode()}")

# Test 2: Execute /bin/bash
exit_code, output = container.exec_run(
    "/bin/bash",
    stderr=True
)

print("\n--- Test 2: Execute /bin/bash ---")
print(f"Exit Code: {exit_code}")
print(f"Output: {output.decode()}")

print("\nContainer left running for verification.")
