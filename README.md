# Insta Clone  
#### 07/12/2021   
#### By **Annalis Kirwa** 
## Description  
Insta Clone is a clone of the website for the popular photo app Instagram. In this web app, the  user can sign in and upload pictures in the application.
Users can also follow other users and like their pictures or comment or both.  

## Behaviour Driven Development(BDD) 
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Register into the application | Fill in th eregistration form with details | Details saved, the user can log in |
| View pictures | Log in to the app and navigate to home| Sees a list of pictures from other users of the web app |
| Like a picture | Click at the like button at the bottom of the picture | Increases the number of likes on the picture by 1 |
| Comment on a picture | Click on the comment button and write your comment | The comment is saved under the list of comments |
| Update profile | Click on update profile | Users recently changed profile is displayed |  

## Features 
As a user of Insta Clone web application, you will be able to:  
* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.  

## Setup/Installation Requirements  
 ### To interact with the Insta Clone web application:
 * Have the latest version of browser installed   
 * Click on this <a href = "https://instacloneann.herokuapp.com/">link</a> to use Insta Clone  
  ### To contribute to Fotoo web application:  
 #### Clone the Repo  
 * Create an account on Github
* Fork the repository from Github with this <a href = "https://github.com/Annaliskirwa/_Insta_Clone" >link </a>
* Clone the repository
* Open the project cloned project
####  Activate virtual environment
Activate virtual environment using python3.6 as default handler
    `virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE instaclone;  
    
#### Run initial Migration
    python3.8 manage.py makemigrations instaclone  
    python3.8 manage.py migrate
#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000  
    
  ## Known Bugs
There are no known bugs so far
## Technologies Used  
* Python v3.8  
* HTML
* Bootstrap
* Django  
* Postgres  
## Support and contact details
In case of any problem while interacting with the web application, reach out to me at annalis.kirwa@student.moringaschool.com
### License.
MIT Copyright (c) 2021 **[MITlicense](LICENSE)**



