# Ops Challenge: Psutil

## Overview

Python is known for its versatile and diverse selection of libraries. Libraries are installable toolkits that add new functions to the language on your system. Today you will use Psutil to fetch system information.

`psutil` stands for "process and system utilities". It is a Python library used for system monitoring, resource management, and process control. It allows you to retrieve detailed information about running processes, including their CPU and memory usage, process IDs (PIDs), parent-child relationships, process creation time, and termination of processes. It also enables you to monitor system resources in real-time by providing functions to track network activity, disk I/O, and process-related metrics.

Common functionalities provided by `psutil`:
- Process Management
  - Get a list of running processes.
  - Retrieve information about a specific process, such as its PID (Process ID), name, status, CPU and memory usage, and more.
  - Terminate or send signals to processes.
- System Information
  - Retrieve system-wide information such as CPU count, CPU utilization, memory usage, disk partitions, and network statistics.
  - Get information about system uptime and boot time.
- Disk and Network Monitoring
  - Monitor disk usage, including available and total disk space.
  - Monitor network statistics, such as network connections and network I/O.
- Sensor Information (on some platforms)
  - Access sensor information, such as temperature and fan speed.

`psutil` is platform-independent and works on various operating systems, including Windows, macOS, and different Linux distributions. It provides a consistent API to access system information, making it easier to write cross-platform code that deals with system resources.

Here's a basic example of how to use `psutil` to retrieve CPU and memory information:

```python
import psutil

# Get CPU information
cpu_count = psutil.cpu_count()
cpu_percent = psutil.cpu_percent(interval=1)  # CPU usage percentage over 1 second

# Get memory information
memory_info = psutil.virtual_memory()

print(f"CPU Count: {cpu_count}")
print(f"CPU Usage Percent: {cpu_percent}%")
print(f"Total Memory: {memory_info.total} bytes")
print(f"Available Memory: {memory_info.available} bytes")
```

Keep in mind that you may need to install the `psutil` library using a package manager like pip (`pip install psutil`) before using it in your Python code.

## Floats in Python

In Python, a **float** is a data type that represents decimal numbers, also known as floating-point numbers. Floats are used to store real numbers, including both integers and numbers with fractional parts. They are a fundamental part of the Python language and are widely used for performing mathematical operations that involve non-integer values.

Key characteristics of float numbers in Python:

**Representation**: Floats are represented using the IEEE 754 standard for double-precision floating-point numbers, which allows them to store a wide range of values, including very large and very small numbers.

**Syntax**: Float literals can be created by writing a number with a decimal point (e.g., `3.14`) or by using scientific notation (e.g., `2.0e-3` represents 0.002).

**Operations**: Floats can be used in arithmetic operations like addition, subtraction, multiplication, and division. Python's math module provides additional mathematical functions and constants for working with floats.

  ```python
  a = 3.5
  b = 2.0

  # Basic arithmetic operations
  result_addition = a + b
  result_subtraction = a - b
  result_multiplication = a * b
  result_division = a / b

  print(result_addition)        # 5.5
  print(result_subtraction)     # 1.5
  print(result_multiplication)  # 7.0
  print(result_division)        # 1.75
  ```

**Precision**: Floats have limited precision due to the finite number of bits used to represent them. This can lead to rounding errors in certain calculations. For critical applications requiring high precision, Python provides the `decimal` module, which allows for arbitrary-precision arithmetic.

  ```python
  from decimal import Decimal

  a = Decimal("0.1")
  b = Decimal("0.2")
  result = a + b

  print(result)  # 0.3
  ```

**Conversion**: You can convert other data types to floats using the `float()` constructor, and you can convert floats to integers using the `int()` constructor, which truncates the fractional part.

   ```python
   float_num = float("3.14")
   int_num = int(3.9)

   print(float_num)  # 3.14
   print(int_num)    # 3
   ```

## `repr()` in Python

In Python, `repr()` is a built-in function that returns a string representation of an object. The name "repr" stands for "representation," and the purpose of this function is to provide a representation of an object that can be used to recreate the object, or at least provide detailed information about it, typically for debugging and development purposes.

The primary use cases of `repr()` are as follows:

**Debugging and Development**: When you're debugging code or developing a program, you may want to inspect the contents of objects, especially custom objects you've created. The `repr()` function provides a human-readable string that helps you understand the internal state of an object.

**Unambiguous Representation**: The string returned by `repr()` is often unambiguous and can be used to recreate the original object using `eval()` or by passing it to the constructor of the object's class (assuming the class has implemented an appropriate `__repr__()` method). This can be useful for serialization or creating objects dynamically.

