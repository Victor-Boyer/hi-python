def hangmandesign0():
    print("""
    ***********
    *         *
    *         *
    *         *
    *         *
    *         *
    ***********
    """)

def hangmandesign1():
    print("""
    ***********
    *         *
    *         *
    *         *
    *         *
    * ---     *
    ***********
    """)

def hangmandesign2():
    print("""
    ***********
    *         *
    *  |      *
    *  |      *
    *  |      *
    * ---     *
    ***********
    """)

def hangmandesign3():
    print("""
    ***********
    *  -----  *
    *  |      *
    *  |      *
    *  |      *
    * ---     *
    ***********
    """)

def hangmandesign4():
    print("""
    ***********
    *  -----  *
    *  |   O  *
    *  |      *
    *  |      *
    * ---     *
    ***********
    """)

def hangmandesign5():
    print("""
    ***********
    *  -----  *
    *  |   O  *
    *  |  /   *
    *  |      *
    * ---     *
    ***********
    """)

def hangmandesign6():
    print("""
    ***********
    *  -----  *
    *  |   O  *
    *  |  /O  *
    *  |      *
    * ---     *
    ***********
    """)

def hangmandesign7():
    print("""
    ***********
    *  -----  *
    *  |   O  *
    *  |  /O\ *
    *  |      *
    * ---     *
    ***********
    """)

def hangmandesign8():
    print("""
    ***********
    *  -----  *
    *  |   O  *
    *  |  /O\ *
    *  |  /   *
    * ---     *
    ***********
    """)

def hangmandesign9():
    print("""
    ***********
    *  -----  *
    *  |   O  *
    *  |  /O\ *
    *  |  / \ *
    * ---     *
    ***********
    """)

def hangmandesign(pdv):
    if pdv == 9:
        hangmandesign0()
    elif pdv == 8:
        hangmandesign1()
    elif pdv == 7:
        hangmandesign2()
    elif pdv == 6:
        hangmandesign3()
    elif pdv == 5:
        hangmandesign4()
    elif pdv == 4:
        hangmandesign5()
    elif pdv == 3:
        hangmandesign6()
    elif pdv == 2:
        hangmandesign7()
    elif pdv == 1:
        hangmandesign8()
    elif pdv == 0:
        hangmandesign9()
