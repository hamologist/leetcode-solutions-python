interface TopK {
  num: number,
  count: number,
}

function compareTopK(a: TopK, b: TopK) {
  if (a.count < b.count) {
    return 1;
  }
  if (a.count > b.count) {
    return -1;
  }
  return 0;
}

function topKFrequentNoSort(nums: number[], k: number): number[] {
  const countLookup = new Map<number, number>();
  const topK: Array<TopK> = [];

  for (let num of nums) {
    countLookup.set(num, (countLookup.get(num) || 0) + 1);
  }

  for (let num of countLookup.keys()) {
    topK.push({num: num, count: countLookup.get(num) || 0})
  }

  topK.sort(compareTopK);

  let ans = [];
  for (let i = 0; i < k; i++) {
    ans.push(topK[i].num);
  }
  return ans;
}

function topKFrequent(nums: number[], k: number): number[] {
  nums.sort();
  const topK: Array<TopK> = [];
  let prev = nums[0]
  let count = 0;
  let num: number = 0;
  for (num of nums) {
    if (prev == num) {
      count++;
    } else {
      topK.push({num: prev, count: count})
      prev = num;
      count = 1;
    }
  }
  topK.push({num: num, count: count})

  topK.sort(compareTopK);

  let ans = [];
  for (let i = 0; i < k; i++) {
    ans.push(topK[i].num);
  }
  return ans;
}

console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));
console.log(topKFrequent([1], 1));
console.log(topKFrequentNoSort([4, 1, -1, 2, -1, 2, 3], 2))
