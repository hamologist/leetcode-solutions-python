interface Pointer {
  row: number,
  rowPosition: number,
  currentValue: number,
}

const MAX_POINTER: Pointer = {
  row: 0,
  rowPosition: 0,
  currentValue: Number.MAX_SAFE_INTEGER,
}

function kthSmallest(matrix: number[][], k: number): number {
  let current = 0;
  let currentValue = 0;
  const rowPointers = new Array<Pointer>(matrix.length);

  for (let i = 0; i < matrix.length; i++) {
    rowPointers[i] = {
      row: i,
      rowPosition: 0,
      currentValue: matrix[i][0],
    }
  }

  while (current < k) {
    current += 1;
    let smallestPointer: Pointer = MAX_POINTER;
    for (let pointer of rowPointers) {
      if (smallestPointer.currentValue > pointer.currentValue) {
        smallestPointer = pointer;
      }
    }

      currentValue = smallestPointer.currentValue;
      smallestPointer.rowPosition++;

    if (smallestPointer.rowPosition === matrix.length) {
      rowPointers.splice(rowPointers.indexOf(smallestPointer), 1);
    } else {
      smallestPointer.currentValue = matrix[smallestPointer.row][smallestPointer.rowPosition]
    }
  }

  return currentValue;
}

console.log(kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 8));
console.log(kthSmallest([[0,0,0],[2,7,9],[7,8,11]], 7));
console.log(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8));
console.log(kthSmallest([[-5]], 1));
