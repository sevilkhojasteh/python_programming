# this is how to push to github
# git add .
# git commit -m "Your descriptive message here"
# git push origin main

"""
Me writing code using programming language --> compiler/interpreter --> machine code --> computer executes the code

Programming Languages:
in the past: LOAD_A 14 : it means load the value 14 into register A
machine code, machine language = the binary code that the computer understands, it is made up of 0s and 1s. Each instruction is represented by a specific sequence of bits. For example, the instruction to load a value into a register might be represented by a specific binary code.
high-level description of a language: pseudocode, which is a way to describe algorithms in a human-readable format that is not tied to any specific programming language. It uses natural language and simple constructs to outline the logic of the code without worrying about syntax.
LOAD_A 14 is a assembly language instruction, which is a low-level programming language that is closely related to machine code. It provides a more human-readable way to write instructions that will be translated into machine code by an assembler. In this case, LOAD_A 14 would be translated into the corresponding machine code that tells the computer to load the value 14 into register A.

each line of assembly language corresponds to a specific machine code instruction. For example, if LOAD_A 14 is represented by the binary code 0001 1110 (where 0001 is the opcode for the load instruction and 1110 is the binary representation of the value 14), then when the assembler processes this line of assembly code, it will generate the corresponding machine code that the computer can execute.

Rust is an another new popular programming language that is designed for performance and safety, especially in systems programming. It provides memory safety without using a garbage collector, which makes it a good choice for performance-critical applications. Rust has a strong type system and ownership model that helps prevent common programming errors such as null pointer dereferencing and data
Maybe if you had time you can learn Rust as well, but for now we will focus on Python, which is a high-level programming language that is widely used for various applications, including web development, data analysis, artificial intelligence, and more. Python is known for its simplicity and readability, making it a great choice for beginners. It has a large standard library and a vibrant ecosystem of third-party packages that allow you to do almost anything you can imagine with code.

WHY PYTHON?
The syntax is really simple--> number of keyword is very small, and the code is very readable. It is a great language for beginners to learn programming concepts without getting bogged down by complex syntax. Python also has a large and active community, which means there are plenty of resources available for learning and troubleshooting. Additionally, Python is versatile and can be used for a wide range of applications, from web development to data science to machine learning. This makes it a valuable skill to have in the job market as well.
machine learning
web development-->django, flask
data analysis-->pandas, numpy
automation-->selenium, pyautogui
game development-->pygame
GUI development-->tkinter, PyQt


PYTHON:
Dynamic typing: you don't need to declare the type of a variable, it is determined at runtime. 
Eaxmple:
x = 5
x = "hello"
x = [1, 2, 3]
Memory management: Python uses automatic memory management, which means that it handles memory allocation and deallocation for you. This makes it easier to write code without worrying about memory leaks or other issues related to manual memory management.
Example:
a = [1, 2, 3]
a = [4, 5, 6] # the memory allocated for the original list [1, 2, 3] will be automatically deallocated when it is no longer referenced
Extensive standard library: Python comes with a large standard library that provides a wide range of modules and functions for various tasks, such as file I/O, regular expressions, networking, and more. This allows you to accomplish many tasks without needing to install additional packages.
Example:
import os
Third-party packages: In addition to the standard library, Python has a vast ecosystem of third-party packages that can be easily installed using tools like pip. These packages cover a wide range of functionalities, from web development frameworks to data analysis libraries to machine learning tools.
Example:
import numpy as np
Object-oriented programming: Python supports object-oriented programming (OOP) paradigms, which allows you to create classes and objects to organize your code and model real-world entities. This can help improve code reusability and maintainability.
Example:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age  

Data analysis and machine learning: Python has become the go-to language for data analysis and machine learning due to its powerful libraries such as NumPy, pandas, scikit-learn, and TensorFlow. These libraries provide efficient tools for data manipulation, analysis, and building machine learning models.
Example:
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
"""


