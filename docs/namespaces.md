# Namespaces

## Introduction to Namespaces

Namespaces in PHP are a way of encapsulating items to avoid name conflicts. They allow you to organize your code better by grouping related classes, interfaces, functions, and constants together. Namespaces are especially useful when integrating libraries and packages from different sources that might have classes or functions with the same names.

## Defining Namespaces

To define a namespace, you use the `namespace` keyword at the top of a PHP file. Here’s an example of defining a namespace:

```php
<?php
namespace MyApp\Utilities;

class Logger {
    public function log($message) {
        echo $message;
    }
}
?>
```

In this example, `MyApp\Utilities` is the namespace for the `Logger` class. The fully qualified name of the `Logger` class is now `MyApp\Utilities\Logger`.

## Using Namespaces

To use a class from a namespace, you need to either reference it with its fully qualified name or import it using the `use` keyword. Here are both approaches:

### Fully Qualified Name

```php
<?php
require 'path/to/Logger.php';

$logger = new \MyApp\Utilities\Logger();
$logger->log("This is a log message.");
?>
```

### Importing with `use` Keyword

```php
<?php
require 'path/to/Logger.php';

use MyApp\Utilities\Logger;

$logger = new Logger();
$logger->log("This is a log message.");
?>
```

Using the `use` keyword simplifies the code by avoiding the need to write the fully qualified name every time you use the class.

## Namespace Aliases

Sometimes, you may want to create an alias for a namespace to shorten its name or avoid conflicts. You can do this using the `as` keyword with the `use` statement:

```php
<?php
require 'path/to/Logger.php';

use MyApp\Utilities\Logger as Log;

$logger = new Log();
$logger->log("This is a log message.");
?>
```

In this example, `Log` is an alias for `MyApp\Utilities\Logger`, making it easier to reference the class.

## Examples

### Organizing Classes with Namespaces

Let’s consider a more complex example where you organize a project with multiple namespaces. Assume you are building a web application with separate components for controllers, models, and utilities.

#### Directory Structure

```
/myapp
    /controllers
        HomeController.php
    /models
        User.php
    /utilities
        Logger.php
    index.php
```

#### HomeController.php

```php
<?php
namespace MyApp\Controllers;

class HomeController {
    public function index() {
        echo "Welcome to the home page!";
    }
}
?>
```

#### User.php

```php
<?php
namespace MyApp\Models;

class User {
    public function getUserInfo() {
        return "User information";
    }
}
?>
```

#### Logger.php

```php
<?php
namespace MyApp\Utilities;

class Logger {
    public function log($message) {
        echo $message;
    }
}
?>
```

#### index.php

```php
<?php
require 'controllers/HomeController.php';
require 'models/User.php';
require 'utilities/Logger.php';

use MyApp\Controllers\HomeController;
use MyApp\Models\User;
use MyApp\Utilities\Logger;

$homeController = new HomeController();
$homeController->index(); // Output: Welcome to the home page!

$user = new User();
echo $user->getUserInfo(); // Output: User information

$logger = new Logger();
$logger->log("This is a log message."); // Output: This is a log message.
?>
```

In this example, we’ve organized the classes into different namespaces based on their functionality, making the codebase more manageable and avoiding potential name conflicts.
