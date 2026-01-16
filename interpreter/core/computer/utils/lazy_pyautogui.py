
# Lazy import of pyautogui with error handling for missing dependencies (like tkinter)
class _PyAutoGUIWrapper:
    def __init__(self):
        self._module = None
        self._tried_import = False

    def _ensure_imported(self):
        if not self._tried_import:
            try:
                import pyautogui
                self._module = pyautogui
            except (ImportError, SystemExit) as e:
                # pyautogui (via mouseinfo) calls sys.exit() if tkinter is missing on Linux
                # We catch this to prevent the whole application from exiting
                print(f"Warning: pyautogui could not be imported: {e}")
                self._module = None
            except Exception as e:
                print(f"Warning: pyautogui import failed with error: {e}")
                self._module = None
            self._tried_import = True

    def __getattr__(self, name):
        self._ensure_imported()
        
        if self._module:
            return getattr(self._module, name)
        raise ImportError("pyautogui is not available (requires tkinter). Please install python3-tk.")

pyautogui = _PyAutoGUIWrapper()
