public class Node 
{
	String word;
	int number;
	public Node next;
	
	public static Node createNode(String word, int number)
	{
		Node newNode = new Node();
		newNode.word = word;
		newNode.number = number;
		return newNode;
	}
}
