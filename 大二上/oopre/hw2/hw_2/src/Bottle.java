// package ooprehomework_2023_22373180_hw_2.src;

public class Bottle {
    private int id;
    private String name;
    private int capacity;

    public Bottle(int id, String name, int capacity) {
        this.id = id;
        this.name = name;
        this.capacity = capacity;
    }

    public String showName() {
        return this.name;
    }
}