import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Objects;

public class Adventurer implements Commodity {
    private int id;
    private String name;

    private String type;

    private int hitPoint;

    private int level;

    private long price;

    private long maxPrice;

    private int count;

    private HashSet<Commodity> commodities = new HashSet<>();

    private HashSet<Adventurer> adventurers = new HashSet<>();

    private HashMap<Integer, Bottle> bottles = new HashMap<>();

    private HashSet<Bottle> bottleBag = new HashSet<>();

    private HashMap<Integer, Food> foods = new HashMap<>();

    private HashSet<Food> foodBag = new HashSet<>();
    private HashMap<Integer, Equipment> equipments = new HashMap<>();

    private HashSet<Equipment> equipmentBag = new HashSet<>();

    private ArrayList<String> fightLog = new ArrayList<>();

    private ArrayList<String> foughtLog = new ArrayList<>();

    public void fightLogAdd(String s) {
        fightLog.add(s);
    }

    public void foughtLogAdd(String s) {
        foughtLog.add(s);
    }

    public Adventurer(int id, String name, int hitPoint, int level) {
        this.id = id;
        this.name = name;
        this.hitPoint = hitPoint;
        this.level = level;
        this.price = 0;
        this.maxPrice = 0;
        this.count = 0;
        this.type = "Adventurer";
    }

    public long showPrice() {
        return this.price;
    }

    public String showType() {
        return this.type;
    }

    public long showMaxPrice() {
        return this.maxPrice;
    }

    public int showCount() {
        return this.count;
    }

    public int showId() {
        return this.id;
    }

    public String showName() {
        return this.name;
    }

    public int showAttr() {
        return this.level;
    }

    public int showHit() { return this.hitPoint; }

    public String showComName(int comId) {
        for (Commodity obj : commodities) {
            if (obj.showId() == comId) {
                return obj.showType();
            }
        }
        return null;
    }

    public void calc() {
        this.price = 0;
        this.maxPrice = 0;
        for (Commodity obj : commodities) {
            if (Objects.equals(obj.showType(), "Adventurer")) {
                Adventurer adventurer = (Adventurer) obj;
                adventurer.calc();
            }
            this.price += obj.showPrice();
            if (this.maxPrice < obj.showPrice()) {
                this.maxPrice = obj.showPrice();
            }
        }
    }

    public void addAdv(Adventurer adventurer) {
        int flag = 0;
        for (Adventurer obj : adventurers) {
            if (obj.showId() == adventurer.showId()) {
                flag = 1;
                break;
            }
        }
        if (flag == 0) {
            this.count += 1;
            commodities.add(adventurer);
            adventurers.add(adventurer);
        }
    }

    public void addBot(int botId, String name, int capacity, int price, String type, double o) {
        if (Objects.equals(type, "RegularBottle")) {
            Bottle bottle = new RegularBottle(botId, name, capacity, price, type, 0);
            bottles.put(botId, bottle);
            commodities.add(bottle);
        } else if (Objects.equals(type, "ReinforcedBottle")) {
            Bottle bottle = new ReinforcedBottle(botId, name, capacity, price, type, o);
            bottles.put(botId, bottle);
            commodities.add(bottle);
        } else {
            Bottle bottle = new RecoverBottle(botId, name, capacity, price, type, o);
            bottles.put(botId, bottle);
            commodities.add(bottle);
        }
        this.count += 1;
    }

    public void subBot(int botId) {
        Bottle bottle = bottles.get(botId);
        bottles.remove(botId,bottle);
        bottleBag.remove(bottle);
        commodities.remove(bottle);
        this.count -= 1;
    }

    public String showBotName(int botId) {
        Bottle bottle = bottles.get(botId);
        return bottle.showName();
    }

    public int showBotSize() {
        return bottles.size();
    }

    public void addEqu(int equId, String name, int star, int price, String type, double o) {
        if (Objects.equals(type, "RegularEquipment")) {
            Equipment equipment = new RegularEquipment(equId, name, star, price, type, 0);
            equipments.put(equId,equipment);
            commodities.add(equipment);
        } else if (Objects.equals(type, "CritEquipment")) {
            Equipment equipment = new CritEquipment(equId, name, star, price, type, o);
            equipments.put(equId,equipment);
            commodities.add(equipment);
        } else {
            Equipment equipment = new EpicEquipment(equId, name, star, price, type, o);
            equipments.put(equId,equipment);
            commodities.add(equipment);
        }
        this.count += 1;
    }

    public void subEqu(int equId) {
        Equipment equipment = equipments.get(equId);
        if (equipment != null) {
            this.count -= 1;
            equipments.remove(equId,equipment);
            equipmentBag.remove(equipment);
            commodities.remove(equipment);
        }
    }

    public int showEquSize() {
        return equipments.size();
    }

    public String showEquName(int equId) {
        Equipment equipment = equipments.get(equId);
        if (equipment != null) {
            return equipment.showName();
        }
        return null;
    }

    public void addStar(int equId) {
        Equipment equipment = equipments.get(equId);
        if (equipment != null) {
            equipment.addS();
        }
    }

    public int showStar(int equId) {
        Equipment equipment = equipments.get(equId);
        if (equipment != null) {
            return equipment.showAttr();
        }
        return -1;
    }

    public void addFood(int foodId, String name, int energy, int price) {
        Food food = new Food(foodId, name, energy, price);
        foods.put(foodId, food);
        commodities.add(food);
        this.count += 1;
    }

