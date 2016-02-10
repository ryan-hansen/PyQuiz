Feature: User can access home page
  As a user
  I want to visit the home page
  So that I can see that it's a functioning Django application

  Scenario: Home page loaded
    Given I am a user
    When I visit the home page
    Then The title says "Welcome to Django"
