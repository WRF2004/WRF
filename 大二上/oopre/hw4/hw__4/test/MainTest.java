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
        String parts[] = {"1", "123", "1", "wrf", "2"};
        Main main1 = new Main();
        main1.type2(parts);
    }

    @Test
    public void type3() {
        String parts[] = {"1", "123", "1"};
        Main main1 = new Main();
        main1.type3(parts);
    }

    @Test
    public void type4() {
        String parts[] = {"1", "123", "1", "wrf", "2"};
        Main main1 = new Main();
        main1.type4(parts);
    }

    @Test
    public void type5() {
        String parts[] = {"1", "123", "1"};
        Main main1 = new Main();
        main1.type5(parts);
    }

    @Test
    public void type6() {
        String parts[] = {"1", "123", "1", "wrf", "2"};
        Main main1 = new Main();
        main1.type4(parts);
        String parts1[] = {"1", "123", "1"};
        main1.type6(parts1);
    }

    @Test
    public void type7() {
        String parts[] = {"1", "123", "1", "wrf", "34"};
        Main main1 = new Main();
        main1.type7(parts);
    }

    @Test
    public void type8() {
        String parts[] = {"1", "123", "1"};
        Main main1 = new Main();
        main1.type8(parts);
    }

    @Test
    public void type9() {
        String parts[] = {"1", "123", "1"};
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
}