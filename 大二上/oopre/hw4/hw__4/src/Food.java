public class Food {
    private int energy;

    private int foodId;
    private String name;

    public Food(int foodId, String name, int energy) {
        this.foodId = foodId;
        this.name = name;
        this.energy = energy;
    }

    public String showName() { return this.name; }

    public int showId() { return this.foodId; }

    public int showEnergy() { return this.energy; }
}
