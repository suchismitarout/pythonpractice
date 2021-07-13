from stack import Stack

def reverse_string(input_string):
    k = ""
    for i in input_string:
        k = i + k
    print(k)



reverse_string("sukkum")


def reverse(input_string):
    n = len(input_string)
    st = Stack()
    l = ""
    for i in range(n):
        st.push(input_string[i])

    for j in range(n):
        l += st.pop()
    print(l)


reverse("hello")