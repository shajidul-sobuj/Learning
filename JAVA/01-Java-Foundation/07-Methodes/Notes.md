# Methods in Java

## 1. What is a method?

A method is a reusable block of code that performs a task. It is similar to a function in C/C++.

## 2. Basic syntax

```java
static returnType methodName(parameters) {
    // Method body
    return value; // If the return type is not void
}
```

- `static`: lets you call the method through the class without creating an object.
- `returnType`: the type of value returned, such as `int`, `double`, or `boolean`.
- `void`: means the method does not return a value.
- `parameters`: inputs received by the method; they may be empty.
- `return`: sends a value back to the caller and ends the method.

## 3. Common method forms

- No parameters, `void` return.
- Parameters, `void` return.
- No parameters, returns a value.
- Parameters, returns a value.

## 4. Calling a method

Call a method by writing its name followed by parentheses and a semicolon. Pass arguments if the method declares parameters.

## 5. Parameters and arguments

- **Parameter:** variable declared in the method definition.
- **Argument:** actual value passed when calling the method.

## 6. Method overloading

Java allows multiple methods with the same name if their parameter lists differ (number, types, or order).

Changing only the return type is not enough to overload a method.

## 7. `static` vs instance methods

- A `static` method belongs to the class and can be called without creating an object.
- An instance method belongs to an object and is called through an instance.
- A `static` method cannot directly access instance fields or call instance methods without an object.

## 8. Java vs C/C++

- Java methods are declared inside a class.
- Java passes arguments by value. For object arguments, the copied value is the reference, so a method can modify the referenced object's state but cannot reassign the caller's reference.
- Java does not support standalone free functions like C/C++; methods belong to classes.

## 9. Quick revision

- Use methods to reuse code and split a program into smaller tasks.
- `void` means no returned value.
- Use `return` to return a value from a non-`void` method.
- Parameters receive values; arguments are supplied by the caller.
- Method overloading requires different parameter lists.