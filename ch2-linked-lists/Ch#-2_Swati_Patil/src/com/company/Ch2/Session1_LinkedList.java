package com.company.Ch2;


public class Session1_LinkedList {
    Node head = null;
    Node tail = null;

    public void addNode(int data){
        Node newNode = new Node(data);
        if(head == null && tail == null){
            head = tail = newNode;
        }
        while(tail!=null){
            tail.next = newNode;
            tail = newNode;
        }
    }



//    Question 2.1:
    public Node removeDuplicates(Node head){
        Node current = head;
        while(current != null && current.next != null){
            if(current.data == current.next.data){
                current.next = current.next.next;
            }else{
                current = current.next;
            }
        }
        return head;
    }

//    Question 2.2:
public Node removeKthElement(Node head, int k){
        Node dummyHead = new Node(0);
        dummyHead.next = head;
        Node slow = dummyHead;
        Node fast =dummyHead;

        for(int i=1; i<=k+1; i++){
            fast = fast.next;
        }
        while(fast!=null){
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
        return dummyHead.next;
}

//    Question 2.3:
    public Node removeMiddle(Node head){
        Node slow = head;
        Node fast = head;
        Node prev = null;

        if(head == null || head.next == null){
            return null;
        }

        while(fast!=null && fast.next!=null){
            fast = fast.next.next;
            prev = slow;
            slow = slow.next;
        }
        prev.next = slow.next;
        return head;
    }

}



