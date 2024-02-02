"""
The `os` library in Python is your Swiss Army knife for interacting with the underlying operating system from within your Python script. It's a powerful tool that lets you do all sorts of cool things, like:

    **File and directory management:**

* Create, move, rename, and delete files and directories
* List the contents of a directory
* Check if a file or directory exists
* Join paths correctly for different operating systems


       **Process management:**

* Execute shell commands
* Get information about running processes
* Control process behavior


       **Environment variables:**

* Access and modify environment variables
* Read the values of environment variables set by the system


       **System information:**

* Get the operating system name (e.g., "Linux", "Windows")
* Find out the current working directory
* Access system resources like disk space and network information

           **How it works:**

1. **Import time:** 
   The first step is to import the `os` module into your script:

```python
import os
```

2. **Choose your weapon:** 
   The `os` module offers a bunch of functions for different tasks. Choose the one you need and check the documentation for its arguments and usage:

3. **Remember portability:** 
   While the `os` module tries to be consistent across platforms, some functions might work differently on Windows vs. Linux, for example. Keep this in mind when writing portable code.

           **Bonus tip:** 
   For higher-level file and directory operations, check out the `shutil` module. It provides convenient functions for copying, moving, and deleting files and directories in bulk.
"""


# importing the os library
import os


#           File system operations include:
# Creating a new directory
os.mkdir("directory_name")

# removing directory
os.rmdir("directory_name")

# removing files
os.remove("filename")

# renaming a directory
os.rename("old_dir", "new_dir")

# listing directory contents
os.listdir("path")

# checking file existence and attributes
os.path.exists("path")

# getting file size
os.path.getsize("filename")

# getting modification time
os.path.getmtime("filename")

# changing file permissions


# Get the current working directory
current_dir = os.getcwd()
