def Stack(): 
    stack=[]
    def method(*args): #*args merupakan magic variable yang fungsinya mengubah parameter kebentuk tuple
        if args[0]=='push':  
            stack.append(args[1])
        elif args[0]=="pop": 
            return (stack.pop())
        elif args[0]=='peek': 
            return (stack[-1]) 
        elif args[0]=="size": 
            return (len(stack))
    return method 

def Priority(char):
    if char == "^":
        return 3
    elif char == "/" or char == "*":
        return 2
    elif char == "+" or char == "-":
        return 1
    return float("inf")

def prefxToInfix(expression): 
    if isinstance(expression, list): #isIntance merupakan built in function di dalam Python yang dapat mengembalikan nilai True jika objek sama seperti tipe data yang kita tentukan
        operator, kiri, kanan = expression
        return '(' + prefxToInfix(kiri) + operator + prefxToInfix(kanan) + ')'
    else:
        return str(expression)

def InfixToPostfix(expression):
    listStack = []
    output = ""
    for karakter in expression:
        if karakter.isalnum(): #isalnum merupakan built in function di dalam Python yang dapat mengembalikan nilai True jika semua karakter di dalam list merupakan nilai alnumerik atau a-z dan 0-9
            output += karakter
        elif karakter in ["^", "*", "/", "+", "-", "("]:
            while ( len(listStack) > 0 and listStack[-1] != "(" and Priority(listStack[-1]) >= Priority(karakter)):
                output += listStack.pop()
            listStack.append(karakter)
        elif karakter == ")":
            while listStack[-1] != "(":
                output += listStack.pop()
            listStack.pop()
    while len(listStack) > 0:
        output += listStack.pop()
    return output

print("Prefix : + / 7Y - A Z * 11D W")
a = prefxToInfix(['+',['/', ["(", 7, "Y", ], ["-", "A", "Z"]], ["*", ['(', 11, "D"],"W"]])  #untuk kode program ini kita harus menentukan letak dari penentuan tanda kurung sikunya ([]), dengan cara mencari PrefixToInfixnya terlebih dahulu secara manual
b = a.replace("(", "")
c = b.replace(")", "")
d = " ".join(c)

infix = a
print(f"Infix: {d}")
x = InfixToPostfix(infix)
y = x.replace("(", "")
z = y.replace(")", "")
zz = " ".join(z)
print("Postfix: ", zz)

print()
print("Fungsi yang digunakan dalam program ini adalah Prefix To Infix and Infix To Postfix")
print("Prefix To Infix = (7Y)/(A-Z)+(11D*W)")
print("Infix To Postfix = 7YAZ-/11DW*+ ")






"""" Referensi program 
 1. https://www.geeksforgeeks.org/prefix-postfix-conversion/
 2. https://www.geeksforgeeks.org/prefix-infix-conversion/?ref=rp
 3. https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
 4. http://codinginpro.blogspot.com/2018/07/infix-prefix-dan-postfix-python.html
 5. https://www.codesdope.com/
 6. https://github.com/lilianweng/LeetcodePython/blob/master/expression.py
"""