# Copilot Instructions for chananya-page

This repository is a small static web app for GPS-based attendance check-in. It is not a multi-page framework app or a Node.js project; the core logic lives directly in `index.html` with styling in `css/style.css`.

- `index.html` is the main app. It contains the UI, inline JavaScript, and the key configuration constants:
  - `GOOGLE_SHEETS_URL` is the external Google Apps Script endpoint used to persist attendance data.
  - `CAMPUS_CENTER` is the fixed campus location.
  - `ALLOWED_RADIUS_METERS` is the permitted radius for check-in validation.
- `css/style.css` defines the visual design and responsive layout. The app uses custom CSS variables and a single mobile breakpoint at `max-width: 640px`.
- There is no build system, package manager, or bundler in this repo. Changes are usually validated by opening the page in a browser or deploying via GitHub Pages.

Important behaviors to preserve:
- The app uses `navigator.geolocation.getCurrentPosition(...)` and handles permission errors explicitly in `handleError()`.
- Distance validation uses the Haversine formula in `getDistanceMeters(...)` and only allows check-in when distance is within `ALLOWED_RADIUS_METERS`.
- `sendToSheets()` posts JSON to the configured `GOOGLE_SHEETS_URL` and expects a response containing `status: 'success'`.

Project-specific workflow notes:
- The repo includes `.github/workflows/jekyll-gh-pages.yml`, which deploys the site to GitHub Pages. This is the closest thing to a CI/deploy workflow in this project.
- The local app may fail under `file://` due to CORS when talking to Google Apps Script. Prefer previewing from a local HTTP server or GitHub Pages.
- The `misc/google_sheets_apps_script.txt` file documents how to create the corresponding Google Apps Script backend and obtain the deployable `exec` URL.

What not to do:
- Do not assume there is a React/Vue/Angular app or any server-side backend in the repo.
- Do not invent a build command or npm workflow; no `package.json` exists.
- Do not change the repo structure into a framework-based project unless the user explicitly asks for it.

When editing:
- Keep UI logic inside `index.html` unless the user asks to extract it.
- Keep the app’s text and labels in Thai unless asked to add multilingual support.
- Preserve the `GOOGLE_SHEETS_URL` placeholder handling so the app still gives a meaningful message when the URL is not configured.

If you need more context, inspect `index.html` first, then `misc/google_sheets_apps_script.txt` for backend integration details.
