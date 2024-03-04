import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

public class Main {
    private static HashMap<Integer, Adventurer> adventurers = new HashMap<>();

    private static Scanner scanner = new Scanner(System.in);

    private static ArrayList<String> fightTimeLog = new ArrayList<>();

    public static void type1(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        Adventurer adventurer = new Adventurer(advId, parts[2], 500, 1);
        adventurers.put(advId, adventurer);
    }

    public static void type2(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        Adventurer adventurer = adventurers.get(advId);
        adventurer.addBot(Integer.parseInt(parts[2]), parts[3], Integer.parseInt(parts[4]));
    }

    public static void type3(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        String name = adventurers.get(advId).showBotName(Integer.parseInt(parts[2]));
        adventurers.get(advId).subBot(Integer.parseInt(parts[2]));
        System.out.printf("%d %s\n",adventurers.get(advId).showBotSize(),name);
    }

    public static void type4(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        int equId = Integer.parseInt(parts[2]);
        adventurers.get(advId).addEqu(equId, parts[3], Integer.parseInt(parts[4]));
    }

    public static void type5(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        String name = adventurers.get(advId).showEquName(Integer.parseInt(parts[2]));
        adventurers.get(advId).subEqu(Integer.parseInt(parts[2]));
        System.out.printf("%d %s\n",adventurers.get(advId).showEquSize(),name);
    }

    public static void type6(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        int equId = Integer.parseInt(parts[2]);
        String name = adventurers.get(advId).showEquName(Integer.parseInt(parts[2]));
        adventurers.get(advId).addStar(Integer.parseInt(parts[2]));
        System.out.printf("%s %d\n",name,adventurers.get(advId).showStar(equId));
    }

    public static void type7(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        int foodId = Integer.parseInt(parts[2]);
        int energy = Integer.parseInt(parts[4]);
        adventurers.get(advId).addFood(foodId, parts[3], energy);
    }

    public static void type8(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        int foodId = Integer.parseInt(parts[2]);
        String name = adventurers.get(advId).showFoodName(foodId);
        adventurers.get(advId).subFood(foodId);
        System.out.printf("%d %s\n",adventurers.get(advId).showFoodSize(),name);
    }

    public static void type9(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        adventurers.get(advId).addEquBag(Integer.parseInt(parts[2]));
    }

    public static void type10(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        int botId = Integer.parseInt(parts[2]);
        adventurers.get(advId).addBotBag(botId);
    }

    public static void type11(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        int foodId = Integer.parseInt(parts[2]);
        Adventurer adventurer = adventurers.get(advId);
        adventurer.addFoodBag(foodId);
    }

    public static void type12(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        String name = parts[2];
        Adventurer adventurer = adventurers.get(advId);
        adventurer.useBot(name);
    }

    public static void type13(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        String name = parts[2];
        Adventurer adventurer = adventurers.get(advId);
        adventurer.useFood(name);
    }

    public static int patternCheck(String fightLog) {
        String pattErn1 = "\\d{4}/(0[1-9]|1[0-2])-[^\\s@#-]{1,39}-[^\\s@#-]{1,39}";
        String pattErn2 = "\\d{4}/(0[1-9]|1[0-2])-[^\\s@#-]{1,39}@[^\\s@#-]{1,39}-[^\\s@#-]{1,39}";
        String pattErn3 = "\\d{4}/(0[1-9]|1[0-2])-[^\\s@#-]{1,39}@#-[^\\s@#-]{1,39}";
        Pattern pattern1 = Pattern.compile(pattErn1);
        Pattern pattern2 = Pattern.compile(pattErn2);
        Pattern pattern3 = Pattern.compile(pattErn3);
        Matcher matcher1 = pattern1.matcher(fightLog);
        Matcher matcher2 = pattern2.matcher(fightLog);
        Matcher matcher3 = pattern3.matcher(fightLog);
        if (matcher1.find()) {
            return 1;
        } else if (matcher2.find()) {
            return 2;
        } else if (matcher3.find()) {
            return 3;
        }
        return -1;
    }

    public static int fighterCheck(ArrayList<String> fighter, String advName) {
        for (String obj : fighter) {
            if (Objects.equals(obj, advName)) {
                return 1;
            }
        }
        return -1;
    }

    public static Adventurer adventurerFind(String name) {
        for (Map.Entry<Integer, Adventurer> entry : adventurers.entrySet()) {
            Adventurer adventurer = entry.getValue();
            if (Objects.equals(adventurer.showName(), name)) {
                return adventurer;
            }
        }
        return null;
    }

    public static void fightLogP1(String fightLog, ArrayList<String> fighter) {
        String[] group = fightLog.split("-");
        if (fighterCheck(fighter, group[1]) == 1) {
            Adventurer adventurer = adventurerFind(group[1]);
            if (adventurer.useBotCheck(group[2]) == 1) {
                adventurer.fightUseBot(group[2]);
                String s = group[0] + " " + group[1] + " " + "used" + " " + group[2];
                fightTimeLog.add(s);
            } else {
                System.out.print("Fight log error\n");
            }
        } else {
            System.out.print("Fight log error\n");
        }
    }

