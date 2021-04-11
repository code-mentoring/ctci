package com.company.Ch2;

public class Session2_Linked_List {

    //  Question 2.7:
    public Node checkIntersection(Node headA, Node headB){
        Node aPointer = headA;
        Node bPointer = headB;

        while(aPointer != bPointer){
            if(aPointer == null){
                aPointer = headB;
            }else{
                aPointer = aPointer.next;
            }

            if(bPointer == null){
                bPointer = headA;
            }else{
                bPointer = bPointer.next;
            }
        }
        return aPointer;
    }
}


