import static org.junit.jupiter.api.Assertions.*;
import static org.junit.Assert.assertEquals;
import org.junit.jupiter.api.Test;


class IsPresentAndValueTest
{
    @Test
    void test_createNewIVPInstance_isPresentIsFalse()
    {
        IsPresentAndValue<?> ivp = new IsPresentAndValue<Object>();
        assertEquals(ivp.isPresent(), false);
    }

    @Test
    void test_setValue_isPresentIsTrue()
    {
        IsPresentAndValue<String> ivp = new IsPresentAndValue<String>();
        ivp.setValue("piggy");
        assertEquals(ivp.isPresent(), true);
    }

    @Test
    void test_setValue_getValueEqualsSetValue()
    {
        IsPresentAndValue<String> ivp = new IsPresentAndValue<String>();
        ivp.setValue("pig");
        assertEquals(ivp.getValue(), "pig");
    }

    @Test
    void test_reset_isPresentIsFalse()
    {
        IsPresentAndValue<String> ivp = new IsPresentAndValue<String>();
        ivp.setValue("wild boar");
        assertEquals(ivp.isPresent(), true);
        assertEquals("wild boar", ivp.getValue());

        ivp.reset();
        assertEquals(ivp.isPresent(), false);
    }
}
