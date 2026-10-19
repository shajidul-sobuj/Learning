# Strings in Java

## 1. What is a String?

A `String` represents a sequence of characters. In Java, `String` is a class, not a primitive data type.

```java
String name = "Sobuj";
```

## 2. Common operations

| Operation | Syntax |
|---|---|
| Length | `text.length()` |
| Character at index | `text.charAt(0)` |
| Join strings | `first + second` |
| Compare contents | `first.equals(second)` |
| Ignore case while comparing | `first.equalsIgnoreCase(second)` |
| Uppercase | `text.toUpperCase()` |
| Lowercase | `text.toLowerCase()` |
| Contains text | `text.contains("Java")` |
| Extract a substring | `text.substring(start, end)` |
| Remove leading/trailing basic whitespace | `text.trim()` |
| Check empty string | `text.isEmpty()` |

## 3. Indexing and substring

- String indexes start at `0`.
- The last character index is `text.length() - 1`.
- `substring(start, end)` includes `start` but excludes `end`.
- `charAt(index)` throws an exception if the index is out of range.

## 4. Compare strings correctly

Use `.equals()` to compare string contents.

```java
a.equals(b)
```

Do not normally use `a == b` for content comparison: `==` checks whether references point to the same object.

## 5. Strings are immutable

A `String` cannot be changed after it is created. Methods such as `toUpperCase()` return a new string; assign the result if you want to keep it.

## 6. String vs C/C++

- Java `String` is an object and provides built-in methods.
- Use `text.length()` for length; Java arrays instead use `array.length`.
- Use `.equals()` for content comparison.
- Java strings are immutable.
- A `char` stores one UTF-16 code unit; some Unicode characters require more than one `char`.

## 7. Quick revision

- Declare with `String text = "Hello";`.
- Use `length()` and `charAt(index)`.
- Use `.equals()` instead of `==` for content comparison.
- `substring(start, end)` excludes the ending index.
- Strings are immutable; assign the result of transformations.