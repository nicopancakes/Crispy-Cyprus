import subprocess
import os
import sys
import tempfile
from .scripts import embedded_scripts

# Paths to Electron apps
apps = {
    "D": r"C:\Path\To\D.exe",
    "DPTB": r"C:\Path\To\DPTB.exe",
    "DCanary": r"C:\Path\To\DCanary.exe"
}

# Injection toggle
injection_enabled = True
selected_script = "oneko"

def write_temp_script(name, content):
    """Write the embedded TypeScript script to a temp file"""
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, f"{name}.ts")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return file_path

def run_app(app_name):
    app_path = apps.get(app_name)
    if not app_path or not os.path.exists(app_path):
        print(f"{app_name} not found!")
        return

    if injection_enabled:
        script_content = embedded_scripts.get(selected_script)
        if not script_content:
            print(f"Script {selected_script} not found!")
        else:
            temp_script = write_temp_script(selected_script, script_content)
            print(f"Injecting {selected_script} into {app_name}...")
            subprocess.run(["pnpm", "inject", temp_script])

    print(f"Launching {app_name}...")
    subprocess.Popen([app_path])

def toggle_injection():
    global injection_enabled
    injection_enabled = not injection_enabled
    print(f"Injection {'enabled' if injection_enabled else 'disabled'}.")

def select_script():
    global selected_script
    print("Available scripts:")
    for s in embedded_scripts:
        print(f"- {s}")
    choice = input("Select a script: ").strip()
    if choice in embedded_scripts:
        selected_script = choice
        print(f"Selected script: {selected_script}")
    else:
        print("Invalid choice.")

def main():
    while True:
        print("\nAvailable apps:")
        for app in apps:
            print(f"- {app}")
        print("Commands: toggle, select, run <app>, exit")
        cmd = input("> ").strip().lower()
        if cmd == "exit":
            sys.exit()
        elif cmd == "toggle":
            toggle_injection()
        elif cmd == "select":
            select_script()
        elif cmd.startswith("run "):
            _, app_name = cmd.split(maxsplit=1)
            run_app(app_name)
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
