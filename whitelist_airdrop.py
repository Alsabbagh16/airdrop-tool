import subprocess
import time

output_log_path = 'whitelist_airdrop_output_log.txt'

with open('Whitelist_airdrop.txt', 'r') as f:
    wallet_addresses = f.readlines()

with open(output_log_path, 'w') as output_log:
    for i, wallet_address in enumerate(wallet_addresses):
        # Use subprocess to transfer 1 token
        process = subprocess.Popen(["spl-token", "transfer", "--fund-recipient", "H6Jz41jUjNV7kNDBQuvJqNnpEYhGF6wJ5DR8bMLZDqvR", "1", wallet_address.strip()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Log the output to the file
        output_log.write(f"Transaction {i + 1} - Token transferred to {wallet_address.strip()}\n")
        output_log.write(f"STDOUT: {stdout.decode()}\n")
        output_log.write(f"STDERR: {stderr.decode()}\n")
        output_log.write("=" * 40 + "\n")

        print(f"Transaction {i + 1} - Token transferred to {wallet_address.strip()}")

        # Introduce a cooldown of 15 seconds
        time.sleep(15)

print(f"Transaction log saved to {output_log_path}")
