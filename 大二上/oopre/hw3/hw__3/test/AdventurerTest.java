import org.junit.Test;

import java.util.HashMap;
import java.util.HashSet;

import static org.junit.Assert.*;

public class AdventurerTest {
    private HashMap<Integer, Bottle> bottles = new HashMap<>();

    private HashSet<Bottle> bottleBag = new HashSet<>();

    private HashMap<Integer, Food> foods = new HashMap<>();

    private HashSet<Food> foodBag = new HashSet<>();
    private HashMap<Integer, Equipment> equipments = new HashMap<>();

    private HashSet<Equipment> equipmentBag = new HashSet<>();
    Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
    @Test
    public void addBot() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 12);
        Bottle bottle = bottles.get(1);
        assertNull (bottle);
    }

    @Test
    public void subBot() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 12);
        adventurer.subBot(1);
        Bottle bottle = bottles.get(1);
        assertNull (bottle);
    }

    @Test
    public void showBotName() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 12);
        assertEquals (adventurer.showBotName(1), "w");

    }

    @Test
    public void showBotSize() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 12);
        assertTrue (adventurer.showBotSize() == 1);
    }

    @Test
    public void addEqu() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1, "w", 12);
        Equipment equipment = equipments.get(1);
        assertNull (equipment);
    }

    @Test
    public void subEqu() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1, "w", 12);
        adventurer.subEqu(1);
        Equipment equipment = equipments.get(1);
        assertNull (equipment);
    }

    @Test
    public void showEquSize() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1, "w", 12);
        assertTrue (adventurer.showEquSize() == 1);
    }

    @Test
    public void showEquName() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1, "w", 12);
        assertEquals (adventurer.showEquName(1), "w");
    }

    @Test
    public void addStar() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1,"w", 12);
        adventurer.addStar(1);
    }

    @Test
    public void showStar() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1,"w", 12);
        assertTrue (adventurer.showStar(1) == 12);
    }

    @Test
    public void addFood() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1,"w", 1);
        Food food = foods.get(1);
        assertNull (food);
    }

    @Test
    public void subFood() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1, "w", 12);
        adventurer.subFood(1);
        assertNull (foods.get(1));
    }

    @Test
    public void showFoodName() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1, "w", 12);
        assertEquals (adventurer.showFoodName(1), "w");
    }

    @Test
    public void showFoodSize() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1, "w", 12);
        assertTrue (adventurer.showFoodSize() == 1);
    }

    @Test
    public void addEquBag() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1, "w", 1);
        adventurer.addEqu(2, "w", 12);
        adventurer.addEqu(3, "wrf", 1);
        adventurer.addEquBag(1);
        adventurer.addEquBag(2);
        Equipment equipment = equipments.get(2);
        adventurer.addEquBag(3);
    }

    @Test
    public void addBotBag() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 1);
        adventurer.addBot(2, "w", 12);
        adventurer.addBot(3, "wrf", 1);
        adventurer.addBotBag(1);
        adventurer.addBotBag(2);
    }

    @Test
    public void addFoodBag() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1, "w", 1);
        adventurer.addFood(2, "w", 12);
        adventurer.addFood(3, "wrf", 1);
        adventurer.addFoodBag(1);
        adventurer.addFoodBag(2);
        adventurer.addFoodBag(3);
    }

    @Test
    public void useBot() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 1);
        adventurer.addBot(3, "wrf", 1);
        adventurer.addBot(2, "w", 12);
        adventurer.addBotBag(1);
        adventurer.addBotBag(2);
        adventurer.addBotBag(3);
        adventurer.useBot("w");
        adventurer.useBot("q");
    }

    @Test
    public void useFood() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1, "w", 1);
        adventurer.addFood(2, "w", 12);
        adventurer.addFood(3, "wrf", 1);
        adventurer.addFoodBag(1);
        adventurer.addFoodBag(2);
        adventurer.addFoodBag(3);
        adventurer.useFood("w");
        adventurer.useFood("q");
    }

    @Test
    public void testAddBot() {
    }

    @Test
    public void testSubBot() {
    }

    @Test
    public void testShowBotName() {
    }

    @Test
    public void testShowBotSize() {
    }

    @Test
    public void testAddEqu() {
    }

    @Test
    public void testSubEqu() {
    }

    @Test
    public void testShowEquSize() {
    }

    @Test
    public void testShowEquName() {
    }

    @Test
    public void testAddStar() {
    }

    @Test
    public void testShowStar() {
    }

    @Test
    public void testAddFood() {
    }

    @Test
    public void testSubFood() {
    }

    @Test
    public void testShowFoodName() {
    }

    @Test
    public void testShowFoodSize() {
    }

    @Test
    public void testAddEquBag() {
    }

    @Test
    public void testAddBotBag() {
    }

    @Test
    public void testAddFoodBag() {
    }

    @Test
    public void testUseBot() {
    }

    @Test
    public void testUseFood() {
    }
}