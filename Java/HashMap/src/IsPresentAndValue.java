public class IsPresentAndValue<T>
{
    private boolean isPresent;
    private T value;

    public IsPresentAndValue(T value)
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

    public void setValue(T value)
    {
        this.value = value;
        this.isPresent = true;
    }

    public T getValue()
    {
        if(!isPresent)
        {
            throw new NullPointerException("Not present");
        }

        return value;
    }
}
