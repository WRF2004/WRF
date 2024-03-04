import org.junit.Test;
import static org.junit.Assert.*;

public class FoodTest {
    Food food = new Food(1, "wrf", 12, 10);
    @Test
    public void showName() {
        Food food = new Food(1, "wrf", 12, 10);
        assertTrue (food.showName() == "wrf");
    }

    @Test
    public void showId() {
        Food food = new Food(1, "wrf", 12, 10);
        assertTrue (food.showId() == 1);
    }

    @Test
    public void showType() {
        Food food = new Food(1, "wrf", 12, 10);
        assertTrue (food.showType() == "Food");
    }

    @Test
    public void showEnergy() {
        Food food = new Food(1, "wrf", 12, 10);
        assertTrue (food.showAttr() == 12);
    }

    @Test
    public void showPrice() {
        Food food = new Food(1, "wrf", 12, 10);
        assertTrue (food.showPrice() == 10);
    }
}