import org.junit.Test;
import static org.junit.Assert.*;

public class BottleTest {
    Bottle bottle = new Bottle(12, "wrf", 1, 10, "ReinforcedBottle", 0.3);
    @Test
    public void showName() {
        Bottle bottle = new Bottle(12, "wrf", 1, 10, "ReinforcedBottle", 0.3);
        assertTrue (bottle.showName() == "wrf");
    }

    @Test
    public void showId() {
        Bottle bottle = new Bottle(12, "wrf", 1, 10, "ReinforcedBottle", 0.3);
        assertTrue (bottle.showId() == 12);
    }

    @Test
    public void showCap() {
        Bottle bottle = new Bottle(12, "wrf", 1, 10, "ReinforcedBottle", 0.3);
        assertTrue (bottle.showCap() == 1);
    }

    @Test
    public void showPrice() {
        Bottle bottle = new Bottle(12, "wrf", 1, 10, "ReinforcedBottle", 0.3);
        assertTrue (bottle.showPrice() == 10);
    }

    @Test
    public void showAttr() {
        Bottle bottle = new Bottle(12, "wrf", 1, 10, "ReinforcedBottle", 0.3);
        assertTrue (bottle.showAttr() == 1);
    }

    @Test
    public void subCap() {
        Bottle bottle = new Bottle(12, "wrf", 1, 10, "ReinforcedBottle", 0.3);
        bottle.subCap();
        assertTrue (bottle.showCap() == 0);
    }
}