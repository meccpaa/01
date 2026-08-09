# Risk illustrations: interest rate futures
A company has a commitment to borrow $80 million in five months' time for a period of six months and is concerned that interest rates could significantly increase in the next five months. Currently, the company can borrow at HIBOR + 1%, and three-month HIBOR is at 7%. The current futures price is 92.10 and each futures contract is for $5 million.

**Approach**
(1) Risk?
Interest rates increase

(2) Action?
Sell futures (borrowing)

(3) Settlement date?
Nearest to the date when the money is needed.

(4) Number of contracts?
Futures contracts are for notional deposits of three months. To hedge the risk for a different interest rate period, the number of contracts is adjusted by a factor: (length of interest period/3 months), as follows:
![](Risk%20illustrations%20interest%20rate%20futures/31F0F244-5C58-4307-80CE-9BB1CCD8C8D0.png)
(5) Tick value?
(0.0001% x $5m x 3 / 12 ) = $125
What is the outcome in five months' time, if HIBOR is 9% and the futures price is 90.74?
![](Risk%20illustrations%20interest%20rate%20futures/9EBDD956-88E9-469E-98F0-14371D15959F.png)
When the futures position was opened, HIBOR was 7% and the company would have been able to borrow at that date at a rate of 8%. Hedging with futures has restricted the effective borrowing cost to 8.64%, which is less than the 10% actual interest payable on the $80 million loan.

In summary, if interest rates move against the company, the futures will protect it. Any loss suffered on the underlying cash position (actual borrowing or lending) is offset by the profits on the futures deal. However, should interest rates move for the company, any gain on the underlying cash position is wiped out by the loss on the futures position. Therefore, with a futures hedge, the company cannot lose (too much) but it cannot gain (too much) either.

#QP/b/Practice/risks
