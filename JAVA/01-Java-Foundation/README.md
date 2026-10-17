# Java Foundation

Begin with the Java language basics and add topics as you study them.

## Topics

- [Getting Started](01-Getting-Started/examples/)
- [Variables and Data Types](02-Variables-and-Data-Types/examples/)
- [Operators and Type Casting](03-Operators-and-Type-Casting/examples/)

## Run the Examples

Run these commands from the `JAVA/` directory. They use `out/` for compiled
classes so generated files stay separate from the source examples.

```sh
mkdir -p out

# Getting started
javac -d out 01-Java-Foundation/01-Getting-Started/examples/first_code_in_java.java
java -cp out first_code_in_java
javac -d out 01-Java-Foundation/01-Getting-Started/examples/src/welcome.java
java -cp out src.welcome Sobuj

# Variables and data types
javac -d out 01-Java-Foundation/02-Variables-and-Data-Types/examples/Variables.java
java -cp out Variables
javac -d out 01-Java-Foundation/02-Variables-and-Data-Types/examples/lab.java
java -cp out lab

# Operators
javac -d out 01-Java-Foundation/03-Operators-and-Type-Casting/examples/Operators/Arithmetic.java
java -cp out Operators.Arithmetic
```
