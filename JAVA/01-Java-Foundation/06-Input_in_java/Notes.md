# User Input in Java — Notes

## 1. Purpose of input

Input allows a program to receive values while it runs instead of relying only on hard-coded values.

## 2. `Scanner`

- `Scanner` is a beginner-friendly class for reading console input.
- Import it with `java.util.Scanner`.
- `System.in` represents standard input, usually the keyboard in a console program.
- `System.out.print()` displays a prompt without starting a new line.
- `System.out.println()` displays output and then starts a new line.

## 3. Common input methods

| Method | Reads |
|---|---|
| `nextInt()` | An integer |
| `nextLong()` | A long integer |
| `nextFloat()` | A float |
| `nextDouble()` | A double |
| `nextBoolean()` | `true` or `false` |
| `next()` | The next token, ending at whitespace |
| `nextLine()` | The remaining text on the current line |

## 4. `next()` vs `nextLine()`

- `next()` reads one token. It stops at whitespace.
- `nextLine()` reads the remaining content of a line, including spaces, until the line separator.
- After methods such as `nextInt()` or `nextDouble()`, the line separator may remain in the input.
- If `nextLine()` is called immediately afterward, it may consume that leftover line separator and return an empty string.
- To read a new full line after numeric token input, consume the pending line separator first.

## 5. Reading multiple values

- `Scanner` token methods treat whitespace as a separator.
- Multiple numeric values can be supplied on one line or on separate lines.
- Read each expected value using the method matching its data type.

## 6. Input with conditions and loops

- Input values can be checked using `if`, `else-if`, and `else`.
- Loops can repeatedly read values, calculate totals, or count values that match a condition.
- Validate ranges when the problem requires limits, such as marks between 0 and 100.

## 7. Invalid input

- A numeric method such as `nextInt()` expects a valid integer token.
- Reading incompatible input can throw `InputMismatchException`.
- `hasNextInt()` checks whether the next token can be read as an integer without consuming it.
- For robust programs, decide what to do when input is invalid rather than assuming it is always correct.

## 8. `BufferedReader`

- `BufferedReader` is another option for console input and is often useful when reading large amounts of input.
- `readLine()` returns a `String`.
- Convert a string to an integer with `Integer.parseInt()` or to a decimal number with `Double.parseDouble()`.
- Parsing can fail with `NumberFormatException`; line reading can fail with `IOException`.

## 9. `Scanner` vs `BufferedReader`

| Feature | `Scanner` | `BufferedReader` |
|---|---|---|
| Ease of use | Simpler for beginners | Requires explicit parsing |
| Typed token methods | Available | Not built in |
| Full-line input | `nextLine()` | `readLine()` |
| Large input | Can be slower | Often faster |

## 10. Common mistakes

- Forgetting to import `Scanner`.
- Choosing an input method that does not match the expected data type.
- Confusing `next()` with `nextLine()`.
- Forgetting about a pending line separator after reading a token.
- Assuming invalid input will be accepted by a numeric method.
- Closing a scanner wrapping `System.in` before other parts of the program have finished reading input.

## 11. Quick revision

- Use `Scanner` for straightforward beginner console programs.
- Use `nextInt()` and similar methods for typed tokens.
- Use `nextLine()` for full lines containing spaces.
- Handle the leftover newline when mixing token methods and `nextLine()`.
- Use `hasNextInt()` to check integer input.
- Consider `BufferedReader` for large or line-oriented input.