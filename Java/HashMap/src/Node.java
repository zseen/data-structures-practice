public class Node
{
    String key;
    String value;
    public Node next;

    public static Node createNode(String key, String value)
    {
        Node newNode = new Node();
        newNode.key = key;
        newNode.value = value;
        return newNode;
    }
}
