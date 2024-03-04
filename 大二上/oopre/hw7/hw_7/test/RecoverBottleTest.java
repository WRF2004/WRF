import static org.junit.Assert.*;

public class RecoverBottleTest {
    RecoverBottle recoverBottle = new RecoverBottle(1, "wrf", 2, 32, "RegularEquipment", 0);
    @org.junit.Test
    public void showAttr() {
        assertTrue(recoverBottle.showAttr() == 2);
    }
}