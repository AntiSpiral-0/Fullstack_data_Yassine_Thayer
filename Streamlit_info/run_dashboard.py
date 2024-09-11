import subprocess
from pathlib import Path

if __name__ == "__main__":
    dashboard_path = "/Streamlit_info/dashboard.py"
    subprocess.run(f"streamlit run '{dashboard_path}'", shell=True)
    