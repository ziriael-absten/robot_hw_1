SELECT age, COUNT(id) AS users_num
FROM users
GROUP BY age
ORDER BY users_num DESC, age ASC;