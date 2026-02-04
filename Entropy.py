import sys
import os

# Add 'src' directory to Python path so we can find the 'entropy' package
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

try:
    from entropy.ui.app import EntropyApp
except ImportError:
    print("Error: Could not import 'entropy' package.")
    print("Make sure you have 'rich' installed (pip install rich)")
    print("and that the 'src' directory exists.")
    sys.exit(1)

if __name__ == "__main__":
    app = EntropyApp()
    app.run()
