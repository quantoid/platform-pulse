# Platform Pulse

A Streamlit app for monitoring platform metrics and insights, hosted on Streamlit Community Cloud.

## Setup

This project uses `uv` for package management with Python 3.11+.

Set up environment:

    python -m venv .venv
    source .venv/bin/activate
    pip install --no-cache-dir uv
    uv sync

## Run the app

Start the Streamlit app locally:

    streamlit run app.py

The app will be available at http://localhost:8501

## Configuration

Streamlit configuration is stored in `.streamlit/config.toml`.

Secrets should be stored in `.streamlit/secrets.toml` (not committed to git).

## Testing

Run tests with pytest:

    pytest tests/

## Deployment

This app is configured for deployment on Streamlit Community Cloud. The `requirements.txt` file is maintained for cloud deployment compatibility.

## Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **altair**: Declarative statistical visualization
- **pytest**: Testing framework