    public void subFood(int foodId) {
        Food food = foods.get(foodId);
        this.count -= 1;
        foods.remove(foodId);
        foodBag.remove(food);
        commodities.remove(food);
    }

    public String showFoodName(int foodId) {
        Food food = foods.get(foodId);
        return food.showName();
    }

    public int showFoodSize() {
        return foods.size();
    }

    public void addEquBag(int equId) {
        Equipment equipment = equipments.get(equId);
        if (equipment != null) {
            String name = equipment.showName();
            int flag = 0;
            for (Equipment obj : equipmentBag) {
                if (Objects.equals(obj.showName(), name) && obj.showId() == equId) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                int flag1 = 0;
                for (Equipment obj : equipmentBag) {
                    if (Objects.equals(obj.showName(), name)) {
                        equipmentBag.remove(obj);
                        equipmentBag.add(equipment);
                        flag1 = 1;
                        break;
                    }
                }
                if (flag1 == 0) {
                    equipmentBag.add(equipment);
                }
            }
        }
    }

    public Equipment useEquCheck(String name) {
        for (Equipment obj : equipmentBag) {
            if (Objects.equals(obj.showName(), name)) {
                return obj;
            }
        }
        return null;
    }

    public int foughtHitpoint(int hurt) {
        this.hitPoint -= hurt;
        return this.hitPoint;
    }

    public void addBotBag(int botId) {
        int maxBottles = this.level / 5 + 1;
        int sum = 0;
        int flag = 0;
        Bottle bottle = bottles.get(botId);
        String name = bottle.showName();
        for (Bottle obj : bottleBag) {
            if (Objects.equals(name, obj.showName()) && botId == obj.showId()) {
                flag = 1;
                break;
            }
        }
        if (flag == 0) {
            for (Bottle obj : bottleBag) {
                if (Objects.equals(name, obj.showName())) {
                    sum += 1;
                }
            }
            if (sum < maxBottles) {
                bottleBag.add(bottle);
            }
        }
    }

    public void addFoodBag(int foodId) {
        Food food = foods.get(foodId);
        String name = food.showName();
        int flag = 0;
        for (Food obj : foodBag) {
            if (Objects.equals(obj.showName(), name) && obj.showId() == foodId) {
                flag = 1;
                break;
            }
        }
        if (flag == 0) {
            foodBag.add(food);
        }
    }

    public int useBotCheck(String name) {
        Bottle bottle = null;
        for (Bottle obj : bottleBag) {
            if (Objects.equals(obj.showName(), name)) {
                bottle = obj;
                break;
            }
        }
        if (bottle == null) {
            return -1;
        }
        return 1;
    }

    public void fightUseBot(String name) {
        Bottle bottle = null;
        for (Bottle obj : bottleBag) {
            if (Objects.equals(obj.showName(), name)) {
                if (bottle == null) {
                    bottle = obj;
                }
                else {
                    if (bottle.showId() > obj.showId()) {
                        bottle = obj;
                    }
                }
            }
        }
        int botId = bottle.showId();
        if (bottle.showAttr() == 0) {
            this.count -= 1;
            commodities.remove(bottle);
            bottleBag.remove(bottle);
            bottles.remove(botId);
        }
        else {
            if (Objects.equals(bottle.showType(), "RecoverBottle")) {
                this.hitPoint += (int) (bottle.showOthers() * this.hitPoint);
            }
            else {
                this.hitPoint += bottle.showAttr();
            }
            bottle.subCap();
        }
        System.out.printf("%d %d\n", botId, this.hitPoint);
    }

    public void useBot(String name) {
        Bottle bottle = null;
        for (Bottle obj : bottleBag) {
            if (Objects.equals(obj.showName(), name)) {
                if (bottle == null) {
                    bottle = obj;
                }
                else {
                    if (bottle.showId() > obj.showId()) {
                        bottle = obj;
                    }
                }
            }
        }
        if (bottle == null) {
            System.out.printf("fail to use %s\n", name);
        }
        else {
            int botId = bottle.showId();
            if (bottle.showAttr() == 0) {
                this.count -= 1;
                commodities.remove(bottle);
                bottleBag.remove(bottle);
                bottles.remove(botId);
            }
            else {
                if (Objects.equals(bottle.showType(), "RecoverBottle")) {
                    this.hitPoint += (int) (this.hitPoint * bottle.showOthers());
                }
                else {
                    this.hitPoint += bottle.showAttr();
                }
                bottle.subCap();
            }
            System.out.printf("%d %d\n", botId, this.hitPoint);
        }
    }

    public void useFood(String name) {
        Food food = null;
        for (Food obj : foodBag) {
            if (Objects.equals(obj.showName(), name)) {
                if (food == null) {
                    food = obj;
                } else {
                    if (food.showId() > obj.showId()) {
                        food = obj;
                    }
                }
            }
        }
        if (food == null) {
            System.out.printf("fail to eat %s\n", name);
        } else {
            int foodId = food.showId();
            this.level += food.showAttr();
            System.out.printf("%d %d\n", foodId, this.level);
            this.count -= 1;
            commodities.remove(food);
            foodBag.remove(food);
            foods.remove(foodId);
        }
    }

    public void fightCheck() {
        if (fightLog.isEmpty()) {
            System.out.print("No Matched Log\n");
        } else {
            for (String str : fightLog) {
                System.out.printf("%s\n", str);
            }
        }
    }

    public void foughtCheck() {
        if (foughtLog.isEmpty()) {
            System.out.print("No Matched Log\n");
        } else {
            for (String str : foughtLog) {
                System.out.printf("%s\n", str);
            }
        }
    }
}