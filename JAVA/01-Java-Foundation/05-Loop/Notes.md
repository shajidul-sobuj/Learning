# Loops in Java

> **Goal:** Learn how to repeat code using `for`, `while`, `do-while`, enhanced `for`, nested loops, and loop-control statements.

## 1. What is a loop?

A loop repeats a block of code while a condition is satisfied or for each item in a collection.

Without a loop, printing numbers from 1 to 5 requires repeated statements:

```java
System.out.println(1);
System.out.println(2);
System.out.println(3);
System.out.println(4);
System.out.println(5);
```

With a loop:

```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```

Output:

```text
1
2
3
4
5
```

## 2. The `for` loop

Use a `for` loop when the repetition count or iteration pattern is known.

### Syntax

```java
for (initialization; condition; update) {
    // Code to repeat
}
```

- **Initialization:** Runs once at the beginning.
- **Condition:** Checked before each iteration. If it is `true`, the body runs.
- **Update:** Runs after each iteration.

### Example: print 1 to 5

```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```

Execution:
1. Set `i = 1`.
2. Check `i <= 5`.
3. Print `i`.
4. Increase `i` by 1.
5. Repeat until the condition becomes false.

### Example: print even numbers from 2 to 10

```java
for (int i = 2; i <= 10; i += 2) {
    System.out.println(i);
}
```

### Example: count backwards

```java
for (int i = 5; i >= 1; i--) {
    System.out.println(i);
}
```

## 3. The `while` loop

Use `while` when repetition depends on a condition and the number of iterations may not be known beforehand.

### Syntax

```java
while (condition) {
    // Code to repeat
    // Update state so the condition can eventually become false
}
```

### Example: print 1 to 5

```java
int i = 1;

while (i <= 5) {
    System.out.println(i);
    i++;
}
```

**Important:** If the condition never becomes false, the loop may run forever (an infinite loop).

### Example: repeatedly halve a number

```java
int number = 40;

while (number > 1) {
    System.out.println(number);
    number /= 2;
}
```

## 4. The `do-while` loop

A `do-while` loop checks its condition **after** executing the body, so the body always runs at least once.

### Syntax

```java
do {
    // Code to repeat
} while (condition);
```

Notice the semicolon after `while (condition);`.

### Example

```java
int i = 1;

do {
    System.out.println(i);
    i++;
} while (i <= 5);
```

### Difference from `while`

```java
int a = 10;

while (a < 5) {
    System.out.println("while body");
}

int b = 10;

do {
    System.out.println("do-while body");
} while (b < 5);
```

Output:

```text
do-while body
```

The `while` body runs zero times; the `do-while` body runs once.

## 5. Enhanced `for` loop (for-each)

Use an enhanced `for` loop to visit each element of an array or a compatible collection when you do not need the index.

### Syntax

```java
for (type item : arrayOrCollection) {
    // Use item
}
```

### Example: traverse an array

```java
int[] numbers = {10, 20, 30, 40};

for (int number : numbers) {
    System.out.println(number);
}
```

Output:

```text
10
20
30
40
```

If you need the index, use a regular `for` loop:

```java
int[] numbers = {10, 20, 30, 40};

for (int i = 0; i < numbers.length; i++) {
    System.out.println("Index " + i + ": " + numbers[i]);
}
```

## 6. Nested loops

A nested loop is a loop inside another loop. For each iteration of the outer loop, the inner loop completes its iterations.

### Example: print a 3 × 4 grid of stars

```java
for (int row = 1; row <= 3; row++) {
    for (int col = 1; col <= 4; col++) {
        System.out.print("* ");
    }
    System.out.println();
}
```

Output:

```text
* * * *
* * * *
* * * *
```

### Example: right triangle pattern

```java
for (int row = 1; row <= 4; row++) {
    for (int col = 1; col <= row; col++) {
        System.out.print("* ");
    }
    System.out.println();
}
```

Output:

```text
*
* *
* * *
* * * *
```

Nested loops are useful for patterns and two-dimensional arrays, but they can increase execution time. Two loops each running `n` times usually perform about `n × n` inner iterations.

## 7. `break` and `continue`

### `break`

`break` immediately exits the nearest enclosing loop.

```java
for (int i = 1; i <= 10; i++) {
    if (i == 5) {
        break;
    }
    System.out.println(i);
}
```

Output:

```text
1
2
3
4
```

### `continue`

`continue` skips the rest of the current iteration and moves to the next iteration.

```java
for (int i = 1; i <= 5; i++) {
    if (i == 3) {
        continue;
    }
    System.out.println(i);
}
```

Output:

```text
1
2
4
5
```

In a `for` loop, `continue` still leads to the update expression before the next condition check. In a `while` loop, make sure any required update is not accidentally skipped.

## 8. Using loops with `if`

Loops and conditions are often used together.

### Example: print numbers divisible by 3

```java
for (int i = 1; i <= 20; i++) {
    if (i % 3 == 0) {
        System.out.println(i);
    }
}
```

### Example: count even numbers in an array

```java
int[] numbers = {2, 7, 8, 11, 14, 19};
int count = 0;

for (int number : numbers) {
    if (number % 2 == 0) {
        count++;
    }
}

System.out.println("Even count: " + count);
```

Output:

```text
Even count: 3
```

## 9. Common loop patterns

### Sum from 1 to `n`

```java
int n = 5;
int sum = 0;

for (int i = 1; i <= n; i++) {
    sum += i;
}

System.out.println("Sum: " + sum); // Sum: 15
```

### Factorial of a positive integer

```java
int n = 5;
long factorial = 1;

for (int i = 1; i <= n; i++) {
    factorial *= i;
}

System.out.println(factorial); // 120
```

`0!` is also `1`. A `long` can still overflow for sufficiently large factorials, so this example is intended for small inputs.

### Multiplication table

```java
int number = 7;

for (int i = 1; i <= 10; i++) {
    System.out.println(number + " x " + i + " = " + (number * i));
}
```

## 10. Choosing the right loop

| Loop | When to use it |
|---|---|
| `for` | The iteration pattern or count is clear |
| `while` | Repeat while a condition remains true |
| `do-while` | The body must execute at least once |
| Enhanced `for` | Visit each array or collection element without needing its index |

## 11. Common mistakes

### Mistake 1: Off-by-one errors

```java
for (int i = 0; i < 5; i++) {
    System.out.println(i); // Prints 0 through 4
}
```

For an array, valid indexes run from `0` to `array.length - 1`. Use `i < array.length`, not `i <= array.length`.

### Mistake 2: Forgetting to update a `while` loop variable

```java
int i = 1;

while (i <= 5) {
    System.out.println(i);
    i++; // Needed to make progress
}
```

Without `i++`, this example never reaches a false condition.

### Mistake 3: Extra semicolon after the loop header

```java
for (int i = 1; i <= 5; i++); {
    System.out.println("This block is not the loop body");
}
```

Do not put an accidental semicolon after the `for` or `while` header.

### Mistake 4: Wrong update direction

If the condition is `i <= 5`, using `i--` from `i = 1` makes the condition remain true indefinitely. Make sure the update moves toward termination.

### Mistake 5: Integer division and unexpected results

Integer division drops the fractional part:

```java
System.out.println(5 / 2);    // 2
System.out.println(5.0 / 2);  // 2.5
```

This matters when calculating averages inside loops.
