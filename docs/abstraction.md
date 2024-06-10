# Abstraction

## Introduction to Abstraction

Abstraction is one of the core principles of object-oriented programming (OOP). It involves the concept of hiding the complex implementation details and showing only the essential features of the object. Abstraction allows you to focus on what an object does instead of how it does it. In PHP, abstraction is achieved using abstract classes and abstract methods.

## Abstract Classes

An abstract class is a class that cannot be instantiated on its own and must be extended by other classes. It can contain both abstract methods (methods without implementation) and concrete methods (methods with implementation). Abstract classes are defined using the `abstract` keyword.

### Example

```php
<?php
abstract class Animal {
    public $name;

    public function __construct($name) {
        $this->name = $name;
    }

    abstract public function makeSound();

    public function sleep() {
        echo "$this->name is sleeping.\n";
    }
}
?>
```

## Abstract Methods

An abstract method is a method that is declared but not implemented in the abstract class. Subclasses that extend the abstract class must implement the abstract methods. Abstract methods are also defined using the `abstract` keyword.

### Example

```php
<?php
abstract class Animal {
    public $name;

    public function __construct($name) {
        $this->name = $name;
    }

    abstract public function makeSound();

    public function sleep() {
        echo "$this->name is sleeping.\n";
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

$dog = new Dog('Rover');
$dog->makeSound(); // Output: Bark
$dog->sleep(); // Output: Rover is sleeping.

$cat = new Cat('Whiskers');
$cat->makeSound(); // Output: Meow
$cat->sleep(); // Output: Whiskers is sleeping.
?>
```

## Examples

### Abstract Vehicle Class

In this example, we define an abstract class `Vehicle` with abstract methods `startEngine` and `stopEngine`. Concrete classes `Car` and `Motorcycle` extend the `Vehicle` class and implement the abstract methods.

```php
<?php
abstract class Vehicle {
    public $make;
    public $model;

    public function __construct($make, $model) {
        $this->make = $make;
        $this->model = $model;
    }

    abstract public function startEngine();
    abstract public function stopEngine();

    public function getDetails() {
        return "Make: $this->make, Model: $this->model";
    }
}

class Car extends Vehicle {
    public function startEngine() {
        echo "Starting the car engine.\n";
    }

    public function stopEngine() {
        echo "Stopping the car engine.\n";
    }
}

class Motorcycle extends Vehicle {
    public function startEngine() {
        echo "Starting the motorcycle engine.\n";
    }

    public function stopEngine() {
        echo "Stopping the motorcycle engine.\n";
    }
}

$car = new Car('Toyota', 'Corolla');
echo $car->getDetails() . "\n"; // Output: Make: Toyota, Model: Corolla
$car->startEngine(); // Output: Starting the car engine.
$car->stopEngine(); // Output: Stopping the car engine.

$motorcycle = new Motorcycle('Yamaha', 'MT-07');
echo $motorcycle->getDetails() . "\n"; // Output: Make: Yamaha, Model: MT-07
$motorcycle->startEngine(); // Output: Starting the motorcycle engine.
$motorcycle->stopEngine(); // Output: Stopping the motorcycle engine.
?>
```

### Implementing Abstract Methods

In this example, we define an abstract class `Shape` with abstract methods `calculateArea` and `calculatePerimeter`. Concrete classes `Circle` and `Rectangle` extend the `Shape` class and implement the abstract methods.

```php
<?php
abstract class Shape {
    abstract public function calculateArea();
    abstract public function calculatePerimeter();

    public function displayDetails() {
        echo "Area: " . $this->calculateArea() . "\n";
        echo "Perimeter: " . $this->calculatePerimeter() . "\n";
    }
}

class Circle extends Shape {
    private $radius;

    public function __construct($radius) {
        $this->radius = $radius;
    }

    public function calculateArea() {
        return pi() * pow($this->radius, 2);
    }

    public function calculatePerimeter() {
        return 2 * pi() * $this->radius;
    }
}

class Rectangle extends Shape {
    private $width;
    private $height;

    public function __construct($width, $height) {
        $this->width = $width;
        $this->height = $height;
    }

    public function calculateArea() {
        return $this->width * $this->height;
    }

    public function calculatePerimeter() {
        return 2 * ($this->width + $this->height);
    }
}

$circle = new Circle(5);
$circle->displayDetails();
// Output:
// Area: 78.539816339745
// Perimeter: 31.4159265358979

$rectangle = new Rectangle(4, 6);
$rectangle->displayDetails();
// Output:
// Area: 24
// Perimeter: 20
?>
```
