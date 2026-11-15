# Montserrat

Unmodified WOFF2 files from Google Fonts, release `v31`, downloaded on 2026-11-15.
License: [SIL Open Font License 1.1](OFL.txt).

Source stylesheet:
https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap

License source:
https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/OFL.txt

The local declarations in `../css/style.css` preserve the original variable
weight range (100–900), normal and italic styles, and all five Unicode subsets
per style. The files are not modified or converted. Only normal Cyrillic and
Latin are preloaded; the browser requests other subsets when needed.

## Deployment

These assets are included by the existing Django staticfiles configuration.
Run `python manage.py collectstatic --noinput` during deployment, and serve the
collected files through the existing `/static/` web-server configuration.

Configure caching in the production static-file server, for example
`Cache-Control: public, max-age=2592000` (30 days) for these versioned WOFF2 files.
Use new filenames and update the CSS and preload links when replacing font data.
Production web-server configuration is not part of this repository; Django's
development server is not used to configure production caching.
