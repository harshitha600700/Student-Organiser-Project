# Student-Organiser-Project

The Student Organizer is a web-based productivity application built using Flask. It is designed to help students manage academic responsibilities in one place, including task tracking, notes, weekly timetables, grade logging, reminders, and a Pomodoro timer. The application also supports theme switching to allow a personalized user interface.

## Features

- Task management with due dates
- Notes section for important information
- Weekly timetable organized by days
- Grade tracker for academic subjects
- Pomodoro timer with 25-minute work and 5-minute break intervals
- Daily motivational quote display
- Reminder system for pending tasks
- Theme switching between three modes:
  - Light theme
  - Dark mode
  - Aesthetic (pink) theme

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Templating Engine:** Jinja2
- **Data Storage:** JSON file

## File Structure

student-organizer/
│
├── app.py               # Main Flask application (routes, logic, data handling)
├── data.json            # JSON file for storing tasks, notes, timetable, grades, etc.
│
├── templates/
│   └── index.html       # Main webpage (UI layout using Jinja templating)
│
├── static/
│   ├── kawaii.css       # Aesthetic pink theme
│   ├── dark.css         # Dark mode theme
│   ├── light.css        # Light theme
│   └── theme.js         # JavaScript for dynamic theme switching and local storage

## How It Works

- The application is served through Flask with routing handled in `app.py`.
- Data is read from and written to `data.json`, simulating a database for persistence.
- The front-end UI is rendered using Jinja2 templating inside `index.html`, allowing dynamic content updates.
- JavaScript handles theme switching and Pomodoro timer functionality.
- Users interact with the interface to add, update, or remove tasks, notes, timetable entries, and grades.
