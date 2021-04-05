function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) {
    return false;
  }

  const lookup = new Map<string, number>();
  for (let i = 0; i < s.length; i++) {
    lookup.set(s[i], (lookup.get(s[i]) || 0) + 1)
    lookup.set(t[i], (lookup.get(t[i]) || 0) - 1)
  }

  for (let count of lookup.values()) {
    if (count !== 0) {
      return false;
    }
  }

  return true;
}

function isAnagramWithSort(s: string, t: string): boolean {
  if (s.length !== t.length) {
    return false;
  }

  return s.split('').sort().join('') == t.split('').sort().join('');
}

console.log(isAnagram('anagram', 'nagaram'))
console.log(isAnagram('rat', 'car'))
console.log();
console.log(isAnagramWithSort('anagram', 'nagaram'))
console.log(isAnagramWithSort('rat', 'car'))
