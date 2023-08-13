# Description

Boilerplate <u>logging code</u> that is a good starting point for any Python project.

Based on the native `logging` module of Python.

This Python project is modeled on a simple ETL pipeline where you have some data loading modules. In addition there is a folder of `util` modules, one of which is the `logger_util` module. Finally, you have the `main` runner of the whole pipeline, as the top level orchestrator. That is the entry point of the code, and when you hit run on that module the whole pipeline kicks off and you can see the log statements in your console.