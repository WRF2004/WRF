import org.junit.Test;
import static org.junit.Assert.*;

public class EquipmentTest {
    Equipment equipment = new Equipment(1, "wrf", 1);
    @Test
    public void showName() {
        Equipment equipment = new Equipment(1, "wrf", 1);
        assertTrue (equipment.showName() == "wrf");
    }

    @Test
    public void addS() {
        Equipment equipment = new Equipment(1, "wrf", 1);
        equipment.addS();
        assertTrue (equipment.showStar() == 2);
    }

    @Test
    public void showStar() {
        Equipment equipment = new Equipment(1, "wrf", 1);
        assertTrue (equipment.showStar() == 1);
    }

    @Test
    public void showId() {
        Equipment equipment = new Equipment(1, "wrf", 1);
        assertTrue (equipment.showId() == 1);
    }
}