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
        String parts1[] = {"2", "123", "1", "wrf", "2", "20", "RegularBottle", "0.3"};
        Main main2 = new Main();
        main2.type2(parts1);
    }

    @Test
    public void type3() {
        String parts[] = {"3", "123", "1"};
        Main main1 = new Main();
        main1.type3(parts);
    }

    @Test
    public void type4() {
        String parts[] = {"4", "123", "1", "wrf", "2", "20", "RegularEquipment", "0.3"};
        Main main1 = new Main();
        main1.type4(parts);
        String parts1[] = {"4", "123", "1", "wrf", "2", "20", "EpicEquipment", "0.3"};
        Main main2 = new Main();
        main2.type4(parts1);
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
        assertNotEquals(main1.patternCheck("2022/09-advName1-botName"), -2);
        assertNotEquals(main1.patternCheck("2022/09-advName1@botName"), -2);
        assertNotEquals(main1.patternCheck("2022/09-advName2@#-equName"), -2);
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
        String fightLog = "2022/09-wrf-botName";
        main1.fightLogP1(fightLog, fighter);
    }

    @Test
    public void fightLogP2() {
        Main main1 = new Main();
        ArrayList<String> fighter = new ArrayList<>();
        fighter.add("wrf");
        fighter.add("advName1");
        String fightLog = "2022/09-wrf@botName-advName1";
        main1.fightLogP2(fightLog, fighter);
    }

    @Test
    public void fightLogP3() {
        Main main1 = new Main();
        ArrayList<String> fighter = new ArrayList<>();
        fighter.add("wrf");
        fighter.add("fre");
        String fightLog = "2022/09-wrf@#-equName";
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
        String parts[] = {"14", "3", "0", "qkf$u?Z?b1", "Ke7ge+", "opD5fE*b"};
        Main main1 = new Main();
        main1.type14(parts);
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
        String parts[] = {"8", "3"};
        Adventurer adventurer = new Adventurer(3, "wrf", 500, 1);
        adventurers.put(3, adventurer);
        Main main1 = new Main();
        main1.type17(parts);
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
        String parts[] = {"20", "123"};
        Main main1 = new Main();
        main1.type20(parts);
    }

    @Test
    public void type21() {
    }

    @Test
    public void testMain() {
    }

    @Test
    public void testType18() {
    }

    @Test
    public void testType21() {
    }

    @Test
    public void testType31() {
    }

    @Test
    public void testType41() {
    }

    @Test
    public void testType51() {
    }

    @Test
    public void testType61() {
    }

    @Test
    public void testType71() {
    }

    @Test
    public void testType81() {
    }

    @Test
    public void testType91() {
    }

    @Test
    public void testType101() {
    }

    @Test
    public void testType111() {
    }

    @Test
    public void testType121() {
    }

    @Test
    public void testType131() {
    }

    @Test
    public void testPatternCheck1() {
    }

    @Test
    public void testFighterCheck1() {
    }

    @Test
    public void testAdventurerFind1() {
    }

    @Test
    public void testFightLogP11() {
    }

    @Test
    public void testFightLogP21() {
    }

    @Test
    public void testFightLogP31() {
    }

    @Test
    public void testFightLogProcess1() {
    }

    @Test
    public void testType141() {
    }

    @Test
    public void testType151() {
    }

    @Test
    public void testType161() {
    }

    @Test
    public void testType171() {
    }

    @Test
    public void testType181() {
    }

    @Test
    public void testType19() {
    }

    @Test
    public void testType20() {
    }

    @Test
    public void testType211() {
    }

    @Test
    public void type22() {
    }

    @Test
    public void type23() {
    }

    @Test
    public void testMain1() {
    }

    @Test
    public void testType110() {
    }

    @Test
    public void testType22() {
    }

    @Test
    public void testType32() {
    }

    @Test
    public void testType42() {
    }

    @Test
    public void testType52() {
    }

    @Test
    public void testType62() {
    }

    @Test
    public void testType72() {
    }

    @Test
    public void testType82() {
    }

    @Test
    public void testType92() {
    }

    @Test
    public void testType102() {
    }

    @Test
    public void testType112() {
    }

    @Test
    public void testType122() {
    }

    @Test
    public void testType132() {
    }

    @Test
    public void testPatternCheck2() {
    }

    @Test
    public void testFighterCheck2() {
    }

    @Test
    public void testAdventurerFind2() {
    }

    @Test
    public void testFightLogP12() {
    }

    @Test
    public void testFightLogP22() {
    }

    @Test
    public void testFightLogP32() {
    }

    @Test
    public void testFightLogProcess2() {
    }

    @Test
    public void testType142() {
    }

    @Test
    public void testType152() {
    }

    @Test
    public void testType162() {
    }

    @Test
    public void testType172() {
    }

    @Test
    public void testType182() {
    }

    @Test
    public void testType191() {
    }

    @Test
    public void testType201() {
    }

    @Test
    public void testType212() {
    }

    @Test
    public void testType221() {
    }

    @Test
    public void testType23() {
    }

    @Test
    public void testMain2() {
    }

    @Test
    public void testType113() {
    }

    @Test
    public void testType24() {
    }

    @Test
    public void testType33() {
    }

    @Test
    public void testType43() {
    }

    @Test
    public void testType53() {
    }

    @Test
    public void testType63() {
    }

    @Test
    public void testType73() {
    }

    @Test
    public void testType83() {
    }

    @Test
    public void testType93() {
    }

    @Test
    public void testType103() {
    }

    @Test
    public void testType114() {
    }

    @Test
    public void testType123() {
    }

    @Test
    public void testType133() {
    }

    @Test
    public void testPatternCheck3() {
    }

    @Test
    public void testFighterCheck3() {
    }

    @Test
    public void testAdventurerFind3() {
    }

    @Test
    public void testFightLogP13() {
    }

    @Test
    public void testFightLogP23() {
    }

    @Test
    public void testFightLogP33() {
    }

    @Test
    public void testFightLogProcess3() {
    }

    @Test
    public void testType143() {
    }

    @Test
    public void testType153() {
    }

    @Test
    public void testType163() {
    }

    @Test
    public void testType173() {
    }

    @Test
    public void testType183() {
    }

    @Test
    public void testType192() {
    }

    @Test
    public void testType202() {
    }

    @Test
    public void testType213() {
    }

    @Test
    public void testType222() {
    }

    @Test
    public void testType231() {
    }

    @Test
    public void testMain3() {
    }
}