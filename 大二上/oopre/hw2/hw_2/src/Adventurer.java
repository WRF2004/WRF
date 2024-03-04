// package ooprehomework_2023_22373180_hw_2.src;
import java.util.HashMap;

public class Adventurer {
    private int id;
    private String name;
    private HashMap<Integer, Bottle> bottles = new HashMap<>();
    private HashMap<Integer, Equipment> equipments = new HashMap<>();

    public Adventurer(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public void addBot(int botId, String name, int capacity) {
        Bottle bottle = new Bottle(botId, name, capacity);
        bottles.put(botId, bottle);
    }

    public void subBot(int botId) {
        Bottle bottle = bottles.get(botId);
        bottles.remove(botId,bottle);
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
}