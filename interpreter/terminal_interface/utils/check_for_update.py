from importlib.metadata import version, PackageNotFoundError
import requests



def check_for_update():
    # Fetch the latest version from the PyPI API
    response = requests.get(f"https://pypi.org/pypi/open-gemini/json")
    latest_version = response.json()["info"]["version"]

    # Get the current version using importlib.metadata
    try:
        current_version = version("open-gemini")
    except PackageNotFoundError:
        # Fallback to open-interpreter if open-gemini is not found
        try:
            current_version = version("open-interpreter")
        except PackageNotFoundError:
            # If neither package is found, assume we're up to date to avoid errors
            return False

    return latest_version > current_version
