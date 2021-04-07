function titleToNumber(columnTitle: string): number {
  let columnNumber = 0;
  for (let i = columnTitle.length - 1; i >= 0; i--) {
    columnNumber += Math.pow(26, i) * (columnTitle.charCodeAt(columnTitle.length - 1 - i) - 64);
  }

  return columnNumber;
}

console.log(titleToNumber("A"));
console.log(titleToNumber("AB"));
console.log(titleToNumber("ZY"));
console.log(titleToNumber("FXSHRXW"));
