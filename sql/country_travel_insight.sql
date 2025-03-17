-- -- How many countries speaks French
SELECT COUNT(countryname) as FrenchSpeaking FROM [dbo].[countries]
WHERE (frenchspeaking_countries) = 'True';
--46

-- How many countries speaks English

SELECT COUNT(countryname) as EngSpeaking FROM [dbo].[countries]
WHERE (englishspeaking_countries) = 'True';
--91

-- How many countries have more than 1 official language

SELECT COUNT(countryname) as official_language_more_one FROM [dbo].[countries]
WHERE language_count > 1
   --96

-- With Result AS (
-- 	SELECT CA.*, value AS LANG
-- 	FROM [dbo].[countries] AS CA
-- 	CROSS APPLY STRING_SPLIT(CA.languages, ',') 
-- )
-- SELECT countryname, COUNT(LANG) AS NUM FROM Result
-- GROUP BY countryname
-- HAVING COUNT(LANG) >1


-- How many country is from West europe

SELECT COUNT(countryname) as Western_Europe
from [dbo].[countries]
WHERE "sub region" = 'Western Europe' 
--8
-- How many countries are dependent
SELECT COUNT(countryname) as Dependent_country
FROM [dbo].countries
WHERE independence = 'False'
--55

--How many countries with official currency is Euro
select count('countryname') as eurocurrency
from [dbo].[countries]
where currencyname = 'Euro'
--36

-- How many distinct continent and how many country from each
SELECT DISTINCT("continents") AS continents, COUNT(countryname) AS numberofcountry
FROM [dbo].[countries]
GROUP BY "continents"

-- How many country whose start of the week is not Monday
SELECT COUNT(countryname) AS Startofweek_not_monday
FROM [dbo].countries
WHERE startOfWeek <> 'Monday'
--21

-- How many countries are not United Nation member
SELECT COUNT(countryname) AS Not_UNmember
FROM [dbo].countries
WHERE [united nation member] = 'False'
--58

-- How many countries are United Nation member
SELECT COUNT(countryname) AS UNmember
FROM [dbo].countries
WHERE [united nation member] = 'True'
--192

-- Least 2 countries with the lowest population for each continents

SELECT c1.[continents], c1.[countryname], c1.population
FROM countries c1
WHERE (
    SELECT COUNT(*)
    FROM countries c2
    WHERE c2.continents= c1.continents AND c2.population < c1.population
) < 2
ORDER BY c1.continents, c1.population;


-- Top 5 countries with the largest Area
SELECT TOP 5 area, [countryname] AS Largest_Area
FROM [dbo].countries
order by area desc

-- Top 5 countries with the lowest Area
SELECT TOP 5 area, countryname AS Lowest_Area
FROM [dbo].countries
order by area 

--Top 2 countries with the largest Area for each continent
SELECT c1.[continents], c1.[countryname], c1.area as largest_area
FROM countries c1
WHERE (
    SELECT COUNT(*)
    FROM countries c2
    WHERE c2.continents= c1.continents AND c2.area > c1.area
) < 2
ORDER BY c1.continents, c1.area DESC;

