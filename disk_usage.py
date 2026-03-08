import os
import shutil

def get_disk_usage(path="/"):
    """
    Returns disk usage statistics about the given path.
    """
    total, used, free = shutil.disk_usage(path)
    
    print(f"Disk Usage for '{path}':")
    print(f"Total: {total // (2**30):>3} GB")
    print(f"Used:  {used // (2**30):>3} GB")
    print(f"Free:  {free // (2**30):>3} GB")
    print(f"Usage: {(used/total)*100:>5.2f}%")

if __name__ == "__main__":
    # In Windows, we can check the C: drive
    path = "C:/" if os.name == "nt" else "/"
    get_disk_usage(path)
