# FI Example: Cash flow hedge - interest rate swap
On 1 January 20X1, Arlington Co. lends $10 million to another entity, with a maturity date of three years later on 31 December 20X3. The interest rate attached to the loan is variable at HIBOR + 2%, and interest is due annually on 31 December.

Arlington expects interest rates to decline and so simultaneously enters an [[9.6.5 interest rate swaps]] on 1 January 20X1 in order to hedge its position.

The terms of the swap are as follows:
- There is no initial cost.
- The notional principal is $10 million.
- Arlington will receive fixed interest at 7%.
- Arlington will pay variable interest at HIBOR.
- Net settlement is made annually on 31 December, and the swap is also repriced on this date.

The fair value of the swap, determined by ~projecting future settlement~ amounts using the current year's variable rate and discounting these to present value is:

31 December 20X1 	$300,000
31 December 20X2 	$125,000
31 December 20X3	nil

HIBOR at each of these dates is:
31 December 20X1 	7%
31 December 20X2 	6%
31 December 20X3	5%

All criteria for cash flow hedge accounting have been met and the hedging relationship is expected to be 100% effective at inception and on an ongoing basis.

What journal entries are required in respect of the loan and cash flow hedge throughout the three-year term?
- - - -
Solution
The purpose of the cash flow hedge is to **fix the interest receivable at 9%.** Interest receivable per the terms of the loan agreement is:
![](FI%20Example%20Cash%20flow%20hedge%20-%20interest%20rate%20swap/62FE455F-0092-4329-9E01-4BBEFCD3FF2F.png)
The net settlement in respect of the swap on each of these dates is:
![](FI%20Example%20Cash%20flow%20hedge%20-%20interest%20rate%20swap/990FEB10-E90F-4C85-A809-DFCC91ED1723.png)
Therefore, in each of the three years, the total amount of the interest income (i.e. loan interest income + net position on the swap) is $900,000.

The journal entries are as follows:
- - - -
1 January 20X1
DEBIT	loan receivable	$10M
CREDIT	Cash			$10M
To record the inception of the loan.
(Note. No entry is required in respect of the swap as it was ::acquired at no cost.::)
- - - -
31 December 20X1
DEBIT 	Cash			$900K
CREDIT	interest income	$900K
To record the receipt of interest in respect of the loan.

DEBIT	interest rate swap$300K
CREDIT	OCI				$300K
To record the fair value of the interest rate swap
- - - -
31 December 20X2
DEBIT	cash			$800K
CREDIT	Interest income	$800K
To record the receipt of the interest in respect of the loan.

DEBIT	Cash			$100K
CREDIT	OCI				$100K
To record the cash received on net settlement of the interest rate swap.

DEBIT	OCI				$100K
CREDIT	Interest income	$100K
To recycle into earnings amounts in OCI on account of the cash flow hedge, so that they are matched with the relevant cash flow.

DEBIT	OCI				$175K
CREDIT	int rate swap 	$175K
To reduce the carrying value of the interest rate swap from its initial fair value of $300,000 to current fair value of $125,000
- - - -
31 December 20X3
DEBIT	cash			$700K
CREDIT	Interest income	$700K
To record the receipt of the interest in respect of the loan.

DEBIT	Cash			$200K
CREDIT	OCI				$200K
To record the cash received on net settlement of the interest rate swap.

DEBIT	OCI				$200K
CREDIT	Interest income	$200K
To recycle into earnings amounts in OCI on account of the cash flow hedge, so that they are matched with the relevant cash flow.

DEBIT	OCI				$125K
CREDIT	int rate swap 	$125K
To adjust the carrying value of the interest rate swap to current fair value.

DEBIT	cash			$10M
CREDIT	Loan receivable	$10M
To record repayment of the loan at the maturity date.

#QP/a/Practice/FI
