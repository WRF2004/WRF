import org.junit.Test;

public class BottleTest {
    Bottle bottle = new Bottle(12, "wrf", 1);
    @Test
    public void showName() {
        Bottle bottle = new Bottle(12, "wrf", 1);
        assert (bottle.showName() == "wrf");
    }

    @Test
    public void showId() {
        Bottle bottle = new Bottle(12, "wrf", 1);
        assert (bottle.showId() == 12);
    }

    @Test
    public void showCap() {
        Bottle bottle = new Bottle(12, "wrf", 1);
        assert (bottle.showCap() == 1);
    }

    @Test
    public void subCap() {
        Bottle bottle = new Bottle(12, "wrf", 1);
        bottle.subCap();
        assert (bottle.showCap() == 0);
    }
}