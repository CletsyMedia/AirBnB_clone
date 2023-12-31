# Echoes of Abodes: A Symphony in Code, the ALX AirBnB_clone Project

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231207%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231207T232946Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=60290bb3e38198070872a61e3cbcec780eaa17be22e269e64499afc283a63405)

## Project Overview

This project focuses on the backend development of an AirBnB clone, with an interface through a console application utilizing the `cmd` module in Python. Data, represented as Python objects, is generated and stored in a JSON file, accessible through the `json` module.

### Command Interpreter Description

The command-line interpreter mimics the Bash shell but is tailored for specific commands relevant to the AirBnB website. Serving as the frontend of the web app, users can interact with the backend developed using Python OOP programming.

### Available Commands

- `quit` or `EOF`: Exits the program.
- `help`: Provides information on how to use a command.
- `create`: Creates a new instance of a valid class and saves it to the JSON file.
- `show`: Prints the string representation of an instance based on the class name and ID.
- `destroy`: Deletes an instance based on the class name and ID.
- `all`: Prints all string representations of instances based on the class name.
- `update`: Updates an instance based on the class name and ID by adding or updating attributes.
- `count`: Retrieves the number of instances of a class.

The command line interpreter, coupled with the backend and file storage system, supports various actions, including creating new objects, retrieving objects, performing operations, updating attributes, and destroying objects.

## Getting Started

### Installation

Clone the repository from GitHub:

```bash
git clone https://github.com/CletsyMedia/AirBnB_clone.git
```

### Project Files

The project includes the following essential files:

- `console.py`: The main executable of the project, serving as the command interpreter.
- `models/engine/file_storage.py`: Class for serializing instances to a JSON file and deserializing from JSON.
- `models/__init__.py`: Unique FileStorage instance for the application.
- `models/base_model.py`: Class defining common attributes/methods for other classes.
- Additional classes: `user.py`, `state.py`, `city.py`, `amenity.py`, `place.py`, `review.py`.

### Usage

The program can run in two modes: Interactive and Non-interactive.

### Interactive Mode

```bash
./console.py
```

In this mode, a prompt (hbnb) appears, allowing users to enter commands.

### Non-Interactive Mode

```bash
echo "help" | ./console.py
```

In this mode commands can be piped into the shell for non-interactive mode.

```(hbnb)
Documented commands (type help <topic>):
========================================

EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

### Format of Command Input

Commands must be piped through `echo` in non-interactive mode. In interactive mode, commands are entered directly when the prompt appears.

## Arguments

Most commands support various options or arguments. Ensure proper spacing when entering parameters.

### Example

To create a `BaseModel` instance, use the command `create BaseModel` in the console. This will generate a unique identifier (id). To display the created `BaseModel` instance, use the command `show BaseModel` followed by the identifier. If you wish to destroy a `BaseModel` instance, you can use the `destroy` command with `BaseModel` and the identifier.

```bash
./console.py
(hbnb) create BaseModel
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
```

## Contact

For queries, echoes, and thoughts that bloom and fuss, don't hesitate to connect, in my haven. [Cletus Samuel](https://cletsymedia.github.io/Prof-Portfolio/)🙏🙏🙏🙏🙏🙏🙏
