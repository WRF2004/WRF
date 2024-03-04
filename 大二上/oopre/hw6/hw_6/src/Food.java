public class Food implements Commodity {
    private int energy;

    private int foodId;
    private String name;

    private long price;

    private String type;

    public Food(int foodId, String name, int energy, long price) {
        this.foodId = foodId;
        this.name = name;
        this.energy = energy;
        this.price = price;
        this.type = "Food";
    }

    public String showName() { return this.name; }

    public int showId() { return this.foodId; }

    public int showAttr() { return this.energy; }

    public long showPrice() { return this.price; }

    @Override
    public String showType() {
        return this.type;
    }
}
