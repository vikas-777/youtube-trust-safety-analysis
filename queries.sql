-- Total content count
SELECT COUNT(*) AS total_content FROM content_data;

-- Category distribution
SELECT category, COUNT(*) AS count
FROM content_data
GROUP BY category
ORDER BY count DESC;

-- Flagged content
SELECT COUNT(*) AS flagged_content
FROM content_data
WHERE flagged = 'Yes';

-- Policy violations (removed content)
SELECT COUNT(*) AS violations
FROM content_data
WHERE decision = 'Removed';

-- Top violating categories
SELECT category, COUNT(*) AS violations
FROM content_data
WHERE decision = 'Removed'
GROUP BY category
ORDER BY violations DESC;

-- Region-wise violations
SELECT region, COUNT(*) AS violations
FROM content_data
WHERE decision = 'Removed'
GROUP BY region
ORDER BY violations DESC;

-- High-risk content (flagged + removed)
SELECT *
FROM content_data
WHERE flagged = 'Yes' AND decision = 'Removed';
