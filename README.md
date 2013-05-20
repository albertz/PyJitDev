Just-in-time development for Python is a framework where you can develop your Python application on-the-fly. That means, you run your Python code with a special compiler which will add the Python code to all all classes/functions and which provides functions to edit this code and to recompile the bytecode after you changed anything. You will once run the application and make all further development while it is running. You can create new classes on-the-fly and write the code for it. Then you can create instances of these new classes and assign it to new attributes of existing objects. You can also stop the execution at some point and add new code there. The idea is also that you can extend any application (a game, a webserver or whatever) while it is running. Or you can also fix bugs while it is running. The framework should provide functions which will update all the Python code files while you are modifying the application, so when you restart the application, it will be with all your last modifications.

Example of function development:

For example, FuncModify.py:replace_code:

When writing the function, you specify some example input. Then, while writing it, it instancely also evaluates it. While editing, it tries to intelligently detect what to re-evaluate but the user can also do it manually.

