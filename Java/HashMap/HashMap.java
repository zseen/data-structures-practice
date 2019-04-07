public class HashMap {
	public static final int hashSize = 100;
	
	public static Node[] hashTable = new Node[hashSize];
	
	public static void insertItemIntoHashTable(String word)
	{
		int index = getHashedValue(word);
		Node currentNode = new Node();
		currentNode.word = word;
		
		if (hashTable[index] == null)
		{
			hashTable[index] = currentNode;
		}
	}
	
	public static int getHashedValue(String word)
	{
		int sum = 0;
		for (int i = 0; i < word.length(); i++)
		{
			sum += word.charAt(i);
		}
		
		return sum % hashSize;	
	}
	
	public static boolean isWordInHashTable(String word)
	{
		int index = getHashedValue(word);
		
		if (hashTable[index] == null)
		{
			return false;
		}
		
		return true;
	}
	

	public static void main(String[] args) {
		HashMap h = new HashMap();
		insertItemIntoHashTable("cat");
		System.out.println(isWordInHashTable("dog"));
		System.out.println(isWordInHashTable("cat"));
		

	}

}
