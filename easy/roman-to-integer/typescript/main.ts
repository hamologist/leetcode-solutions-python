const ROMAN_LOOKUP = new Map<string, number>([
  ["I", 1],
  ["V", 5],
  ["X", 10],
  ["L", 50],
  ["C", 100],
  ["D", 500],
  ["M", 1000],
])

function romanToInt(s: string): number {
  let num = 0;
  let prev = 0;
  for (let i = s.length - 1; i >= 0; i--) {
    const current = ROMAN_LOOKUP.get(s[i]) || 0
    if (current >= prev) {
      num += current;
      prev = current;
    } else {
      num -= current;
    }
  }

  return num;
}

console.log(romanToInt("III"));
console.log(romanToInt("IV"));
console.log(romanToInt("IX"));
console.log(romanToInt("LVIII"));
console.log(romanToInt("MCMXCIV"));
