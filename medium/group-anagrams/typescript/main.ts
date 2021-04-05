function groupAnagrams(strs: string[]): string[][] {
  const lookup = new Map<string, string[]>();

  for (let word of strs) {
    const key = word.split('').sort().join('');

    if (lookup.has(key)) {
      lookup.get(key)?.push(word);
    } else {
      lookup.set(key, [word]);
    }
  }

  return [...lookup.values()];
}

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))