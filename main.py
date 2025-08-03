#!/usr/bin/env python3
"""
CareerWise AI - Simple launcher for the Streamlit application
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Run the CareerWise AI Streamlit application"""
    print("🚀 Starting CareerWise AI Streamlit Application...")
    
    # Path to the main Streamlit app
    app_path = Path(__file__).parent / "src" / "ui" / "streamlit_app.py"
    
    if not app_path.exists():
        print(f"❌ Application file not found: {app_path}")
        sys.exit(1)
    
    # Run streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", str(app_path),
            "--server.port=8501",
            "--server.address=0.0.0.0"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
