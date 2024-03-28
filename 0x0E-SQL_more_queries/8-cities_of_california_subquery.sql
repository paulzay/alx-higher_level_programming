-- list cities
SELECT id, name 
      FROM hbtn_0d_usa 
      WHERE name = 'California'
      ORDER BY hbtn_0d_usa.cities.id ASC;
