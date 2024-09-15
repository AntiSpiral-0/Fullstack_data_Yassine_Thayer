import subprocess
from pathlib import Path

if __name__ == "__main__":
    dashboard_path = "/Executive_board/dashboard.py"
    subprocess.run(f"streamlit run '{dashboard_path}'", shell=True)