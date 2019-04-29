@SuppressWarnings("hiding")
public class Pair<Boolean, String>
{ 
    @Override
	public java.lang.String toString()
    {
		return "(" + isInHashTable + ", " + value + ")";
	}
    
	public final Boolean isInHashTable; 
    public final String value; 
    public Pair(Boolean isInHashTable, String value)
    { 
        this.isInHashTable = isInHashTable; 
        this.value = value; 
    }
}
   