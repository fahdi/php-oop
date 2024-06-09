# Encapsulation in PHP

Encapsulation is a fundamental concept in object-oriented programming that helps protect an object's data by restricting access to its internal state. PHP provides three access modifiers to control the visibility of class properties and methods:

- **public**: The property or method can be accessed from anywhere.
- **private**: The property or method can only be accessed within the class itself.
- **protected**: The property or method can be accessed within the class itself and by inheriting classes.

Let's see how these modifiers work with some examples.

### Example 1: Using Public, Private, and Protected Access Modifiers

We'll start with a `BankAccount` class that uses these access modifiers to control access to its properties and methods.

```php
<?php
class BankAccount {
    // Properties
    public $accountNumber;
    private $balance;
    protected $accountHolderName;

    // Constructor
    public function __construct($accountNumber, $accountHolderName, $balance) {
        $this->accountNumber = $accountNumber;
        $this->accountHolderName = $accountHolderName;
        $this->balance = $balance;
    }

    // Public method
    public function displayInfo() {
        return "Account Number: " . $this->accountNumber . ", Account Holder: " . $this->accountHolderName;
    }

    // Private method
    private function updateBalance($amount) {
        $this->balance += $amount;
    }

    // Protected method
    protected function getBalance() {
        return $this->balance;
    }

    // Public method to deposit money
    public function deposit($amount) {
        if ($amount > 0) {
            $this->updateBalance($amount);
            echo "Deposited $" . $amount . "\n";
        } else {
            echo "Invalid amount.\n";
        }
    }

    // Public method to withdraw money
    public function withdraw($amount) {
        if ($amount > 0 && $amount <= $this->balance) {
            $this->updateBalance(-$amount);
            echo "Withdrew $" . $amount . "\n";
        } else {
            echo "Invalid amount or insufficient balance.\n";
        }
    }
}

// Creating an object of the BankAccount class
$account = new BankAccount("12345678", "John Doe", 1000);

// Accessing public properties and methods
echo $account->displayInfo(); // Output: Account Number: 12345678, Account Holder: John Doe
echo "\n";
$account->deposit(200); // Output: Deposited $200
$account->withdraw(100); // Output: Withdrew $100

// Trying to access private and protected properties and methods
// echo $account->balance; // Error: Cannot access private property
// echo $account->getBalance(); // Error: Cannot access protected method
?>
```

### Example 2: Inheritance with Protected Access Modifier

Let's create a subclass `SavingsAccount` that inherits from `BankAccount` and demonstrates the use of the protected access modifier.

```php
<?php
class SavingsAccount extends BankAccount {
    // Method to display balance
    public function displayBalance() {
        return "Balance: $" . $this->getBalance();
    }
}

// Creating an object of the SavingsAccount class
$savingsAccount = new SavingsAccount("98765432", "Jane Doe", 1500);

// Accessing public methods from the parent class
echo $savingsAccount->displayInfo(); // Output: Account Number: 98765432, Account Holder: Jane Doe
echo "\n";
$savingsAccount->deposit(300); // Output: Deposited $300
$savingsAccount->withdraw(150); // Output: Withdrew $150

// Accessing the protected method through a public method in the subclass
echo $savingsAccount->displayBalance(); // Output: Balance: $1650
?>
```

### Key Points:

1. **Public Access Modifier**:
    - Properties and methods are accessible from anywhere, including outside the class.
2. **Private Access Modifier**:
    - Properties and methods are only accessible within the class they are defined.
3. **Protected Access Modifier**:
    - Properties and methods are accessible within the class they are defined and by any subclasses.

   
## Encapsulation with Getter and Setter Methods

Getter and setter methods are used to access and modify private properties from outside the class. Here’s an example using a `Person` class:

```php
<?php
class Person {
    // Private properties
    private $name;
    private $age;

    // Constructor
    public function __construct($name, $age) {
        $this->name = $name;
        $this->age = $age;
    }

    // Getter for name
    public function getName() {
        return $this->name;
    }

    // Setter for name
    public function setName($name) {
        $this->name = $name;
    }

    // Getter for age
    public function getAge() {
        return $this->age;
    }

    // Setter for age
    public function setAge($age) {
        if ($age > 0) {
            $this->age = $age;
        } else {
            echo "Invalid age.\n";
        }
    }

    // Method to display person information
    public function displayInfo() {
        return "Name: " . $this->name . ", Age: " . $this->age;
    }
}

// Creating an object of the Person class
$person = new Person("Alice", 30);

// Accessing private properties using getter methods
echo $person->getName(); // Output: Alice
echo "\n";
echo $person->getAge(); // Output: 30
echo "\n";

// Modifying private properties using setter methods
$person->setName("Bob");
$person->setAge(35);

// Displaying updated information
echo $person->displayInfo(); // Output: Name: Bob, Age: 35
?>
```

### Key Points:

1. **Private Properties**: Properties are declared as `private` to restrict direct access from outside the class.
2. **Getter Methods**: Methods like `getName()` and `getAge()` are used to access the values of private properties.
3. **Setter Methods**: Methods like `setName()` and `setAge()` are used to modify the values of private properties. Additional logic, such as validation, can be included in setter methods to ensure data integrity.

This example demonstrates how encapsulation can be used to protect and manage access to an object's internal state using getter and setter methods.