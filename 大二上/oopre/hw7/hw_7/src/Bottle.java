public class Bottle implements Commodity {
    private int id;
    private String name;
    private int capacity;

    private int preCap;

    private long price;

    private String type;

    private double others;

    public Bottle(int id, String name, int capacity, long price, String type, double o) {
        this.id = id;
        this.name = name;
        this.capacity = capacity;
        this.preCap = capacity;
        this.price = price;
        this.type = type;
        this.others = o;
    }

    public String showName() {
        return this.name;
    }

    public int showId() { return this.id; }

    public int showCap() {
        return this.capacity;
    }

    public int showAttr() { return this.capacity; }

    public int showPc() { return this.preCap; }

    public long showPrice() {
        return this.price;
    }

    public double showOthers() {
        return this.others;
    }

    public String showType() {
        return this.type;
    }

    public void subCap() { this.capacity = 0; }
}