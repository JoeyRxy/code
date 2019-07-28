package m.ttest;

/**
 * ObjectArrayTest
 */
public class ObjectArrayTest {

    public int x;
    public int y;

    public ObjectArrayTest(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void show() {
        System.out.print("(x, y) : (" + this.x + ", " + this.y + ")\n");
    }

    public static void main(String[] args) {
        String[] strArray = { "String", "Test", "is", "OK" };
        for (int i = 0; i < strArray.length; i++) {
            System.out.println(strArray[i]);
        }
        // ATTENTION : How to init a Object Array by {}
        ObjectArrayTest[] arrayTest = { new ObjectArrayTest(10, 20), new ObjectArrayTest(20, 10),
                new ObjectArrayTest(30, 40) };
        for (int i = 0; i < arrayTest.length; i++) {
            arrayTest[i].show();
        }
    }
}