Here's a basic example of how `repr()` is used:

```python
class MyClass:
  def __init__(self, value):
    self.value = value

  def __repr__(self):
    return f"MyClass({self.value})"

obj = MyClass(42)
print(repr(obj))  # Output: MyClass(42)
```

In this example, the `__repr__()` method is defined for the `MyClass` class to provide a string representation of the object. When `repr(obj)` is called, it returns a string that, when executed as Python code, would recreate the object.

It's important to note that the `repr()` function is distinct from the `str()` function. The primary difference is in their intended use cases:

- `repr()` aims for unambiguous, developer-friendly representations that can recreate the object.
- `str()` aims for a more user-friendly, human-readable representation of the object. If an object does not define a `__str__()` method, Python will fall back to using the `__repr__()` method if it exists.

For many built-in data types, `repr()` and `str()` return similar or identical results. However, custom classes can provide distinct implementations for these methods to cater to different use cases.

## `str()` in Python

In Python, `str()` is a built-in function used to convert an object into its string representation. This function returns a human-readable string that represents the object. The primary purpose of `str()` is to provide a text-based representation of an object that is suitable for display to users or for creating formatted output.

Here are the key aspects of `str()` in Python:

**Converting Objects to Strings**: You can use `str()` to convert various types of objects into strings. This includes numbers, lists, dictionaries, custom objects, and more. When called on an object, Python looks for the object's `__str__()` method to determine how it should be represented as a string.

**Human-Readable Representation**: The primary goal of `str()` is to provide a human-readable representation of an object. This means that the resulting string should be easy for people to understand. It is often used for logging, printing, or displaying information to users.

**Fallback to `repr()`**: If an object does not define a `__str__()` method, Python will fall back to using the `__repr__()` method (if it exists) to generate the string representation. However, it is generally recommended to provide a custom `__str__()` method for user-friendly string representations when necessary.

Here's a basic example of using `str()`:

```python
class MyClass:
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return f"MyClass instance with value: {self.value}"

obj = MyClass(42)
str_representation = str(obj)
print(str_representation)  # Output: "MyClass instance with value: 42"
```

In this example, the `__str__()` method is defined for the `MyClass` class to provide a custom string representation when `str()` is called on an instance of the class.

It's worth noting that while `str()` aims to provide human-readable representations, `repr()` is more focused on creating unambiguous representations that can be used to recreate an object. In many cases, you'll want to implement both `__str__()` and `__repr__()` methods in your custom classes to cater to different use cases: one for human-readable output and the other for debugging and development purposes.

## Resources

- [`psutil` Documentation](https://psutil.readthedocs.io/en/latest/){:target="blank"}
- [Python libraries and their features](https://www.codingninjas.com/blog/2020/07/24/python-libraries-and-their-features/){:target="blank"}
  - This article defines the terms module, package, and library in the context of understanding what libraries are.
- [Psutil module in Python](https://www.geeksforgeeks.org/psutil-module-in-python/){:target="blank"}
- [Five Python libraries for cyber security](https://medium.com/ediblesec/5-python-libraries-for-cyber-security-8f34f5f1e3b8){:target="blank"}
  - If you're wondering what libraries you should be practicing to prepare yourself for a cyber role, have a look at Chris Doucette's top five in this article. The libraries mentioned in this article (requests and nmap in particular) should be used ethically and with a firm comprehension of what the tools do and any legal liabilities that may arise from improper use.

## Demonstration

Refer to [DEMO.md](DEMO.md)

## Notes

1. Fill in the details of some methods you might be working with in this challenge.
    - `psutil.cpu_times()`
      - description: It provides information about how the CPU time is distributed across different activities.
      - input: This method does not require any input parameters.
      - output: The output is a tuple containing the CPU times for various categories, such as user mode, system mode, idle time, interrupt time, and more.
    - `psutil.cpu_percent()`
      - description: This method calculates the CPU usage percentage for the whole system or a specific CPU. It measures the percentage of time that the CPU is being utilized by processes.
      - input: It accepts an optional parameter interval which specifies the duration (in seconds) over which the CPU usage is averaged. By default, it uses a 1-second interval.
      - output: The output is a float value representing the CPU usage percentage. It indicates how much of the CPU's processing capacity is currently being used by running processes during the specified interval.
    - `psutil.cpu_times().user`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().system`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().idle`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().nice`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().iowait`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().irq`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().softirq`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().steal`
      - description:
      - input:
      - output:
    - `psutil.cpu_times().guest`
      - description:
      - input:
      - output:

