"""Application entry point."""
from os import getenv
from app import init_app


app = init_app()


if __name__ == "__main__":
    app.run(debug=getenv("DASH_DEBUG_MODE", False))