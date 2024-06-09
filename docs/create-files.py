import os

# List of markdown files to be created
files = [
    'classes.md',
    'encapsulation.md',
    'inheritance.md',
    'polymorphism.md',
    'abstraction.md',
    'namespaces.md',
    'exceptions.md',
    'design-patterns.md',
    'real-world-applications.md'
]

# Content for each markdown file
content = {
    'classes.md': '# Classes and Objects\n\n## Introduction to Classes and Objects\n\n## Defining a Class\n\n## Creating Objects\n\n## Using Constructors\n\n## Class Methods\n\n## Properties\n\n## Static Properties and Methods\n\n## Constants\n\n## Examples\n\n### Car Class\n\n### Book Class\n\n### Student Class\n\n### Product Class\n\n### Movie Class\n',
    'encapsulation.md': '# Encapsulation\n\n## Introduction to Encapsulation\n\n## Public, Private, and Protected Access Modifiers\n\n## Getters and Setters\n\n## Magic Methods: `__get`, `__set`, `__call`\n\n## Examples\n\n### User Class\n\n### Person Class with Getters and Setters\n',
    'inheritance.md': '# Inheritance\n\n## Introduction to Inheritance\n\n## Simple Inheritance\n\n## The `parent` Keyword\n\n## Overriding Methods\n\n## Final Keyword\n\n## Traits\n\n## Examples\n\n### Animal and Dog Classes\n\n### ParentClass and ChildClass\n',
    'polymorphism.md': '# Polymorphism\n\n## Introduction to Polymorphism\n\n## Method Overriding\n\n## Interfaces\n\n## Abstract Classes and Methods\n\n## Examples\n\n### Shape Interface\n\n### Abstract Class and Derived Classes\n',
    'abstraction.md': '# Abstraction\n\n## Introduction to Abstraction\n\n## Abstract Classes\n\n## Abstract Methods\n\n## Examples\n\n### Abstract Vehicle Class\n\n### Implementing Abstract Methods\n',
    'namespaces.md': '# Namespaces\n\n## Introduction to Namespaces\n\n## Defining Namespaces\n\n## Using Namespaces\n\n## Namespace Aliases\n\n## Examples\n\n### Organizing Classes with Namespaces\n',
    'exceptions.md': '# Exception Handling\n\n## Introduction to Exception Handling\n\n## Try, Catch, and Finally\n\n## Custom Exceptions\n\n## Examples\n\n### Handling Exceptions in a PHP Application\n',
    'design-patterns.md': '# Design Patterns\n\n## Introduction to Design Patterns\n\n## Singleton Pattern\n\n## Factory Pattern\n\n## Observer Pattern\n\n## Strategy Pattern\n\n## Examples\n\n### Using Design Patterns in PHP\n',
    'real-world-applications.md': '# Real-World Applications\n\n## Building a Simple Blog\n\n### Requirements and setup\n\n### Implementation steps\n\n## Building a Shopping Cart\n\n### Requirements and setup\n\n### Implementation steps\n\n## Building a User Authentication System\n\n### Requirements and setup\n\n### Implementation steps\n'
}

# Create each file if it doesn't exist and write the corresponding content
for file in files:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            f.write(content[file])
        print(f"Created {file}")
    else:
        print(f"{file} already exists")
