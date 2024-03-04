public class Equipment implements Commodity {
    private int id;
    private String name;
    private int star;

    private long price;

    private String type;

    private double others;

    public Equipment(int id, String name, int star, long price, String type, double others) {
        this.id = id;
        this.name = name;
        this.star = star;
        this.price = price;
        this.type = type;
        this.others = others;
    }

    public String showName() {
        return this.name;
    }

    public void addS() {
        this.star += 1;
    }

    public int showAttr() {
        return this.star;
    }

    public long showPrice() {
        return this.price;
    }

    public double showOthers() {
        return this.others;
    }

    public String showType() {
        return this.type;
    }

    public int showId() { return this.id; }
}