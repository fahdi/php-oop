# Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit properties and methods from another class. It establishes an "is-a" relationship between classes, enabling code reuse and the creation of class hierarchies. In PHP, inheritance is implemented using the `extends` keyword.

### Example: Inheritance

```php
<?php
// Base class
class Animal {
    public $name;

    public function __construct($name) {
        $this->name = $name;
    }

    public function makeSound() {
        return "Animal sound";
    }
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

// Create objects of child classes
$dog = new Dog("Rex");
$cat = new Cat("Whiskers");

echo $dog->name . " says " . $dog->makeSound() . "\n"; // Output: Rex says Bark
echo $cat->name . " says " . $cat->makeSound() . "\n"; // Output: Whiskers says Meow
?>
```

In this example:

- The `Animal` class is the base class.
- The `Dog` and `Cat` classes inherit from `Animal` and override the `makeSound` method to provide specific implementations.

### Summary

- **Inheritance** allows a class to inherit properties and methods from another class.
- The `extends` keyword is used to implement inheritance in PHP.
- **Child classes** can override methods from the parent class to provide specific implementations.
- Inheritance helps in **code reusability** and promotes code organization and modularity.
- Inheritance establishes an **"is-a" relationship** between classes, where a child class is a specialized version of the parent class.

### Key Points

- **Code Reusability**: Inheritance allows you to reuse existing code by creating a new class that extends an existing class.
- **Method Overriding**: Child classes can provide specific implementations for methods defined in the parent class.
- **Hierarchy Creation**: Inheritance can be used to create class hierarchies, where each level adds more specific behavior.
- **Combined with Other OOP Concepts**: Inheritance works well with other OOP concepts like polymorphism, encapsulation, and abstraction.
- **Real-World Modeling**: Inheritance helps model real-world relationships between entities and objects.

### Additional Resources

- [PHP Manual: Inheritance](https://www.php.net/manual/en/language.oop5.inheritance.php)
- [PHP Object-Oriented Programming (OOP) - Inheritance](https://www.tutorialrepublic.com/php-tutorial/php-oop-inheritance.php)
- [PHP Inheritance Tutorial](https://www.w3schools.com/php/php_oop_inheritance.asp)
- [PHP Object-Oriented Programming: Inheritance](https://www.codecademy.com/articles/what-is-inheritance)
- [PHP Inheritance and Interfaces](https://www.geeksforgeeks.org/php-inheritance-and-interfaces/)
- [PHP OOP: Inheritance and Polymorphism](https://www.javatpoint.com/php-oops-inheritance-and-polymorphism)
