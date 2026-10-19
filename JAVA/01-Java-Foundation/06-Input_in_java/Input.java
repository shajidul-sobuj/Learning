import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

/**
 * InputSyntaxExamples.java
 *
 * A reference file containing common Java console-input syntax.
 *
 * Run the default example:
 *   javac InputSyntaxExamples.java
 *   java InputSyntaxExamples
 *
 * To try another example, replace the method call in main() with the
 * method you want to run. Run only one demo at a time because each reads
 * from System.in.
 */
public class Input {

    public static void main(String[] args) {
        basicScannerInput();
        // Uncomment ONE of these at a time to try another example:
        // readCommonDataTypes();
        // nextVsNextLine();
        // numberThenFullLine();
        // readMultipleNumbers();
        // inputWithCondition();
        // inputWithLoop();
        // validateIntegerInput();
        // bufferedReaderInput();
    }

    // 1. Basic Scanner syntax
    static void basicScannerInput() {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = input.nextInt();

        System.out.println("Your age is " + age);

        input.close();
    }

    // 2. Syntax for common data types
    static void readCommonDataTypes() {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter an integer: ");
        int age = input.nextInt();

        System.out.print("Enter a long integer: ");
        long population = input.nextLong();

        System.out.print("Enter a float: ");
        float height = input.nextFloat();

        System.out.print("Enter a decimal number: ");
        double cgpa = input.nextDouble();

        System.out.print("Enter true or false: ");
        boolean isStudent = input.nextBoolean();

        input.nextLine(); // Consume the newline left by nextBoolean()

        System.out.print("Enter one word: ");
        String word = input.next();

        input.nextLine(); // Consume the rest of the current line

        System.out.print("Enter a full line: ");
        String fullLine = input.nextLine();

        System.out.println("int: " + age);
        System.out.println("long: " + population);
        System.out.println("float: " + height);
        System.out.println("double: " + cgpa);
        System.out.println("boolean: " + isStudent);
        System.out.println("word: " + word);
        System.out.println("full line: " + fullLine);

        input.close();
    }

    // 3. next() reads one token; nextLine() reads the rest of a line
    static void nextVsNextLine() {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a full name: ");
        String fullName = input.nextLine();

        System.out.print("Enter a single word: ");
        String word = input.next();

        System.out.println("Full name: " + fullName);
        System.out.println("Word: " + word);

        input.close();
    }

    // 4. Correctly read a full line after reading a number
    static void numberThenFullLine() {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = input.nextInt();
        input.nextLine(); // Consume the pending line separator

        System.out.print("Enter your full name: ");
        String name = input.nextLine();

        System.out.println(name + " is " + age + " years old.");

        input.close();
    }

    // 5. Read multiple whitespace-separated values
    // Example input can be "10 25" or 10 and 25 on separate lines.
    static void readMultipleNumbers() {
        Scanner input = new Scanner(System.in);

        int a = input.nextInt();
        int b = input.nextInt();

        System.out.println("Sum = " + (a + b));

        input.close();
    }

    // 6. Use input with if-else
    static void inputWithCondition() {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = input.nextInt();

        if (age >= 18) {
            System.out.println("Adult");
        } else {
            System.out.println("Minor");
        }

        input.close();
    }

    // 7. Use input with a loop
    static void inputWithLoop() {
        Scanner input = new Scanner(System.in);

        System.out.print("How many numbers? ");
        int n = input.nextInt();

        long sum = 0;

        for (int i = 0; i < n; i++) {
            System.out.print("Enter number " + (i + 1) + ": ");
            sum += input.nextInt();
        }

        System.out.println("Sum = " + sum);

        input.close();
    }

    // 8. Check whether the next token is an integer before reading it
    static void validateIntegerInput() {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter an integer: ");

        if (input.hasNextInt()) {
            int number = input.nextInt();
            System.out.println("You entered: " + number);
        } else {
            System.out.println("Invalid input: please enter an integer.");
        }

        input.close();
    }

    // 9. BufferedReader syntax: reads a full line as a String.
    // Integer.parseInt() converts that String into an int.
    static void bufferedReaderInput() {
        try {
            BufferedReader reader =
                    new BufferedReader(new InputStreamReader(System.in));

            System.out.print("Enter an integer: ");
            int number = Integer.parseInt(reader.readLine());

            System.out.println("Number = " + number);
        } catch (IOException e) {
            System.out.println("Could not read input.");
        } catch (NumberFormatException e) {
            System.out.println("Please enter a valid integer.");
        }
    }
}
