-- 코드를 입력하세요
SELECT A.CAR_ID, MAX(A.AVAILABILITY)
FROM
(SELECT 
    CAR_ID,
    CASE WHEN START_DATE <= "2022-10-16" AND "2022-10-16" <= END_DATE THEN "대여중"
    ELSE "대여 가능" END AVAILABILITY
   
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) A
GROUP BY A.CAR_ID
ORDER BY A.CAR_ID DESC
