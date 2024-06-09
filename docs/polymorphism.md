# Polymorphism

## Introduction to Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common super class. It is the ability of different objects to respond to the same method call in different ways. Polymorphism is typically achieved through method overriding and interfaces.

## Method Overriding

Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass. This allows the subclass to modify or extend the behavior of that method.

### Implementation

```php
<?php
class Animal {
    public function makeSound() {
        echo "Some generic animal sound\n";
    }
}

class Dog extends Animal {
    public function makeSound() {
        echo "Bark\n";
    }
}

class Cat extends Animal {
    public function makeSound() {
        echo "Meow\n";
    }
}

$animal = new Animal();
$dog = new Dog();
$cat = new Cat();

$animal->makeSound(); // Output: Some generic animal sound
$dog->makeSound(); // Output: Bark
$cat->makeSound(); // Output: Meow
?>
```

## Interfaces

An interface defines a contract for what methods a class must implement, without providing the method implementations. Interfaces allow you to specify what methods a class should implement, promoting the use of a consistent API.

### Implementation

```php
<?php
interface Shape {
    public function draw();
}

class Circle implements Shape {
    public function draw() {
        echo "Drawing a circle\n";
    }
}

class Square implements Shape {
    public function draw() {
        echo "Drawing a square\n";
    }
}

function drawShape(Shape $shape) {
    $shape->draw();
}

$circle = new Circle();
$square = new Square();

drawShape($circle); // Output: Drawing a circle
drawShape($square); // Output: Drawing a square
?>
```

## Abstract Classes and Methods

Abstract classes are classes that cannot be instantiated on their own and must be extended by other classes. An abstract class can contain abstract methods, which are methods declared without a body and must be implemented by subclasses.

### Implementation

```php
<?php
abstract class Animal {
    abstract public function makeSound();

    public function sleep() {
        echo "Sleeping\n";
    }
}

class Dog extends Animal {
    public function makeSound() {
        echo "Bark\n";
    }
}

class Cat extends Animal {
    public function makeSound() {
        echo "Meow\n";
    }
}

$dog = new Dog();
$cat = new Cat();

$dog->makeSound(); // Output: Bark
$dog->sleep(); // Output: Sleeping

$cat->makeSound(); // Output: Meow
$cat->sleep(); // Output: Sleeping
?>
```

## Examples

### Shape Interface

Here is an example of using an interface to define a contract for different shape classes:

```php
<?php
interface Shape {
    public function draw();
}

class Circle implements Shape {
    public function draw() {
        echo "Drawing a circle\n";
    }
}

class Square implements Shape {
    public function draw() {
        echo "Drawing a square\n";
    }
}

function drawShape(Shape $shape) {
    $shape->draw();
}

$circle = new Circle();
$square = new Square();

drawShape($circle); // Output: Drawing a circle
drawShape($square); // Output: Drawing a square
?>
```

### Abstract Class and Derived Classes

Here is an example of using an abstract class and derived classes to implement polymorphism:

```php
<?php
abstract class Animal {
    abstract public function makeSound();

    public function sleep() {
        echo "Sleeping\n";
    }
}

class Dog extends Animal {
    public function makeSound() {
        echo "Bark\n";
    }
}

class Cat extends Animal {
    public function makeSound() {
        echo "Meow\n";
    }
}

$dog = new Dog();
$cat = new Cat();

$dog->makeSound(); // Output: Bark
$dog->sleep(); // Output: Sleeping

$cat->makeSound(); // Output: Meow
$cat->sleep(); // Output: Sleeping
?>
```

In these examples, we have demonstrated how polymorphism can be achieved through method overriding, interfaces, and abstract classes in PHP. This allows for flexible and reusable code, where different classes can implement their own versions of methods defined in a common interface or abstract class.
