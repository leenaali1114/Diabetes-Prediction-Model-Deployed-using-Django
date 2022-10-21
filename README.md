# Diabetes-Prediction-Model-Deployed-using-Django
Deploy a Machine Learning model using the Django  framework 

Django is a high-level Python framework for creating scalable and robust web applications. In Python, this is the most widely used framework. It adheres to the MVT (Model-View-Template) design pattern. Other MVC frameworks, such as Ruby on Rails and Laravel, are closely linked to it. The display and model elements of the MVC framework are managed by the Controller, but in Django, the framework handles the tasks of a controller implicitly. Django allows you to develop several applications within a single project. The application has all the necessary features to function independently. The app is regarded as a package that may be reused in other applications without major modifications. This is the most significant benefit of using Django to create web apps.

### What is Django REST Framework?
The Django REST framework is an excellent tool for building strong web APIs with Django and Python. It allows you to easily serialize data and share it with other programs. It acts as a barrier between the database and the application that performs database queries and data formatting. In most cases, JSON is used to format the data.

### Ways to Integrate Machine Learning models in Django
Models for machine learning are typically developed in Python and executed locally in a Jupyter notebook or other IDEs (Integrated Development Environment). To make your machine learning model available on a web application, the following can be done.

In web apps, hard code the ML model. This is the simplest approach to deploy machine learning models on the web, such as support vector machine or linear regression classifiers. However, if you're trying to create more complex models like Neural Networks, it has a lot of limitations.

The most efficient method is to create a communication interface between the ML model and the web interface. It will acquire data for the model, which will then process it on its own. This interface will navigate you back to the web application's end once you've received the prediction from the model. We can do this through REST APIs or WebSocket.


### Integrating a Diabetes Prediction Model in a Django Project
There are a few steps to integrate your machine learning model in a Django project.

  -Firstly, you will need to download the machine learning model as a .py file.

  -Then, the model should be saved after training to avoid overfitting.

  -Later, an app should be created that takes user data through an HTML form and output the prediction.
  
  The form the user will have to enter data in, can look something like the below screenshot.
  
![Screenshot (197)](https://user-images.githubusercontent.com/67731093/197136812-d651ddf2-085c-462b-99ef-3c9ba8435d05.png)

The result page can look something like the below screenshot.

![Screenshot (196)](https://user-images.githubusercontent.com/67731093/197136882-523ac3fc-70ec-4058-bcf4-a8cb3827bf05.png)
