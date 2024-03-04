import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Objects;

public class Adventurer {
    private int id;
    private String name;

    private int hitPoint;

    private int level;
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
    }

    public int showId() {
        return this.id;
    }

    public String showName() {
        return this.name;
    }

    public int showLevel() {
        return this.level;
    }

    public void addBot(int botId, String name, int capacity) {
        Bottle bottle = new Bottle(botId, name, capacity);
        bottles.put(botId, bottle);
    }

    public void subBot(int botId) {
        Bottle bottle = bottles.get(botId);
        bottles.remove(botId,bottle);
        bottleBag.remove(bottle);
    }

    public String showBotName(int botId) {
        Bottle bottle = bottles.get(botId);
        return bottle.showName();
    }

    public int showBotSize() {
        return bottles.size();
    }

    public void addEqu(int equId, String name, int star) {
        Equipment equipment = new Equipment(equId, name, star);
        equipments.put(equId,equipment);
    }

    public void subEqu(int equId) {
        Equipment equipment = equipments.get(equId);
        equipments.remove(equId,equipment);
        equipmentBag.remove(equipment);
    }

    public int showEquSize() {
        return equipments.size();
    }

    public String showEquName(int equId) {
        Equipment equipment = equipments.get(equId);
        return equipment.showName();
    }

    public void addStar(int equId) {
        Equipment equipment = equipments.get(equId);
        equipment.addS();
    }

    public int showStar(int equId) {
        Equipment equipment = equipments.get(equId);
        return equipment.showStar();
    }

    public void addFood(int foodId, String name, int energy) {
        Food food = new Food(foodId, name, energy);
        foods.put(foodId, food);
    }

    public void subFood(int foodId) {
        Food food = foods.get(foodId);
        foods.remove(foodId);
        foodBag.remove(food);
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
        if (bottle.showCap() == 0) {
            bottleBag.remove(bottle);
            bottles.remove(botId);
        }
        else {
            this.hitPoint += bottle.showCap();
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
            if (bottle.showCap() == 0) {
                bottleBag.remove(bottle);
                bottles.remove(botId);
            }
            else {
                this.hitPoint += bottle.showCap();
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
            this.level += food.showEnergy();
            foodBag.remove(food);
            foods.remove(foodId);
            System.out.printf("%d %d\n", foodId, this.level);
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