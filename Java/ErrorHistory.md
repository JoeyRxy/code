# This file records my Error while using Java.

1. `Cannot infer type arguments for testForGeneric<>`   
   CODE:
   ```java
   public class testForGeneric<T extends Comparable<T>> {

    public testForGeneric(T[] a) {
    }

    public static void main(String[] args) {
        int[] a = { 3, 2, 4, 5, 6, 8, 9, 10, 7 };
        testForGeneric<Integer> t = new testForGeneric<>(a);
    }
    ```
    because `a` is a `int` array,while `testForGeneric` requires a `Integer` array.

    and I wonder Java can't figure it out by itself?`int` auto to `Integer`