Copyright 2020 Evgeny Kondratenko

Test task for JetBrains research project Coding Assistant:
    Write kotlin program to make open brackets between letters in a first half of string, and closed in second one
    Between every neighbour pair of brackets must be at least 1 character

Description:
    - For odd length of string brackets should be around the middle character
    - For even numbers it should be around two middle ones characters

Examples:
    add_brackets("a")            -> a
    add_brackets("ac")           -> ac
    add_brackets("eSctRts")      -> e(S(c(t)R)t)s
    add_brackets("abcDeFRGghht") -> a(b(c(D(e(FR)G)g)h)h)t
