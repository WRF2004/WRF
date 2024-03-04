// package ooprehomework_2023_22373180_hw_2.src;

public class Equipment {
    private int id;
    private String name;
    private int star;

    public Equipment(int id, String name, int star) {
        this.id = id;
        this.name = name;
        this.star = star;
    }

    public String showName() {
        return this.name;
    }

    public void addS() {
        this.star += 1;
    }

    public int showStar() {
        return this.star;
    }
}