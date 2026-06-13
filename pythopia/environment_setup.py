# IDE is the place you write the code, edit, and manage your project files. It provides features like code completion, debugging, and version control integration to enhance your coding experience.
# IDE stands for Integrated Development Environment. It is a software application that provides comprehensive facilities to computer programmers for software development. An IDE typically includes a code editor, a compiler or interpreter, and a debugger that the

"""
Package manager?
You use packages written by other people, a package manager automates the entire process of managing these libraries, including installation, updates, and dependency management. It ensures that you have the correct versions of libraries and their dependencies, making it easier to maintain your project and avoid conflicts between different packages.

"""

"""
How the file systems Works in UNIX_based systems?
everything starts from root: /
cd / --> goes to root

Actions:
ls --> list the content of the current directory
ls -l --> list the content of the current directory in long format (detailed information)
ls -a --> list all files, including hidden files (those starting with a dot)
ls -la --> list all files in long format (detailed information, including hidden files)
cd .. --> go to the parent directory
cd ~ --> go to the home directory
cd - --> go to the previous directory
cd /path/to/directory --> go to a specific directory
pwd --> print the current working directory

mkdir directory_name --> create a new directory
rmdir directory_name --> remove an empty directory
rm -r directory_name --> remove a directory and its contents
touch file_name --> create a new empty file or update the timestamp of an existing file
rm file_name --> remove a file

cp source_file destination_file --> copy a file
cp -r source_directory destination_directory --> copy a directory and its contents
mv source_file destination_file --> move or rename a file
mv source_directory destination_directory --> move or rename a directory

history --> show the command history
clear --> clear the terminal screen

wget url --> download a file from the specified URL

curl url --> transfer data from or to a server, can be used to download files or interact with APIs


"""

"""
One of the most well-known repositories is PyPI (Python Package Index), which is the official repository for Python packages. It hosts a vast collection of libraries and tools that can be easily installed using package managers like pip. Other popular repositories include npm for JavaScript, RubyGems for Ruby, and Maven Central for Java.

"""

"""
How to create an environment in conda?
conda create --name myenv python=3.8
How to activate the environment?
conda activate myenv
How to deactivate the environment?
conda deactivate
How to delete the environment?
conda remove --name myenv --all
To update the environment with new packages or updates, you can use:
conda install package_name
conda update package_name
How to see the list of environments?
conda env list
How to see the installed packages in the environment?
conda list
** even if you use "pip" to install packages in a conda environment, they will be available in that environment as well, but it's generally recommended to use "conda install" when working within a conda environment to ensure better compatibility and dependency management.
How to remove a package from the environment?
conda remove package_name
How to export the environment to a file?
conda env export > environment.yml
How to create an environment from a file?
conda env create -f environment.yml
how to see .yml file content?
cat environment.yml

"""
"""
When to create a new environment?
1. When working on a new project: Creating a new environment for each project helps to keep dependencies isolated and prevents conflicts between different projects.
2. When testing new packages or versions: If you want to try out a new package or a different version of an existing package, creating a new environment allows you to test it without affecting your existing projects.
3. When collaborating with others: If you're working on a project with other developers, creating a shared environment ensures that everyone is using the same dependencies and versions, which can help avoid compatibility issues.
4. When managing different Python versions: If you need to work with different versions of Python for different projects, creating separate environments allows you to easily switch between them without conflicts.
"""
