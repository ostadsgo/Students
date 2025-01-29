"""
Calcualte area of a rectangle.
If width or hight is not positive interger number 
returns zero.
Parameters:
-----------
width: int
    Width of the rectangle.
height: int
    Hight of the rectangle
Return
------
outs: int
    Calculate area and return the result.
"""

def area(w, h):
    pass

# -----------------------------------
def run_test():
    fn_name = "area"
    # Tests
    tests = {
        "test#1": {"param": (2, 3), "result": 6},
        "test#2": {"param": (0, 0), "result": 0},
        "test#3": {"param": (1, 1), "result": 1},
        "test#4": {"param": (-1, 1), "result": 0},
        "test#5": {"param": (4, 2), "result": 8},
    }

    for name, value in tests.items():
        param = value["param"] if value.get("param") is not None else ()
        result = value.get("result")
        r = area(*param)
        if r == result:
            print(f"✅{name.upper()} passed.")
        else:
            print(f"❌{name.upper()} failed.")
            print(f"{fn_name}{param} Expect {result} but got {r}")
        

if __name__ == "__main__":
    run_test()
