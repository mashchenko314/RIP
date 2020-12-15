Feature: Compatibility check via wrapper

    Scenario: Checking a square peg of suitable size
        Given size of square peg - width "20" and size of round hole - "10"
        Then peg and hole compatible after conversion via adapter

    Scenario: Checking a square peg if unsuitable size
        Given size of square peg - width "30" and size of round hole - "10"
        Then peg and hole incompatible after conversion via adapter