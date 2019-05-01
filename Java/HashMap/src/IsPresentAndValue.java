public class IsPresentAndValue
{
    private boolean isPresent;
    public String value;

    public IsPresentAndValue(String value)
    {
        this.value = value;
        this.isPresent = true;
    }

    public IsPresentAndValue()
    {
        this.value = null;
        this.isPresent = false;
    }

    public boolean isPresent()
    {
        return isPresent;
    }

    public void reset()
    {
        isPresent = false;
    }

    public String getValue()
    {
        if(!isPresent)
        {
            throw new NullPointerException("Not present");
        }

        return value;
    }
}
