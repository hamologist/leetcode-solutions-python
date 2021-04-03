function generateParenthesis(n: number): string[] {
  let vals: Array<string> = [];
  function inner(left: number, right: number, acc: string) {
    if (left == 0 && right == 0) {
      vals.push(acc);
      return;
    }
    if (left == 0) {
      return inner(left, right-1, `${acc})`);
    }
    if (right > left) {
      inner(left, right-1, `${acc})`);
    }
    inner(left-1, right, `${acc}(`);
  }

  inner(n-1, n, "(");
  return vals;
}

console.log(generateParenthesis(1))
console.log(generateParenthesis(2))
console.log(generateParenthesis(3))