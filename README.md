# Config API Documentation

## Introduction

The Config API is a Python module that allows users to manage configuration files in a structured way. It provides a simple interface to create, read, update, and delete configuration files in a specified directory.

## Installation

To use the Config API, simply import the `config` class from the module.

```python
from config_api import config
```

## Getting Started

The `config` class provides several methods to manage configuration files. Here are some examples of how to use them:

### List all configurations

```python
cfg = config()
all_configs = cfg.configs
print(all_configs)
```

This will return a list of all the configurations in the `./configs/` directory.

### Add a new configuration file

```python
data = {"key": "value"}
msg = cfg.add_config(data, "new_config", "path/to/dir")
print(msg)
```

This will create a new configuration file named `new_config.json` in the `./configs/path/to/dir/` directory with the contents of the `data` dictionary.

### Remove a configuration file

```python
msg = cfg.remove_config("config_to_remove", "path/to/dir")
print(msg)
```

This will remove the `config_to_remove.json` file from the `./configs/path/to/dir/` directory.

### Get the contents of a configuration file

```python
config_data = cfg.get_config("config_to_get", "path/to/dir")
print(config_data)
```

This will return the contents of the `config_to_get.json` file in the `./configs/path/to/dir/` directory.

## Conclusion

The Config API provides a simple interface to manage configuration files in a structured way. It is easy to use and can be integrated into any Python project.
