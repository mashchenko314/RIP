Feature: Compatibility check

    Scenario:  Checking a round peg of suitable size
        Given size of round peg - radius "10" and size of round hole - "10"
        Then peg and hole compatible

    Scenario:  Checking a round peg of unsuitable size
        Given size of round peg - radius "20" and size of round hole - "10"
        Then peg and hole incompatible

    Scenario:  Checking a square detail
        Given size of square peg - width "10" and size of round hole - "10"
        Then the square peg is not comparable to the round hole