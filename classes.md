Let's create a few simple classes with properties and methods. We'll start with two examples: a `Book` class and a `Person` class.

### Example 1: `Book` Class

This class will represent a book with properties like `title`, `author`, and `year`. It will also have a method to display the book's information.

```php
<?php
class Book {
    // Properties
    public $title;
    public $author;
    public $year;

    // Constructor
    public function __construct($title, $author, $year) {
        $this->title = $title;
        $this->author = $author;
        $this->year = $year;
    }

    // Method to display book information
    public function displayInfo() {
        return "Title: " . $this->title . ", Author: " . $this->author . ", Year: " . $this->year;
    }
}

// Creating objects of the Book class
$book1 = new Book("1984", "George Orwell", 1949);
$book2 = new Book("To Kill a Mockingbird", "Harper Lee", 1960);

// Displaying information about the books
echo $book1->displayInfo(); // Output: Title: 1984, Author: George Orwell, Year: 1949
echo "\n";
echo $book2->displayInfo(); // Output: Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960
?>
```

### Example 2: `Person` Class

This class will represent a person with properties like `name`, `age`, and `gender`. It will also have a method to display the person's information.

```php
<?php
class Person {
    // Properties
    public $name;
    public $age;
    public $gender;

    // Constructor
    public function __construct($name, $age, $gender) {
        $this->name = $name;
        $this->age = $age;
        $this->gender = $gender;
    }

    // Method to display person information
    public function displayInfo() {
        return "Name: " . $this->name . ", Age: " . $this->age . ", Gender: " . $this->gender;
    }
}

// Creating objects of the Person class
$person1 = new Person("Alice", 30, "Female");
$person2 = new Person("Bob", 25, "Male");

// Displaying information about the persons
echo $person1->displayInfo(); // Output: Name: Alice, Age: 30, Gender: Female
echo "\n";
echo $person2->displayInfo(); // Output: Name: Bob, Age: 25, Gender: Male
?>
```

Let's see three more examples with different classes:

### Example 3: `Student` Class

This class will represent a student with properties like `name`, `studentId`, and `major`. It will also have a method to display the student's information.

```php
<?php
class Student {
    // Properties
    public $name;
    public $studentId;
    public $major;

    // Constructor
    public function __construct($name, $studentId, $major) {
        $this->name = $name;
        $this->studentId = $studentId;
        $this->major = $major;
    }

    // Method to display student information
    public function displayInfo() {
        return "Name: " . $this->name . ", Student ID: " . $this->studentId . ", Major: " . $this->major;
    }
}

// Creating objects of the Student class
$student1 = new Student("John Doe", "S12345", "Computer Science");
$student2 = new Student("Jane Smith", "S67890", "Mathematics");

// Displaying information about the students
echo $student1->displayInfo(); // Output: Name: John Doe, Student ID: S12345, Major: Computer Science
echo "\n";
echo $student2->displayInfo(); // Output: Name: Jane Smith, Student ID: S67890, Major: Mathematics
?>
```

### Example 4: `Product` Class

This class will represent a product with properties like `name`, `price`, and `category`. It will also have a method to display the product's information.

```php
<?php
class Product {
    // Properties
    public $name;
    public $price;
    public $category;

    // Constructor
    public function __construct($name, $price, $category) {
        $this->name = $name;
        $this->price = $price;
        $this->category = $category;
    }

    // Method to display product information
    public function displayInfo() {
        return "Product: " . $this->name . ", Price: $" . $this->price . ", Category: " . $this->category;
    }
}

// Creating objects of the Product class
$product1 = new Product("Laptop", 999.99, "Electronics");
$product2 = new Product("Coffee Maker", 49.99, "Kitchen Appliances");

// Displaying information about the products
echo $product1->displayInfo(); // Output: Product: Laptop, Price: $999.99, Category: Electronics
echo "\n";
echo $product2->displayInfo(); // Output: Product: Coffee Maker, Price: $49.99, Category: Kitchen Appliances
?>
```

### Example 5: `Movie` Class

This class will represent a movie with properties like `title`, `director`, and `releaseYear`. It will also have a method to display the movie's information.

```php
<?php
class Movie {
    // Properties
    public $title;
    public $director;
    public $releaseYear;

    // Constructor
    public function __construct($title, $director, $releaseYear) {
        $this->title = $title;
        $this->director = $director;
        $this->releaseYear = $releaseYear;
    }

    // Method to display movie information
    public function displayInfo() {
        return "Title: " . $this->title . ", Director: " . $this->director . ", Release Year: " . $this->releaseYear;
    }
}

// Creating objects of the Movie class
$movie1 = new Movie("Inception", "Christopher Nolan", 2010);
$movie2 = new Movie("The Matrix", "The Wachowskis", 1999);

// Displaying information about the movies
echo $movie1->displayInfo(); // Output: Title: Inception, Director: Christopher Nolan, Release Year: 2010
echo "\n";
echo $movie2->displayInfo(); // Output: Title: The Matrix, Director: The Wachowskis, Release Year: 1999
?>
```

These additional examples demonstrate the use of classes to represent different real-world entities: students, products, and movies. Each class includes properties to store relevant data and a method to display this data. By creating objects from these classes, you can see how OOP helps organize and manage data in a structured way. 

### Key Points:

1. **Class Definition**: Use the `class` keyword to define a class.
2. **Properties**: Define properties inside the class.
3. **Constructor**: Use the `__construct` method to initialize the properties.
4. **Methods**: Define methods to perform actions or return information about the object.
5. **Object Creation**: Create objects by using the `new` keyword followed by the class name and passing the required parameters to the constructor.

These examples demonstrate the basic structure and usage of classes in PHP. You can now practice creating your own classes with different properties and methods to become more comfortable with the concepts. 