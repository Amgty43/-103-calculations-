# 2025 NFL schedule explorer

This project now uses a lightweight Flask application to render the mock 2025 NFL schedules without any client-side JavaScript. All HTML is embedded directly in `app.py` using Flask's `render_template_string`, so you only need that single file to run the explorer. Legacy browser assets have been removed to keep the project entirely Python-driven.

## Running locally

1. Install dependencies (a virtual environment is recommended):

   ```bash
   pip install -r requirements.txt
   ```

2. Start the development server:

   ```bash
   flask --app app --debug run
   ```

3. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) and select a team to view its generated schedule.

Update the team or schedule logic inside `app.py` when official information becomes available.
