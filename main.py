#!/usr/bin/env python3
"""
CareerWise AI - Streamlit Application Launcher

A smart career mentoring tool that analyzes resumes and GitHub profiles
to provide personalized career guidance using Ollama LLM.

Usage:
    python main.py              # Run with default settings
    python main.py --port 8502  # Run on custom port
    python main.py --help       # Show help

Streamlit App Features:
    - Resume PDF analysis and skill extraction
    - GitHub profile analysis and repository insights
    - AI-powered career recommendations
    - Weekly progress email reports
"""

import sys
import os
import argparse
from pathlib import Path
import subprocess

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = ['streamlit', 'pdfplumber', 'github', 'python-dotenv', 'ollama']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("\n❌ Missing required packages:")
        for pkg in missing_packages:
            print(f"   - {pkg}")
        print("\n💡 Please install them using:")
        print(f"   pip install {' '.join(missing_packages)}")
        print("   OR")
        print("   pip install -r requirements.txt")
        return False
    return True

def check_environment():
    """Check if environment is properly configured"""
    env_file = Path(".env")
    if not env_file.exists():
        print("\n⚠️  Environment file '.env' not found!")
        print("\n💡 Please create it by copying the example:")
        print("   cp config/.env.example .env")
        print("   Then edit .env with your credentials")
        return False
    
    # Load and check environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    required_vars = ['GITHUB_TOKEN', 'EMAIL_ADDRESS', 'EMAIL_PASSWORD']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("\n⚠️  Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n💡 Please set them in your .env file")
        return False
    
    return True

def main():
    """Main function to run the CareerWise AI application"""
    parser = argparse.ArgumentParser(
        description="CareerWise AI - Intelligent Career Mentoring Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Run with default settings
  python main.py --port 8502        # Run on custom port
  python main.py --no-browser       # Don't open browser automatically

For more information, visit: http://localhost:8501
        """
    )
    
    parser.add_argument(
        '--port', 
        type=int, 
        default=8501, 
        help='Port to run the application on (default: 8501)'
    )
    
    parser.add_argument(
        '--host', 
        type=str, 
        default='0.0.0.0', 
        help='Host address to bind to (default: 0.0.0.0)'
    )
    
    parser.add_argument(
        '--no-browser', 
        action='store_true', 
        help='Do not open browser automatically'
    )
    
    parser.add_argument(
        '--debug', 
        action='store_true', 
        help='Run in debug mode with detailed logging'
    )
    
    args = parser.parse_args()
    
    print("🚀 Starting CareerWise AI...")
    print("=" * 50)
    
    # Check dependencies
    print("📦 Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    print("✅ All dependencies are installed")
    
    # Check environment
    print("🔧 Checking environment configuration...")
    if not check_environment():
        sys.exit(1)
    print("✅ Environment is properly configured")
    
    # Verify application files
    streamlit_app_path = src_path / "ui" / "streamlit_app.py"
    if not streamlit_app_path.exists():
        print(f"\n❌ Application file not found: {streamlit_app_path}")
        print("\n💡 Please ensure the project structure is correct")
        sys.exit(1)
    
    print("\n🎯 Starting CareerWise AI application...")
    print(f"   Host: {args.host}")
    print(f"   Port: {args.port}")
    print(f"   URL: http://localhost:{args.port}")
    print("\n📝 Application logs:")
    print("-" * 30)
    
    # Build streamlit command
    cmd = [
        sys.executable, "-m", "streamlit", "run", 
        str(streamlit_app_path),
        f"--server.port={args.port}",
        f"--server.address={args.host}",
        "--server.headless=true",
        "--browser.gatherUsageStats=false"
    ]
    
    if args.no_browser:
        cmd.append("--server.runOnSave=false")
    
    if args.debug:
        cmd.extend(["--logger.level=debug"])
    
    try:
        # Run the Streamlit application
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n\n👋 CareerWise AI application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"\n\n❌ Error running application: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
