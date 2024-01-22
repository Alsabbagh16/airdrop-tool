import subprocess
import time

output_log_path = 'list_output_log.txt'

with open('airdrop_amount_list.txt', 'r') as f:
    lines = f.readlines()

with open(output_log_path, 'w') as output_log:
    for line in lines:
        # Split each line into wallet address and amount
        wallet_address, amount = line.strip().split(', ')

        # Use subprocess to transfer the specified amount of tokens
        process = subprocess.Popen(["spl-token", "transfer", "--fund-recipient", "H6Jz41jUjNV7kNDBQuvJqNnpEYhGF6wJ5DR8bMLZDqvR", amount, wallet_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Log the output to the file
        output_log.write(f"Tokens transferred to {wallet_address} - Amount: {amount}\n")
        output_log.write(f"STDOUT: {stdout.decode()}\n")
        output_log.write(f"STDERR: {stderr.decode()}\n")
        output_log.write("=" * 40 + "\n")

        print(f"Tokens transferred to {wallet_address} - Amount: {amount}")

        # Introduce a cooldown of 15 seconds
        time.sleep(5)

print(f"Transaction log saved to {output_log_path}")
