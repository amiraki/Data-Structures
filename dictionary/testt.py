MAX = 50
class Node:

    data = '@'
    isEndOfString = 1
    left = None
    eq = None
    right = None
class TurnaryTree:

    root1 = None

    def newNode(self, data):

        temp = Node()
        temp.data = data;
        temp.isEndOfString = 0;
        temp.left = temp.eq = temp.right = None;
        return temp;

    def insert(self, word, ind, size):
        if (self.root1 == None):
            self.root1 = self.newNode(word[ind])
        self.root1 = self.insert1(self.root1, word, ind, size)

    def insert1(self, root, word, ind, size):
        #print("First")
        #print(root.data, "    ", root.left, "    ", root.eq, "    ", root.right, "    ", ind, "     ", word[ind])
        if root == None:
            return self.newNode(word[ind])
            root.data = word[ind]
            #print(ind, "   ", root.data)
        if word[ind] < root.data:
            root.left = self.insert1(root.left, word, ind, size)
        elif word[ind] > root.data:
            root.right = self.insert1(root.right, word, ind, size)
        else:
            if (ind+1) < len(word):
                root.eq = self.insert1(root.eq, word, ind+1, len(word));
            else:
                root.isEndOfString = 1;
        return root


    def traverseTSTUtil(self, root, buffer):
        if root != None:
            print(root.data, str(root.isEndOfString))
            self.traverseTSTUtil(root.left, buffer)
            buffer = buffer + root.data + str(root.isEndOfString)
            #print(buffer)
            if (root.isEndOfString):
                print(buffer, end="")
                buffer = ""
            self.traverseTSTUtil(root.eq, buffer)
            self.traverseTSTUtil(root.right, buffer)
      

    def traverseTST(self):        
        self.traverseTST1(self.root1)

    def traverseTST1(self, root):
        buffer = ""
        self.traverseTSTUtil(root, buffer)
     
    def searchTST1(self, root, word, ind):

        if root == None:
            return False;
        print(word[ind])
        if word[ind] < root.data:
            return self.searchTST1(root.left, word[ind], ind)
     
        elif word[ind] > root.data:
            return self.searchTST1(root.right, word[ind], ind)
     
        else:


            if ind+1 == len(word):
                return True#root.isEndOfString
     
            return self.searchTST1(root.eq, word, ind+1)

    def searchTST(self, word, ind):
        return self.searchTST1(self.root1, word, ind)
     
T = TurnaryTree()

T.insert("cat", 0, 3)

T.insert("cats", 0, 4)
print(T.root1== None)
T.insert("cats", 0, 4)
T.insert("up", 0, 2)
T.insert("bug", 0, 3)

print("Following is traversal of ternary search tree\n")
T.traverseTST()
print(T.searchTST("cat", 0))
print(T.searchTST("up", 0))
print(T.searchTST("upssss", 0))
#print(T.searchTST("up", 0))
# printf("\nFollowing are search results for cats, bu and cat respectively\n");
# searchTST(root, "cats")? printf("Found\n"): printf("Not Found\n");
# searchTST(root, "bu")?   printf("Found\n"): printf("Not Found\n");
# searchTST(root, "cat")?  printf("Found\n"): printf("Not Found\n");
