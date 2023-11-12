# 0x00. AirBnB clone - The console

## Description

This project is part of the AirBnB clone series - a larger project to build a complete web application replicating the AirBnB platform. In this specific segment, we focus on building the command interpreter (console) to manage AirBnB objects.

The console will:
- Create new objects (e.g., User, Place)
- Retrieve an object from a file or database
- Perform operations on objects (e.g., count, compute stats)
- Update attributes of an object
- Destroy an object

## How to Start the Console

To start the console in interactive mode, run:

```
$ ./console.py
```

In non-interactive mode, use:

```
$ echo "<command>" | ./console.py
```

## Usage

Here are some common commands you can use in the console:

- `help`: Displays a list of available commands.
- `quit`: Exits the console.
- `create <class name>`: Creates a new instance of a given class, saves it (to the JSON file) and prints the id. If the class name is missing or doesn't exist, appropriate error messages are displayed.
- `show <class name> <id>`: Retrieves and prints the string representation of a specific instance of a class based on its id. If the class name is missing, doesn't exist, or the instance id is missing or not found, appropriate error messages are displayed.
- `destroy <class name> <id>`: Deletes an instance of a class based on its id, and saves the change into the JSON file. Error messages are displayed if the class name is missing, doesn't exist, the id is missing, or the instance is not found.
- `all [<class name>]`: Prints all instances, or if a class name is provided, all instances of that class. If the class name doesn't exist, an error message is displayed.
- `update <class name> <id> <attribute name> "<attribute value>"`: Updates an instance based on the class name and id by adding or updating an attribute, and saves the change to the JSON file. Only one attribute can be updated at a time. The command includes checks for missing class name, non-existing class, missing id, instance not found, missing attribute name, and missing value for the attribute.

## Examples

Creating a new User:

```
(hbnb) create User
```

Retrieving a User instance:

```
(hbnb) show User <user_id>
```

## Authors

This project was created by:
- [Amine Lamuadni](https://github.com/aminelamuadni/)

For a full list of contributors, see the `AUTHORS` file.
