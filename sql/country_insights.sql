-- -- How many countries speaks French
SELECT COUNT(name_common) as FrenchSpeaking FROM [dbo].[RESTCountry2]
WHERE fra = 'French'

-- How many countries speaks French
SELECT COUNT(name_common) as EnglishSpeaking FROM [dbo].[RESTCountry2]
WHERE eng = 'English'

-- How many country have more than 1 official language

SELECT COUNT(name_common) as official FROM [dbo].[RESTCountry2]
WHERE fra = 'French'
      OR eng = 'English'
      OR ita ='Italy'

-- How many country is from West europe
 SELECT COUNT(name_common)
from [dbo].[RESTCountry2]
WHERE subregion = 'Western Europe'     

-- How many country has not yet gain independence
SELECT COUNT(name_common) as Dependent_country
FROM [dbo].RESTCountry2
WHERE independent = 'False'

-- How many distinct continent and how many country from each
SELECT 
DISTINCT("continents'][") AS continents, COUNT(name_common) AS numberofcountry
FROM [dbo].[RESTCountry2]
GROUP BY "continents']["


-- How many country whose start of the week is not Monday
SELECT COUNT(name_common) AS Startofweek_not_monday
FROM [dbo].RESTCountry2
WHERE startOfWeek <> 'Monday'

-- How many countries are not United Nation member
SELECT COUNT(name_common) AS Not_UNmember
FROM [dbo].RESTCountry2
WHERE unMember = 'False'

-- How many countries are United Nation member
SELECT COUNT(name_common) AS Not_UNmember
FROM [dbo].RESTCountry2
WHERE unMember = 'True'

SELECT COUNT(name_common) AS Startofweek_not_monday
FROM [dbo].RESTCountry2
WHERE unMember = 'True'

-- Least 2 countries with the lowest population for each continents
SELECT "continents'][", name_common, "population"
FROM (
    SELECT g."continents'][", c.name_common, f."population",
           ROW_NUMBER() OVER (PARTITION BY g."continents'][" ORDER BY f."population" ASC) AS rank
    FROM [dbo].[RESTCountry2] f
	JOIN [dbo].[RESTCountry2] c ON f.name_common = c.name_common
    JOIN [dbo].[RESTCountry2] g ON f.name_common = g.name_common
) AS ranked
WHERE rank <= 2;



-- Top 5 countries with the largest Area
SELECT TOP 5 area, name_common AS Largest_Area
FROM [dbo].RESTCountry2
order by area desc

-- Top 5 countries with the lowest Area
SELECT TOP 5 area, name_common AS Lowest_Area
FROM [dbo].RESTCountry2
order by area 

