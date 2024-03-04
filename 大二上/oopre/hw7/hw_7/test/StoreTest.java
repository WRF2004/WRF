import org.junit.Test;

import java.util.HashSet;

import static org.junit.Assert.*;

public class StoreTest {

    @Test
    public void addBot() {
        Store store = new Store();
        store.addBot(new Bottle(1, "wrf", 2, 3, "RegularBottle", 0));
    }

    @Test
    public void addEqu() {
        Store store = new Store();
        store.addEqu(new Equipment(1, "wrf", 2, 3, "RegularEquipment", 0));
    }

    @Test
    public void addBotBag() {
        Store store = new Store();
        HashSet<Bottle> bot = new HashSet<>();
        store.addBotBag(bot);
    }

    @Test
    public void addEquBag() {
        Store store = new Store();
        HashSet<Equipment> bot = new HashSet<>();
        store.addEquBag(bot);
    }

    @Test
    public void addFoodBag() {
        Store store = new Store();
        HashSet<Food> bot = new HashSet<>();
        store.addFoodBag(bot);
    }

    @Test
    public void addFood() {
        Store store = new Store();
        store.addFood(new Food(1, "wrf", 2, 3));
    }

    @Test
    public void attr() {
        Store store = new Store();
        assertNotEquals(-1, store.Attr("Food"));
        assertNotEquals(-1, store.Attr("RegularBottle"));
        assertNotEquals(-1, store.Attr("ReinforcedBottle"));
        assertNotEquals(-1, store.Attr("RecoverBottle"));
        assertNotEquals(-1, store.Attr("RegularEquipment"));
    }

    @Test
    public void price() {
        Store store = new Store();
        assertNotEquals(-1, store.Price("Food"));
        assertNotEquals(-1, store.Price("RegularBottle"));
        assertNotEquals(-1, store.Price("ReinforcedBottle"));
        assertNotEquals(-1, store.Price("RecoverBottle"));
        assertNotEquals(-1, store.Price("RegularEquipment"));
    }
}