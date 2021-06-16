# Vaccination Centers
A simple map application to show COVID-19 vaccination centers in Uganda. It uses [OpenStreetMaps](https://openstreetmap.org/) to show the different centers on a map of Uganda. It's written using Django, a Python web framework.

## Demo
![](/docs/screenshot.png)

Here is the demo link: [http://vaccination-centers.herokuapp.com](http://vaccination-centers.herokuapp.com)

## Development Setup. 
The assumption is that you know how to write apps in Django. 

- Clone the repository and activate your virtual environment. 

- Install the dependencies by running this command: `pip install -r requirements.txt`

- Ensure you have `Postgres` installed on your machine. 

- Rename `.env.sample` file to `.env`

- Run migrations using this command: `python manage.py makemigrations`

- Run the web app using this command: `python manage.py runserver`
