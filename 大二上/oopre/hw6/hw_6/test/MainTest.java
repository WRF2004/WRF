import org.junit.Test;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;

import static org.junit.Assert.*;

public class MainTest {

    private static HashMap<Integer, Adventurer> adventurers = new HashMap<>();

    private static Scanner scanner = new Scanner(System.in);

    private static ArrayList<String> fightTimeLog = new ArrayList<>();

    @Test
    public void type1() {
        String parts[] = {"1", "123", "advName1"};
        Main main1 = new Main();
        main1.type1(parts);
        int advId = Integer.parseInt(parts[1]);
        Adventurer adventurer = adventurers.get(advId);
        assertNull(adventurer);
    }

    @Test
    public void type2() {
        String parts[] = {"2", "123", "1", "wrf", "2", "20", "ReinforcedBottle", "0.3"};
        Main main1 = new Main();
        main1.type2(parts);
    }

    @Test
    public void type3() {
        String parts[] = {"3", "123", "1"};
        Main main1 = new Main();
        main1.type3(parts);
    }

    @Test
    public void type4() {
        String parts[] = {"4", "123", "1", "wrf", "2", "20", "EpicEquipment", "0.3"};
        Main main1 = new Main();
        main1.type4(parts);
    }

    @Test
    public void type5() {
        String parts[] = {"5", "123", "1"};
        Main main1 = new Main();
        main1.type5(parts);
    }

    @Test
    public void type6() {
        String parts2[] = {"1", "123", "wrf"};
        Main main1 = new Main();
        main1.type1(parts2);
        String parts[] = {"4", "123", "1", "wrf", "2", "2", "EpicEquipment", "0.3"};
        main1.type4(parts);
        String parts1[] = {"6", "123", "1"};
        main1.type6(parts1);
    }

    @Test
    public void type7() {
        String parts[] = {"7", "123", "1", "wrf", "34", "23"};
        Main main1 = new Main();
        main1.type7(parts);
    }

    @Test
    public void type8() {
        String parts[] = {"8", "123", "1"};
        Main main1 = new Main();
        main1.type8(parts);
    }

    @Test
    public void type9() {
        String parts[] = {"9", "123", "1"};
        Main main1 = new Main();
        main1.type9(parts);
    }

    @Test
    public void type10() {

    }

    @Test
    public void type11() {

    }

    @Test
    public void type12() {

    }

    @Test
    public void type13() {

    }

    @Test
    public void patternCheck() {
        Main main1 = new Main();
        main1.patternCheck("2022/09-advName1-botName");
        main1.patternCheck("2022/09-advName2@#-equName");
    }

    @Test
    public void fighterCheck() {
        Main main1 = new Main();
        ArrayList<String> fighter = new ArrayList<>();
        fighter.add("wrf");
        fighter.add("fre");
        main1.fighterCheck(fighter, "wrf");
        main1.fighterCheck(fighter, "f");
    }

    @Test
    public void adventurerFind() {
        Adventurer adventurer1 = new Adventurer(1, "wrf", 500, 1);
        Adventurer adventurer2 = new Adventurer(2, "rf", 500, 1);
        adventurers.put(1, adventurer1);
        adventurers.put(2, adventurer2);
        Main main1 = new Main();
        main1.adventurerFind("wrf");
        main1.adventurerFind("f");
    }

    @Test
    public void fightLogP1() {
        Main main1 = new Main();
        ArrayList<String> fighter = new ArrayList<>();
        fighter.add("wrf");
        fighter.add("fre");
        String fightLog = "2022/09-advName1-botName";
        main1.fightLogP1(fightLog, fighter);
    }

    @Test
    public void fightLogP2() {
        Main main1 = new Main();
        ArrayList<String> fighter = new ArrayList<>();
        fighter.add("wrf");
        fighter.add("fre");
        String fightLog = "2022/09-advName1@botName-wrf";
        main1.fightLogP2(fightLog, fighter);
    }

    @Test
    public void fightLogP3() {
        Main main1 = new Main();
        ArrayList<String> fighter = new ArrayList<>();
        fighter.add("wrf");
        fighter.add("fre");
        String fightLog = "2022/09-advName2@#-equName";
        main1.fightLogP3(fightLog, fighter);
    }

    @Test
    public void fightLogProcess() {
        Main main1 = new Main();
        ArrayList<String> fighter = new ArrayList<>();
        fighter.add("wrf");
        fighter.add("fre");
        String fightLog = "2022/09-advName2@#-equName";
        main1.fightLogProcess(fightLog, fighter);
        fightLog = "2022/09-advName1@botName-wrf";
        main1.fightLogProcess(fightLog, fighter);
        fightLog = "2022/09-advName1-botName";
        main1.fightLogProcess(fightLog, fighter);
    }

    @Test
    public void type14() {
    }

    @Test
    public void type15() {
        String parts[] = {"8", "3"};
        Main main1 = new Main();
        main1.type15(parts);
    }

    @Test
    public void type16() {
        String parts[] = {"8", "3"};
        Adventurer adventurer = new Adventurer(3, "wrf", 500, 1);
        adventurers.put(3, adventurer);
        Main main1 = new Main();
        main1.type16(parts);
    }

    @Test
    public void type17() {

    }

    @Test
    public void main() {
    }

    @Test
    public void testType1() {
    }

    @Test
    public void testType2() {
    }

    @Test
    public void testType3() {
    }

    @Test
    public void testType4() {
    }

    @Test
    public void testType5() {
    }

    @Test
    public void testType6() {
    }

    @Test
    public void testType7() {
    }

    @Test
    public void testType8() {
    }

    @Test
    public void testType9() {
    }

    @Test
    public void testType10() {
    }

    @Test
    public void testType11() {
    }

    @Test
    public void testType12() {
    }

    @Test
    public void testType13() {
    }

    @Test
    public void testPatternCheck() {
    }

    @Test
    public void testFighterCheck() {
    }

    @Test
    public void testAdventurerFind() {
    }

    @Test
    public void testFightLogP1() {
    }

    @Test
    public void testFightLogP2() {
    }

    @Test
    public void testFightLogP3() {
    }

    @Test
    public void testFightLogProcess() {
    }

    @Test
    public void testType14() {
    }

    @Test
    public void testType15() {
    }

    @Test
    public void testType16() {
    }

    @Test
    public void testType17() {
    }

    @Test
    public void type18() {
        String parts[] = {"18", "123", "33"};
        Main main1 = new Main();
        main1.type18(parts);
    }

    @Test
    public void type19() {
        String parts[] = {"19", "123", "33"};
        Main main1 = new Main();
        main1.type19(parts);
    }

    @Test
    public void type20() {
    }

    @Test
    public void type21() {
    }

    @Test
    public void testMain() {
    }
}