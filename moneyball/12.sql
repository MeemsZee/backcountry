"""Hits are great, but so are RBIs! In 12.sql, write a SQL query to find the players among the 10 least expensive players per hit and among 
the 10 least expensive players per RBI in 2001.

Your query should return a table with two columns, one for the players’ first names and one of their last names.
You can calculate a player’s salary per RBI by dividing their 2001 salary by their number of RBIs in 2001.
You may assume, for simplicity, that a player will only have one salary and one performance in 2001.
Order your results by player ID, least to greatest (or alphabetically by last name, as both are the same in this case!).
Keep in mind the lessons you’ve learned in 10.sql and 11.sql!"""

SELECT DISTINCT(last_name), first_name
FROM players
WHERE id IN (
    SELECT pl.id
    FROM players AS pl 
    JOIN performances AS pr 
    ON pl.id = pr.player_id
    JOIN salaries AS s
    ON  s.player_id = pl.id
    WHERE s.year = 2001 and pr.year = 2001 AND RBI > 0 
    ORDER by salary/RBI
    LIMIT 10)
INTERSECT
SELECT DISTINCT(last_name), first_name
FROM players 
WHERE id IN (
    SELECT pl.id
    FROM players AS pl 
    JOIN performances AS pr 
    ON pl.id = pr.player_id
    JOIN salaries AS s
    ON  s.player_id = pl.id
    WHERE s.year = 2001 and pr.year = 2001 AND H > 0
    ORDER by salary/H
    LIMIT 10);

SELECT first_name, last_name, (SELECT salary FROM salaries WHERE s.year = 2001)/(SELECT H FROM s) salary, H
FROM players AS pl 
JOIN performances AS pr 
ON pl.id = pr.player_id
JOIN salaries AS s
ON  s.player_id = pl.id
ORDER BY salary/H
Limit 10;

SELECT * FROM performances
LIMIT 2;


