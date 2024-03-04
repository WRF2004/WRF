import static org.junit.Assert.*;

public class EpicEquipmentTest {
    EpicEquipment epicequipment = new EpicEquipment(12, "wrf", 3, 23, "CritEquipment", 2);
    @org.junit.Test
    public void showAttr() {
        assertTrue (epicequipment.showAttr() == 3);
    }
}