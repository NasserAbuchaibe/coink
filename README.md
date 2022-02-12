# WebApp technical test

## **Description**  

Webapp that stores registration and generates queries in the database, registers the creation event in a txt file  

## **Enviroment:**

### **Backend:**
* Python
* Flask 
* Flask-SQLAlchemy
* SQLAlchemy
* WTForms
* Flask-WTF
* SQlite

### **Frontend:**
* HTML5
* Boostrap

## This project was developed in a virtual environment using virtualenv with python 3.8.5 

### For testing purposes, I suggest using virtualenv and installing the necessary libraries using the requirements.txt file. 


## **Installation:**
1. Create or define the directory where the project will be cloned and enter the directory.  
``` 
$  mkdir my_dir  
$  cd my_dir 
```

2. Clone Github repository
```
   $ git clone https://github.com/NasserAbuchaibe/coink.git
```

3. Create and activate virtual environment (for this step you must have virtualenv installed).
```
  $ virtualenv venv
  $ source venv/bin/activate
```
4. Enter the coink directory.
```
   (venv)$ cd coink
```
5.  Install dependencies.
```
    (venv)$ pip install -r requirements.txt
```
6. Start server.
```
    (venv)$ flask run
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## **User registration form**  


  
<img src="https://i.imgur.com/mdKdhU5.png">  


<br>

## **record created** 
<img src="https://i.imgur.com/yghHLTd.png"> 

<br>

## **listing stored records**  


<img src="https://i.imgur.com/rvckaVv.png">  

<br>

## **Automatically generated .txt file with creation event logs**  

<img src="https://i.imgur.com/6Ty4Be7.png">  

 <br>
 
## **Author:**
* **Nasser Abuchaibe** - [NasserAbuchaibe](https://github.com/NasserAbuchaibe)