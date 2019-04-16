public class HashMap
{
    private static final int hashSize = 100;

    private Node[] hashTable = new Node[hashSize];

    public void add(String key, Object value)
    {
        int index = getHashedKey(key);
        Node currentNode = Node.createNode(key, String.valueOf(value));

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

    public String get(String key)
    {
        int index = getHashedKey(key);

        Node currentNode = hashTable[index];
        while (currentNode != null)
        {
            if (currentNode.key == key)
            {
                return currentNode.value;
            }

            currentNode = currentNode.next;
        }

        return null;
    }

    private int getHashedKey(String word)  // This hash function is pretty rudimentary, it gives the same result for anagrams, and also for e.g., �az� and �by� 
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
        hm.add("tac", "2");
        hm.add("cat", 3);
        hm.add("dog", 4.12);
        System.out.println(hm.get("cat"));
        System.out.println(hm.get("dog"));
        System.out.println(hm.get("tac"));
        System.out.println(hm.get("c"));
    }
}
