# Holberton School - AirBnB Clone Console

### Project Description:

This project creates an AirBnB console. The console serves as a command interpreter which enables the execution of commands to interact with the web application. This is the first step towards building our first full web application - in which we will use what we built during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

### Table of Contents

<ul>

<li>
<a href="#getting-started">Getting Started</a>
	<ul>
	<li><a href="#installation">Installation</a></li>
	<li><a href="#how-to-run-the-console">How to run the console</a></li>
	<li><a href="#testing">Testing</a></li>
	<li><a href="#command-reference">Command Reference</a></li>
	</ul>
</li>
<li>
<a href="#console-usage">Console Usage</a>
<ul>
<li><a href="#Examples-of-commands">Examples of commands</a></li>
<li><a href="#interactive-mode">Interactive Mode</a></li>
<li><a href="#non-interactive-mode">Non-interactive Mode</a></li>
</ul>
</li>
<li>
<a href="#authors">Authors</a>
</li>
</ul>

### Getting Started

### Installation:

Clone this repository to your local machine using the following command:

```
git clone https://github.com/yichehnc/holbertonschool-AirBnB_clone
```

You need to have Python3 installed in order to be able to use the console:

    sudo apt-get install python3

### How to run the console:

If you want to execute the console use:

     python3 console.py or ./console.py

### Testing:

We use these functions to test our work:

    python3 -m unittest discover tests

### Command Reference

| Command  | Explanation                                                                          | Example                                                    |
| -------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| `create` | Creates a new instance of `BaseModel` then saved to its JSON file and prints its ID. | `$ create BaseModel`                                       |
| `show`   | Displays info of an instance using its class name and ID.                            | `$ show BaseModel 001-002-003`                             |
| `all`    | Lists all instances, optionally filtered by class name.                              | `$ all BaseModel`                                          |
| `update` | Modifies an instance using its class name, ID, and given attribute.                  | `$ update BaseModel 001-002-003 email "example@email.com"` |

### How to use commands?

These interpreter commands can be used to aid you in handling data requirements:
| Command | Function |
| -------- | ------------------------------------------------- |
| create | create a new instance of a class |
| show | show the info of an instance of a class |
| destroy | destroy a instance of a class |
| update | update the info of the objects in an instance |
| all | update the info of the objects in an instance |
| quit | exit the console |
| help | show the help of the commands |

### Command Input Examples:

### Simple Commands

| Command | Example                                         |
| ------- | ----------------------------------------------- |
| create  | create [class name]                             |
| show    | show [class name] [id]                          |
| all     | create [class name] [id]                        |
| update  | create [class name] [id] [arg_name] [arg_value] |

### Alternative Commands

| Command                                                              | Example                                                                                              |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| [class name].all()                                                   | User.all()                                                                                           |
| [class name].count()                                                 | User.count()                                                                                         |
| [class name].show()                                                  | User.show()                                                                                          |
| [class name].destroy()                                               | User.destroy()                                                                                       |
| [class name].update([id], [attribute name], [attribute value].all()) | User.update("12345678-9012-3456-7890-123456789012", "first_name", "Betty")                           |
| (class name).update([id], [dictionary representation])               | User.update("12345678-9012-3456-7890-123456789012", {"first_name": "Betty", "last_name": Holberton}) |

### Reservation System Objects

These are objects that can be passed to the console:
| Object | Function |
|----------|-------------------------------------------|
| `city` | city of the reservation |
| `state` | country state of the reservation |
| `place` | name of the place of reservation |
| `user` | name of the user placed reservation |
| `amenity`| benefits of the place, its highlights |
| `review` | review of the room and guest |

### Console Usage

### Interactive Mode

To utilize the console in interactive mode, execute the subsequent command:

```bash
$ ./console.py
```

Once initiated, the console will present the `(hbnb)` prompt:

```bash
(hbnb)
```

#### Create a Model

Input the `create` command followed by your desired model name:

```bash
(hbnb) create User
```

Upon execution, the ID of the newly instantiated model will be showcased.

#### Display Model Attributes

To showcase the attributes of a designated model, use the command:

```bash
(hbnb) show User [id]
```

The console will then enumerate all attributes associated with the stipulated model.

#### Requesting Assistance

For an overview of permissible commands, input:

```bash
(hbnb) help
```

To conclude the interactive session, either employ the `Ctrl+D` keyboard shortcut or input the `quit` command.

### Non-Interactive Mode

The console's functionality extends to a non-interactive mode as evidenced below:

```bash
$ echo "create User" | ./console.py
$ echo "help" | ./console.py
```

### Data Management

Each time a model is instantiated, the information is stored in `file.json`, located within the primary directory.

### Authors

To contact the authors of this page and to review the code or submit pull requests, please visit:

- [Nick Ng](https://github.com/haoningng)
- [Yichen Cao](https://github.com/yichehnc)

<a href="#top">Back to top</a>
