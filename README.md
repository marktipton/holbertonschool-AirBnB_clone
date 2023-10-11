# holbertonschool-AirBnB_clone Console

![815046647d23428a14ca](https://github.com/kier-ious/holbertonschool-AirBnB_clone/assets/128427866/d0e97b32-f5fa-492a-a40b-65ddbb484a7e)

## Purpose
We created a mock property managemnt program with a simple command-line interface or, CLI. It is designed to manage various types of objects (users, states, cities) using a simple, text-based interface. The core files include *base_model.py* for defining a common object structure, *file_storage.py* for handling object storage in a JSON file, and model classes derived from the BaseModel. The *console.py* serves as the entry point and offers commands for creating, displaying, updating, and deleting instances of these models. Together, these components enable users to interact with and manage property-related data through the command line, making it a convenient and flexible tool for property management tasks.

## Files
```
.
├── AUTHORS
├── README.md
├── console.py
├── file.json
├── models
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── __init__.py
│   │   └── file_storage.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
└── tests
    ├── __init__.py
    └── test_models
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py

```

### `base_model.py`

- The `BaseModel` class is initialized with a unique `id`, `created_at`, and `updated_at` attributes.
- The `save()` method updates the `updated_at` attribute with the current datetime and saves the instance to the storage.
- The `to_dict()` method converts the instance to a dictionary representation.

### `file_storage.py`

This file defines a `FileStorage` class for serializing and deserializing instances to and from a JSON file. 
- The `FileStorage` class has methods for managing instances, such as `all()`, `new()`, `save()`, and `reload()`.
- `all()` returns a dictionary of all instances.
- `new(obj)` adds a new instance to the internal dictionary.
- `save()` serializes the instances to a JSON file.
- `reload()` deserializes the JSON file and populates the internal dictionary.

### `console.py`

This file serves as the entry point for a command-line interface (CLI). It uses the `cmd` module to interact with the user and provides commands for managing instances of various classes. Console commands:

- `quit`: Exits the program.
- `create`: Creates a new instance of a specified class.
- `show`: Prints the string representation of an instance.
- `destroy`: Destroys an instance.
- `all`: Prints the string representation of all instances of a specified class.
- `update`: Updates attributes of an instance.
- `help`: get information about commands or see available commands

## Usage examples in interactive mode
```
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
```
- Typing in the wrong class name or one that doesn't exits, you'll get this output. You want to make sure that the class that you're typing in the console matches exactly.
```
(hbnb) create city
** class doesn't exist **
(hbnb)
```
- You can then use the City ID and show method to print out string representation of an instance of the specified class.
```
(hbnb) create City
e023cb3e-9a57-473d-8e0b-e59f2800663f
(hbnb) show City e023cb3e-9a57-473d-8e0b-e59f2800663f
[City] (e023cb3e-9a57-473d-8e0b-e59f2800663f) {'id': 'e023cb3e-9a57-473d-8e0b-e59f2800663f', 'created_at': datetime.datetime(2023, 10, 10, 18, 38, 5, 54484), 'updated_at': datetime.datetime(2023, 10, 10, 18, 38, 5, 54600)}
(hbnb)
```
- You can update the City class while also adding an email address to it. 
```
(hbnb) create City
1cdce72c-ce33-446b-8b5d-91aec020176e
(hbnb) update City 1cdce72c-ce33-446b-8b5d-91aec020176e email "catdog@aol.com"
(hbnb) show City 1cdce72c-ce33-446b-8b5d-91aec020176e
[City] (1cdce72c-ce33-446b-8b5d-91aec020176e) {'id': '1cdce72c-ce33-446b-8b5d-91aec020176e', 'created_at': datetime.datetime(2023, 10, 10, 18, 47, 4, 417269), 'updated_at': datetime.datetime(2023, 10, 10, 18, 48, 17, 857187), 'email': '"catdog@aol.com"'}
```
### Usage examples in non-interactive Mode
```
root@b998a81b1124:/holbertonschool-AirBnB_clone# echo "create" Place | ./consol
e.py 
(hbnb) ce86f497-9b18-43ef-9a8c-a4adb816664e
(hbnb)
```

## Authors
- Kier McAlister: https://github.com/kier-ious

- Mark Tipton: https://github.com/marktipton
