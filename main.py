import pandas as pd
import sqlite3

# Connections
conn1 = sqlite3.connect('planets.db')
conn2 = sqlite3.connect('dogs.db')
conn3 = sqlite3.connect('babe_ruth.db')

# Step 1: Planets with 0 moons
df_no_moons = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons = 0;
""", conn1)

# Step 2: Planets with exactly 7-letter names
df_name_seven = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE length(name) = 7;
""", conn1)

# Step 3: Planets with mass <= 1.00
df_mass = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE mass <= 1.00;
""", conn1)

# Step 4: Planets with >= 1 moon and mass < 1.00
df_mass_moon = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons >= 1
AND mass < 1.00;
""", conn1)

# Step 5: Planets whose color contains 'blue'
df_blue = pd.read_sql("""
SELECT name, color
FROM planets
WHERE color LIKE '%blue%';
""", conn1)

# Step 6: Hungry dogs sorted youngest to oldest
df_hungry = pd.read_sql("""
SELECT name, age, breed
FROM dogs
WHERE hungry = 1
ORDER BY age ASC;
""", conn2)

# Step 7: Hungry dogs aged 2-7, sorted alphabetically
df_hungry_ages = pd.read_sql("""
SELECT name, age, hungry
FROM dogs
WHERE hungry = 1
AND age BETWEEN 2 AND 7
AND name IS NOT NULL
ORDER BY name ASC;
""", conn2)

# Step 8: 4 oldest dogs sorted by breed (handles ties)
df_4_oldest = pd.read_sql("""
SELECT name, age, breed
FROM dogs
ORDER BY age DESC, breed ASC
LIMIT 4

 """,conn2)

# Step 9: Total years Babe Ruth played
df_ruth_years = pd.read_sql("""
SELECT COUNT(year) AS num_years
FROM babe_ruth_stats;
""", conn3)

# Step 10: Total career homeruns
df_hr_total = pd.read_sql("""
SELECT SUM(HR) AS num_hr
FROM babe_ruth_stats;
""", conn3)

# Step 11: Years played per team
df_teams_years = pd.read_sql("""
SELECT team, COUNT(year) AS number_years
FROM babe_ruth_stats
GROUP BY team;
""", conn3)

# Step 12: Teams where Babe Ruth averaged over 200 at bats
df_at_bats = pd.read_sql("""
SELECT team, AVG(at_bats) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(at_bats) > 200;
""", conn3)

conn1.close()
conn2.close()
conn3.close()
