# Exception Handling

## Introduction to Exception Handling

Exception handling is a crucial aspect of robust and reliable software development. It allows a program to handle unexpected situations or errors gracefully, without crashing or producing incorrect results. In PHP, exceptions provide a way to handle errors and other exceptional conditions in a structured manner.

## Try, Catch, and Finally

In PHP, exceptions are managed using the `try`, `catch`, and `finally` blocks. 

### Try Block

The `try` block contains code that might throw an exception. If an exception occurs, the rest of the code inside the `try` block is skipped.

### Catch Block

The `catch` block is used to handle the exception. It defines how to respond to the exception, allowing the program to continue running or to log the error for later review.

### Finally Block

The `finally` block contains code that will be executed regardless of whether an exception was thrown or not. This is useful for cleanup tasks, such as closing files or releasing resources.

### Implementation

```php
<?php
function divide($numerator, $denominator) {
    if ($denominator == 0) {
        throw new Exception("Division by zero");
    }
    return $numerator / $denominator;
}

try {
    echo divide(10, 2); // Output: 5
    echo divide(10, 0); // Throws exception
} catch (Exception $e) {
    echo "Caught exception: " . $e->getMessage();
} finally {
    echo "Execution completed.";
}
?>
```

In this example, if the denominator is zero, an exception is thrown, which is then caught by the `catch` block. The `finally` block executes regardless of whether an exception was thrown.

## Custom Exceptions

In addition to the built-in exceptions, PHP allows you to create your own custom exceptions. Custom exceptions can provide more detailed and specific error handling.

### Implementation

```php
<?php
class CustomException extends Exception {
    public function errorMessage() {
        return "Error on line " . $this->getLine() . " in " . $this->getFile()
            . ": <b>" . $this->getMessage() . "</b>";
    }
}

function testException($value) {
    if ($value < 0) {
        throw new CustomException("Negative value not allowed");
    }
    return true;
}

try {
    testException(-1);
} catch (CustomException $e) {
    echo $e->errorMessage();
}
?>
```

In this example, a `CustomException` class is created by extending the base `Exception` class. The `testException` function throws a `CustomException` if the value is negative, and the custom exception is caught and handled in the `catch` block.

## Examples

### Handling Exceptions in a PHP Application

Here is an example of handling exceptions in a PHP application that reads a file and processes its content:

```php
<?php
class FileNotFoundException extends Exception {}

function readFileContent($filename) {
    if (!file_exists($filename)) {
        throw new FileNotFoundException("File not found: $filename");
    }
    
    $content = file_get_contents($filename);
    return $content;
}

try {
    $content = readFileContent("example.txt");
    echo $content;
} catch (FileNotFoundException $e) {
    echo "Caught exception: " . $e->getMessage();
} catch (Exception $e) {
    echo "An unexpected error occurred: " . $e->getMessage();
} finally {
    echo "File reading process completed.";
}
?>
```

In this example, a custom exception `FileNotFoundException` is defined to handle the specific case of a missing file. The `readFileContent` function throws this exception if the file does not exist. The `try` block attempts to read the file, the `catch` blocks handle both specific and general exceptions, and the `finally` block ensures that the process completion message is displayed.

By using exceptions in PHP, you can create more reliable and maintainable code, ensuring that your application can handle unexpected situations gracefully.
