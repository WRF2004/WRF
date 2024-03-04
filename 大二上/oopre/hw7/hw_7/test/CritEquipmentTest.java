import static org.junit.Assert.*;

public class CritEquipmentTest {
    CritEquipment critequipment = new CritEquipment(12, "wrf", 3, 23, "CritEquipment", 2);
    @org.junit.Test
    public void showAttr() {
        assertTrue (critequipment.showAttr() == 3);
    }
}