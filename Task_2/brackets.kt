// Copyright 2020 Evgeny Kondratenko
// Make brackets between letters in string

fun add_brackets(s: String): String {
  val n = s.length
  if (n <= 2)
    return s
  var l = 0
  var r = n - 1
  var result = CharArray(2 * n - 2 + n % 2)
  var l_pos = 0
  var r_pos = 2 * n - 3 + n % 2
  while (l + 1 < r) {
    result[l_pos++] = s[l++]
    result[l_pos++] = '('
    result[r_pos--] = s[r--]
    result[r_pos--] = ')'
  }
  result[l_pos++] = s[l++]
  result[r_pos--] = s[r--]
    
  return result.joinToString("")
}


fun main() {
  println(add_brackets(""))
  println(add_brackets("a"))
  println(add_brackets("ab"))
  println(add_brackets("abc"))
  println(add_brackets("abcd"))
  println(add_brackets("abcde"))
  println(add_brackets("abcdef"))
  println(add_brackets("eSctRts"))
  println(add_brackets("abcDeFRGghht"))
  println(add_brackets("ab"))
  println(add_brackets("c"))
}
