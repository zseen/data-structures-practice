import java.util.Optional;

public class HashMap
{
    private static final int hashSize = 100;

    private Node[] hashTable = new Node[hashSize];

    public void add(String key, String value)
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

    public Optional<String> get(String key)
    {
        int index = getHashedKey(key);


        Node currentNode = hashTable[index];
        while (currentNode != null)
        {
            if (currentNode.key == key)
            {
                Optional<String> val = Optional.ofNullable(currentNode.value);
                return val;
            }

            currentNode = currentNode.next;
        }

        Optional<String> val = Optional.ofNullable(null);
        return val;
    }

    // This hash function is pretty rudimentary
    // It gives the same result for anagrams, and also for e.g., “az” and “by”
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
        hm.add("tac", "2");
        hm.add("cat", "3");
        hm.add("bunny", null);
        System.out.println(hm.get("cat"));
        System.out.println(hm.get("tac"));
        System.out.println(hm.get("c"));
        System.out.println(hm.get("bunny"));
    }
}

