import sys
from package.gui import Webview

if __name__ == "__main__":
    window = Webview()

    sys.exit(window.run().exec_())
