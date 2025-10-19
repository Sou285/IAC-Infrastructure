import os
import time
import sys

# Set console encoding to UTF-8 for Windows
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

# =========================
# Infrastructure as Code Simulation
# =========================

def create_infrastructure():
    print("\n[STARTING] Applying Infrastructure as Code...")
    time.sleep(1)
    
    # Create main infrastructure folder and subfolders
    os.makedirs("infrastructure/web_server", exist_ok=True)
    os.makedirs("infrastructure/database", exist_ok=True)
    os.makedirs("infrastructure/storage", exist_ok=True)

    # Create a file to describe the simulated resources
    with open("infrastructure/overview.txt", "w") as f:
        f.write("Infrastructure as Code (IaC) Simulation\n")
        f.write("---------------------------------------\n")
        f.write("Resources Provisioned:\n")
        f.write("- Web Server\n")
        f.write("- Database\n")
        f.write("- Storage Bucket\n")
        f.write("\nStatus: Active ")

    print("[SUCCESS] Infrastructure created successfully!")
    print("Check the 'infrastructure' folder to see the resources.")

def destroy_infrastructure():
    print("\n🧹 Destroying Infrastructure...")
    time.sleep(1)
    
    if os.path.exists("infrastructure"):
        # Remove all files and folders recursively
        for root, dirs, files in os.walk("infrastructure", topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir("infrastructure")
        print("[SUCCESS] All resources destroyed successfully!")
    else:
        print("[WARNING] No infrastructure found to destroy.")
def main():
    print("========= Infrastructure as Code Simulation =========")
    print("1. Apply Infrastructure")
    print("2. Destroy Infrastructure")
    choice = input("\nEnter your choice (1 or 2): ")

    if choice == "1":
        create_infrastructure()
    elif choice == "2":
        destroy_infrastructure()
    else:
        print("[ERROR] Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()