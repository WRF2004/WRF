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

    public int showId() { return this.id; }

    public int showCap() { return this.capacity; }

    public void subCap() { this.capacity = 0; }
}