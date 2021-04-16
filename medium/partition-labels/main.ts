interface Partition {
  left: number;
  right: number;
}

function partitionLabels(S: string): number[] {
  if (S.length === 0) {
    return [0];
  }

  const letterLookup = new Map<string, Partition>();
  const letterPartitions: Partition[] = [];
  const finalPartitions: Partition[] = [];

  for (let i = 0; i < S.length; i++) {
    let partition = letterLookup.get(S[i]);
    if (partition) {
      partition.right = i;
    } else {
      partition = { left: i, right: i };
      letterLookup.set(S[i], partition);
      letterPartitions.push(partition);
    }
  }

  let currentPartition = { left: 0, right: 0 };
  finalPartitions.push(currentPartition);
  for (const partition of letterPartitions) {
    if (currentPartition.right >= partition.left) {
      currentPartition.right = Math.max(currentPartition.right, partition.right);
    } else {
      currentPartition = partition;
      finalPartitions.push(currentPartition);
    }
  }

  return finalPartitions.map((value) => value.right - value.left + 1);
}

console.log(partitionLabels('ababcbacadefegdehijhklij'));
