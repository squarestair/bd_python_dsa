from l07_stack import Stack


def is_balanced(input_str):
    st = Stack()
    if not input_str:
        return True
    for c in input_str:
        if c == "(":
            st.push(c)
        if c == ")":
            e = st.pop()
            if e is None:
                return False
    return st.size() < 1
