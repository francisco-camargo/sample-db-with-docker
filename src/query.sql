SELECT *
FROM employees as e
JOIN salaries as s
ON e.emp_no = s.emp_no 
WHERE e.hire_date > '1999-01-01';
