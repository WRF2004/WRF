public class ReinforcedBottle extends Bottle {
    public ReinforcedBottle(int id, String name, int capacity, long price, String type, double o) {
        super(id, name, capacity, price, type, o);
    }

    @Override
    public int showAttr() {
        return (int) ((1 + this.showOthers()) * this.showCap());
    }
}
