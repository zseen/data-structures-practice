public class HashMap {
	public static final int hashSize = 100;
	
	public static Node[] hashTable = new Node[hashSize];
	
	public static void insertItemIntoHashTable(String word)
	{
		int index = getHashedValue(word);
		Node currentNode = createNode(word)
		
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
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
