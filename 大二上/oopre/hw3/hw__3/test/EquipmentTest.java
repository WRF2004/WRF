import org.junit.Test;

public class EquipmentTest {
    Equipment equipment = new Equipment(1, "wrf", 1);
    @Test
    public void showName() {
        Equipment equipment = new Equipment(1, "wrf", 1);
        assert (equipment.showName() == "wrf");
    }

    @Test
    public void addS() {
        Equipment equipment = new Equipment(1, "wrf", 1);
        equipment.addS();
        assert (equipment.showStar() == 2);
    }

    @Test
    public void showStar() {
        Equipment equipment = new Equipment(1, "wrf", 1);
        assert (equipment.showStar() == 1);
    }

    @Test
    public void showId() {
        Equipment equipment = new Equipment(1, "wrf", 1);

    }
}