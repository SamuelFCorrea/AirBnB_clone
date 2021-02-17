# AirBnB_clone

The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy inn our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

#### Functionalities of this command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

## Get started
* Clone the repository `$ git clone https://github.com/SamuelFCorrea/AirBnB_clone.git`
* Open the command line `$ ./console` (Also in non-interactive mode `echo "create User" | ./console`)
#### Usage
* `EOF` - `$ EOF`
* `quit`- `$ quit`
* `create` - `$ create <class name>` or `$ <class name>.create()`
* `destroy` - `$ destroy <class name> <id>` or `$ <class name>.destroy(<id>)`
* `show` - `$ show <class name <id>` or `$ <class name>.show(<id>)`
* `all` - `$ all` or `$ all <class name>` or `$ <class name>.all`
* `update`- `$ update <class name> <id> <attribute name> <attribute value>` or `$ <class name>.update(<id>, <attribute name>, <attribute value>)`