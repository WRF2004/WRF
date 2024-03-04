import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
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

    private ArrayList<String> fightLog = new ArrayList<>();

    private ArrayList<String> foughtLog = new ArrayList<>();
    Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
    @Test
    public void addBot() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 12, 10, "RegularBottle", 0);
        Bottle bottle = bottles.get(1);
        assertNull (bottle);
    }

    @Test
    public void moneyCheck() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.moneyCheck();
    }

    @Test
    public void subBot() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 12, 10, "ReinforcedBottle", 0.3);
        adventurer.subBot(1);
        Bottle bottle = bottles.get(1);
        assertNull (bottle);
    }

    @Test
    public void showBotName() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 12, 10, "ReinforcedBottle", 0.3);
        assertEquals (adventurer.showBotName(1), "w");

    }

    @Test
    public void showBotSize() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 12, 10, "ReinforcedBottle", 0.3);
        assertTrue (adventurer.showBotSize() == 1);
    }

    @Test
    public void addEqu() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1, "w", 12, 10, "EpicEquipment", 0.3);
        Equipment equipment = equipments.get(1);
        assertNull (equipment);
    }

    @Test
    public void subEqu() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1, "w", 12, 10, "EpicEquipment", 0.3);
        adventurer.subEqu(1);
        Equipment equipment = equipments.get(1);
        assertNull (equipment);
    }

    @Test
    public void showEquSize() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1, "w", 12, 10, "EpicEquipment", 0.3);
        assertTrue (adventurer.showEquSize() == 1);
    }

    @Test
    public void showEquName() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1, "w", 12, 10, "EpicEquipment", 0.3);
        assertEquals (adventurer.showEquName(1), "w");
    }

    @Test
    public void addStar() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1,"w", 12, 10, "EpicEquipment", 0.3);
        adventurer.addStar(1);
    }

    @Test
    public void showStar() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1,"w", 12, 10, "EpicEquipment", 0.3);
        assertTrue (adventurer.showStar(1) == 12);
    }

    @Test
    public void addFood() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1,"w", 1, 10);
        Food food = foods.get(1);
        assertNull (food);
    }

    @Test
    public void subFood() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1, "w", 12, 10);
        adventurer.subFood(1);
        assertNull (foods.get(1));
    }

    @Test
    public void showFoodName() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1, "w", 12, 10);
        assertEquals (adventurer.showFoodName(1), "w");
    }

    @Test
    public void showFoodSize() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1, "w", 12, 10);
        assertTrue (adventurer.showFoodSize() == 1);
    }

    @Test
    public void addEquBag() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1, "w", 1, 10, "EpicEquipment", 0.3);
        adventurer.addEqu(2, "w", 12, 10, "EpicEquipment", 0.3);
        adventurer.addEqu(3, "wrf", 1, 10, "EpicEquipment", 0.3);
        adventurer.addEquBag(1);
        adventurer.addEquBag(2);
        Equipment equipment = equipments.get(2);
        adventurer.addEquBag(3);
    }

    @Test
    public void addBotBag() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 1, 10, "ReinforcedBottle", 0.3);
        adventurer.addBot(2, "w", 12, 10, "ReinforcedBottle", 0.3);
        adventurer.addBot(3, "wrf", 1, 10, "ReinforcedBottle", 0.3);
        adventurer.addBotBag(1);
        adventurer.addBotBag(2);
    }

    @Test
    public void addFoodBag() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1, "w", 1, 10);
        adventurer.addFood(2, "w", 12, 20);
        adventurer.addFood(3, "wrf", 1, 30);
        adventurer.addFoodBag(1);
        adventurer.addFoodBag(2);
        adventurer.addFoodBag(3);
    }

    @Test
    public void useBot() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 1, 10, "ReinforcedBottle", 0.3);
        adventurer.addBot(3, "wrf", 1, 10, "ReinforcedBottle", 0.3);
        adventurer.addBot(2, "w", 12, 10, "ReinforcedBottle", 0.3);
        adventurer.addBotBag(1);
        adventurer.addBotBag(2);
        adventurer.addBotBag(3);
        adventurer.useBot("w");
        adventurer.useBot("q");
    }

    @Test
    public void useFood() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addFood(1, "w", 1, 10);
        adventurer.addFood(2, "w", 12, 10);
        adventurer.addFood(3, "wrf", 1, 20);
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

    @Test
    public void fightLogAdd() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        String s = "wrf";
        adventurer.fightLogAdd(s);
    }

    @Test
    public void foughtLogAdd() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        String s = "wrf";
        adventurer.foughtLogAdd(s);
    }

    @Test
    public void showId() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        assertTrue(adventurer.showId() == 1);
    }

    @Test
    public void showName() {
        assertTrue(adventurer.showName() == "wrf");
    }

    @Test
    public void showAttr() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        assertTrue(adventurer.showAttr() == 1);
    }

    @Test
    public void testAddBot1() {
    }

    @Test
    public void testSubBot1() {
    }

    @Test
    public void testShowBotName1() {
    }

    @Test
    public void testShowBotSize1() {
    }

    @Test
    public void testAddEqu1() {
    }

    @Test
    public void testSubEqu1() {
    }

    @Test
    public void testShowEquSize1() {
    }

    @Test
    public void testShowEquName1() {
    }

    @Test
    public void testAddStar1() {
    }

    @Test
    public void testShowStar1() {
    }

    @Test
    public void testAddFood1() {
    }

    @Test
    public void testSubFood1() {
    }

    @Test
    public void testShowFoodName1() {
    }

    @Test
    public void testShowFoodSize1() {
    }

    @Test
    public void testAddEquBag1() {
    }

    @Test
    public void useEquCheck() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addEqu(1, "w", 1, 10, "EpicEquipment", 0.3);
        adventurer.addEqu(2, "w", 12, 10, "EpicEquipment", 0.3);
        adventurer.addEqu(3, "wrf", 1, 10, "EpicEquipment", 0.3);
        adventurer.addEquBag(1);
        adventurer.addEquBag(2);
        adventurer.useEquCheck("w");
        adventurer.useEquCheck("wrf");
    }

    @Test
    public void foughtHitpoint() {
        adventurer.foughtHitpoint(1);
        assertTrue(adventurer.showAttr() == 1);
    }

    @Test
    public void testAddBotBag1() {
    }

    @Test
    public void testAddFoodBag1() {
    }

    @Test
    public void useBotCheck() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(1, "w", 1, 10, "ReinforcedBottle", 0.3);
        adventurer.addBot(2, "w", 12, 10, "ReinforcedBottle", 0.3);
        adventurer.addBot(3, "wrf", 1, 10, "ReinforcedBottle", 0.3);
        adventurer.addBotBag(1);
        adventurer.addBotBag(2);
        adventurer.useBotCheck("w");
        adventurer.useBotCheck("wrf");
    }

    @Test
    public void fightUseBot() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.addBot(2, "w", 12, 10, "ReinforcedBottle", 0.3);
        adventurer.addBot(1, "w", 0, 10, "ReinforcedBottle", 0.3);
        adventurer.addBot(3, "w", 1, 10, "ReinforcedBottle", 0.3);
        adventurer.addBot(4, "wrf", 1, 10, "ReinforcedBottle", 0.3);
        adventurer.addBotBag(1);
        adventurer.addBotBag(2);
        adventurer.addBotBag(3);
        adventurer.addBotBag(4);
        adventurer.fightUseBot("w");
        adventurer.fightUseBot("wrf");
    }

    @Test
    public void testUseBot1() {
    }

    @Test
    public void testUseFood1() {
    }

    @Test
    public void fightCheck() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.fightCheck();
        String s = "wrf";
        adventurer.fightLogAdd(s);
        adventurer.fightCheck();
    }

    @Test
    public void foughtCheck() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.foughtCheck();
        String s = "wrf";
        adventurer.foughtLogAdd(s);
        adventurer.foughtCheck();
    }

    @Before
    public void setUp() throws Exception {
        assertTrue(1 == adventurer.showId());
    }

    @Test
    public void testFightLogAdd() {
    }

    @Test
    public void testFoughtLogAdd() {
    }

    @Test
    public void testShowId() {
    }

    @Test
    public void testShowName() {
    }

    @Test
    public void testShowLevel() {
    }

    @Test
    public void testAddBot2() {
    }

    @Test
    public void testSubBot2() {
    }

    @Test
    public void testShowBotName2() {
    }

    @Test
    public void testShowBotSize2() {
    }

    @Test
    public void testAddEqu2() {
    }

    @Test
    public void testSubEqu2() {
    }

    @Test
    public void testShowEquSize2() {
    }

    @Test
    public void testShowEquName2() {
    }

    @Test
    public void testAddStar2() {
    }

    @Test
    public void testShowStar2() {
    }

    @Test
    public void testAddFood2() {
    }

    @Test
    public void testSubFood2() {
    }

    @Test
    public void testShowFoodName2() {
    }

    @Test
    public void testShowFoodSize2() {
    }

    @Test
    public void testAddEquBag2() {
    }

    @Test
    public void testUseEquCheck() {
    }

    @Test
    public void testFoughtHitpoint() {
    }

    @Test
    public void testAddBotBag2() {
    }

    @Test
    public void testAddFoodBag2() {
    }

    @Test
    public void testUseBotCheck() {
    }

    @Test
    public void testFightUseBot() {
    }

    @Test
    public void testUseBot2() {
    }

    @Test
    public void testUseFood2() {
    }

    @Test
    public void testFightCheck() {
    }

    @Test
    public void testFoughtCheck() {
    }

    @Test
    public void testFightLogAdd1() {
    }

    @Test
    public void testFoughtLogAdd1() {
    }

    @Test
    public void showPrice() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        assertTrue(adventurer.showPrice() == 0);
    }

    @Test
    public void showType() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        assertTrue(adventurer.showType() == "Adventurer");
    }

    @Test
    public void showMaxPrice() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        assertTrue(adventurer.showMaxPrice() == 0);
    }

    @Test
    public void showCount() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        assertTrue(adventurer.showCount() == 0);
    }

    @Test
    public void testShowId1() {
    }

    @Test
    public void testShowName1() {
    }

    @Test
    public void showHit() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        assertTrue(adventurer.showHit() == 500);
    }

    @Test
    public void showComName() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.showComName(1);
    }

    @Test
    public void calc() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.calc();
    }

    @Test
    public void addAdv() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        Adventurer adventurer1 = new Adventurer(2, "wf", 500, 1);
        adventurer.addAdv(adventurer1);
    }

    @Test
    public void testAddBot3() {
    }

    @Test
    public void testSubBot3() {
    }

    @Test
    public void testShowBotName3() {
    }

    @Test
    public void testShowBotSize3() {
    }

    @Test
    public void testAddEqu3() {
    }

    @Test
    public void testSubEqu3() {
    }

    @Test
    public void testShowEquSize3() {
    }

    @Test
    public void testShowEquName3() {
    }

    @Test
    public void testAddStar3() {
    }

    @Test
    public void testShowStar3() {
    }

    @Test
    public void testAddFood3() {
    }

    @Test
    public void testSubFood3() {
    }

    @Test
    public void testShowFoodName3() {
    }

    @Test
    public void testShowFoodSize3() {
    }

    @Test
    public void testAddEquBag3() {
    }

    @Test
    public void testUseEquCheck1() {
    }

    @Test
    public void testFoughtHitpoint1() {
    }

    @Test
    public void testAddBotBag3() {
    }

    @Test
    public void testAddFoodBag3() {
    }

    @Test
    public void testUseBotCheck1() {
    }

    @Test
    public void testFightUseBot1() {
    }

    @Test
    public void testUseBot3() {
    }

    @Test
    public void testUseFood3() {
    }

    @Test
    public void testFightCheck1() {
    }

    @Test
    public void testFoughtCheck1() {
    }

    @Test
    public void testFightLogAdd2() {
    }

    @Test
    public void testFoughtLogAdd2() {
    }

    @Test
    public void getBottleBag() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        assertNotNull(adventurer.getBottleBag());
    }

    @Test
    public void getEquipmentBag() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        assertNotNull(adventurer.getEquipmentBag());
    }

    @Test
    public void getFoodBag() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        assertNotNull(adventurer.getFoodBag());
    }

    @Test
    public void showMoney() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        assertEquals(adventurer.showMoney(), 0);
    }

    @Test
    public void subMoney() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        adventurer.subMoney(2);
    }

    @Test
    public void clearBag() {
        Adventurer adventurer = new Adventurer(1, "wrf", 500, 1);
        Bottle bottle = new Bottle(1,"wrf", 2, 0, "RegularBottle", 0);
        Equipment equipment = new Equipment(2, "w", 2, 0, "RegularEquipment", 0);
        Food food = new Food(3, "wr", 2, 0);
        bottleBag.add(bottle);
        foodBag.add(food);
        equipmentBag.add(equipment);
        assertEquals(adventurer.clearBag(), 0);
    }

    @Test
    public void testShowPrice() {
    }

    @Test
    public void testShowType() {
    }

    @Test
    public void testShowMaxPrice() {
    }

    @Test
    public void testShowCount() {
    }

    @Test
    public void testShowId2() {
    }

    @Test
    public void testShowName2() {
    }

    @Test
    public void testShowAttr() {
    }

    @Test
    public void testShowHit() {
    }

    @Test
    public void testShowComName() {
    }

    @Test
    public void sellBot() {

    }

    @Test
    public void sellEqu() {
    }

    @Test
    public void sellFood() {
    }

    @Test
    public void testCalc() {
    }

    @Test
    public void testAddAdv() {
    }

    @Test
    public void testAddBot4() {
    }

    @Test
    public void testSubBot4() {
    }

    @Test
    public void testShowBotName4() {
    }

    @Test
    public void testShowBotSize4() {
    }

    @Test
    public void testAddEqu4() {
    }

    @Test
    public void testSubEqu4() {
    }

    @Test
    public void testShowEquSize4() {
    }

    @Test
    public void testShowEquName4() {
    }

    @Test
    public void testAddStar4() {
    }

    @Test
    public void testShowStar4() {
    }

    @Test
    public void testAddFood4() {
    }

    @Test
    public void testSubFood4() {
    }

    @Test
    public void testShowFoodName4() {
    }

    @Test
    public void testShowFoodSize4() {
    }

    @Test
    public void testAddEquBag4() {
    }

    @Test
    public void testUseEquCheck2() {
    }

    @Test
    public void testFoughtHitpoint2() {
    }

    @Test
    public void testAddBotBag4() {
    }

    @Test
    public void testAddFoodBag4() {
    }

    @Test
    public void testUseBotCheck2() {
    }

    @Test
    public void bottleCheck() {
    }

    @Test
    public void useBottle() {
    }

    @Test
    public void testFightUseBot2() {
    }

    @Test
    public void testUseBot4() {
    }

    @Test
    public void testUseFood4() {
    }

    @Test
    public void testFightCheck2() {
    }

    @Test
    public void testFoughtCheck2() {
    }
}