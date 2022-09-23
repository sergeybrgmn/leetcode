--| LINK https://leetcode.com/problems/bank-account-summary-ii/

SELECT 
    u.name,
    sum(t.amount) as balance
FROM Transactions t
LEFT JOIN Users u ON u.account=t.account
GROUP BY u.name
HAVING balance > 10000
