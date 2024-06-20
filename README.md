# Dynamic Portfolio

This is a dynamic portfolio website built using Python, Django, HTML, CSS, JavaScript, and MongoDB. It is hosted on Vercel. The portfolio includes home, project, about, and contact pages. It also features an edit page with a login system to authenticate and manage your data.

## Features

- **Home Page**: Overview of the portfolio, showcasing a brief introduction and featured projects.
- **Projects Page**: Detailed list of projects with descriptions, technologies used, and links to live demos or repositories.
- **About Page**: Information about the portfolio owner, including background, skills, and experience.
- **Contact Page**: Form for visitors to get in touch, including social media links.
- **Edit Page**: Authenticated page to edit portfolio content. Users can log in to update their details and project information.
- **Responsive Design**: Mobile-friendly layout for optimal viewing on different devices.
- **Animation and Interactivity**: Smooth transitions and interactive elements for an engaging user experience.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB
- **Hosting**: Vercel

## Installation and Setup

### Prerequisites

- Python 3.x
- Django
- MongoDB
- Vercel account

### Clone the Repository

bash

Copy code

`git clone https://github.com/NagiPragalathan/NewBlackTheamPortfolio.git
cd NewBlackTheamPortfolio` 

### Install Dependencies

bash

Copy code

`pip install -r requirements.txt` 

### Configure MongoDB

Update the `settings.py` file in the Django project to include your MongoDB connection details.

python

Copy code

`DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': '<your-database-name>',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': '<your-mongodb-uri>',
        }
    }
}` 

### Migrate the Database

bash

Copy code

`python manage.py migrate` 

### Create a Superuser

bash

Copy code

`python manage.py createsuperuser` 

Follow the prompts to create a superuser account.

### Run the Development Server

bash

Copy code

`python manage.py runserver` 

Visit `http://127.0.0.1:8000` in your browser to see the portfolio in action.

### Deploy to Vercel

Follow the instructions on Vercel to deploy your Django project. You can refer to Vercel's documentation for more details.

## Usage

- **Login to Edit**: Visit the `/admin` page to log in with your superuser account. Use the Django admin panel to manage content.
- **Home Page**: Displays a brief introduction and featured projects.
- **Projects Page**: Lists all projects with detailed information.
- **About Page**: Contains information about the portfolio owner.
- **Contact Page**: Includes a contact form and social media links.

## Links

- [Repository](https://github.com/NagiPragalathan/NewBlackTheamPortfolio)
- [Live Example](https://nagipragalathan.vercel.app/)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
