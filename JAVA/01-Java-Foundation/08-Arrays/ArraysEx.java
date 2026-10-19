import java.util.Arrays;

public class ArraysEx {

    public static void main(String[] args) {
        // 1. Declare and initialize an array
        int[] numbers = {10, 20, 30, 40, 50};

        // 2. Access elements (index starts at 0)
        System.out.println(numbers[0]); // 10
        System.out.println(numbers[4]); // 50

        // 3. Update an element
        numbers[1] = 25;

        // 4. Array length
        System.out.println(numbers.length); // 5

        // 5. Traverse with a regular for loop (index needed)
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // 6. Traverse with an enhanced for loop
        for (int number : numbers) {
            System.out.println(number);
        }

        // 7. Create an array with a fixed size
        int[] values = new int[3]; // Initially {0, 0, 0}
        values[0] = 5;
        values[1] = 10;
        values[2] = 15;

        // 8. Find the sum
        int sum = 0;
        for (int number : values) {
            sum += number;
        }
        System.out.println("Sum = " + sum);

        // 9. Useful built-in utilities
        Arrays.sort(numbers); // Sort in ascending order
        System.out.println(Arrays.toString(numbers));
    }
}
