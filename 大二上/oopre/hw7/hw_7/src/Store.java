import java.util.HashSet;
import java.util.Objects;

public class Store {
    private static HashSet<Bottle> bottles = new HashSet<>();

    private static HashSet<Food> foods = new HashSet<>();

    private static HashSet<Equipment> equipments = new HashSet<>();

    public void addBot(Bottle bottle) {
        bottles.add(bottle);
    }

    public void addEqu(Equipment equipment) {
        equipments.add(equipment);
    }

    public void addBotBag(HashSet<Bottle> botBag) {
        bottles.addAll(botBag);
    }

    public void addEquBag(HashSet<Equipment> equBag) {
        equipments.addAll(equBag);
    }

    public void addFoodBag(HashSet<Food> foodBag) {
        foods.addAll(foodBag);
    }

    public void addFood(Food food) {
        foods.add(food);
    }

    public int Attr(String type) {
        int attr = 0;
        if (Objects.equals(type, "Food")) {
            if (!foods.isEmpty()) {
                for (Food obj : foods) {
                    attr += obj.showAttr();
                }
                attr /= foods.size();
            }
        } else if (Objects.equals(type, "RegularBottle")) {
            if (!bottles.isEmpty()) {
                for (Bottle obj : bottles) {
                    attr += obj.showPc();
                }
                attr /= bottles.size();
            }
        } else if (Objects.equals(type, "ReinforcedBottle")) {
            if (!bottles.isEmpty()) {
                for (Bottle obj : bottles) {
                    attr += obj.showPc();
                }
                attr /= bottles.size();
            }
        } else if (Objects.equals(type, "RecoverBottle")) {
            if (!bottles.isEmpty()) {
                for (Bottle obj : bottles) {
                    attr += obj.showPc();
                }
                attr /= bottles.size();
            }
        } else {
            if (!equipments.isEmpty()) {
                for (Equipment obj : equipments) {
                    attr += obj.showAttr();
                }
                attr /= equipments.size();
            }
        }
        return attr;
    }

    public long Price(String type) {
        long price = 0;
        if (Objects.equals(type, "Food")) {
            if (!foods.isEmpty()) {
                for (Food obj : foods) {
                    price += obj.showPrice();
                }
                price /= foods.size();
            }
        } else if (Objects.equals(type, "RegularBottle")) {
            if (!bottles.isEmpty()) {
                for (Bottle obj : bottles) {
                    price += obj.showPrice();
                }
                price /= bottles.size();
            }
        } else if (Objects.equals(type, "ReinforcedBottle")) {
            if (!bottles.isEmpty()) {
                for (Bottle obj : bottles) {
                    price += obj.showPrice();
                }
                price /= bottles.size();
            }
        } else if (Objects.equals(type, "RecoverBottle")) {
            if (!bottles.isEmpty()) {
                for (Bottle obj : bottles) {
                    price += obj.showPrice();
                }
                price /= bottles.size();
            }
        } else {
            if (!equipments.isEmpty()) {
                for (Equipment obj : equipments) {
                    price += obj.showPrice();
                }
                price /= equipments.size();
            }
        }
        return price;
    }
}
