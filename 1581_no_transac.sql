--My Solution
SELECT 
    v.customer_id,
    COUNT(v.visit_id) as count_no_trans
FROM Visits v 
LEFT JOIN Transactions t 
ON t.visit_id = v.visit_id
WHERE t.visit_id IS NULL    
GROUP BY v.customer_id
ORDER BY count_no_trans DESC

--More readable solution
select customer_id, count(visit_id) as count_no_trans
from visits
where visit_id not in (select visit_id from transactions)
group by customer_id
