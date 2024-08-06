
# NF Page - Dance Studio Website

Welcome to the NF Page repository! This project aims to create a website for Nanda Fouad Espaço de Dança, showcasing class schedules, information about dance styles, and more.


## Features

- Display class schedules for different dance styles.
- Provide information about the dance studio and its instructors.
- Engage users with an attractive homepage and easy navigation.


## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/micaelcosmo/nf_page.git
   cd nf_page

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run Migrations:**
   ```bash
    python manage.py migrate

5. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser

6. **Start the Development Server:**
   ```bash
   python manage.py runserver

7. **Access the Admin Panel:**
   ```bash
   Go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
   Add dance styles, instructors, and class schedules.


## Customization

- Update the base.css file in the static folder to style your pages.
- Modify the templates (e.g., horarios.html, index.html) in the templates folder to match your design.

### Contributing
- Contributions are welcome! If you find any issues or want to enhance the project, feel free to submit a pull request.

### License
- This project is licensed under the MIT License - see the LICENSE file for details.