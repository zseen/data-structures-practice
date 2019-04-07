public class HashMap {
	public static final int hashSize = 100;
	
	public static Node[] hashTable = new Node[hashSize];
	
	public static void insertItemIntoHashTable(String word, int number)
	{
		int index = getHashedValue(word);
		Node currentNode = new Node();
		currentNode.word = word;
		currentNode.number = number;
		
		
		if (hashTable[index] == null)
		{
			hashTable[index] = currentNode;
		}
		else
		{
			currentNode.next = hashTable[index];
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
		else
		{
			Node currNode = hashTable[index];
			while (currNode != null)
			{
				if (currNode.word == word)
				{
					return true;
				}
			
				currNode = currNode.next;
			}
		}
		return false;
	}
	
	public static int getValue(String key)
	{
		return 0;
	}
	

	public static void main(String[] args) {
		insertItemIntoHashTable("tac", 2);
		insertItemIntoHashTable("cat", 3);
		System.out.println(isWordInHashTable("tac"));
		System.out.println(isWordInHashTable("cat"));
		System.out.println(isWordInHashTable("act"));
		
		

	}

}

