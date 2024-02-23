package Stack;

import java.util.Arrays;

public class CustomStack {
    protected int[] data;
    private static final int DEFAULT_SIZE = 10;
    int lastindx = -1;
    public CustomStack(){
        this(DEFAULT_SIZE);
    }
    public CustomStack(int size) {
        this.data = new int[size];
    }
    public boolean push(int item) {
        if (isFull()) {
            System.out.println("Stack is full!!");
            return false;
        }
        lastindx++;
        data[lastindx] = item;
        return true;
    }

    public int pop() throws StackException {
        if (isEmpty()) {
            throw new StackException("Cannot pop from an empty stack!");
        }
        return data[lastindx--];
    }

    public int peek() throws StackException {
        if (isEmpty()) {
            throw new StackException("Cannot peek from an empty stack!");
        }
        return data[lastindx];
    }

    public boolean isFull() {
        return lastindx == data.length - 1;
    }
    public boolean isEmpty() {
        return lastindx == -1;
    }

    public static void main(String[] args) {
        CustomStack s1=new CustomStack(12);
        s1.push(12);
        System.out.println(Arrays.toString(s1.data));
    }
}
class StackException extends Exception{
    public StackException(String message) {
        super(message);
    }
}
