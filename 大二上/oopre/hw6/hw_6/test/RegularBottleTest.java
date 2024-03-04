import static org.junit.Assert.*;

public class RegularBottleTest {
    RegularBottle regularBottle = new RegularBottle(1, "wrf", 2, 32, "RegularEquipment", 0);
    @org.junit.Test
    public void showAttr() {
        assertTrue(regularBottle.showAttr() == 2);
    }
}