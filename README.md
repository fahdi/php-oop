# php-oop

Want to learn PHP OOP from scratch? This repository contains a step-by-step guide to mastering Object-Oriented Programming (OOP) in PHP. Let's dive in!

Let's start with the basics of Object-Oriented Programming (OOP) in PHP and gradually move towards design patterns.

### Introduction to Object-Oriented Programming (OOP) in PHP

#### 1. Basic Concepts of OOP:
- **[Class](classes.md)**: A blueprint for creating objects (a particular data structure), providing initial values for state (member variables or properties), and implementations of behavior (member functions or methods).
- **Object**: An instance of a class.
- **Property**: A variable that belongs to a class.
- **Method**: A function that belongs to a class.
- **Inheritance**: A mechanism for a new class to inherit properties and methods of an existing class.
- **Encapsulation**: The bundling of data with the methods that operate on that data.
- **Polymorphism**: The ability to present the same interface for different underlying data types.
- **Abstraction**: The concept of hiding the complex implementation details and showing only the essential features of the object.

#### 2. Creating Classes and Objects

Here's a basic example to illustrate these concepts:

```php
<?php
class Car {
    // Properties
    public $make;
    public $model;
    private $year;

    // Constructor
    public function __construct($make, $model, $year) {
        $this->make = $make;
        $this->model = $model;
        $this->year = $year;
    }

    // Method
    public function displayInfo() {
        return "Make: " . $this->make . ", Model: " . $this->model . ", Year: " . $this->year;
    }

    // Getter for private property
    public function getYear() {
        return $this->year;
    }

    // Setter for private property
    public function setYear($year) {
        $this->year = $year;
    }
}

// Creating an object
$car = new Car("Toyota", "Corolla", 2020);
echo $car->displayInfo(); // Output: Make: Toyota, Model: Corolla, Year: 2020
?>
```

### Step-by-Step Guide to Mastering PHP OOP

#### [Step 1: Understanding Classes and Objects](classes.md)
- Create simple classes with properties and methods.
- Instantiate objects from these classes.
- Practice using constructors to initialize object properties.

#### [Step 2: Encapsulation](encapsulation.md)
- [Use public, private, and protected access modifiers.](encapsulation.md#example-1-using-public-private-and-protected-access-modifiers)
- [Create getter and setter methods for accessing and modifying private properties.](encapsulation.md#encapsulation-with-getter-and-setter-methods)

#### Step 3: Inheritance
- Create a base class and extend it with child classes.
- Override methods in the child class.
- Use the `parent` keyword to access methods and properties of the parent class.

#### Step 4: Polymorphism
- Implement method overriding.
- Use interfaces to define method signatures that multiple classes can implement.
- Implement abstract classes and methods.

#### Step 5: Abstraction
- Create abstract classes with abstract methods.
- Ensure that child classes implement the abstract methods.

#### Step 6: Design Patterns
- Learn about common design patterns like Singleton, Factory, Strategy, Observer, etc.
- Implement these patterns in small projects to understand their usage and benefits.

### Example: Inheritance and Polymorphism

```php
<?php
// Base class
abstract class Animal {
    public $name;

    public function __construct($name) {
        $this->name = $name;
    }

    // Abstract method
    abstract public function makeSound();
}

// Child class
class Dog extends Animal {
    public function makeSound() {
        return "Bark";
    }
}

// Child class
class Cat extends Animal {
    public function makeSound() {
        return "Meow";
    }
}

// Using polymorphism
$animals = [
    new Dog("Rex"),
    new Cat("Whiskers")
];

foreach ($animals as $animal) {
    echo $animal->name . " says " . $animal->makeSound() . "\n";
}
?>
```

### Moving Forward

1. **Practice Exercises**:
    - Create a few simple classes and objects.
    - Implement inheritance and polymorphism in small projects.

2. **Advanced Concepts**:
    - Study and implement interfaces and traits.
    - Explore namespaces for better code organization.

3. **Design Patterns**:
    - Start with simple patterns like Singleton and Factory.
    - Gradually move to more complex patterns like Observer and Strategy.

4. **Resources**:
    - **Books**: "PHP Objects, Patterns, and Practice" by M. Zandstra.
    - **Online Courses**: Look for PHP OOP courses on platforms like Udemy, Coursera, etc.
    - **Documentation**: Official PHP documentation for OOP concepts.


