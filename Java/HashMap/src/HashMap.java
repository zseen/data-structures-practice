public class HashMap
{
    private static final int hashSize = 100;

    private static Node[] hashTable = new Node[hashSize];

    public static void add(String key, int value)
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

    public static Integer get(String key)
    {
        if (!isKeyInHashTable(key))
        {
            return null;
        }
        else
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
        }

        return null;
    }

    private static int getHashedKey(String word)
    {
        int sum = 0;
        for (int i = 0; i < word.length(); i++)
        {
            sum += word.charAt(i);
        }

        return sum % hashSize;
    }

    private static boolean isKeyInHashTable(String key)
    {
        int index = getHashedKey(key);

        if (hashTable[index] == null)
        {
            return false;
        }
        else
        {
            Node currentNode = hashTable[index];
            while (currentNode != null)
            {
                if (currentNode.word == key)
                {
                    return true;
                }

                currentNode = currentNode.next;
            }

            return false;
        }
    }

    public static void main(String[] args)
    {
        add("tac", 2);
        add("cat", 3);
        add("dog", 4);
        System.out.println(get("cat"));
        System.out.println(get("c"));
    }
}

