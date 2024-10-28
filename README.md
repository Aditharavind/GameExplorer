

# GameExplorer

**GameExplorer** is a Django-based web application designed for gamers to discover upcoming games and check the compatibility of existing games with their PC specifications. This platform provides an engaging way for gamers to stay informed about the gaming landscape while ensuring they have the right hardware for their favorite titles.

## Features

- **Upcoming Games**: Browse a curated list of upcoming games with release dates, trailers, and detailed descriptions.
- **PC Compatibility Checker**: Input your PC specifications and check whether existing games can run on your system, helping you make informed purchasing decisions.
- **User-Friendly Interface**: Navigate through an intuitive layout designed for a seamless user experience.

## Technologies Used
- **Backend**: Python with Django
- **Database**: SQLite (or specify another database if used)
- **Frontend**: HTML/CSS for the user interface.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gameexplorer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd gameexplorer
   ```

3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application in your browser at `http://127.0.0.1:8000`.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

