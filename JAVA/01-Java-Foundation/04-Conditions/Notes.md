# Conditional Statements in Java

> **Goal:** Understand how to make decisions in Java using `if`, `if-else`, `else-if`, nested `if`, and `switch`.

## 1. What is a conditional statement?

A conditional statement lets a program choose which code to execute based on whether a condition is `true` or `false`.

```java
int age = 20;

if (age >= 18) {
    System.out.println("Adult");
}
```

Here, `age >= 18` is the condition. Because it is `true`, Java executes the code inside the braces.

## 2. Comparison operators

Comparison operators compare two values and produce a `boolean` result (`true` or `false`).

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

```java
int a = 10;
int b = 20;

System.out.println(a < b);   // true
System.out.println(a == b);  // false
```

**Important:** `=` assigns a value; `==` compares values.

## 3. The `if` statement

Use `if` when code should run only if a condition is true.

### Syntax

```java
if (condition) {
    // Runs when condition is true
}
```

### Example: positive number

```java
int number = 7;

if (number > 0) {
    System.out.println("Positive number");
}
```

If the condition is false, the body is skipped.

## 4. The `if-else` statement

Use `if-else` when there are two alternative paths.

### Syntax

```java
if (condition) {
    // Runs if condition is true
} else {
    // Runs if condition is false
}
```

### Example: even or odd

```java
int number = 12;

if (number % 2 == 0) {
    System.out.println("Even");
} else {
    System.out.println("Odd");
}
```

`%` is the remainder operator. An integer is even when its remainder after division by `2` is `0`.

## 5. The `else-if` ladder

Use an `else-if` ladder when multiple conditions must be checked in order. Java executes the **first matching branch** and skips the rest.

```java
int marks = 78;

if (marks >= 80) {
    System.out.println("Grade: A+");
} else if (marks >= 70) {
    System.out.println("Grade: A");
} else if (marks >= 60) {
    System.out.println("Grade: A-");
} else if (marks >= 50) {
    System.out.println("Grade: B");
} else {
    System.out.println("Grade: Fail");
}
```

Output:

```text
Grade: A
```

**Order matters.** Put more specific or higher-threshold conditions first. If `marks >= 50` were checked first, a mark of `78` would match it and later branches would never run.

## 6. Nested `if`

A nested `if` is an `if` statement inside another conditional statement. Use it when a second check is relevant only after the first condition passes.

```java
int age = 22;
boolean hasNid = true;

if (age >= 18) {
    if (hasNid) {
        System.out.println("Eligible for the service");
    } else {
        System.out.println("NID is required");
    }
} else {
    System.out.println("Must be at least 18");
}
```

Avoid deep nesting when a simpler condition would be easier to read.

## 7. Logical operators

Logical operators combine or reverse boolean conditions.

| Operator | Meaning | Example |
|---|---|---|
| `&&` | AND — both conditions must be true | `age >= 18 && hasNid` |
| `\|\|` | OR — at least one condition must be true | `isWeekend \|\| isHoliday` |
| `!` | NOT — reverses a boolean value | `!isLoggedIn` |

### Example: range check

```java
int age = 21;

if (age >= 18 && age <= 30) {
    System.out.println("Age is between 18 and 30");
} else {
    System.out.println("Age is outside the range");
}
```

**Short-circuit behavior:**
- With `&&`, Java does not evaluate the right side if the left side is `false`.
- With `||`, Java does not evaluate the right side if the left side is `true`.

## 8. The `switch` statement

Use `switch` when one expression is compared against several discrete cases, such as menu choices or day numbers.

### Traditional `switch`

```java
int day = 3;

switch (day) {
    case 1:
        System.out.println("Sunday");
        break;
    case 2:
        System.out.println("Monday");
        break;
    case 3:
        System.out.println("Tuesday");
        break;
    default:
        System.out.println("Invalid day");
}
```

Output:

```text
Tuesday
```

- `case` defines a possible matching value.
- `break` exits the `switch` so execution does not continue into later cases.
- `default` runs when no case matches; it is optional.

### Switch expression with arrow labels (modern Java)

```java
int day = 3;

String dayName = switch (day) {
    case 1 -> "Sunday";
    case 2 -> "Monday";
    case 3 -> "Tuesday";
    default -> "Invalid day";
};

System.out.println(dayName);
```

Arrow-style cases do not fall through to the next case. Switch expressions are supported in modern Java (standard since Java 14).

## 9. Ternary operator

The ternary operator is a compact expression for choosing between two values. It is not a replacement for every `if-else`.

### Syntax

```java
result = condition ? valueIfTrue : valueIfFalse;
```

### Example

```java
int number = 9;
String result = (number % 2 == 0) ? "Even" : "Odd";

System.out.println(result);
```

Output:

```text
Odd
```

Prefer ordinary `if-else` when the logic is complex or when branches perform multiple actions.

## 10. `if` vs `switch` vs ternary

| Use | Best fit |
|---|---|
| `if` / `else-if` | Ranges and complex boolean conditions |
| `switch` | Several discrete values of one expression |
| Ternary `?:` | A short choice between two values |

## 11. Common mistakes

### Mistake 1: Using `=` instead of `==`

```java
int number = 5;

if (number == 5) { // Correct: comparison
    System.out.println("Number is 5");
}
```

### Mistake 2: Forgetting braces

Braces are optional for a single statement, but using them consistently reduces bugs and improves readability.

```java
if (number > 0) {
    System.out.println("Positive");
}
```

### Mistake 3: Incorrect condition order

Check higher thresholds first in grade systems and similar ranges.

### Mistake 4: Using `||` when both conditions are required

```java
// Both conditions must be true:
if (age >= 18 && hasNid) {
    System.out.println("Eligible");
}
```

### Mistake 5: Comparing strings with `==`

For string content, normally use `.equals()`:

```java
String role = "admin";

if (role.equals("admin")) {
    System.out.println("Administrator");
}
```

`==` checks whether two object references refer to the same object; `.equals()` checks string content.

### Mistake 6: Accidental fall-through in traditional `switch`

Remember `break` unless fall-through is intentional. Arrow-style `case ->` avoids this issue.

