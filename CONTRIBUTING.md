## Development Setup

### Fork and clone the repository
Fork this repository by clicking on the fork button on the top of this page. This will create a copy of this repository in your account.

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the copy to clipboard icon.

```git clone "url you just copied"```

### Setup and installation
Change to the repository directory on your computer 

```cd vaccination-centres```

Create a virtual environment using the following command

```python3 -m venv env```

Once you’ve created a virtual environment, you may activate it.

On Windows, run:

```env\Scripts\activate.bat```

On Linux or MacOS, run:

```source env/bin/activate```

You can install the project requirements from the `requirements.txt` file using the following command

```python -m pip install -r requirements.txt```

Create a `.env` file, copy all the contents from `.env.sample` file and paste them in the `.env` file you just created.

Make migrations to sync and create a database

```python manage.py migrate```

Run the web app using this command: 

```python manage.py runserver```

## Making contributions
Create a new branch where your change(s) will reside, run:

```git checkout -b new-branch```

Make a necessary change and commit

For example:
If you fixed a typo in `README.md` file, run: `git status` to see the files that have been changed

Add these changes to your branch

```git add README.md```

Now commit these changes to your branch with a meaningful message, run:

```git commit -m "fix typo in README.md file"```

Push these changes to github

```git push origin new-branch```

Submit your changes for review, If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.

Add a brief description and submit the pull request.

Soon I'll be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.
