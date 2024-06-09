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

Encapsulation helps to protect the integrity of the data by controlling access and modification. This way, you can ensure that the internal state of an object is not changed unexpectedly from outside the class.
