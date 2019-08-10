# Write your MySQL query statement below
SELECT actor_id, director_id
FROM 
(
    SELECT actor_id, director_id, COUNT(timestamp) as c
    FROM ActorDirector
    GROUP BY actor_id, director_id
) temp
WHERE temp.c >= 3