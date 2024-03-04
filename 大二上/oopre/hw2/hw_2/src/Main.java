// package ooprehomework_2023_22373180_hw_2.src;

import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<Integer, Adventurer> adventurers = new HashMap<>();
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < n; i++) {
            String str = scanner.nextLine();
            String[] parts = str.split(" ");
            int type = Integer.parseInt(parts[0]);
            if (type == 1) {
                int advId = Integer.parseInt(parts[1]);
                String name = parts[2];
                Adventurer adventurer = new Adventurer(advId, name);
                adventurers.put(advId, adventurer);
            } else if (type == 2) {
                int advId = Integer.parseInt(parts[1]);
                int botId = Integer.parseInt(parts[2]);
                String name = parts[3];
                int capacity = Integer.parseInt(parts[4]);
                Adventurer adventurer = adventurers.get(advId);
                adventurer.addBot(botId, name, capacity);
            } else if (type == 3) {
                int advId = Integer.parseInt(parts[1]);
                int botId = Integer.parseInt(parts[2]);
                Adventurer adventurer = adventurers.get(advId);
                String name = adventurer.showBotName(botId);
                adventurer.subBot(botId);
                int size = adventurer.showBotSize();
                System.out.printf("%d %s\n",size,name);
            } else if (type == 4) {
                int advId = Integer.parseInt(parts[1]);
                int equId = Integer.parseInt(parts[2]);
                String name = parts[3];
                int star = Integer.parseInt(parts[4]);
                Adventurer adventurer = adventurers.get(advId);
                adventurer.addEqu(equId, name, star);
            } else if (type == 5) {
                int advId = Integer.parseInt(parts[1]);
                int equId = Integer.parseInt(parts[2]);
                Adventurer adventurer = adventurers.get(advId);
                String name = adventurer.showEquName(equId);
                adventurer.subEqu(equId);
                int size = adventurer.showEquSize();
                System.out.printf("%d %s\n",size,name);
            } else if (type == 6) {
                int advId = Integer.parseInt(parts[1]);
                int equId = Integer.parseInt(parts[2]);
                Adventurer adventurer = adventurers.get(advId);
                String name = adventurer.showEquName(equId);
                adventurer.addStar(equId);
                int starNum = adventurer.showStar(equId);
                System.out.printf("%s %d\n",name,starNum);
            }
        }
    }
}
