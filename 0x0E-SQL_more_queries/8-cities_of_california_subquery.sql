-- This select all california cities
-- It Orders them in ascending order.
SELECT `id`, `name` FROM `cities` WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = 'California') ORDER BY `id` ASC;
