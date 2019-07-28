I know there is a similar [quesion](https://stackoverflow.com/questions/217065/cannot-create-an-array-of-linkedlists-in-java),but the answer is telling me how to do it but not the reason.*And I have another way to create but I don't know why*

```java
public class testForGeneric<T> {

    public testForGeneric(T[] a) {
        int len = a.length;
        Node<T>[] nodes =  new Node<T>[len];//THE PROBLEM!
        for (int i = 0; i < len; i++) 
            nodes[i] = new Node<>(a[i], i);
    }

    public static void main(String[] args) {
        Integer[] a = { 3, 2, 4 };
        testForGeneric<Integer> t = new testForGeneric<>(a);
    }
}
```
The Error at the problem line is:
> Cannot create a generic array of Node<T>

## Trial & Question
If you change the line to `Node<T> nodes = new Node[len]`,that will be right.
But you will get a warning:
> Type safety: The expression of type Node[] needs unchecked conversion to conform to Node<T>[]

I don't know why this is right.Node[len] is like some normal array.and from the warning,why the `Node[]` can convert to `Node<T>[]`?

and Why the element in array should initialized with `Node<>()`?

and if you using `Object` array casting to `Node<T>[]` array,that's also wrong.

the `Node.java`:
```java
public class Node<T> {

    public T val;
    public int index;

    public Node(T val, int index) {
        this.index = index;
        this.val = val;
    }

    public Node() {
    }
}
```
*THIS IS JUST A TEST FOR GENERIC ARRAY*

I want to know why it's right or wrong.