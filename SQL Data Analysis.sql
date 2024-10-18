use employee;
select AGE from raju;
describe raju;
select patient_id,age from raju;
select * from raju where gender='female' and age>40;
-- Q3
select avg(bmi) from raju;
select * from raju order by blood_glucose_level desc;
-- Q5
select * from raju where hypertension=1 and diabetes =1;
-- Q6
select count(*) from raju where heart_disease = 1;
-- Q7
select count(patient_id) from raju group by smoking_history having smoking_history='current';
 select count(patient_id) from raju group by smoking_history having smoking_history='never';
-- Q8
select patient_id from raju where bmi> (select avg(bmi) from raju);
-- Q9
select * from raju where HbA1c_level =(select max(HbA1c_level) from raju);
select * from raju where HbA1c_level =(select min(HbA1c_level) from raju);
-- Q10 Calculate the age of patients in years (assuming the current date as of now).
 
-- Q11
SELECT
    Patient_id,
    Gender,
    Blood_Glucose_Level,
    RANK() OVER (PARTITION BY Gender ORDER BY Blood_Glucose_Level) AS Glucose_Level_Rank
FROM raju ;
-- Q12
update raju set smoking_history= 'Ex-smoker' where age>50;
-- Q13
insert into raju values ('Piyush Gupta','PT100101','Male',23,0,0,'never',21.43,4,80,0);
-- Q14
delete from raju where heart_disease=1;
-- Q15
select patient_id from raju where hypertension=1 
except
 select patient_id from raju where diabetes=1;
-- Q16  Define a unique constraint on the "patient_id" column to ensure its values are unique.
ALTER TABLE raju
MODIFY patient_id char(8);
ALTER TABLE raju
ADD CONSTRAINT unique_patient_id UNIQUE (patient_id);
-- Q17
create view patientinfo
as select  patient_id,age,bmi from raju ;
select * from patientinfo;
-- Q18

-- Q19

USE GUPTA_LTD;
select patient_id,age,year(CURDATE())- age as estimate from raju;
SELECT year(CURDATE());

(select * from raju where HbA1c_level =(select max(HbA1c_level) from raju)
UNION ALL
(select * from raju where HbA1c_level =(select min(HbA1c_level) from raju);

(SELECT * FROM raju WHERE HbA1c_level = (SELECT MAX(HbA1c_level) FROM raju) LIMIT 1)
UNION ALL
(SELECT * FROM raju WHERE HbA1c_level = (SELECT MIN(HbA1c_level) FROM raju)LIMIT 1);


 