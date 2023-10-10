# holbertonschool-AirBnB_clone Console

![815046647d23428a14ca](https://github.com/kier-ious/holbertonschool-AirBnB_clone/assets/128427866/d0e97b32-f5fa-492a-a40b-65ddbb484a7e)

## Purpose

## Files

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
- 'help': get information about commands or see available commands

## Usage

### Interactive Mode

### Non-interactive Mode

## Bugs

## Authors

## License
