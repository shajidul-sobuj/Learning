# Arrays in Java

## 1. What is an array?

An array stores a fixed number of values of the same type. Like C/C++, array indexing starts at `0`.

## 2. Declare and initialize

```java
int[] numbers = {10, 20, 30};
int[] values = new int[5];
```

- `int[]` means an array of integers.
- `new int[5]` creates an array with 5 elements.
- Numeric elements default to `0`, `boolean` elements to `false`, and reference elements to `null`.
- An array's size is fixed after creation.

## 3. Access and update

```java
numbers[0]       // First element
numbers[1] = 99; // Update an element
numbers.length   // Number of elements
```

Java arrays use `.length` (without parentheses), unlike `String.length()`.

## 4. Traversing an array

- Use a regular `for` loop when you need the index.
- Use an enhanced `for` loop (`for (int value : numbers)`) when you only need each value.

## 5. Bounds

For an array of length `n`, valid indexes are `0` through `n - 1`. Accessing an invalid index causes `ArrayIndexOutOfBoundsException`.

## 6. Common operations

- Sum or count elements by looping through the array.
- `Arrays.sort(array)` sorts primitive arrays in ascending order.
- `Arrays.toString(array)` gives a readable string representation for printing.
- Import these utilities with `import java.util.Arrays;`.

## 7. Java vs C/C++

- Java arrays are objects and have a fixed length.
- Use `array.length` to get the size; a C-style array does not provide this property.
- Java checks array bounds at runtime.
- Arrays can be created with `new`, such as `new int[5]`.

## 8. Quick revision

- Indexing starts at `0`.
- The last valid index is `array.length - 1`.
- Array size is fixed after creation.
- Use `.length`, not `.length()`.
- Use `Arrays.toString()` to print all elements in a readable format.