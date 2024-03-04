import static org.junit.Assert.*;

public class RegularEquipmentTest {
    RegularEquipment regularEquipment = new RegularEquipment(1, "wrf", 2, 32, "RegularEquipment", 0);
    @org.junit.Test
    public void showAttr() {
        assertTrue(regularEquipment.showAttr() == 2);
    }
}