    public static void fightLogP2(String fightLog, ArrayList<String> fighter) {
        String[] group = fightLog.split("[-@]");
        if (fighterCheck(fighter, group[1]) == 1 && fighterCheck(fighter, group[2]) == 1) {
            Adventurer adventurer1 = adventurerFind(group[1]);
            Adventurer adventurer2 = adventurerFind(group[2]);
            if (adventurer1.useEquCheck(group[3]) != null) {
                int level = adventurer1.showLevel();
                int hurt = adventurer1.useEquCheck(group[3]).showStar() * level;
                int hitpoint = adventurer2.foughtHitpoint(hurt);
                System.out.printf("%d %d\n", adventurer2.showId(), hitpoint);
                String s1 = group[0] + " " + group[1] + " " + "attacked" + " " + group[2];
                String s2 = s1 + " " + "with" + " " + group[3];
                adventurer1.fightLogAdd(s2);
                adventurer2.foughtLogAdd(s2);
                fightTimeLog.add(s2);
            } else {
                System.out.print("Fight log error\n");
            }
        } else {
            System.out.print("Fight log error\n");
        }
    }

    public static void fightLogP3(String fightLog, ArrayList<String> fighter) {
        String[] group = fightLog.split("[-@#]");
        if (fighterCheck(fighter, group[1]) == 1) {
            Adventurer adventurer = adventurerFind(group[1]);
            if (adventurer.useEquCheck(group[4]) != null) {
                int level = adventurer.showLevel();
                int hurt = adventurer.useEquCheck(group[4]).showStar() * level;
                String s1 = group[0] + " " + group[1] + " " + "AOE-attacked" + " " + "with";
                String s2 =  s1 + " " + group[4];
                adventurer.fightLogAdd(s2);
                fightTimeLog.add(s2);
                for (String name : fighter) {
                    if (!Objects.equals(name, group[1])) {
                        Adventurer adventurer1 = adventurerFind(name);
                        adventurer1.foughtLogAdd(s2);
                        int hitpoint = adventurer1.foughtHitpoint(hurt);
                        System.out.printf("%d ",hitpoint);
                    }
                }
                System.out.println();
            } else {
                System.out.print("Fight log error\n");
            }
        } else {
            System.out.print("Fight log error\n");
        }
    }

    public static void fightLogProcess(String fightLog, ArrayList<String> fighter) {
        if (patternCheck(fightLog) == 1) {
            fightLogP1(fightLog, fighter);
        } else if (patternCheck(fightLog) == 2) {
            fightLogP2(fightLog, fighter);
        } else if (patternCheck(fightLog) == 3) {
            fightLogP3(fightLog, fighter);
        }
    }

    public static void type14(String[] parts) {
        int m = Integer.parseInt(parts[1]);
        int k = Integer.parseInt(parts[2]);
        ArrayList<String> fighter = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            fighter.add(parts[i + 3]);
        }
        System.out.print("Enter Fight Mode\n");
        for (int i = 0; i < k; i++) {
            String fightLog = scanner.nextLine();
            fightLogProcess(fightLog, fighter);
        }
    }

    public static void type15(String[] parts) {
        int flag = 0;
        for (String str : fightTimeLog) {
            if (str.contains(parts[1])) {
                System.out.printf("%s\n", str);
                flag = 1;
            }
        }
        if (flag == 0) {
            System.out.print("No Matched Log\n");
        }
    }

    public static void type16(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        Adventurer adventurer = adventurers.get(advId);
        if (adventurer != null) {
            adventurer.fightCheck();
        }
    }

    public static void type17(String[] parts) {
        int advId = Integer.parseInt(parts[1]);
        Adventurer adventurer = adventurers.get(advId);
        adventurer.foughtCheck();
    }

    public static void main(String[] args) {
        int n = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < n; i++) {
            String str = scanner.nextLine();
            String[] parts = str.split(" ");
            int type = Integer.parseInt(parts[0]);
            if (type == 1) {
                type1(parts);
            } else if (type == 2) {
                type2(parts);
            } else if (type == 3) {
                type3(parts);
            } else if (type == 4) {
                type4(parts);
            } else if (type == 5) {
                type5(parts);
            } else if (type == 6) {
                type6(parts);
            } else if (type == 7) {
                type7(parts);
            } else if (type == 8) {
                type8(parts);
            } else if (type == 9) {
                type9(parts);
            } else if (type == 10) {
                type10(parts);
            } else if (type == 11) {
                type11(parts);
            } else if (type == 12) {
                type12(parts);
            } else if (type == 13) {
                type13(parts);
            } else if (type == 14) {
                type14(parts);
            } else if (type == 15) {
                type15(parts);
            } else if (type == 16) {
                type16(parts);
            } else if (type == 17) {
                type17(parts);
            }
        }
    }
}
