interface LetterLookup {
  index: number;
  count: number;
}

function firstUniqChar(s: string): number {
  const lookup = new Map<string, LetterLookup>();
  for (let i = 0; i < s.length; i++) {
    const letter = lookup.get(s[i]);
    if (letter) {
      letter.count += 1;
    } else {
      lookup.set(s[i], { index: i, count: 1 });
    }
  }

  for (const letter of lookup.values()) {
    if (letter.count === 1) {
      return letter.index;
    }
  }

  return -1;
}

console.log(firstUniqChar('leetcode'));
console.log(firstUniqChar('loveleetcode'));
console.log(firstUniqChar('aabb'));
