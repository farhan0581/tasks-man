# tasks-man
Demo depicting use of Django and Django rest framework for a simple Task application

# Instructions to Run the project (for ubuntu)
1. Clone the project and enter the directory.
2. Create virtual environment inside the project directory.
3. Activate it using source name_of_your_environment/bin/activate
4. Now run pip install -r requirements.txt
5. This will install all the requirements in your machine.
6. Then start the server using : python manage.py runserver
7. Go to your browser and type 127.0.0.1:8000/tasks_man/task_list
8. Use the Navbar for navigation.

#  Task App
If you are a new user then create a new account using signup option.
1. You can add Tasks using /tasks_man/add
2. You can view your task list using /tasks_man/task_list. On this page you can delete and chage status of your tasks.
	You can also sort them by clicking on column name such as name, complete by and added on either descending or ascending.
3.To view activity go to tasks_man/activity/.

# Rest APIS:
There are three APIS:
1. Add Task using POST hit to 127.0.0.1:8000/tasks_man/tasks
	form data consists of task name, deadline and user id.
	eg: name:learn djano
		deadline:30 May, 2017
		user:1
2. TO view all tasks corresponding to a user:
    GET 127.0.0.1:8000/tasks_man/tasks/user_id
    eg 127.0.0.1:8000/tasks_man/tasks/1

3. TO delete task:
	DELETE 127.0.0.1:8000/tasks_man/tasks/user_id/task_id
	eg 127.0.0.1:8000/tasks_man/tasks/1/4 will delete task with id 4 for user with id 1.

# Issues
There are issues with the UI.