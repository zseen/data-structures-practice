public class HashMap
{
    private static final int hashSize = 100;

    private Node[] hashTable = new Node[hashSize];

    public void add(String key, int value)
    {
        int index = getHashedKey(key);
        Node currentNode = Node.createNode(key, value);

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

    public Integer get(String key)
    {
		int index = getHashedKey(key);

		Node currentNode = hashTable[index];
		while (currentNode != null)
		{
			if (currentNode.word == key)
			{
				return currentNode.number;
			}

			currentNode = currentNode.next;
		}
        
        return null;
    }

    private int getHashedKey(String word)
    {
        int sum = 0;
        for (int i = 0; i < word.length(); i++)
        {
            sum += word.charAt(i);
        }

        return sum % hashSize;
    }

    public static void main(String[] args)
    {
    	HashMap hm = new HashMap();
        hm.add("tac", 2);
        hm.add("cat", 3);
        hm.add("dog", 4);
        System.out.println(hm.get("cat"));
        System.out.println(hm.get("c"));
    }
}

