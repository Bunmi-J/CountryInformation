-- How many countries speaks French
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
      
SELECT COUNT(name_common) as Dependent_country
FROM [dbo].RESTCountry2
WHERE independent = 'False'

SELECT COUNT(name_common) AS Startofweek_not_monday
FROM [dbo].RESTCountry2
WHERE startOfWeek <> 'Monday'

SELECT COUNT(name_common) AS Not_UNmember
FROM [dbo].RESTCountry2
WHERE unMember = 'False'

SELECT COUNT(name_common) AS Startofweek_not_monday
FROM [dbo].RESTCountry2
WHERE unMember = 'True'

SELECT TOP 5 population, name_common AS Lowest_Population
FROM [dbo].RESTCountry2
order by population

SELECT TOP 5 area, name_common AS Largest_Area
FROM [dbo].RESTCountry2
order by area desc

SELECT TOP 5 area, name_common AS Lowest_Area
FROM [dbo].RESTCountry2
order by area 

