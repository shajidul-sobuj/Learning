public class MethodsEx {

    public static void main(String[] args) {
        // Call a method
        sayHello();

        // Method with parameters
        greet("Sobuj");

        // Method that returns a value
        int result = add(10, 20);
        System.out.println(result);

        // Method with two parameters
        System.out.println(multiply(4, 5));

        // Method with a condition
        System.out.println(isEven(8));
    }

    // No parameter, no return value
    static void sayHello() {
        System.out.println("Hello, Java!");
    }

    // Parameter, no return value
    static void greet(String name) {
        System.out.println("Hello, " + name);
    }

    // Parameters and a return value
    static int add(int a, int b) {
        return a + b;
    }

    static int multiply(int a, int b) {
        return a * b;
    }

    static boolean isEven(int number) {
        return number % 2 == 0;
    }
}
