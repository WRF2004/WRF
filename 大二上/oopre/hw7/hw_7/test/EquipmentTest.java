import org.junit.Test;

import java.util.Objects;

import static org.junit.Assert.*;

public class EquipmentTest {
    Equipment equipment = new Equipment(1, "wrf", 1, 10, "EpicEquipment", 0.3);
    @Test
    public void showName() {
        Equipment equipment = new Equipment(1, "wrf", 1, 10, "EpicEquipment", 0.3);
        assertTrue (equipment.showName() == "wrf");
    }

    @Test
    public void addS() {
        Equipment equipment = new Equipment(1, "wrf", 1, 10, "EpicEquipment", 0.3);
        equipment.addS();
        assertTrue (equipment.showAttr() == 2);
    }

    @Test
    public void showStar() {
        Equipment equipment = new Equipment(1, "wrf", 1, 10, "EpicEquipment", 0.3);
        assertTrue (equipment.showAttr() == 1);
    }

    @Test
    public void showOthers() {
        Equipment equipment = new Equipment(1, "wrf", 1, 10, "EpicEquipment", 0.3);
        assertTrue (equipment.showOthers() == 0.3);
    }

    @Test
    public void showPrice() {
        Equipment equipment = new Equipment(1, "wrf", 1, 10, "EpicEquipment", 0.3);
        assertTrue (equipment.showPrice() == 10);
    }

    @Test
    public void showType() {
        Equipment equipment = new Equipment(1, "wrf", 1, 10, "EpicEquipment", 0.3);
        assertTrue (Objects.equals(equipment.showType(), "EpicEquipment"));
    }

    @Test
    public void showId() {
        Equipment equipment = new Equipment(1, "wrf", 1, 10, "EpicEquipment", 0.3);
        assertTrue (equipment.showId() == 1);
    }
}