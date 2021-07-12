-- script that displays the max temperature of each state
SELECT state, MAX(value) FROM temperatures GROUP BY `state` ORDER BY `state` ASC;
