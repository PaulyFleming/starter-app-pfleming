## Starter App

This is a simple Flask app that runs 2 dynos, a web and a clock.
The web process is a simple frontend that could be expanded upon in later versions.
The clock process runs a scheduled task every 15 seconds. This task checks to see if it can connect to the list of databases.
If it connects - happy days. If not; it reports the time a database is down.

Note: there's currently a bug in my implementation and the time a database went down at is getting updated incorrectly.

To see What's happening - view the app logs: `heroku logs -t -a starter-app-pfleming`