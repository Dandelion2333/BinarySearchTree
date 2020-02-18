import PrintShape
import Insert
import Search


if __name__ == "__main__":
    BinaryTree = []
    GenerateData = []
    
    # Building a basic database
    for cnt in range(0,8):
        value = Insert.RandomVaule(1, 100)
        GenerateData.append(value)
        Insert.InsertElement(value, BinaryTree)
    
    print(GenerateData)
    print(BinaryTree)

    # Visual print binary tree
    PrintShape.BinaryTreePrinter(BinaryTree)

    # search data
    value = GenerateData[5]
    print(value)
    result = Search.SearchData(value, 0, BinaryTree)
    print("result:",result)
