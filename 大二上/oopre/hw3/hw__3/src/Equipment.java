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

    public int showId() { return this.id; }
}