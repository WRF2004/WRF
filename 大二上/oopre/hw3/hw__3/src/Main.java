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
            int advId = Integer.parseInt(parts[1]);
            if (type == 1) {
                Adventurer adventurer = new Adventurer(advId, parts[2], 500, 1);
                adventurers.put(advId, adventurer);
            } else if (type == 2) {
                Adventurer adventurer = adventurers.get(advId);
                adventurer.addBot(Integer.parseInt(parts[2]), parts[3], Integer.parseInt(parts[4]));
            } else if (type == 3) {
                String name = adventurers.get(advId).showBotName(Integer.parseInt(parts[2]));
                adventurers.get(advId).subBot(Integer.parseInt(parts[2]));
                System.out.printf("%d %s\n",adventurers.get(advId).showBotSize(),name);
            } else if (type == 4) {
                int equId = Integer.parseInt(parts[2]);
                adventurers.get(advId).addEqu(equId, parts[3], Integer.parseInt(parts[4]));
            } else if (type == 5) {
                String name = adventurers.get(advId).showEquName(Integer.parseInt(parts[2]));
                adventurers.get(advId).subEqu(Integer.parseInt(parts[2]));
                System.out.printf("%d %s\n",adventurers.get(advId).showEquSize(),name);
            } else if (type == 6) {
                int equId = Integer.parseInt(parts[2]);
                String name = adventurers.get(advId).showEquName(Integer.parseInt(parts[2]));
                adventurers.get(advId).addStar(Integer.parseInt(parts[2]));
                System.out.printf("%s %d\n",name,adventurers.get(advId).showStar(equId));
            } else if (type == 7) {
                int foodId = Integer.parseInt(parts[2]);
                int energy = Integer.parseInt(parts[4]);
                adventurers.get(advId).addFood(foodId, parts[3], energy);
            } else if (type == 8) {
                int foodId = Integer.parseInt(parts[2]);
                String name = adventurers.get(advId).showFoodName(foodId);
                adventurers.get(advId).subFood(foodId);
                System.out.printf("%d %s\n",adventurers.get(advId).showFoodSize(),name);
            } else if (type == 9) {
                adventurers.get(advId).addEquBag(Integer.parseInt(parts[2]));
            } else if (type == 10) {
                int botId = Integer.parseInt(parts[2]);
                adventurers.get(advId).addBotBag(botId);
            } else if (type == 11) {
                int foodId = Integer.parseInt(parts[2]);
                Adventurer adventurer = adventurers.get(advId);
                adventurer.addFoodBag(foodId);
            } else if (type == 12) {
                String name = parts[2];
                Adventurer adventurer = adventurers.get(advId);
                adventurer.useBot(name);
            } else if (type == 13) {
                String name = parts[2];
                Adventurer adventurer = adventurers.get(advId);
                adventurer.useFood(name);
            }
        }
    }
}
