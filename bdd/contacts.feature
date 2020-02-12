Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename> and <lastname>
  When I add the contact into the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname  | middlename  | lastname  |
  | firstname1 | middlename1 | lastname1 |
  | firstname2 | middlename2 | lastname2 |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact