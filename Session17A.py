cpp_source_code = """#include<iostream>
using namespace std;
int main(){
    cout<<"Hello World";
    return 0;
}
"""

dart_source_code = """void main(){
    print("Hello World");
}
"""

java_source_code = """class App{
    public static void main(String[] args){
        System.out.println("Hello World");
    }
}
"""

python_source_code = """print("Hello World")
"""

"""
print("We will generate a hello world program :)")
print("Which source code would you like to generate ?")
choice = input("Enter Programming Language: ")

file_name = ""
data = None

if choice == "cpp":
    file_name = "hello.cpp"
    data = cpp_source_code
elif choice == "java":
    file_name = "hello.java"
    data = java_source_code
elif choice == "dart":
    file_name = "hello.dart"
    data = dart_source_code
elif choice == "python":
    file_name = "hello.py"
    data = python_source_code
else:
    print("Sorry !! I do Not Support Generating Source Code for", choice)

if len(file_name) != 0:
    file = open("/Users/ishantkumar/Downloads/{}".format(file_name), "w")
    file.write(data)
    print("Source Code Saved :)")

"""

file_contents = {
    "file_name": "",
    "data": ""
}

print("Hello, This is John")
print("Tell me which programming language would you like to explore")
choice = input("Enter Choice:")
words = choice.split()
if "cpp" in words:
    file_contents['file_name'] = "hello.cpp"
    file_contents['data'] = cpp_source_code

elif "dart" in words:
    file_contents['file_name'] = "hello.dart"
    file_contents['data'] = dart_source_code

else:
    print("Sorry! I do not support this yet")


if len(file_contents['file_name']) != 0:
    file = open("/Users/ishantkumar/Downloads/{}".format(file_contents['file_name']), "w")
    file.write(file_contents['data'])
    print("Please check your Downloads Directory")