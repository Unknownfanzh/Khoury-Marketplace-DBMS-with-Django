# Khoury-Marketplace-DBMS-with-Django
This is a DBMS with MySql for backend and Django for frontend deployed on GCP.
The Khoury Marketplace is a dynamic web application designed to facilitate the buying, selling, and auctioning of items within the Khoury community. Built with Django and MySQL, and deployed on Google Cloud Platform, this platform offers an intuitive interface for users to interact with the database effectively.

## Features

- **User Authentication**: Secure login and registration system for users.
- **Query Interface**: Users can run SQL queries directly from the web interface.
- **Responsive Design**: Adaptively designed for both desktop and mobile viewing experiences.

## Live Demo

Check out the live demo of the Khoury Marketplace: [Visit Khoury Marketplace](https://db-group5-415506.uw.r.appspot.com)

## Local Setup

To set up the project locally, follow these steps:

1. **Clone the Repository**

```bash
git clone https://github.com/Unknownfanzh/Khoury-Marketplace-DBMS-with-Django.git
cd yourrepositoryname
```

2. **Set Up a Virtual Environment**
```bash
python -m venv venv
```
For Windows:
```bash
venv\Scripts\activate
```
For Unix or MacOS:
```bash
source venv/bin/activate
```

3. Install Dependencies
Make sure you have MySQL running and configure the database settings in settings.py accordingly.
```bash
python manage.py migrate
```

4. Run the Server
```bash
python manage.py runserver
```

The project should now be running on http://127.0.0.1:8000/

## Technologies Used
- **Backend**: Django
- **Database**: MySQL
- **Frontend**: HTML, CSS
- **Deployment**: Google Cloud Platform

## Contributions
Contributions are welcome! Please feel free to submit a pull request.

