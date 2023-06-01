SELECT age, COUNT(id) AS users_num
FROM users
GROUP BY age
HAVING COUNT(id) > 1;