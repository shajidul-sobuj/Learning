public class StringsEx {

    public static void main(String[] args) {
        String name = "Sobuj";
        String message = "Hello Java";

        // 1. Print a string
        System.out.println(name);

        // 2. Length and character access
        System.out.println(name.length()); // 5
        System.out.println(name.charAt(0)); // S

        // 3. Concatenation
        System.out.println("Hello, " + name);

        // 4. Compare string contents (use equals, not ==)
        String a = "Java";
        String b = "Java";
        System.out.println(a.equals(b)); // true

        // 5. Case-insensitive comparison
        System.out.println("java".equalsIgnoreCase("JAVA")); // true

        // 6. Common methods
        System.out.println(message.toUpperCase()); // HELLO JAVA
        System.out.println(message.toLowerCase()); // hello java
        System.out.println(message.contains("Java")); // true
        System.out.println(message.substring(0, 5)); // Hello
        System.out.println("  hi  ".trim()); // hi

        // 7. Check whether a string is empty
        String empty = "";
        System.out.println(empty.isEmpty()); // true

        // 8. Loop through characters
        for (int i = 0; i < name.length(); i++) {
            System.out.println(name.charAt(i));
        }

        // 9. String is immutable: methods return a new string
        String word = "java";
        word.toUpperCase();
        System.out.println(word); // java (original unchanged)
        word = word.toUpperCase();
        System.out.println(word); // JAVA
    }
}
