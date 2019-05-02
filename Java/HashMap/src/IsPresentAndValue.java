public class IsPresentAndValue
{
    private boolean isPresent;
    private String value;

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

    public void setValue(String value)
    {
        this.value = value;
        this.isPresent = true;
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
