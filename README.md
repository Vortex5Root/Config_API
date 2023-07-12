# Documentation

## Introduction

This documentation provides an overview of the Python code in the Config_API repository, which includes the `Config` class for managing configuration files. The code allows you to create, load, save, and modify JSON-based configuration files easily.

## Installation

To install the `Config_API` package from the provided GitHub repository, use the following command:

```bash
poetry add git+https://github.com/Vortex5Root/Config_API.git
```

## How to use

### Config Class

#### Creating a Configuration Instance

To create a new configuration instance, use the `Config` class provided by the `Config_API` package. You can specify the name of the configuration file during initialization. Here's an example:

```python
from Config_API import Config

# Example
config = Config("example")
```

#### Setting the Configuration Path

You can set the path for the configuration files using the `path` property of the `Config` instance. By default, the path is set to `"./config/"`. Here's an example of setting a custom path:

```python
config.path = "example_folder"
```

#### Changing the Configuration File

You can change the configuration file within the specified path using the `file_name` property of the `Config` instance. Here's an example:

```python
config.file_name = "new_example"
```

#### Loading a Configuration File

To load a configuration file, use the `load()` method of the `Config` instance. By default, it loads the file from the current path. However, you can specify a different folder by passing it as an argument. Here's an example:

```python
config.load()  # Load from the current path
config.load("custom_folder")  # Load from a custom folder
```

#### Saving a Configuration File

To save the current configuration to a file, use the `save()` method of the `Config` instance. By default, it saves the file to the current path. You can also specify a different folder by passing it as an argument. Here's an example:

```python
config.save()  # Save to the current path
config.save("custom_folder")  # Save to a custom folder
```

#### Modifying the Configuration

Once the configuration file is loaded, you can access and modify its contents through the `config` attribute of the `Config` instance, which represents the JSON data. Here's an example:

```python
config.config["key"] = "value"  # Add or modify a key-value pair
```

### Example Usage

Here's an example code snippet demonstrating the usage of the `Config` class:

```python
from Config_API import Config

# Example
config = Config("example")
config.path = "example_folder"
config.file_name = "new_example"
config.load()
print(config.config)
config.config["row"] = "value"
config.save()
```

## Conclusion

The `Config_API` package provides a convenient way to manage configuration files in Python. By using the `Config` class, you can create, load, save, and modify JSON-based configuration files with ease. Feel free to explore the code and customize it according to your needs.