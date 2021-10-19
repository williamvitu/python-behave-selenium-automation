Feature: Table Page
 These scenarios will validate data from the table page.

 
  Scenario: Order by Alphabetical  A-Z
    Given the user clicks on name column button
    Then the table should order the data by alphabetical from Z to A

  Scenario: Order by Alphabetical  Z-A
    Given the user clicks on name column button
    Then the table should order the data by alphabetical from A to Z

  Scenario: Order by default pattern
    Given the user clicks on name column button
    Then the table should sort the data by default 

 
  Scenario: Check Table Pagination item
    Given the user clicks on Page item 2 on table
    Then the table should display the page 2
  
  
