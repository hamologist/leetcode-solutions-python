function maxProfit(prices: number[]): number {
  let profit = 0;
  for (let i = 0; i < prices.length - 1; i++) {
    profit += Math.max(0, prices[i + 1] - prices[i]);
  }

  return profit;
}

(() => {
  console.log(maxProfit([7, 1, 5, 3, 6, 4]))
  console.log(maxProfit([1, 2, 3, 4, 5]))
  console.log(maxProfit([7, 6, 4, 3, 1]))
})()
