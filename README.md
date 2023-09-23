# FastAPI_JWT


This project only contains SignUp/Login and login user can view all user data,
which is authorized by JWT tokens
an also data is saved mysql database


#To Run This project


Create a Virtual Environment in python 3.9 or grater 


$python -m venv envname


activate Virtual Environment


$envname\Scripts\activate  # Hit Enter


Install all packages in Virtual Environment


$pip install -r requirements.txt



Note: Before running the server change the data base settings,


Go to database.py file at line no: 5


file_path : mysql_url_database = "mysql+pymysql://root:password@localhost:3306/fast_db"


replace the password with your mysql root password


To run server


$uvicorn main:app --reload


Hit the url you got in terminal and your good to go.:


If you want to check the api got to this url


http://127.0.0.1:8000/docs  # paste in browser


😁 Happy Coding

