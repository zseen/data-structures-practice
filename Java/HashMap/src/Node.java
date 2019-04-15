public class Node
{
    String key;
    int value;
    public Node next;

    public static Node createNode(String key, int value)
    {
        Node newNode = new Node();
        newNode.key = key;
        newNode.value = value;
        return newNode;
    }
}
