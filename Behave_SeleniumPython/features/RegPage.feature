Feature: Registration feature

  @test
  Scenario: User Registration Page
   Given user navigates to Registartion url
   When user enters Firstname,Middlename and lastname
    And user clicks on Coarse and Gender
    And user enters MobileNumber,Address,Email,Password and ReType password
    Then user clicks on submit Button

