 
class node:

    data = 0 
    next = None
    
    def __init__(self,no):
        self.data =no
        self.next = None


class SinglyLL:
 

    def __init__(self):
        print("Inside Constructor")
        self._first = None
        self._count =0

    def Display(self):
        temp = self._first

        while temp is not None:
            print(temp.data,end="=>")
            temp = temp.next

        print("None")

    def InsertFirst(self ,no):
        
        newn = node(no)


        if self._first is None:
            self._first =newn

        else:
            newn.next = self._first
            self._first = newn

        self._count += 1

    def Count(self):
        return self._count


    def InsertLast(self ,no):
        newn =node(no)

        if self._first is None:
            self._first = newn

        elif self._first.next is None:
            self._first.next = newn

        else:
            Temp = self._first

            while Temp.next is not None:
                Temp = Temp.next

            Temp.next = newn

        self._count += 1
        

    def DeleteFirst(self ):
        if self._first is None:
            print("linked list is empty ")
            return
        else:
            temp = self._first
            self._first = self._first.next

        self._count -= 1


            

    def DeleteLast(self ):
        if self._first is None:
            print("linked list is empty ")
            return
        elif self._first.next is None:
            self._first =None

        else:
            temp = self._first

            while temp.next.next is not None:
                temp = temp.next

            temp.next = None

        self._count -= 1

    def InsertAtpos(self, no,Pos):

        if Pos < 1 or Pos > self._count+1:
            print("Invalid pos ")
            return

        if(Pos == 1):
            self.InsertFirst(no)
            return

        elif(Pos == self._count+1):
            self.InsertLast(no)
            return

        else:
            newn =node(no)
            temp = self._first

            for i in range( Pos -2):
                temp= temp.next

            newn.next = temp.next
            temp.next = newn

        self._count += 1

    def DeleteAtPos(self ,Pos):
        if Pos < 1 or Pos > self._count:
                    print("Invalid pos ")
                    return
        
        if(Pos == 1):
            self.DeleteFirst()
            return

        elif(Pos == self._count):
            self.DeleteLast()
            return

        else:
            temp = self._first

            for i in range( Pos -2):
                temp= temp.next

            target = temp.next
            
            temp.next = temp.next.next

        self._count -= 1



def main():
    sobj = None
    sobj = SinglyLL()

    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)


    sobj.Display()
    print("Number of nodes :",sobj.Count())

    sobj.InsertLast(101)
    sobj.InsertLast(111)
    sobj.InsertLast(121)

    sobj.Display()
    print("Number of nodes : ",sobj.Count())


    

    sobj.DeleteFirst()
    sobj.Display()
    print("Number of nodes : ",sobj.Count())

    sobj.DeleteLast()
    sobj.Display()
    print("Number of nodes : ",sobj.Count())

    sobj.InsertAtpos(105,4)
    sobj.Display()
    print("Number of nodes : ",sobj.Count())

    sobj.DeleteAtPos(4)
    sobj.Display()
    print("Number of nodes : ",sobj.Count())




if __name__ == "__main__":
    main()
