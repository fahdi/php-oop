# Design Patterns

## Introduction to Design Patterns

Design patterns are proven solutions to common software design problems. They provide a template for writing code that is easy to understand, maintain, and extend. By using design patterns, you can avoid common pitfalls and improve the overall quality of your code.

## Singleton Pattern

The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. This is useful when exactly one object is needed to coordinate actions across the system.

### Implementation

```php
<?php
class Singleton {
    private static $instance;

    private function __construct() {
        // private constructor to prevent external instantiation
    }

    public static function getInstance() {
        if (self::$instance === null) {
            self::$instance = new Singleton();
        }
        return self::$instance;
    }
}
?>
```

## Factory Pattern

The Factory pattern defines an interface for creating an object, but allows subclasses to alter the type of objects that will be created. This pattern is useful when the exact type of the object to be created is not known until runtime.

### Implementation

```php
<?php
interface Product {
    public function getType();
}

class ConcreteProductA implements Product {
    public function getType() {
        return "Product A";
    }
}

class ConcreteProductB implements Product {
    public function getType() {
        return "Product B";
    }
}

class Factory {
    public static function createProduct($type) {
        if ($type === 'A') {
            return new ConcreteProductA();
        } elseif ($type === 'B') {
            return new ConcreteProductB();
        }
        throw new Exception("Invalid product type");
    }
}
?>
```

## Observer Pattern

The Observer pattern defines a one-to-many relationship between objects so that when one object changes state, all its dependents are notified and updated automatically. This pattern is commonly used in implementing distributed event-handling systems.

### Implementation

```php
<?php
interface Observer {
    public function update($data);
}

class ConcreteObserver implements Observer {
    public function update($data) {
        echo "Observer notified with data: $data\n";
    }
}

class Subject {
    private $observers = [];
    private $state;

    public function attach(Observer $observer) {
        $this->observers[] = $observer;
    }

    public function setState($state) {
        $this->state = $state;
        $this->notify();
    }

    public function getState() {
        return $this->state;
    }

    private function notify() {
        foreach ($this->observers as $observer) {
            $observer->update($this->state);
        }
    }
}
?>
```

## Strategy Pattern

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern allows the algorithm to vary independently from clients that use it.

### Implementation

```php
<?php
interface Strategy {
    public function execute($data);
}

class ConcreteStrategyA implements Strategy {
    public function execute($data) {
        echo "Executing strategy A with data: $data\n";
    }
}

class ConcreteStrategyB implements Strategy {
    public function execute($data) {
        echo "Executing strategy B with data: $data\n";
    }
}

class Context {
    private $strategy;

    public function setStrategy(Strategy $strategy) {
        $this->strategy = $strategy;
    }

    public function executeStrategy($data) {
        $this->strategy->execute($data);
    }
}
?>
```

## Examples

### Using Design Patterns in PHP

Here is an example of using the Factory and Singleton patterns together to create a simple logging system.

```php
<?php
// Singleton Logger Class
class Logger {
    private static $instance;
    private $logs = [];

    private function __construct() {}

    public static function getInstance() {
        if (self::$instance === null) {
            self::$instance = new Logger();
        }
        return self::$instance;
    }

    public function log($message) {
        $this->logs[] = $message;
    }

    public function getLogs() {
        return $this->logs;
    }
}

// Factory Class to Create Loggers
class LoggerFactory {
    public static function createLogger() {
        return Logger::getInstance();
    }
}

// Using the Factory to get a Logger and log messages
$logger = LoggerFactory::createLogger();
$logger->log("First log message");
$logger->log("Second log message");

print_r($logger->getLogs());
?>
```

In this example, the `Logger` class is a singleton, ensuring that only one instance of the logger exists. The `LoggerFactory` class is used to create and return the singleton instance of the `Logger` class. This setup allows you to easily manage logging across your application using a single, consistent logger instance.
