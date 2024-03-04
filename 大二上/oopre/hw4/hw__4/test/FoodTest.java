import org.junit.Test;

public class FoodTest {
    Food food = new Food(1, "wrf", 12);
    @Test
    public void showName() {
        Food food = new Food(1, "wrf", 12);
        assert (food.showName() == "wrf");
    }

    @Test
    public void showId() {
        Food food = new Food(1, "wrf", 12);
        assert (food.showId() == 1);
    }

    @Test
    public void showEnergy() {
        Food food = new Food(1, "wrf", 12);
        assert (food.showEnergy() == 12);
    }
}