import java.util.Scanner;

public class LoopDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a positive integer: ");
        int n = input.nextInt();

        if (n < 1) {
            System.out.println("Please enter a positive integer.");
        } else {
            long sum = 0;

            for (int i = 1; i <= n; i++) {
                sum += i;
            }

            System.out.println("Sum from 1 to " + n + " = " + sum);
        }

        input.close();
    }
}